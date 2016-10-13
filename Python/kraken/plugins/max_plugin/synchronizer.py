
import logging

from kraken.core.maths import Xfo, Vec3, Quat, Math_degToRad

from kraken.log import getLogger

from kraken.core.synchronizer import Synchronizer
from kraken.plugins.max_plugin.utils import *
from kraken.plugins.max_plugin.utils.curves import curveToKraken

logger = getLogger('kraken')


class Synchronizer(Synchronizer):
    """The Synchronizer is a singleton object used to synchronize data between
    Kraken objects and the DCC objects."""

    def __init__(self):
        super(Synchronizer, self).__init__()


    # ============
    # DCC Methods
    # ============
    def getDCCItem(self, kObject):
        """Gets the DCC Item from the full decorated path.

        Args:
            kObject (object): The Kraken Python object that we must find the corresponding DCC item.

        Returns:
            object: The created DCC object.

        """

        foundItem = None
        path = kObject.getPath()
        pathSections = path.split('.')
        pathObj = kObject
        maxPath = ''
        index = len(pathSections) - 1
        for pathSection in reversed(pathSections):

            if pathObj is None:
                raise Exception("parent not specified for object, so a full path cannot be resolved to a maya object:" + path)

            if pathObj.isTypeOf('AttributeGroup'):
                maxPath = ':baseObject:' + pathObj.getName() + maxPath

            elif pathObj.isTypeOf('Attribute'):
                # The attribute object requires a '.' seperator in the Maya path.
                maxPath = ':' + pathObj.getName()

            else:
                if index > 0:
                    maxPath = '/' + pathObj.getBuildName() + maxPath
                else:
                    maxPath = pathObj.getBuildName() + maxPath

            pathObj = pathObj.getParent()
            index -= 1

        # Find and select object
        objPath = maxPath.split(":", 1)
        MaxPlus.Core.EvalMAXScript("obj = $" + objPath[0])
        if rt.obj is None:
            return foundItem

        rt.select(rt.obj)
        node = MaxPlus.SelectionManager.GetNodes()[0]
        foundItem = node

        logger.debug("ObjPath: {}".format(objPath[0]))

        if kObject.isTypeOf('AttributeGroup'):
            logger.debug("AttributeGroup: {}".format(kObject.getName()))
            foundItem = None
            customAttrContainers = node.BaseObject.GetCustomAttributeContainer()
            if str(customAttrContainers) != "None":
                for i in xrange(len(customAttrContainers)):
                    attrCntr = node.BaseObject.GetCustomAttributeContainer()[i]
                    if attrCntr.GetName() == kObject.getName():
                        foundItem = attrCntr

        elif kObject.isTypeOf('Attribute'):
            attrGrp = None
            customAttrContainers = node.BaseObject.GetCustomAttributeContainer()
            if str(customAttrContainers) != "None":
                for i in xrange(len(customAttrContainers)):
                    attrCntr = node.BaseObject.GetCustomAttributeContainer()[i]
                    if attrCntr.GetName() == kObject.getParent().getName():
                        attrGrp = attrCntr

                if attrGrp is not None:
                    logger.debug("AttributeGroup: {}".format(kObject.getParent().getName()))
                    logger.debug("Attribute: {}".format(kObject.getName()))
                    foundItem = None
                    paramBlock = attrGrp.GetParameterBlock()
                    for i in xrange(paramBlock.NumParameters):
                        param = paramBlock.GetItem(i)
                        paramName = param.GetName()
                        if paramName == kObject.getName():
                            foundItem = param

        logger.debug("foundItem: " + str(foundItem))

        return foundItem


    def syncXfo(self, kObject):
        """Syncs the xfo from the DCC object to the Kraken object.

        Args:
            kObject (object): Object to sync the xfo for.

        Returns:
            Boolean: True if successful.

        """

        if kObject.isOfAnyType(('Rig', 'Container', 'Layer', 'HierarchyGroup', 'ComponentInput', 'ComponentOutput')):
            logger.debug("SyncXfo: Skipping '" + kObject.getName() + "'!")
            return False

        hrcMap = self.getHierarchyMap()

        if kObject not in hrcMap.keys():
            logger.warning("SyncXfo: 3D Object '" + kObject.getName() + "' was not found in the mapping!")
            return False

        dccItem = hrcMap[kObject]['dccItem']

        if dccItem is None:
            logger.warning("SyncXfo: No DCC Item for :" + kObject.getPath())
            return False

        dccPos = dccItem.GetWorldPosition()
        dccQuat = dccItem.GetWorldRotation()
        dccScl = dccItem.GetWorldScale()

        pos = Vec3(x=dccPos.X, y=dccPos.Y, z=dccPos.Z)
        quat = Quat(v=Vec3(dccQuat.X, dccQuat.Y, dccQuat.Z), w=dccQuat.W)

        # If flag is set, pass the DCC Scale values.
        if kObject.testFlag('SYNC_SCALE') is True:
            scl = Vec3(x=dccScl.X, y=dccScl.Y, z=dccScl.Z)
        else:
            scl = Vec3(1.0, 1.0, 1.0)

        newXfo = Xfo(tr=pos, ori=quat, sc=scl)
        rotateUpXfo = Xfo()
        rotateUpXfo.ori = Quat().setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(-90))
        newXfo = rotateUpXfo * newXfo

        kObject.xfo = newXfo

        return True


    def syncAttribute(self, kObject):
        """Syncs the attribute value from the DCC objec to the Kraken object.

        Args:
            kObject (object): Object to sync the attribute value for.

        Returns:
            bool: True if successful.

        """

        if kObject.getParent() is not None and kObject.isTypeOf('AttributeGroup'):
            if kObject.getParent().getParent().isTypeOf('Component'):
                if kObject.getParent().getParent().getComponentType() == "Guide":
                    return False

        hrcMap = self.getHierarchyMap()

        if kObject not in hrcMap.keys():
            logger.warning("SyncAttribute: Attribute '" + kObject.getName() + "' was not found in the mapping!")
            return False

        dccItem = hrcMap[kObject]['dccItem']

        if dccItem is None:
            logger.warning("SyncAttribute: No DCC Item for :" + kObject.getPath())
            return

        kObject.setValue(dccItem.Value)

        return True


    def syncCurveData(self, kObject):
        """Syncs the curve data from the DCC object to the Kraken object.

        Args:
            kObject (object): object to sync the curve data for.

        Returns:
            bool: True if successful.

        """

        hrcMap = self.getHierarchyMap()

        if kObject not in hrcMap.keys():
            logger.warning("SyncCurveData: 3D Object '" + kObject.getName() + "' was not found in the mapping!")
            return False

        dccItem = hrcMap[kObject]['dccItem']

        if dccItem is None:
            logger.warning("SyncCurveData: No DCC Item for :" + kObject.getPath())
            return

        # Get Curve Data from 3dsMax Curve
        data = curveToKraken(dccItem)

        # ===================================
        # TODO: GET CURVE SYNCING WORKING!!!
        # ===================================

        # kObject.setCurveData(data)

        return True
