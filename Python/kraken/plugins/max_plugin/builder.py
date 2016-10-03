"""Kraken Maya - Maya Builder module.

Classes:
Builder -- Component representation.

"""

import json
import logging
import math
import random

from kraken.log import getLogger

from kraken.core.kraken_system import ks
from kraken.core.configs.config import Config

from kraken.core.maths import *

from kraken.core.builder import Builder
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute
from kraken.plugins.max_plugin.utils import *

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad


logger = getLogger('kraken')
logger.setLevel(logging.INFO)


class Builder(Builder):
    """Builder object for building Kraken objects in Maya."""

    def __init__(self):
        super(Builder, self).__init__()

    def deleteBuildElements(self):
        """Clear out all dcc built elements from the scene if exist."""


        for builtElement in self._buildElements:
            if builtElement['src'].isOfAnyType(('Attribute',
                                                'AttributeGroup',
                                                'Constraint')):
                continue

            node = builtElement['tgt']
            if node is None:
                msg = 'Built object is None: {} : {}'
                logger.warning(msg.format(builtElement['src'].getPath(),
                                          builtElement['src'].getTypeName()))
            else:
                try:
                    node.Delete()
                except Exception, e:
                    logger.warning(str(e))
                    msg = "Could not delete built items: {} ({})"
                    logger.warning(msg.format(builtElement['src'].getPath(),
                                              builtElement['src'].getTypeName()))

        self._buildElements = []

        return

    # ========================
    # Object3D Build Methods
    # ========================
    def buildContainer(self, kSceneItem, buildName):
        """Builds a container / namespace object.

        Args:
            kSceneItem (Object): kSceneItem that represents a container to
                be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        obj = MaxPlus.Factory.CreateHelperObject(MaxPlus.ClassIds.Point)
        node = MaxPlus.Factory.CreateNode(obj, buildName)
        node.SetHidden(True)

        if parentNode is not None:
            node.SetParent(parentNode)

        dccSceneItem = node

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        # Build Attributes for storing meta data on the container object
        if kSceneItem.isTypeOf('Rig'):

            krakenRigDataAttrGrp = AttributeGroup("KrakenRig_Data", parent=kSceneItem)
            krakenRigAttr = BoolAttribute('krakenRig', value=True, parent=krakenRigDataAttrGrp)
            krakenRigAttr.setLock(True)

            self.buildAttributeGroup(krakenRigDataAttrGrp)
            self.buildBoolAttribute(krakenRigAttr)

            # Put Rig Data on DCC Item
            metaData = kSceneItem.getMetaData()
            if 'guideData' in metaData:
                pureJSON = metaData['guideData']

                krakenRigDataAttr = StringAttribute('krakenRigData', value=json.dumps(pureJSON, indent=None).replace('"', '\\"'), parent=krakenRigDataAttrGrp)
                krakenRigDataAttr.setLock(True)

                self.buildStringAttribute(krakenRigDataAttr)

        return dccSceneItem

    def buildLayer(self, kSceneItem, buildName):
        """Builds a layer object.

        Args:
            kSceneItem (Object): kSceneItem that represents a layer to
                be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        obj = MaxPlus.Factory.CreateHelperObject(MaxPlus.ClassIds.Point)
        node = MaxPlus.Factory.CreateNode(obj, buildName)
        node.SetHidden(True)

        if parentNode is not None:
            node.SetParent(parentNode)

        dccSceneItem = node

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildHierarchyGroup(self, kSceneItem, buildName):
        """Builds a hierarchy group object.

        Args:
            kSceneItem (Object): kSceneItem that represents a group to
                be built.
            buildName (str): The name to use on the built object.

        Return:
            object: DCC Scene Item that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        obj = MaxPlus.Factory.CreateHelperObject(MaxPlus.ClassIds.Point)
        node = MaxPlus.Factory.CreateNode(obj, buildName)
        node.SetHidden(True)

        if parentNode is not None:
            node.SetParent(parentNode)

        dccSceneItem = node

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildGroup(self, kSceneItem, buildName):
        """Builds a group object.

        Args:
            kSceneItem (Object): kSceneItem that represents a group to
                be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        obj = MaxPlus.Factory.CreateHelperObject(MaxPlus.ClassIds.Point)
        node = MaxPlus.Factory.CreateNode(obj, buildName)
        node.SetHidden(True)

        if parentNode is not None:
            node.SetParent(parentNode)

        dccSceneItem = node

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildJoint(self, kSceneItem, buildName):
        """Builds a joint object.

        Args:
            kSceneItem (Object): kSceneItem that represents a joint to
                be built.
            buildName (str): The name to use on the built object.

        Return:
            object: DCC Scene Item that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        dccSceneItem = None

        bone = pymxs.runtime.boneSys.createBone(rt.Point3(0, 0, 0), rt.Point3(1, 0, 0), rt.Point3(0, 0, 1))
        rdmHash = random.getrandbits(128)
        bone.Name = str(rdmHash)

        node = [x for x in MaxPlus.Core.GetRootNode().Children if x.Name == str(rdmHash)][0]
        node.SetName(buildName)
        node.BaseObject.ParameterBlock.Length.Value = 10.0
        node.BaseObject.ParameterBlock.Width.Value = kSceneItem.getRadius() * 2.5
        node.BaseObject.ParameterBlock.Height.Value = kSceneItem.getRadius() * 2.5

        if parentNode is not None:
            node.SetParent(parentNode)

        dccSceneItem = node

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildLocator(self, kSceneItem, buildName):
        """Builds a locator / null object.

        Args:
            kSceneItem (Object): locator / null object to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        obj = MaxPlus.Factory.CreateHelperObject(MaxPlus.ClassIds.Point)
        node = MaxPlus.Factory.CreateNode(obj, buildName)
        node.SetHidden(True)

        if parentNode is not None:
            node.SetParent(parentNode)

        dccSceneItem = node

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildCurve(self, kSceneItem, buildName):
        """Builds a Curve object.

        Args:
            kSceneItem (Object): kSceneItem that represents a curve to
                be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        kSceneItem.scalePoints(Vec3(10, 10, 10))

        curveData = kSceneItem.getCurveData()

        obj = MaxPlus.Factory.CreateShapeObject(MaxPlus.ClassIds.SplineShape)
        shapeObj = MaxPlus.SplineShape__CastFrom(obj)
        splineShape = shapeObj.GetShape()
        splineShape.NewShape()

        for i, eachSubCurve in enumerate(curveData):
            closedSubCurve = eachSubCurve['closed']
            degreeSubCurve = eachSubCurve['degree']
            points = eachSubCurve['points']

            spline = splineShape.NewSpline()

            if degreeSubCurve == 1:
                knotType = MaxPlus.SplineKnot.CornerKnot
                lineType = MaxPlus.SplineKnot.LineLineType
            else:
                knotType = MaxPlus.SplineKnot.AutoKnot
                lineType = MaxPlus.SplineKnot.CurveLineType

            for point in points:
                point = MaxPlus.Point3(point[0], point[1], point[2])
                spline.AddKnot(MaxPlus.SplineKnot(knotType, lineType, point, point, point))

            if closedSubCurve:
                spline.SetClosed(True)

        crvNode = MaxPlus.Factory.CreateNode(obj)
        crvNode.Name = buildName

        if parentNode is not None:
            crvNode.SetParent(parentNode)

        dccSceneItem = crvNode

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildControl(self, kSceneItem, buildName):
        """Builds a Control object.

        Args:
            kSceneItem (Object): kSceneItem that represents a control to
                be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentNode = self.getDCCSceneItem(kSceneItem.getParent())

        kSceneItem.scalePoints(Vec3(10, 10, 10))

        curveData = kSceneItem.getCurveData()

        obj = MaxPlus.Factory.CreateShapeObject(MaxPlus.ClassIds.SplineShape)
        shapeObj = MaxPlus.SplineShape__CastFrom(obj)
        splineShape = shapeObj.GetShape()
        splineShape.NewShape()

        for i, eachSubCurve in enumerate(curveData):
            closedSubCurve = eachSubCurve['closed']
            degreeSubCurve = eachSubCurve['degree']
            points = eachSubCurve['points']

            spline = splineShape.NewSpline()

            if degreeSubCurve == 1:
                knotType = MaxPlus.SplineKnot.CornerKnot
                lineType = MaxPlus.SplineKnot.LineLineType
            else:
                knotType = MaxPlus.SplineKnot.AutoKnot
                lineType = MaxPlus.SplineKnot.CurveLineType

            for point in points:
                point = MaxPlus.Point3(point[0], point[1], point[2])
                spline.AddKnot(MaxPlus.SplineKnot(knotType, lineType, point, point, point))

            if closedSubCurve:
                spline.SetClosed(True)

        crvNode = MaxPlus.Factory.CreateNode(obj)
        crvNode.Name = buildName

        if parentNode is not None:
            crvNode.SetParent(parentNode)

        dccSceneItem = crvNode

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    # ========================
    # Attribute Build Methods
    # ========================
    def buildBoolAttribute(self, kAttribute):
        """Builds a Bool attribute.

        Args:
            kAttribute (Object): kAttribute that represents a boolean
                attribute to be built.

        Return:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentObject3D = kAttribute.getParent().getParent()
        parentAttrGroup = kAttribute.getParent()

        MaxPlus.SelectionManager.ClearNodeSelection()
        parentDCCSceneItem.Select()

        rt.execute('targetObj = selection[1]')
        customAttr = getattr(rt.targetObj, kAttribute.getParent().getName(), None)

        if customAttr is None:
            raise AttributeError('Could not find Attribute Group: {0} on {1}'.format(parentAttrGroup.getName(), parentObject3D.getName()))

        # Get Attribute
        dataDef = rt.CustAttributes.getDef(customAttr)
        defSource = dataDef.source
        defLines = defSource.splitlines()
        endParamIndex = defLines.index('            -- Param Def End')
        endRolloutIndex = defLines.index('            -- Rollout Def End')

        # Create param format data
        formatData = {
            'padding': '\t\t\t',
            'paramName': kAttribute.getName(),
            'initValue': str(kAttribute.getValue()).lower(),
            'enabled': str(not kAttribute.getLock()).lower()
        }

        newParamLine = '{padding}{paramName} type: #boolean ui:{paramName} default: {initValue}'
        defLines.insert(endParamIndex, newParamLine.format(**formatData))

        newRolloutLine = '{padding}checkbox {paramName} "{paramName}" type: #boolean enabled: {enabled}'
        defLines.insert(endRolloutIndex, newRolloutLine.format(**formatData))

        newDef = '\n'.join(defLines)
        rt.CustAttributes.redefine(dataDef, newDef)

        parentDCCSceneItem.Deselect()

        dccSceneItem = dataDef

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildScalarAttribute(self, kAttribute):
        """Builds a Float attribute.

        Args:
            kAttribute (Object): kAttribute that represents a float attribute
                to be built.

        Return:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentObject3D = kAttribute.getParent().getParent()
        parentAttrGroup = kAttribute.getParent()

        MaxPlus.SelectionManager.ClearNodeSelection()
        parentDCCSceneItem.Select()

        rt.execute('targetObj = selection[1]')
        customAttr = getattr(rt.targetObj, kAttribute.getParent().getName(), None)

        if customAttr is None:
            raise AttributeError('Could not find Attribute Group: {0} on {1}'.format(parentAttrGroup.getName(), parentObject3D.getName()))

        # Get Attribute
        dataDef = rt.CustAttributes.getDef(customAttr)
        defSource = dataDef.source
        defLines = defSource.splitlines()
        endParamIndex = defLines.index('            -- Param Def End')
        endRolloutIndex = defLines.index('            -- Rollout Def End')

        # Create param format data
        formatData = {
            'padding': '\t\t\t',
            'paramName': kAttribute.getName(),
            'initValue': str(kAttribute.getValue()).lower(),
            'enabled': str(not kAttribute.getLock()).lower(),
            'minRange': kAttribute.getMin(),
            'maxRange': kAttribute.getMax()
        }

        newParamLine = '{padding}{paramName} type: #float ui:{paramName} default: {initValue}'
        defLines.insert(endParamIndex, newParamLine.format(**formatData))

        if formatData['minRange'] is not None and formatData['maxRange'] is not None:
            newRolloutLine = '{padding}spinner {paramName} "{paramName}" type: #float range:[{minRange}, {maxRange}, {initValue}] enabled: {enabled}'
        else:
            newRolloutLine = '{padding}spinner {paramName} "{paramName}" type: #float enabled: {enabled}'

        defLines.insert(endRolloutIndex, newRolloutLine.format(**formatData))

        newDef = '\n'.join(defLines)
        rt.CustAttributes.redefine(dataDef, newDef)

        parentDCCSceneItem.Deselect()

        dccSceneItem = dataDef

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildIntegerAttribute(self, kAttribute):
        """Builds a Integer attribute.

        Args:
            kAttribute (Object): kAttribute that represents a integer attribute to be built.

        Return:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentObject3D = kAttribute.getParent().getParent()
        parentAttrGroup = kAttribute.getParent()

        MaxPlus.SelectionManager.ClearNodeSelection()
        parentDCCSceneItem.Select()

        rt.execute('targetObj = selection[1]')
        customAttr = getattr(rt.targetObj, kAttribute.getParent().getName(), None)

        if customAttr is None:
            raise AttributeError('Could not find Attribute Group: {0} on {1}'.format(parentAttrGroup.getName(), parentObject3D.getName()))

        # Get Attribute
        dataDef = rt.CustAttributes.getDef(customAttr)
        defSource = dataDef.source
        defLines = defSource.splitlines()
        endParamIndex = defLines.index('            -- Param Def End')
        endRolloutIndex = defLines.index('            -- Rollout Def End')

        # Create param format data
        formatData = {
            'padding': '\t\t\t',
            'paramName': kAttribute.getName(),
            'initValue': str(kAttribute.getValue()).lower(),
            'enabled': str(not kAttribute.getLock()).lower(),
            'minRange': kAttribute.getMin(),
            'maxRange': kAttribute.getMax()
        }

        newParamLine = '{padding}{paramName} type: #integer ui:{paramName} default: {initValue}'
        defLines.insert(endParamIndex, newParamLine.format(**formatData))

        if formatData['minRange'] is not None and formatData['maxRange'] is not None:
            newRolloutLine = '{padding}spinner {paramName} "{paramName}" type: #integer range:[{minRange}, {maxRange}, {initValue}] enabled: {enabled}'
        else:
            newRolloutLine = '{padding}spinner {paramName} "{paramName}" type: #integer enabled: {enabled}'

        defLines.insert(endRolloutIndex, newRolloutLine.format(**formatData))

        newDef = '\n'.join(defLines)
        rt.CustAttributes.redefine(dataDef, newDef)

        parentDCCSceneItem.Deselect()

        dccSceneItem = dataDef

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildStringAttribute(self, kAttribute):
        """Builds a String attribute.

        Args:
            kAttribute (Object): kAttribute that represents a string attribute
                to be built.

        Return:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentObject3D = kAttribute.getParent().getParent()
        parentAttrGroup = kAttribute.getParent()

        MaxPlus.SelectionManager.ClearNodeSelection()
        parentDCCSceneItem.Select()

        rt.execute('targetObj = selection[1]')
        customAttr = getattr(rt.targetObj, kAttribute.getParent().getName(), None)

        if customAttr is None:
            raise AttributeError('Could not find Attribute Group: {0} on {1}'.format(parentAttrGroup.getName(), parentObject3D.getName()))

        # Get Attribute
        dataDef = rt.CustAttributes.getDef(customAttr)
        defSource = dataDef.source
        defLines = defSource.splitlines()
        endParamIndex = defLines.index('            -- Param Def End')
        endRolloutIndex = defLines.index('            -- Rollout Def End')

        # Create param format data
        formatData = {
            'padding': '\t\t\t',
            'paramName': kAttribute.getName(),
            'initValue': kAttribute.getValue(),
            'enabled': str(not kAttribute.getLock()).lower()
        }

        newParamLine = '{padding}{paramName} type:#string ui:{paramName} default:"{initValue}"'
        defLines.insert(endParamIndex, newParamLine.format(**formatData))

        newRolloutLine = '{padding}edittext {paramName} "{paramName}" type:#string enabled:{enabled}'
        defLines.insert(endRolloutIndex, newRolloutLine.format(**formatData))

        newDef = '\n'.join(defLines)
        rt.CustAttributes.redefine(dataDef, newDef)

        parentDCCSceneItem.Deselect()

        dccSceneItem = dataDef

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildAttributeGroup(self, kAttributeGroup):
        """Builds attribute groups on the DCC object.

        Args:
            kAttributeGroup (object): Kraken object to build the attribute
                group on.

        Return:
            bool: True if successful.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kAttributeGroup.getParent())

        MaxPlus.SelectionManager.ClearNodeSelection()
        parentDCCSceneItem.Select()

        groupName = kAttributeGroup.getName()
        if groupName == "implicitAttrGrp":
            return False

        attrDef = """attrGrpDesc=attributes {0}
        (
            parameters main rollout:{0}Rollout
            (
            -- Param Def Begin
            -- Param Def End
            )

            rollout {0}Rollout "{0}"
            (
            -- Rollout Def Begin
            -- Rollout Def End
            )
        )
        """.format(groupName)

        rt.execute('targetObj = selection[1]')
        count = rt.CustAttributes.count(rt.targetObj)

        rt.execute(attrDef)
        rt.CustAttributes.add(rt.targetObj, rt.attrGrpDesc)
        rt.CustAttributes.makeUnique(rt.targetObj, count + 1)

        parentDCCSceneItem.Deselect()

        attrCntrs = parentDCCSceneItem.BaseObject.GetCustomAttributeContainer()
        attrCntr = None
        for each in attrCntrs:
            if each.GetName() == groupName:
                attrCntr = each
                break

        dccSceneItem = attrCntr

        self._registerSceneItemPair(kAttributeGroup, dccSceneItem)

        return True

    def connectAttribute(self, kAttribute):
        """Connects the driver attribute to this one.

        Args:
            kAttribute (Object): Attribute to connect.

        Return:
            bool: True if successful.

        """

        if kAttribute.isConnected() is True:

            # Detect if driver is visibility attribute and map to correct DCC
            # attribute
            driverAttr = kAttribute.getConnection()
            if driverAttr.getName() == 'visibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                driver = dccItem
                # driver = dccItem.attr('visibility')

            elif driverAttr.getName() == 'shapeVisibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                # shape = dccItem.getShape()
                driver = dccItem
                # driver = shape.attr('visibility')

            else:
                attrGrp = self.getDCCSceneItem(kAttribute.getConnection().getParent())
                driver = None
                paramBlock = attrGrp.GetParameterBlock()
                for i in xrange(paramBlock.NumParameters):
                    param = paramBlock.GetItem(i)
                    if param.GetName() == kAttribute.getConnection().getName():
                        driver = param
                        break

            # Detect if the driven attribute is a visibility attribute and map
            # to correct DCC attribute
            if kAttribute.getName() == 'visibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                driven = dccItem
                # driven = dccItem.attr('visibility')

            elif kAttribute.getName() == 'shapeVisibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                driven = dccItem
                # shape = dccItem.getShape()
                # driven = shape.attr('visibility')
            else:
                attrGrp = self.getDCCSceneItem(kAttribute.getParent())
                driven = None
                paramBlock = attrGrp.GetParameterBlock()
                for i in xrange(paramBlock.NumParameters):
                    param = paramBlock.GetItem(i)
                    if param.GetName() == kAttribute.getName():
                        driven = param
                        break

            srcAttrGrpParent = self.getDCCSceneItem(kAttribute.getConnection().getParent().getParent())
            srcAttrGrpParent.Select()
            MaxPlus.Core.EvalMAXScript('srcAttrGrpParent = selection[1]')
            srcAttrGrpParent.Deselect()

            tgtAttrGrpParent = self.getDCCSceneItem(kAttribute.getParent().getParent())
            tgtAttrGrpParent.Select()
            MaxPlus.Core.EvalMAXScript('tgtAttrGrpParent = selection[1]')
            tgtAttrGrpParent.Deselect()

            srcStr = 'srcAttrGrpParent.baseObject.{}[#{}]'.format(kAttribute.getConnection().getParent().getName(), kAttribute.getConnection().getName())
            tgtStr = 'tgtAttrGrpParent.baseObject.{}[#{}]'.format(kAttribute.getParent().getName(), kAttribute.getName())

            print 'paramWire.connect ' + srcStr + ' ' + tgtStr + ' "' + kAttribute.getConnection().getName() + '"'
            MaxPlus.Core.EvalMAXScript('paramWire.connect ' + srcStr + ' ' + tgtStr + ' "' + kAttribute.getConnection().getName() + '"')
            # logger.warning('Connecting {} to {}'.format(kAttribute.getConnection().getPath(), kAttribute.getPath()))
            # logger.warning(driver)
            # logger.warning(driven)
            # MaxPlus.Core.EvalMAXScript("paramWire.connect srcNode.baseObject.Arm_Settings[#fkik_blend] tgtNode.baseObject.Arm_Settings[#fkik_blend] \"fkik_blend\"")

        return True


    # =========================
    # Constraint Build Methods
    # =========================
    def buildOrientationConstraint(self, kConstraint, buildName):
        """Builds an orientation constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        rotListClassID = MaxPlus.Class_ID(0x4b4b1003, 0x00000000) # Create Rotation List Controller
        rotListCtrl = MaxPlus.Factory.CreateRotationController(rotListClassID)

        rotCns = MaxPlus.Factory.CreateRotationController(MaxPlus.ClassIds.Orientation_Constraint)
        rotListCtrl.AssignController(rotCns, 0)

        rotCtrl = MaxPlus.Factory.CreateRotationController(MaxPlus.ClassIds.Euler_XYZ)

        if kConstraint.getMaintainOffset() is True:
            # Fabric's rotation order enums:
            # We need to use the negative rotation order
            # to calculate propery offset values.
            #
            # 0 XYZ
            # 1 YZX
            # 2 ZXY
            # 3 XZY
            # 4 ZYX
            # 5 YXZ

            rotOrderRemap = {
                0: 1,
                1: 3,
                2: 5,
                3: 2,
                4: 6,
                5: 4
            }

            order = rotOrderRemap[kConstraint.getConstrainee().ro.order]

            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            quat = MaxPlus.Quat()
            quat.SetEuler(math.radians(offsetAngles.x),
                          math.radians(offsetAngles.y),
                          math.radians(offsetAngles.z))

            rotCtrl.SetQuatValue(quat)

        rotListCtrl.AssignController(rotCtrl, 1)

        transform = constraineeDCCSceneItem.GetSubAnim(2)
        transform.AssignController(rotListCtrl, 1)

        for constrainer in [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]:

            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainer = selection[1]')
            constrainer.Deselect()

            MaxPlus.Core.EvalMAXScript('constrainee.rotation.controller[1].appendTarget constrainer 50')

        dccSceneItem = rotListCtrl

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPoseConstraint(self, kConstraint, buildName):
        """Builds an pose constraint represented by the kConstraint.

        Args:
            kConstraint (Object): kraken constraint object to build.

        Return:
            bool: True if successful.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        offsetXfo = kConstraint.computeOffset()

        # ====================
        # Position Constraint
        # ====================
        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        posListClassID = MaxPlus.Class_ID(0x4b4b1002, 0x00000000) # Create Position List Controller
        posListCtrl = MaxPlus.Factory.CreatePositionController(posListClassID)

        posCtrl = MaxPlus.Factory.CreatePositionController(MaxPlus.ClassIds.Position_Constraint)
        posListCtrl.AssignController(posCtrl, 0)

        posCtrl = MaxPlus.Factory.CreatePositionController(MaxPlus.ClassIds.Position_XYZ)

        if kConstraint.getMaintainOffset() is True:
            posCtrl.SetPoint3Value(MaxPlus.Point3(offsetXfo.tr.x, offsetXfo.tr.y, offsetXfo.tr.z))

        posListCtrl.AssignController(posCtrl, 1)

        transform = constraineeDCCSceneItem.GetSubAnim(2)
        transform.AssignController(posListCtrl, 0)

        constraineeDCCSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        constraineeDCCSceneItem.Deselect()

        for constrainer in [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]:

            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainer = selection[1]')
            constrainer.Deselect()

            MaxPlus.Core.EvalMAXScript('constrainee.position.controller[1].appendTarget constrainer 50')
            # MaxPlus.Core.EvalMAXScript('constrainee.position.controller.setName 1 "{}"'.format(buildName))


        # =======================
        # Orientation Constraint
        # =======================
        rotListClassID = MaxPlus.Class_ID(0x4b4b1003, 0x00000000) # Create Rotation List Controller
        rotListCtrl = MaxPlus.Factory.CreateRotationController(rotListClassID)

        rotCns = MaxPlus.Factory.CreateRotationController(MaxPlus.ClassIds.Orientation_Constraint)
        rotListCtrl.AssignController(rotCns, 0)

        rotCtrl = MaxPlus.Factory.CreateRotationController(MaxPlus.ClassIds.Euler_XYZ)

        if kConstraint.getMaintainOffset() is True:
            # Fabric's rotation order enums:
            # We need to use the negative rotation order
            # to calculate propery offset values.
            #
            # 0 XYZ
            # 1 YZX
            # 2 ZXY
            # 3 XZY
            # 4 ZYX
            # 5 YXZ

            rotOrderRemap = {
                0: 1,
                1: 3,
                2: 5,
                3: 2,
                4: 6,
                5: 4
            }

            order = rotOrderRemap[kConstraint.getConstrainee().ro.order]

            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            quat = MaxPlus.Quat()
            quat.SetEuler(math.radians(offsetAngles.x),
                          math.radians(offsetAngles.y),
                          math.radians(offsetAngles.z))

            rotCtrl.SetQuatValue(quat)

        rotListCtrl.AssignController(rotCtrl, 1)

        transform = constraineeDCCSceneItem.GetSubAnim(2)
        transform.AssignController(rotListCtrl, 1)

        for constrainer in [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]:

            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainer = selection[1]')
            constrainer.Deselect()

            MaxPlus.Core.EvalMAXScript('constrainee.rotation.controller[1].appendTarget constrainer 50')

        # ====================
        # Scale Constraint
        # ====================
        # constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        # sclListClassID = MaxPlus.Class_ID(0x4b4b1004, 0x00000000) # Create Position List Controller
        # sclListCtrl = MaxPlus.Factory.CreatePositionController(sclListClassID)

        # posCtrl = MaxPlus.Factory.CreatePositionController(MaxPlus.ClassIds.Position_Constraint)
        # sclListCtrl.AssignController(posCtrl, 0)

        # posCtrl = MaxPlus.Factory.CreatePositionController(MaxPlus.ClassIds.ScaleXYZ)

        # if kConstraint.getMaintainOffset() is True:
        #     posCtrl.SetPoint3Value(MaxPlus.Point3(offsetXfo.tr.x, offsetXfo.tr.y, offsetXfo.tr.z))

        # sclListCtrl.AssignController(posCtrl, 1)

        # transform = constraineeDCCSceneItem.GetSubAnim(2)
        # transform.AssignController(sclListCtrl, 0)

        # constraineeDCCSceneItem.Select()
        # MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        # constraineeDCCSceneItem.Deselect()

        # for constrainer in [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]:

        #     constrainer.Select()
        #     MaxPlus.Core.EvalMAXScript('constrainer = selection[1]')
        #     constrainer.Deselect()

        #     MaxPlus.Core.EvalMAXScript('constrainee.position.controller[1].appendTarget constrainer 50')

        dccSceneItem = posListCtrl

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPositionConstraint(self, kConstraint, buildName):
        """Builds an position constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            bool: True if successful.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        posListClassID = MaxPlus.Class_ID(0x4b4b1002, 0x00000000) # Create Position List Controller
        posListCtrl = MaxPlus.Factory.CreatePositionController(posListClassID)

        posCns = MaxPlus.Factory.CreatePositionController(MaxPlus.ClassIds.Position_Constraint)
        posListCtrl.AssignController(posCns, 0)

        posCtrl = MaxPlus.Factory.CreatePositionController(MaxPlus.ClassIds.Position_XYZ)
        posListCtrl.AssignController(posCtrl, 1)

        transform = tgtNode.GetSubAnim(2)
        transform.AssignController(posListCtrl, 0)

        constraineeDCCSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        constraineeDCCSceneItem.Deselect()

        for constrainer in kConstraint.getConstrainers():

            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainer = selection[1]')
            constrainer.Deselect()

            MaxPlus.Core.EvalMAXScript('constrainee.position.controller[1].appendTarget constrainer 50')
            MaxPlus.Core.EvalMAXScript('constrainee.position.controller.setName 1 "{}"'.format(buildName))

        if kConstraint.getMaintainOffset() is True:
            offsetXfo = kConstraint.computeOffset()
            offsetStr = "{} {} {}".format(offsetXfo.tr.x,
                                          offsetXfo.tr.y,
                                          offsetXfo.tr.z)

            # Set offsets on the scale constraint
            MaxPlus.Core.EvalMAXScript('constrainee.position.controller.setActive 2')
            MaxPlus.Core.EvalMAXScript('constrainee.position.controller[2].value = Point3 ' + offsetStr)
            MaxPlus.Core.EvalMAXScript('constrainee.position.controller.setActive 1')

        dccSceneItem = posListCtrl

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildScaleConstraint(self, kConstraint, buildName):
        """Builds an scale constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            bool: True if successful.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())
        dccSceneItem = None # pm.scaleConstraint(
        #     [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
        #     constraineeDCCSceneItem,
        #     name=buildName,
        #     maintainOffset=kConstraint.getMaintainOffset())

        # if kConstraint.getMaintainOffset() is True:
        #     offsetXfo = kConstraint.computeOffset()

        #     # Set offsets on the scale constraint
        #     dccSceneItem.offset.set([offsetXfo.sc.x,
        #                              offsetXfo.sc.y,
        #                              offsetXfo.sc.z])

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    # ========================
    # Component Build Methods
    # ========================
    def buildAttributeConnection(self, connectionInput):
        """Builds the connection between the attribute and the connection.

        Args:
            connectionInput (Object): Kraken connection to build.

        Return:
            bool: True if successful.

        """

        if connectionInput.isConnected() is False:
            return False

        connection = connectionInput.getConnection()
        connectionTarget = connection.getTarget()
        inputTarget = connectionInput.getTarget()

        if connection.getDataType().endswith('[]'):
            connectionTarget = connection.getTarget()[connectionInput.getIndex()]
        else:
            connectionTarget = connection.getTarget()

        connectionTargetDCCSceneItem = self.getDCCSceneItem(connectionTarget)
        targetDCCSceneItem = self.getDCCSceneItem(inputTarget)

        logger.warning('Connecting {} to {}'.format(connectionTargetDCCSceneItem, targetDCCSceneItem))

        # pm.connectAttr(connectionTargetDCCSceneItem,
        #                targetDCCSceneItem,
        #                force=True)

        return True

    # =========================
    # Operator Builder Methods
    # =========================
    def buildKLOperator(self, kOperator, buildName):
        """Builds KL Operators on the components.

        Args:
            kOperator (Object): Kraken operator that represents a KL
                operator.
            buildName (str): The name to use on the built object.

        Return:
            bool: True if successful.

        """

        # Code to build KL and Canvas based Operators has been merged.
        # It's important to note here that the 'isKLBased' argument is set
        # to true.
        self.buildCanvasOperator(kOperator, buildName, isKLBased=True)

        return True

    def buildCanvasOperator(self, kOperator, buildName, isKLBased=False):
        """Builds Canvas Operators on the components.

        Args:
            kOperator (object): Kraken operator that represents a Canvas
                operator.
            buildName (str): The name to use on the built object.
            isKLBased (bool): Whether the solver is based on a KL object.

        Return:
            bool: True if successful.

        """

        # def validatePortValue(rtVal, portName, portDataType):
        #     """Validate port value type when passing built in Python types.

        #     Args:
        #         rtVal (RTVal): rtValue object.
        #         portName (str): Name of the argument being validated.
        #         portDataType (str): Type of the argument being validated.

        #     """

        #     # Validate types when passing a built in Python type
        #     if type(rtVal) in (bool, str, int, float):
        #         if portDataType in ('Scalar', 'Float32', 'UInt32'):
        #             if type(rtVal) not in (float, int):
        #                 raise TypeError(kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

        #         elif portDataType == 'Boolean':
        #             if type(rtVal) != bool and not (type(rtVal) == int and (rtVal == 0 or rtVal == 1)):
        #                 raise TypeError(kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

        #         elif portDataType == 'String':
        #             if type(rtVal) != str:
        #                 raise TypeError(kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

        # try:
        #     if isKLBased is False:
        #         host = ks.getCoreClient().DFG.host
        #         opBinding = host.createBindingToPreset(kOperator.getPresetPath())
        #         node = opBinding.getExec()

        #         portTypeMap = {
        #             0: 'In',
        #             1: 'IO',
        #             2: 'Out'
        #         }

        #     # Create Canvas Operator
        #     canvasNode = pm.createNode('canvasNode', name=buildName)
        #     self._registerSceneItemPair(kOperator, pm.PyNode(canvasNode))

        #     config = Config.getInstance()
        #     nameTemplate = config.getNameTemplate()
        #     typeTokens = nameTemplate['types']
        #     opTypeToken = typeTokens.get(type(kOperator).__name__, 'op')
        #     solverNodeName = '_'.join([kOperator.getName(), opTypeToken])
        #     solverSolveNodeName = '_'.join([kOperator.getName(), 'solve', opTypeToken])

        #     if isKLBased is True:

        #         pm.FabricCanvasSetExtDeps(mayaNode=canvasNode,
        #                                   execPath="",
        #                                   extDep=kOperator.getExtension())

        #         solverTypeName = kOperator.getSolverTypeName()

        #         # Create Solver Function Node
        #         dfgEntry = "dfgEntry {\n  solver = " + solverTypeName + "();\n}"
        #         solverNodeCode = "{}\n\n{}".format('require ' + kOperator.getExtension() + ';', dfgEntry)

        #         pm.FabricCanvasAddFunc(mayaNode=canvasNode,
        #                                execPath="",
        #                                title=solverNodeName,
        #                                code=solverNodeCode, xPos="-220", yPos="100")

        #         pm.FabricCanvasAddPort(mayaNode=canvasNode,
        #                                execPath=solverNodeName,
        #                                desiredPortName="solver",
        #                                portType="Out",
        #                                typeSpec=solverTypeName,
        #                                connectToPortPath="",
        #                                extDep=kOperator.getExtension())

        #         solverVarName = pm.FabricCanvasAddVar(mayaNode=canvasNode,
        #                                               execPath="",
        #                                               desiredNodeName="solverVar",
        #                                               xPos="-75",
        #                                               yPos="100",
        #                                               type=solverTypeName,
        #                                               extDep=kOperator.getExtension())

        #         pm.FabricCanvasConnect(mayaNode=canvasNode,
        #                                execPath="",
        #                                srcPortPath=solverNodeName + ".solver",
        #                                dstPortPath=solverVarName + ".value")

        #         # Crate Solver "Solve" Function Node
        #         pm.FabricCanvasAddFunc(mayaNode=canvasNode,
        #                                execPath="",
        #                                title=solverSolveNodeName,
        #                                code="dfgEntry {}", xPos="100", yPos="100")

        #         pm.FabricCanvasAddPort(mayaNode=canvasNode,
        #                                execPath=solverSolveNodeName,
        #                                desiredPortName="solver",
        #                                portType="IO",
        #                                typeSpec=solverTypeName,
        #                                connectToPortPath="",
        #                                extDep=kOperator.getExtension())

        #         pm.FabricCanvasConnect(mayaNode=canvasNode,
        #                                execPath="",
        #                                srcPortPath=solverVarName + ".value",
        #                                dstPortPath=solverSolveNodeName + ".solver")

        #         pm.FabricCanvasConnect(mayaNode=canvasNode,
        #                                execPath="",
        #                                srcPortPath=solverSolveNodeName + ".solver",
        #                                dstPortPath="exec")
        #     else:
        #         pm.FabricCanvasSetExtDeps(mayaNode=canvasNode,
        #                                   execPath="",
        #                                   extDep="Kraken")

        #         graphNodeName = pm.FabricCanvasInstPreset(
        #             mayaNode=canvasNode,
        #             execPath="",
        #             presetPath=kOperator.getPresetPath(),
        #             xPos="100",
        #             yPos="100")

        #     portCount = 0
        #     if isKLBased is True:
        #         portCount = len(kOperator.getSolverArgs())
        #     else:
        #         portCount = node.getExecPortCount()

        #     for i in xrange(portCount):

        #         if isKLBased is True:
        #             args = kOperator.getSolverArgs()
        #             arg = args[i]
        #             portName = arg.name.getSimpleType()
        #             portConnectionType = arg.connectionType.getSimpleType()
        #             portDataType = arg.dataType.getSimpleType()
        #         else:
        #             portName = node.getExecPortName(i)
        #             portConnectionType = portTypeMap[node.getExecPortType(i)]
        #             rtVal = opBinding.getArgValue(portName)
        #             portDataType = rtVal.getTypeName().getSimpleType()

        #         if portConnectionType == 'In':
        #             if isKLBased is True:
        #                 pm.FabricCanvasAddPort(mayaNode=canvasNode,
        #                                        execPath="",
        #                                        desiredPortName=portName,
        #                                        portType="In",
        #                                        typeSpec=portDataType,
        #                                        connectToPortPath="")

        #                 pm.FabricCanvasAddPort(mayaNode=canvasNode,
        #                                        execPath=solverSolveNodeName,
        #                                        desiredPortName=portName,
        #                                        portType="In",
        #                                        typeSpec=portDataType,
        #                                        connectToPortPath="")

        #                 pm.FabricCanvasConnect(mayaNode=canvasNode,
        #                                        execPath="",
        #                                        srcPortPath=portName,
        #                                        dstPortPath=solverSolveNodeName + "." + portName)

        #             else:
        #                 if portDataType != 'Execute':
        #                     pm.FabricCanvasAddPort(
        #                         mayaNode=canvasNode,
        #                         execPath="",
        #                         desiredPortName=portName,
        #                         portType="In",
        #                         typeSpec=portDataType,
        #                         connectToPortPath="")

        #                 pm.FabricCanvasConnect(
        #                     mayaNode=canvasNode,
        #                     execPath="",
        #                     srcPortPath=portName,
        #                     dstPortPath=graphNodeName + "." + portName)

        #         elif portConnectionType in ['IO', 'Out']:

        #             if portDataType in ('Execute', 'InlineInstance', 'DrawingHandle'):
        #                 # Don't expose invalid Maya data type InlineInstance, instead connect to exec port
        #                 dstPortPath = "exec"
        #             else:
        #                 dstPortPath = portName

        #             if isKLBased is True:
        #                 srcPortNode = solverSolveNodeName
        #                 pm.FabricCanvasAddPort(
        #                     mayaNode=canvasNode,
        #                     execPath=solverSolveNodeName,
        #                     desiredPortName=portName,
        #                     portType="Out",
        #                     typeSpec=portDataType,
        #                     connectToPortPath="")
        #             else:
        #                 srcPortNode = graphNodeName

        #             if portDataType not in ('Execute', 'InlineInstance', 'DrawingHandle'):
        #                 pm.FabricCanvasAddPort(
        #                     mayaNode=canvasNode,
        #                     execPath="",
        #                     desiredPortName=portName,
        #                     portType="Out",
        #                     typeSpec=portDataType,
        #                     connectToPortPath="")

        #             pm.FabricCanvasConnect(
        #                 mayaNode=canvasNode,
        #                 execPath="",
        #                 srcPortPath=srcPortNode + "." + portName,
        #                 dstPortPath=dstPortPath)

        #         else:
        #             raise Exception("Invalid connection type:" + portConnectionType)

        #         if portDataType == 'EvalContext':
        #             continue
        #         elif portDataType == 'Execute':
        #             continue
        #         elif portDataType == 'DrawingHandle':
        #             continue
        #         elif portDataType == 'InlineDebugShape':
        #             continue
        #         elif portDataType == 'Execute' and portName == 'exec':
        #             continue

        #         if portName == 'time':
        #             pm.expression(o=canvasNode + '.time', s=canvasNode + '.time = time;')
        #             continue
        #         if portName == 'frame':
        #             pm.expression(o=canvasNode + '.frame', s=canvasNode + '.frame = frame;')
        #             continue

        #         # Get the port's input from the DCC
        #         if portConnectionType == 'In':
        #             connectedObjects = kOperator.getInput(portName)
        #         elif portConnectionType in ['IO', 'Out']:
        #             connectedObjects = kOperator.getOutput(portName)

        #         if portDataType.endswith('[]'):

        #             # In CanvasMaya, output arrays are not resized by the system
        #             # prior to calling into Canvas, so we explicily resize the
        #             # arrays in the generated operator stub code.
        #             if connectedObjects is None:
        #                 connectedObjects = []

        #             connectionTargets = []
        #             for i in xrange(len(connectedObjects)):
        #                 opObject = connectedObjects[i]
        #                 dccSceneItem = self.getDCCSceneItem(opObject)

        #                 if hasattr(opObject, "getName"):
        #                     # Handle output connections to visibility attributes.
        #                     if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
        #                         dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
        #                         dccSceneItem = dccItem.attr('visibility')
        #                     elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
        #                         dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
        #                         shape = dccItem.getShape()
        #                         dccSceneItem = shape.attr('visibility')

        #                 connectionTargets.append(
        #                     {
        #                         'opObject': opObject,
        #                         'dccSceneItem': dccSceneItem
        #                     })
        #         else:
        #             if connectedObjects is None:
        #                 if isKLBased:
        #                     opType = kOperator.getExtension() + ":" + kOperator.getSolverTypeName()
        #                 else:
        #                     opType = kOperator.getPresetPath()

        #                 logger.warning("Operator '" + solverSolveNodeName +
        #                                "' of type '" + opType +
        #                                "' port '" + portName + "' not connected.")

        #             opObject = connectedObjects
        #             dccSceneItem = self.getDCCSceneItem(opObject)
        #             if hasattr(opObject, "getName"):
        #                 # Handle output connections to visibility attributes.
        #                 if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
        #                     dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
        #                     dccSceneItem = dccItem.attr('visibility')
        #                 elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
        #                     dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
        #                     shape = dccItem.getShape()
        #                     dccSceneItem = shape.attr('visibility')

        #             connectionTargets = {
        #                 'opObject': opObject,
        #                 'dccSceneItem': dccSceneItem
        #             }

        #         # Add the Canvas Port for each port.
        #         if portConnectionType == 'In':

        #             def connectInput(tgt, opObject, dccSceneItem):
        #                 if isinstance(opObject, Attribute):
        #                     pm.connectAttr(dccSceneItem, tgt)
        #                 elif isinstance(opObject, Object3D):
        #                     pm.connectAttr(dccSceneItem.attr('worldMatrix'), tgt)
        #                 elif isinstance(opObject, Xfo):
        #                     self.setMat44Attr(tgt.partition(".")[0], tgt.partition(".")[2], opObject.toMat44())
        #                 elif isinstance(opObject, Mat44):
        #                     self.setMat44Attr(tgt.partition(".")[0], tgt.partition(".")[2], opObject)
        #                 elif isinstance(opObject, Vec2):
        #                     pm.setAttr(tgt, opObject.x, opObject.y, type="double2")
        #                 elif isinstance(opObject, Vec3):
        #                     pm.setAttr(tgt, opObject.x, opObject.y, opObject.z, type="double3")
        #                 else:
        #                     validatePortValue(opObject, portName, portDataType)

        #                     pm.setAttr(tgt, opObject)

        #             if portDataType.endswith('[]'):
        #                 for i in xrange(len(connectionTargets)):
        #                     connectInput(
        #                         canvasNode + "." + portName + '[' + str(i) + ']',
        #                         connectionTargets[i]['opObject'],
        #                         connectionTargets[i]['dccSceneItem'])
        #             else:
        #                 connectInput(
        #                     canvasNode + "." + portName,
        #                     connectionTargets['opObject'],
        #                     connectionTargets['dccSceneItem'])

        #         elif portConnectionType in ['IO', 'Out']:

        #             def connectOutput(src, opObject, dccSceneItem):
        #                 if isinstance(opObject, Attribute):
        #                     pm.connectAttr(src, dccSceneItem)
        #                 elif isinstance(opObject, Object3D):
        #                     decomposeNode = pm.createNode('decomposeMatrix')
        #                     pm.connectAttr(src,
        #                                    decomposeNode.attr("inputMatrix"),
        #                                    force=True)

        #                     decomposeNode.attr("outputRotate").connect(dccSceneItem.attr("rotate"))
        #                     decomposeNode.attr("outputScale").connect(dccSceneItem.attr("scale"))
        #                     decomposeNode.attr("outputTranslate").connect(dccSceneItem.attr("translate"))
        #                 elif isinstance(opObject, Xfo):
        #                     raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Xfo outputs types directly!")
        #                 elif isinstance(opObject, Mat44):
        #                     raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Mat44 types directly!")
        #                 else:
        #                     raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Python built-in types [%s] directly!" % (src, opObject.__class__.__name__))

        #             if portDataType.endswith('[]'):
        #                 for i in xrange(len(connectionTargets)):
        #                     connectOutput(
        #                         str(canvasNode + "." + portName) + '[' + str(i) + ']',
        #                         connectionTargets[i]['opObject'],
        #                         connectionTargets[i]['dccSceneItem'])
        #             else:
        #                 if connectionTargets['opObject'] is not None:
        #                     connectOutput(
        #                         str(canvasNode + "." + portName),
        #                         connectionTargets['opObject'],
        #                         connectionTargets['dccSceneItem'])

        #     if isKLBased is True:
        #         opSourceCode = kOperator.generateSourceCode()
        #         pm.FabricCanvasSetCode(mayaNode=canvasNode,
        #                                execPath=solverSolveNodeName,
        #                                code=opSourceCode)

        # finally:
        #     pass

        return True

    # ==================
    # Parameter Methods
    # ==================
    def lockParameters(self, kSceneItem):
        """Locks flagged SRT parameters.

        Args:
            kSceneItem (Object): Kraken object to lock the SRT parameters on.

        Return:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        paramMap = {
            'lockXTranslation': 1,
            'lockYTranslation': 2,
            'lockZTranslation': 3,
            'lockXRotation': 4,
            'lockYRotation': 5,
            'lockZRotation': 6,
            'lockXScale': 7,
            'lockYScale': 8,
            'lockZScale': 9
        }

        locks = []


        # Lock Translation
        if kSceneItem.testFlag("lockXTranslation") is True:
            locks.append(1)

        if kSceneItem.testFlag("lockYTranslation") is True:
            locks.append(2)

        if kSceneItem.testFlag("lockZTranslation") is True:
            locks.append(3)


        # Lock Rotation
        if kSceneItem.testFlag("lockXRotation") is True:
            locks.append(4)

        if kSceneItem.testFlag("lockYRotation") is True:
            locks.append(5)

        if kSceneItem.testFlag("lockZRotation") is True:
            locks.append(6)


        # Lock Scale
        if kSceneItem.testFlag("lockXScale") is True:
            locks.append(7)

        if kSceneItem.testFlag("lockYScale") is True:
            locks.append(8)

        if kSceneItem.testFlag("lockZScale") is True:
            locks.append(9)

        lockScript = 'setTransformLockFlags $ #{' + ','.join([str(x) for x in locks]) + '}'

        dccSceneItem.Select()
        MaxPlus.Core.EvalMAXScript(lockScript)
        dccSceneItem.Deselect()

        return True

    # ===================
    # Visibility Methods
    # ===================
    def setVisibility(self, kSceneItem):
        """Sets the visibility of the object after its been created.

        Args:
            kSceneItem (Object): The scene item to set the visibility on.

        Return:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        # Set Visibility
        visAttr = kSceneItem.getVisibilityAttr()
        if visAttr.isConnected() is False and kSceneItem.getVisibility() is False:
            dccSceneItem.SetHidden(False)

        # Set Shape Visibility
        # shapeVisAttr = kSceneItem.getShapeVisibilityAttr()

        return True

    # ================
    # Display Methods
    # ================
    def setObjectColor(self, kSceneItem):
        """Sets the color on the dccSceneItem.

        Args:
            kSceneItem (object): kraken object to set the color on.

        Return:
            bool: True if successful.

        """

        colors = self.config.getColors()
        dccSceneItem = self.getDCCSceneItem(kSceneItem)
        buildColor = self.getBuildColor(kSceneItem)

        if buildColor is not None:

            if type(buildColor) is str:

                # Color in config is stored as rgb scalar values in a list
                if type(colors[buildColor]) is list:
                    dccSceneItem.SetWireColor(MaxPlus.Color(colors[buildColor][0], colors[buildColor][1], colors[buildColor][2]))

                # Color in config is stored as a Color object
                elif type(colors[buildColor]).__name__ == 'Color':
                    dccSceneItem.SetWireColor(MaxPlus.Color(colors[buildColor].r, colors[buildColor].g, colors[buildColor].b))

            elif type(buildColor).__name__ == 'Color':
                dccSceneItem.SetWireColor(MaxPlus.Color(colors[buildColor].r, colors[buildColor].g, colors[buildColor].b))

        return True

    # ==================
    # Transform Methods
    # ==================
    def setTransform(self, kSceneItem):
        """Translates the transform to Maya transform.

        Args:
            kSceneItem -- Object: object to set the transform on.

        Return:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        sceneItemXfo = kSceneItem.xfo
        rotateUpXfo = Xfo()
        rotateUpXfo.ori = Quat().setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))
        maxXfo = rotateUpXfo * sceneItemXfo

        krakenMat44 = maxXfo.toMat44().transpose()

        mat3 = MaxPlus.Matrix3(
            MaxPlus.Point3(krakenMat44.row0.x, krakenMat44.row0.y, krakenMat44.row0.z),
            MaxPlus.Point3(krakenMat44.row1.x, krakenMat44.row1.y, krakenMat44.row1.z),
            MaxPlus.Point3(krakenMat44.row2.x, krakenMat44.row2.y, krakenMat44.row2.z),
            MaxPlus.Point3(maxXfo.tr.x * 10.0,
                           maxXfo.tr.y * 10.0,
                           maxXfo.tr.z * 10.0))

        dccSceneItem.SetWorldTM(mat3)

        rotOrderRemap = {
                0: 1,
                1: 3,
                2: 5,
                3: 2,
                4: 6,
                5: 4
            }

        order = rotOrderRemap[kSceneItem.ro.order]

        dccSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('tgtObj = selection[1]')
        dccSceneItem.Deselect()

        MaxPlus.Core.EvalMAXScript('tgtObj.rotation.controller.axisorder = {}'.format(str(order)))

        return True

    def setMat44Attr(self, dccSceneItemName, attr, mat44):
        """Sets a matrix attribute directly with values from a fabric Mat44.

        Note: Fabric and Maya's matrix row orders are reversed, so we transpose
        the matrix first.

        Args:
            dccSceneItemName (str): name of dccSceneItem.
            attr (str): name of matrix attribute to set.
            mat44 (Mat44): matrix value.

        Return:
            bool: True if successful.

        """

        # mat44 = mat44.transpose()
        # matrix = []
        # rows = [mat44.row0, mat44.row1, mat44.row2, mat44.row3]
        # for row in rows:
        #     matrix.extend([row.x, row.y, row.z, row.t])

        # cmds.setAttr(dccSceneItemName + "." + attr, matrix, type="matrix")

        return True

    # ==============
    # Build Methods
    # ==============
    def _preBuild(self, kSceneItem):
        """Pre-Build commands.

        Args:
            kSceneItem (Object): Kraken kSceneItem object to build.

        Return:
            bool: True if successful.

        """

        return True

    def _postBuild(self, kSceneItem):
        """Post-Build commands.

        Args:
            kSceneItem (object): kraken kSceneItem object to run post-build
                operations on.

        Return:
            bool: True if successful.

        """

        super(Builder, self)._postBuild(kSceneItem)

        MaxPlus.ViewportManager.ForceCompleteRedraw()

        return True
