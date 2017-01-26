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

# Rotation order remapping
# Max's enums don't map directly to the Fabric rotation orders
#
# Fabric | Max
# ---------------
# 0 ZYX  | 6 ZYX
# 1 XZY  | 2 XZY
# 2 YXZ  | 4 YXZ
# 3 YZX  | 3 YZX
# 4 XYZ  | 1 XYZ
# 5 ZXY  | 5 ZXY

ROT_ORDER_REMAP = {
    0: 6,
    1: 2,
    2: 4,
    3: 3,
    4: 1,
    5: 5
}


class Builder(Builder):
    """Builder object for building Kraken objects in Maya."""

    def __init__(self):
        super(Builder, self).__init__()

    def deleteBuildElements(self):
        """Clear out all dcc built elements from the scene if exist."""


        for builtElement in self._buildElements:
            if builtElement['src'].isOfAnyType(('Attribute',
                                                'AttributeGroup',
                                                'Constraint',
                                                'Operator')):
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
                    continue

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
        paramBlock = node.BaseObject.GetParameterBlock()
        sizeParam = paramBlock.GetParamByName('size')
        sizeParam.SetValue(1)

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
        paramBlock = node.BaseObject.GetParameterBlock()
        sizeParam = paramBlock.GetParamByName('size')
        sizeParam.SetValue(1)

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
        paramBlock = node.BaseObject.GetParameterBlock()
        sizeParam = paramBlock.GetParamByName('size')
        sizeParam.SetValue(1)

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
        paramBlock = node.BaseObject.GetParameterBlock()
        sizeParam = paramBlock.GetParamByName('size')
        sizeParam.SetValue(1)

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
        node.BaseObject.ParameterBlock.Length.Value = 1.0
        node.BaseObject.ParameterBlock.Width.Value = kSceneItem.getRadius() * 0.5
        node.BaseObject.ParameterBlock.Height.Value = kSceneItem.getRadius() * 0.5

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
        paramBlock = node.BaseObject.GetParameterBlock()
        sizeParam = paramBlock.GetParamByName('size')
        sizeParam.SetValue(1)

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

        self._registerSceneItemPair(kAttribute, (parentDCCSceneItem, customAttr, kAttribute.getName()))

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

        self._registerSceneItemPair(kAttribute, (parentDCCSceneItem, customAttr, kAttribute.getName()))
        # self._registerSceneItemPair(kAttribute, dccSceneItem)

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
            'enabled': "true",  # str(not kAttribute.getLock()).lower(),
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

        self._registerSceneItemPair(kAttribute, (parentDCCSceneItem, customAttr, kAttribute.getName()))

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

        self._registerSceneItemPair(kAttribute, (parentDCCSceneItem, customAttr, kAttribute.getName()))

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

            srcStr = None
            tgtStr = None

            # Detect if driver is visibility attribute and map to correct DCC
            # attribute
            driverAttr = kAttribute.getConnection()
            if driverAttr.getName() == 'visibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                logger.warning('Connection to/from visibility is not supported currently!')
                pass
                # dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                # driver = dccItem.attr('visibility')

                # TODO: Figure out a valid reliable way to connect attributes to
                # and from visibility!

            elif driverAttr.getName() == 'shapeVisibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                logger.warning('Connection to/from visibility is not supported currently!')
                pass
                # dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                # shape = dccItem.getShape()
                # driver = shape.attr('visibility')

                # TODO: Figure out a valid reliable way to connect attributes to
                # and from visibility!

            else:
                srcAttrGrpParent = self.getDCCSceneItem(kAttribute.getConnection().getParent().getParent())
                srcAttrGrpParent.Select()
                MaxPlus.Core.EvalMAXScript('srcAttrGrpParent = selection[1]')
                srcAttrGrpParent.Deselect()

                srcStr = 'srcAttrGrpParent.baseObject.{}[#{}]'.format(kAttribute.getConnection().getParent().getName(), kAttribute.getConnection().getName())

            # Detect if the driven attribute is a visibility attribute and map
            # to correct DCC attribute
            if kAttribute.getName() == 'visibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                logger.warning('Connection to/from visibility is not supported currently!')
                pass
                # dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                # driven = dccItem.attr('visibility')

                # TODO: Figure out a valid reliable way to connect attributes to
                # and from visibility!

            elif kAttribute.getName() == 'shapeVisibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                logger.warning('Connection to/from visibility is not supported currently!')
                pass
                # dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                # shape = dccItem.getShape()
                # driven = shape.attr('visibility')

                # TODO: Figure out a valid reliable way to connect attributes to
                # and from visibility!
            else:
                tgtAttrGrpParent = self.getDCCSceneItem(kAttribute.getParent().getParent())
                tgtAttrGrpParent.Select()
                MaxPlus.Core.EvalMAXScript('tgtAttrGrpParent = selection[1]')
                tgtAttrGrpParent.Deselect()

                tgtStr = 'tgtAttrGrpParent.baseObject.{}[#{}]'.format(kAttribute.getParent().getName(), kAttribute.getName())

            if srcStr is None or tgtStr is None:
                logger.warning('Connections to visiblity parameters is not currently supported.')
            else:
                MaxPlus.Core.EvalMAXScript('paramWire.connect {} {} "{}"'.format(srcStr, tgtStr, kAttribute.getConnection().getName()))

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

        offsetXfo = kConstraint.computeOffset()

        constraineeDCCSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        constraineeDCCSceneItem.Deselect()

        MaxPlus.Core.EvalMAXScript('oriCns = FabricMatrixController()')
        rt.constrainee.controller = rt.oriCns

        if len(kConstraint.getConstrainers()) == 1:
            # Create Ports and Connections
            rt.oriCns.DFGAddPort("inMatrix",  # desiredPortName
                                    0,  # portType
                                    "Mat44",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"17\"}",
                                    execPath="")

            rt.oriCns.DFGAddPort("offsetQuat",  # desiredPortName
                                    0,  # portType
                                    "Quat",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            matUpperLeftNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.UpperLeft",  # presetPath
                rt.Point2(-500, 95))

            quatFromMatNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.SetFromMat33",  # presetPath
                rt.Point2(-84, 125))

            matMulNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Core.Math.Mul",  # presetPath
                rt.Point2(100, 100))

            matSetRotNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.SetRotation",  # presetPath
                rt.Point2(100, 100))

            rt.oriCns.DFGConnect("inMatrix", matUpperLeftNodeName + ".this", execPath="")
            rt.oriCns.DFGConnect(matUpperLeftNodeName + ".result", quatFromMatNodeName + ".mat", execPath="")
            rt.oriCns.DFGConnect(quatFromMatNodeName + ".result", matMulNodeName + ".lhs", execPath="")
            rt.oriCns.DFGConnect("offsetQuat", matMulNodeName + ".rhs", execPath="")
            rt.oriCns.DFGConnect(matMulNodeName + ".result", matSetRotNodeName + ".q", execPath="")
            rt.oriCns.DFGConnect(matSetRotNodeName + ".this", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                quat = offsetXfo.ori
                quatJSON = quat.getRTVal().getJSON().getSimpleType()
                rt.oriCns.DFGSetArgValue("offsetQuat", quatJSON)

            constrainer = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainerObj = selection[1]')
            constrainer.Deselect()

            script = "constrainee.transform.controller.inMatrix = constrainerObj"
            MaxPlus.Core.EvalMAXScript(script)

        elif len(kConstraint.getConstrainers()) > 1:
            # Create Ports and Connections
            rt.oriCns.DFGAddPort("inMatrices",  # desiredPortName
                                    0,  # portType
                                    "Mat44[]",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"2065\"}",
                                    execPath="")

            rt.oriCns.DFGAddPort("offsetQuat",  # desiredPortName
                                    0,  # portType
                                    "Quat",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            arrayAvgNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Core.Array.Average",  # presetPath
                rt.Point2(-560, 30))

            matUpperLeftNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.UpperLeft",  # presetPath
                rt.Point2(-310, 55))

            quatFromMatNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.SetFromMat33",  # presetPath
                rt.Point2(-150, 75))

            matMulNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Core.Math.Mul",  # presetPath
                rt.Point2(55, 100))

            matSetRotNodeName = rt.oriCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.SetRotation",  # presetPath
                rt.Point2(215, 120))

            rt.oriCns.DFGConnect("inMatrices", arrayAvgNodeName + ".array", execPath="")
            rt.oriCns.DFGConnect(arrayAvgNodeName + ".result", matUpperLeftNodeName + ".this", execPath="")
            rt.oriCns.DFGConnect(matUpperLeftNodeName + ".result", quatFromMatNodeName + ".mat", execPath="")
            rt.oriCns.DFGConnect(quatFromMatNodeName + ".result", matMulNodeName + ".lhs", execPath="")
            rt.oriCns.DFGConnect("offsetQuat", matMulNodeName + ".rhs", execPath="")
            rt.oriCns.DFGConnect(matMulNodeName + ".result", matSetRotNodeName + ".q", execPath="")
            rt.oriCns.DFGConnect(matSetRotNodeName + ".this", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                quat = offsetXfo.ori
                quatJSON = quat.getRTVal().getJSON().getSimpleType()
                rt.oriCns.DFGSetArgValue("offsetQuat", quatJSON)

            # Build array of objects to set to the input
            constrainers = [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]
            MaxPlus.Core.EvalMAXScript('srcArrayObjs = #()')
            for i in xrange(len(constrainers)):
                constrainers[i].Select()
                MaxPlus.Core.EvalMAXScript('append srcArrayObjs selection[1]')
                constrainers[i].Deselect()

            script = "constrainee.transform.controller.inMatrices = srcArrayObjs"
            MaxPlus.Core.EvalMAXScript(script)
        else:
            raise ValueError("There are no constrainers in constraint: {}".format(kConstraint.getPath()))

        dccSceneItem = rt.oriCns

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

        constraineeDCCSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        constraineeDCCSceneItem.Deselect()

        MaxPlus.Core.EvalMAXScript('parentCns = FabricMatrixController()')
        rt.constrainee.controller = rt.parentCns

        if len(kConstraint.getConstrainers()) == 1:
            # Create Ports and Connections
            rt.parentCns.DFGAddPort("inMatrix",  # desiredPortName
                                    0,  # portType
                                    "Mat44",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"17\"}",
                                    execPath="")

            rt.parentCns.DFGAddPort("offsetMatrix",  # desiredPortName
                                    0,  # portType
                                    "Mat44",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            matMulNodeName = rt.parentCns.DFGInstPreset("Fabric.Core.Math.Mul",  # presetPath
                                                        rt.Point2(100, 100))

            rt.parentCns.DFGConnect("inMatrix", matMulNodeName + ".lhs", execPath="")
            rt.parentCns.DFGConnect("offsetMatrix", matMulNodeName + ".rhs", execPath="")
            rt.parentCns.DFGConnect(matMulNodeName + ".result", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                mat44 = offsetXfo.toMat44()
                mat44JSON = mat44.getRTVal().getJSON().getSimpleType()
                rt.parentCns.DFGSetArgValue("offsetMatrix", mat44JSON)

            constrainer = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainerObj = selection[1]')
            constrainer.Deselect()

            script = "constrainee.transform.controller.inMatrix = constrainerObj"
            MaxPlus.Core.EvalMAXScript(script)

        elif len(kConstraint.getConstrainers()) > 1:
            # Create Ports and Connections
            rt.parentCns.DFGAddPort("inMatrices",  # desiredPortName
                                    0,  # portType
                                    "Mat44[]",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"2065\"}",
                                    execPath="")

            rt.parentCns.DFGAddPort("offsetMatrix",  # desiredPortName
                                    0,  # portType
                                    "Mat44",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            arrayAvgNodeName = rt.parentCns.DFGInstPreset("Fabric.Core.Array.Average",  # presetPath
                                                        rt.Point2(-126,78))

            matMulNodeName = rt.parentCns.DFGInstPreset("Fabric.Core.Math.Mul",  # presetPath
                                                        rt.Point2(100, 100))

            rt.parentCns.DFGConnect("inMatrices", arrayAvgNodeName + ".array", execPath="")
            rt.parentCns.DFGConnect(arrayAvgNodeName + ".result", matMulNodeName + ".lhs", execPath="")
            rt.parentCns.DFGConnect("offsetMatrix", matMulNodeName + ".rhs", execPath="")
            rt.parentCns.DFGConnect(matMulNodeName + ".result", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                mat44 = offsetXfo.toMat44()
                mat44JSON = mat44.getRTVal().getJSON().getSimpleType()
                rt.parentCns.DFGSetArgValue("offsetMatrix", mat44JSON)

            # Build array of objects to set to the input
            constrainers = [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]
            MaxPlus.Core.EvalMAXScript('srcArrayObjs = #()')
            for i in xrange(len(constrainers)):
                constrainers[i].Select()
                MaxPlus.Core.EvalMAXScript('append srcArrayObjs selection[1]')
                constrainers[i].Deselect()

            script = "constrainee.transform.controller.inMatrices = srcArrayObjs"
            MaxPlus.Core.EvalMAXScript(script)
        else:
            raise ValueError("There are no constrainers in constraint: {}".format(kConstraint.getPath()))

        dccSceneItem = rt.parentCns

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

        offsetXfo = kConstraint.computeOffset()

        constraineeDCCSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        constraineeDCCSceneItem.Deselect()

        MaxPlus.Core.EvalMAXScript('posCns = FabricMatrixController()')
        rt.constrainee.controller = rt.posCns

        if len(kConstraint.getConstrainers()) == 1:
            # Create Ports and Connections
            rt.posCns.DFGAddPort("inMatrix",  # desiredPortName
                                    0,  # portType
                                    "Mat44",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"17\"}",
                                    execPath="")

            rt.posCns.DFGAddPort("offsetVec",  # desiredPortName
                                    0,  # portType
                                    "Vec3",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            matTransNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.Translation",  # presetPath
                rt.Point2(-40, 106))

            addNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Core.Math.Add",  # presetPath
                rt.Point2(300, 152))

            matSetTransNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.SetTranslation",  # presetPath
                rt.Point2(430, 175))

            degToRadNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Func.Math_degToRad",  # presetPath
                rt.Point2(-380, 242))

            rt.posCns.DFGSetPortDefaultValue(degToRadNodeName + ".val", "90.0")

            quatSetFromAxisNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.SetFromAxisAndAngle",  # presetPath
                rt.Point2(-190, 242))

            axisVecJSON = Vec3(1, 0, 0).getRTVal().getJSON().getSimpleType()
            rt.posCns.DFGSetPortDefaultValue(quatSetFromAxisNodeName + ".axis", axisVecJSON)

            quatRotVecNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.RotateVector",  # presetPath
                rt.Point2(40, 286))

            rt.posCns.DFGConnect("inMatrix", matTransNodeName + ".this", execPath="")
            rt.posCns.DFGConnect(matTransNodeName + ".result", addNodeName + ".lhs", execPath="")
            rt.posCns.DFGConnect(degToRadNodeName + ".result", quatSetFromAxisNodeName + ".angle", execPath="")
            rt.posCns.DFGConnect(quatSetFromAxisNodeName + ".result", quatRotVecNodeName + ".this", execPath="")
            rt.posCns.DFGConnect("offsetVec", quatRotVecNodeName + ".v", execPath="")
            rt.posCns.DFGConnect(quatRotVecNodeName + ".result", addNodeName + ".rhs", execPath="")
            rt.posCns.DFGConnect(addNodeName + ".result", matSetTransNodeName + ".tr", execPath="")
            rt.posCns.DFGConnect(matSetTransNodeName + ".this", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                tr = offsetXfo.tr
                trJSON = tr.getRTVal().getJSON().getSimpleType()
                rt.posCns.DFGSetArgValue("offsetVec", trJSON)

            constrainer = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainerObj = selection[1]')
            constrainer.Deselect()

            script = "constrainee.transform.controller.inMatrix = constrainerObj"
            MaxPlus.Core.EvalMAXScript(script)

        elif len(kConstraint.getConstrainers()) > 1:
            # Create Ports and Connections
            rt.posCns.DFGAddPort("inMatrices",  # desiredPortName
                                    0,  # portType
                                    "Mat44[]",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"2065\"}",
                                    execPath="")

            rt.posCns.DFGAddPort("offsetVec",  # desiredPortName
                                    0,  # portType
                                    "Vec3",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            matTransArrayNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.TranslationArray",  # presetPath
                rt.Point2(-40, 106))

            arrayAvgNodeNameName = rt.posCns.DFGInstPreset(
                "Fabric.Core.Array.Average",  # presetPath
                rt.Point2(-160, 130))

            addNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Core.Math.Add",  # presetPath
                rt.Point2(300, 152))

            matSetTransNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.SetTranslation",  # presetPath
                rt.Point2(430, 175))

            degToRadNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Func.Math_degToRad",  # presetPath
                rt.Point2(-380, 242))

            rt.posCns.DFGSetPortDefaultValue(degToRadNodeName + ".val", "90.0")

            quatSetFromAxisNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.SetFromAxisAndAngle",  # presetPath
                rt.Point2(-190, 242))

            axisVecJSON = Vec3(1, 0, 0).getRTVal().getJSON().getSimpleType()
            rt.posCns.DFGSetPortDefaultValue(quatSetFromAxisNodeName + ".axis", axisVecJSON)

            quatRotVecNodeName = rt.posCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.RotateVector",  # presetPath
                rt.Point2(40, 286))

            rt.posCns.DFGConnect("inMatrices", matTransArrayNodeName + ".this", execPath="")
            rt.posCns.DFGConnect(matTransArrayNodeName + ".result", arrayAvgNodeNameName + ".array", execPath="")
            rt.posCns.DFGConnect(arrayAvgNodeNameName + ".result", addNodeName + ".lhs", execPath="")
            rt.posCns.DFGConnect(degToRadNodeName + ".result", quatSetFromAxisNodeName + ".angle", execPath="")
            rt.posCns.DFGConnect(quatSetFromAxisNodeName + ".result", quatRotVecNodeName + ".this", execPath="")
            rt.posCns.DFGConnect("offsetVec", quatRotVecNodeName + ".v", execPath="")
            rt.posCns.DFGConnect(quatRotVecNodeName + ".result", addNodeName + ".rhs", execPath="")
            rt.posCns.DFGConnect(addNodeName + ".result", matSetTransNodeName + ".tr", execPath="")
            rt.posCns.DFGConnect(matSetTransNodeName + ".this", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                tr = offsetXfo.tr
                trJSON = tr.getRTVal().getJSON().getSimpleType()
                rt.posCns.DFGSetArgValue("offsetVec", trJSON)

            # Build array of objects to set to the input
            constrainers = [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]
            MaxPlus.Core.EvalMAXScript('srcArrayObjs = #()')
            for i in xrange(len(constrainers)):
                constrainers[i].Select()
                MaxPlus.Core.EvalMAXScript('append srcArrayObjs selection[1]')
                constrainers[i].Deselect()

            script = "constrainee.transform.controller.inMatrices = srcArrayObjs"
            MaxPlus.Core.EvalMAXScript(script)
        else:
            raise ValueError("There are no constrainers in constraint: {}".format(kConstraint.getPath()))

        dccSceneItem = rt.posCns

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

        offsetXfo = kConstraint.computeOffset()

        constraineeDCCSceneItem.Select()
        MaxPlus.Core.EvalMAXScript('constrainee = selection[1]')
        constraineeDCCSceneItem.Deselect()

        MaxPlus.Core.EvalMAXScript('sclCns = FabricMatrixController()')
        rt.constrainee.controller = rt.sclCns

        if len(kConstraint.getConstrainers()) == 1:
            # Create Ports and Connections
            rt.sclCns.DFGAddPort("inMatrix",  # desiredPortName
                                    0,  # portType
                                    "Mat44",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"17\"}",
                                    execPath="")

            rt.sclCns.DFGAddPort("offsetVec",  # desiredPortName
                                    0,  # portType
                                    "Vec3",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")

            matDecompNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.Decompose",  # presetPath
                rt.Point2(-40, 106))

            mulNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Core.Math.Mul",  # presetPath
                rt.Point2(300, 152))

            matSetSclNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.SetScaling",  # presetPath
                rt.Point2(430, 175))

            rt.sclCns.DFGConnect("inMatrix", matDecompNodeName + ".this", execPath="")
            rt.sclCns.DFGConnect(matDecompNodeName + ".scaling", mulNodeName + ".lhs", execPath="")
            rt.sclCns.DFGConnect("offsetVec", mulNodeName + ".rhs", execPath="")
            rt.sclCns.DFGConnect(mulNodeName + ".result", matSetSclNodeName + ".v", execPath="")
            rt.sclCns.DFGConnect(matSetSclNodeName + ".this", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                sc = offsetXfo.sc
                scJSON = sc.getRTVal().getJSON().getSimpleType()
                rt.sclCns.DFGSetArgValue("offsetVec", scJSON)

            constrainer = self.getDCCSceneItem(kConstraint.getConstrainers()[0])
            constrainer.Select()
            MaxPlus.Core.EvalMAXScript('constrainerObj = selection[1]')
            constrainer.Deselect()

            script = "constrainee.transform.controller.inMatrix = constrainerObj"
            MaxPlus.Core.EvalMAXScript(script)

        elif len(kConstraint.getConstrainers()) > 1:
            # Create Ports and Connections
            rt.sclCns.DFGAddPort("inMatrices",  # desiredPortName
                                    0,  # portType
                                    "Mat44[]",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"MaxType\": \"2065\"}",
                                    execPath="")

            rt.sclCns.DFGAddPort("offsetVec",  # desiredPortName
                                    0,  # portType
                                    "Vec3",  # typeSpec
                                    portToConnect="",
                                    extDep="",
                                    metaData="{\"uiHidden\": \"true\"}",
                                    execPath="")


            matDecompArrayNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.DecomposeArray",  # presetPath
                rt.Point2(-40, 106))

            arrayAvgNodeNameName = rt.sclCns.DFGInstPreset(
                "Fabric.Core.Array.Average",  # presetPath
                rt.Point2(-160, 130))

            mulNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Core.Math.Mul",  # presetPath
                rt.Point2(300, 152))

            matSetSclNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Exts.Math.Mat44.SetScaling",  # presetPath
                rt.Point2(430, 175))

            quatRotVecNodeName = rt.sclCns.DFGInstPreset(
                "Fabric.Exts.Math.Quat.RotateVector",  # presetPath
                rt.Point2(40, 286))

            rt.sclCns.DFGConnect("inMatrices", matDecompArrayNodeName + ".this", execPath="")
            rt.sclCns.DFGConnect(matDecompArrayNodeName + ".scaling", arrayAvgNodeNameName + ".average", execPath="")
            rt.sclCns.DFGConnect(arrayAvgNodeNameName + ".result", mulNodeName + ".lhs", execPath="")
            rt.sclCns.DFGConnect("offsetVec", mulNodeName + ".rhs", execPath="")
            rt.sclCns.DFGConnect(mulNodeName + ".result", matSetSclNodeName + ".v", execPath="")
            rt.sclCns.DFGConnect(matSetSclNodeName + ".this", "outputValue", execPath="")

            if kConstraint.getMaintainOffset() is True:
                sc = offsetXfo.sc
                scJSON = sc.getRTVal().getJSON().getSimpleType()
                rt.sclCns.DFGSetArgValue("offsetVec", scJSON)

            # Build array of objects to set to the input
            constrainers = [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()]
            MaxPlus.Core.EvalMAXScript('srcArrayObjs = #()')
            for i in xrange(len(constrainers)):
                constrainers[i].Select()
                MaxPlus.Core.EvalMAXScript('append srcArrayObjs selection[1]')
                constrainers[i].Deselect()

            script = "constrainee.transform.controller.inMatrices = srcArrayObjs"
            MaxPlus.Core.EvalMAXScript(script)
        else:
            raise ValueError("There are no constrainers in constraint: {}".format(kConstraint.getPath()))

        dccSceneItem = rt.sclCns

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem


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

        def validatePortValue(rtVal, portName, portDataType):
            """Validate port value type when passing built in Python types.

            Args:
                rtVal (RTVal): rtValue object.
                portName (str): Name of the argument being validated.
                portDataType (str): Type of the argument being validated.

            """

            # Validate types when passing a built in Python type
            if type(rtVal) in (bool, str, int, float):
                if portDataType in ('Scalar', 'Float32', 'UInt32'):
                    if type(rtVal) not in (float, int):
                        raise TypeError(kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

                elif portDataType == 'Boolean':
                    if type(rtVal) != bool and not (type(rtVal) == int and (rtVal == 0 or rtVal == 1)):
                        raise TypeError(kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

                elif portDataType == 'String':
                    if type(rtVal) != str:
                        raise TypeError(kOperator.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

        try:
            if isKLBased is True:
                ports = kOperator.getSolverArgs()
                portCount = len(ports)

                def findPortOfType(dataTypes, connectionTypes):
                        for i in xrange(portCount):
                            arg = ports[i]
                            # argName = arg.name.getSimpleType()
                            argDataType = arg.dataType.getSimpleType()
                            argConnectionType = arg.connectionType.getSimpleType()

                            if argDataType in dataTypes and argConnectionType in connectionTypes:
                                return i

                        return -1

                # Find operatorOwner to attach Canvas Operator to.
                ownerOutPortIndex = findPortOfType(['Mat44', 'Mat44[]'], ['Out', 'IO'])
                if ownerOutPortIndex is -1:
                    raise Exception("Solver '" + kOperator.getName() + "' has no Mat44 outputs!")

                ownerArg = ports[ownerOutPortIndex]
                ownerOutPortName = ownerArg.name.getSimpleType()
                ownerOutPortDataType = ownerArg.dataType.getSimpleType()
                # ownerArgConnectionType = ownerArg.connectionType.getSimpleType()

                if ownerOutPortDataType == 'Mat44[]':
                    operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerOutPortName)[0])
                    ownerOutPortName = ownerOutPortName + str(0)
                else:
                    operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerOutPortName))

                operatorOwner.Select()
                MaxPlus.Core.EvalMAXScript('operatorOwner = selection[1]')
                operatorOwner.Deselect()

                MaxPlus.Core.EvalMAXScript('matCtrl = FabricMatrixController()')
                self._registerSceneItemPair(kOperator, rt.matCtrl)

                rt.operatorOwner.controller = rt.matCtrl

                config = Config.getInstance()
                nameTemplate = config.getNameTemplate()
                typeTokens = nameTemplate['types']
                opTypeToken = typeTokens.get(type(kOperator).__name__, 'op')
                solverNodeName = '_'.join([kOperator.getName(), opTypeToken])
                solverSolveNodeName = '_'.join([kOperator.getName(), 'solve', opTypeToken])

                rt.matCtrl.DFGSetExtDeps(kOperator.getExtension())

                solverTypeName = kOperator.getSolverTypeName()

                # Create Solver Function Node
                dfgEntry = "dfgEntry {\n  solver = " + solverTypeName + "();\n}"
                solverNodeCode = "{}\n\n{}".format('require ' + kOperator.getExtension() + ';', dfgEntry)

                rt.matCtrl.DFGAddFunc(solverNodeName,  # title
                                      solverNodeCode,  # code
                                      rt.Point2(-220, 100),  # position
                                      execPath="")

                rt.matCtrl.DFGAddPort("solver",  # desiredPortName
                                      2,  # portType
                                      solverTypeName,  # typeSpec
                                      portToConnect="",
                                      extDep=kOperator.getExtension(),
                                      metaData="",
                                      execPath=solverNodeName)

                solverVarName = rt.matCtrl.DFGAddVar("solverVar",
                                     solverTypeName,  # desiredNodeName
                                     kOperator.getExtension(),  # extDep
                                     rt.Point2(-75, 100),  # position
                                     execPath="")

                rt.matCtrl.DFGConnect(solverNodeName + ".solver",  # srcPortPath
                                      solverVarName + ".value",  # dstPortPath
                                      execPath="")

                # Crate Solver "Solve" Function Node
                rt.matCtrl.DFGAddFunc(solverSolveNodeName,  # title
                                      "dfgEntry {}",  # code
                                      rt.Point2(100, 100),  # position
                                      execPath="")

                rt.matCtrl.DFGAddPort("solver",  # desiredPortName
                                      1,  # portType
                                      solverTypeName,  # typeSpec
                                      portToConnect="",
                                      extDep=kOperator.getExtension(),
                                      metaData="",
                                      execPath=solverSolveNodeName)

                rt.matCtrl.DFGConnect(solverVarName + ".value",  # srcPortPath
                                      solverSolveNodeName + ".solver",  # dstPortPath
                                      execPath="")

                rt.matCtrl.DFGConnect(solverSolveNodeName + ".solver",  # srcPortPath
                                      "exec",  # dstPortPath
                                      execPath="")

            else:
                host = ks.getCoreClient().DFG.host
                opBinding = host.createBindingToPreset(kOperator.getPresetPath())
                node = opBinding.getExec()

                portTypeMap = {
                    0: 'In',
                    1: 'IO',
                    2: 'Out'
                }

                ownerOutPortData = {
                    'name': None,
                    'typeSpec': None,
                    'execPortType': None
                }

                for i in xrange(node.getExecPortCount()):
                    portName = node.getExecPortName(i)
                    portType = node.getExecPortType(i)
                    rtVal = opBinding.getArgValue(portName)
                    typeSpec = rtVal.getTypeName().getSimpleType()

                    if typeSpec in ['Mat44', 'Mat44[]'] and portTypeMap[portType] in ['Out', 'IO']:
                        ownerOutPortData['name'] = portName
                        ownerOutPortData['typeSpec'] = typeSpec
                        ownerOutPortData['execPortType'] = portTypeMap[portType]
                        break

                # Find operatorOwner to attach Splice Operator to.
                if ownerOutPortData['name'] is None:
                    raise Exception("Graph '" + uniqueNodeName + "' has no Mat44 outputs!")

                ownerOutPortName = ownerOutPortData['name']
                ownerOutPortDataType = ownerOutPortData['typeSpec']
                # ownerOutPortConnectionType = ownerOutPortData['execPortType']

                if ownerOutPortDataType == 'Mat44[]':
                    operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerOutPortName)[0])
                    ownerOutPortName = ownerOutPortName + str(0)
                else:
                    operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerOutPortName))

                operatorOwner.Select()
                MaxPlus.Core.EvalMAXScript('operatorOwner = selection[1]')
                operatorOwner.Deselect()

                MaxPlus.Core.EvalMAXScript('matCtrl = FabricMatrixController()')
                self._registerSceneItemPair(kOperator, rt.matCtrl)

                rt.operatorOwner.controller = rt.matCtrl

                rt.matCtrl.DFGSetExtDeps("Kraken")

                graphNodeName = rt.matCtrl.DFGInstPreset(kOperator.getPresetPath(),  # presetPath
                                         rt.Point2(100, 100))  # position

            portCount = 0
            if isKLBased is True:
                portCount = len(kOperator.getSolverArgs())
            else:
                portCount = node.getExecPortCount()

            for i in xrange(portCount):

                if isKLBased is True:
                    args = kOperator.getSolverArgs()
                    arg = args[i]
                    portName = arg.name.getSimpleType()
                    portConnectionType = arg.connectionType.getSimpleType()
                    portDataType = arg.dataType.getSimpleType()
                else:
                    portName = node.getExecPortName(i)
                    portConnectionType = portTypeMap[node.getExecPortType(i)]
                    rtVal = opBinding.getArgValue(portName)
                    portDataType = rtVal.getTypeName().getSimpleType()

                if portConnectionType == 'In':
                    if isKLBased is True:
                        rt.matCtrl.DFGAddPort(portName,  # desiredPortName
                                              0,  # portType
                                              portDataType,  # typeSpec
                                              portToConnect="",
                                              extDep="",
                                              metaData="",
                                              execPath="")

                        rt.matCtrl.DFGAddPort(portName,  # desiredPortName
                                              0,  # portType
                                              portDataType,  # typeSpec
                                              portToConnect="",
                                              extDep="",
                                              metaData="",
                                              execPath=solverSolveNodeName)

                        rt.matCtrl.DFGConnect(portName,  # srcPortPath
                                              solverSolveNodeName + "." + portName,  # dstPortPath
                                              execPath="")

                    else:
                        if portDataType != 'Execute':
                            rt.matCtrl.DFGAddPort(portName,  # desiredPortName
                                                  0,  # portType
                                                  portDataType,  # typeSpec
                                                  portToConnect="",
                                                  extDep="",
                                                  metaData="",
                                                  execPath="")

                        rt.matCtrl.DFGConnect(portName,  # srcPortPath
                                              graphNodeName + "." + portName,  # dstPortPath
                                              execPath="")

                elif portConnectionType in ['IO', 'Out']:

                    if portDataType in ('Execute', 'InlineInstance', 'DrawingHandle'):
                        # Don't expose invalid Maya data type InlineInstance, instead connect to exec port
                        dstPortPath = "exec"
                    else:
                        dstPortPath = portName

                    if isKLBased is True:
                        srcPortNode = solverSolveNodeName
                        rt.matCtrl.DFGAddPort(portName,  # desiredPortName
                                              2,  # portType
                                              portDataType,  # typeSpec
                                              portToConnect="",
                                              extDep="",
                                              metaData="",
                                              execPath=solverSolveNodeName)
                    else:
                        srcPortNode = graphNodeName

                    if portDataType not in ('Execute', 'InlineInstance', 'DrawingHandle'):
                        rt.matCtrl.DFGAddPort(portName,  # desiredPortName
                                              2,  # portType
                                              portDataType,  # typeSpec
                                              portToConnect="",
                                              extDep="",
                                              metaData="",
                                              execPath="")

                    rt.matCtrl.DFGConnect(srcPortNode + "." + portName,  # srcPortPath
                                          dstPortPath,  # dstPortPath
                                          execPath="")

                else:
                    raise Exception("Invalid connection type:" + portConnectionType)

                if portDataType == 'EvalContext':
                    continue
                elif portDataType == 'Execute':
                    continue
                elif portDataType == 'DrawingHandle':
                    continue
                elif portDataType == 'InlineDebugShape':
                    continue
                elif portDataType == 'Execute' and portName == 'exec':
                    continue

                if portName == 'time':
                    print "Set Expression on 'time' parameter!"
                    # pm.expression(o=canvasNode + '.time', s=canvasNode + '.time = time;')
                    continue
                if portName == 'frame':
                    print "Set Expression on 'frame' parameter!"
                    # pm.expression(o=canvasNode + '.frame', s=canvasNode + '.frame = frame;')
                    continue

                # Get the port's input from the DCC
                if portConnectionType == 'In':
                    connectedObjects = kOperator.getInput(portName)
                elif portConnectionType in ['IO', 'Out']:
                    connectedObjects = kOperator.getOutput(portName)

                if portDataType.endswith('[]'):

                    # In CanvasMaya, output arrays are not resized by the system
                    # prior to calling into Canvas, so we explicily resize the
                    # arrays in the generated operator stub code.
                    if connectedObjects is None:
                        connectedObjects = []

                    connectionTargets = []
                    for i in xrange(len(connectedObjects)):
                        opObject = connectedObjects[i]
                        dccSceneItem = self.getDCCSceneItem(opObject)

                        if hasattr(opObject, "getName"):
                            # Handle output connections to visibility attributes.
                            if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                logger.warning('Connection to/from visibility is not supported currently!')
                                pass
                                # dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                # dccSceneItem = dccItem.attr('visibility')
                            elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                logger.warning('Connection to/from visibility is not supported currently!')
                                pass
                                # dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                # shape = dccItem.getShape()
                                # dccSceneItem = shape.attr('visibility')

                        connectionTargets.append(
                            {
                                'opObject': opObject,
                                'dccSceneItem': dccSceneItem
                            })
                else:
                    if connectedObjects is None:
                        if isKLBased:
                            opType = kOperator.getExtension() + ":" + kOperator.getSolverTypeName()
                        else:
                            opType = kOperator.getPresetPath()

                        logger.debug("Operator '" + solverSolveNodeName +
                                       "' of type '" + opType +
                                       "' port '" + portName + "' not connected.")

                    opObject = connectedObjects
                    dccSceneItem = self.getDCCSceneItem(opObject)
                    if hasattr(opObject, "getName"):
                        # Handle output connections to visibility attributes.
                        if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                            logger.warning('Connection to/from visibility is not supported currently!')
                            pass
                            # dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                            # dccSceneItem = dccItem.attr('visibility')
                        elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                            logger.warning('Connection to/from visibility is not supported currently!')
                            pass
                            # dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                            # shape = dccItem.getShape()
                            # dccSceneItem = shape.attr('visibility')

                    connectionTargets = {
                        'opObject': opObject,
                        'dccSceneItem': dccSceneItem
                    }

                # Connect and Set Port Values
                if portConnectionType == 'In':

                    def connectInput(tgt, opObject, dccSceneItem):
                        if isinstance(opObject, Attribute):

                            node = dccSceneItem[0]
                            attributeGrp = dccSceneItem[1].name
                            attributeName = dccSceneItem[2]

                            node.Select()
                            MaxPlus.Core.EvalMAXScript('srcAttrParentObj = selection[1]')
                            node.Deselect()

                            srcStr = 'srcAttrParentObj.baseObject.{}[#{}]'.format(attributeGrp, attributeName)
                            tgtStr = 'operatorOwner.transform.controller[#{}]'.format(tgt)

                            MaxPlus.Core.EvalMAXScript('paramWire.connect {} {} "{}"'.format(srcStr, tgtStr, attributeName))

                        elif isinstance(opObject, Object3D):

                            if type(dccSceneItem) is list:

                                maxType = rt.matCtrl.GetPortMetaData(tgt, "MaxType")
                                if maxType != "2065":
                                    # Set port to MaxNode mode to connect object
                                    rt.matCtrl.SetMaxTypeForArg(tgt, 2065)

                                # Build array of objects to set to the input
                                MaxPlus.Core.EvalMAXScript('srcArrayObjs = #()')
                                for i in xrange(len(dccSceneItem)):
                                    dccSceneItem[i].Select()
                                    MaxPlus.Core.EvalMAXScript('append srcArrayObjs selection[1]')
                                    dccSceneItem[i].Deselect()

                                script = "operatorOwner.transform.controller.{}".format(tgt)
                                script += " = srcArrayObjs"
                                MaxPlus.Core.EvalMAXScript(script)

                            else:
                                dccSceneItem.Select()
                                MaxPlus.Core.EvalMAXScript('srcMatrixObj = selection[1]')
                                dccSceneItem.Deselect()

                                # Set port to MaxNode mode to connect object
                                rt.matCtrl.SetMaxTypeForArg(tgt, 17)

                                script = "operatorOwner.transform.controller.{}".format(tgt)
                                script += " = srcMatrixObj"
                                MaxPlus.Core.EvalMAXScript(script)

                        elif isinstance(opObject, Xfo):
                            self.setMat44Attr(dccSceneItemName, attr, mat44)

                            rt.matCtrl.DFGEditPort(tgt, 0, metaData="{\"uiHidden\": \"true\"}")

                            mat44 = opObject.toMat44()
                            mat44JSON = mat44.getRTVal().getJSON().getSimpleType()

                            rt.matCtrl.DFGSetArgValue(tgt, mat44JSON)

                        elif isinstance(opObject, Mat44):

                            rt.matCtrl.DFGEditPort(tgt, 0, metaData="{\"uiHidden\": \"true\"}")

                            mat44JSON = opObject.getRTVal().getJSON().getSimpleType()
                            rt.matCtrl.DFGSetArgValue(tgt, mat44JSON)

                        elif isinstance(opObject, Vec2):

                            rt.matCtrl.DFGEditPort(tgt, 0, metaData="{\"uiHidden\": \"true\"}")

                            vec2JSON = opObject.getRTVal().getJSON().getSimpleType()
                            rt.matCtrl.DFGSetArgValue(tgt, vec2JSON)

                        elif isinstance(opObject, Vec3):

                            rt.matCtrl.DFGEditPort(tgt, 0, metaData="{\"uiHidden\": \"true\"}")

                            vec3JSON = opObject.getRTVal().getJSON().getSimpleType()
                            rt.matCtrl.DFGSetArgValue(tgt, vec3JSON)

                        else:  # Set Python value to port
                            rt.matCtrl.DFGEditPort(tgt, 0, metaData="{\"uiHidden\": \"true\"}")

                            validatePortValue(opObject, portName, portDataType)
                            rt.matCtrl.DFGSetArgValue(tgt, str(opObject))

                    if portDataType.endswith('[]'):
                        connectInput(portName,
                                     connectionTargets[0]['opObject'],
                                     [x['dccSceneItem'] for x in connectionTargets])
                    else:
                        connectInput(portName,
                                     connectionTargets['opObject'],
                                     connectionTargets['dccSceneItem'])

                elif portConnectionType in ['IO', 'Out']:

                    # ==========================================
                    # Skip Owner outport as it is handled later
                    # ==========================================
                    if portName == ownerOutPortName:
                        continue

                    def connectOutput(src, opObject, dccSceneItem):
                        if isinstance(opObject, Attribute):
                            logger.warning("Connecting Solver Outputs to Attributes is not Implemented!")

                            # logger.warning("Connecting {} > {}".format(src, dccSceneItem))
                            # node = dccSceneItem[0]
                            # attributeGrp = dccSceneItem[1].name
                            # attributeName = dccSceneItem[2]

                            # node.Select()
                            # MaxPlus.Core.EvalMAXScript('srcAttrParentObj = selection[1]')
                            # node.Deselect()

                            # srcStr = 'srcAttrParentObj.baseObject.{}[#{}]'.format(attributeGrp, attributeName)
                            # tgtStr = 'operatorOwner.transform.controller[#{}]'.format(tgt)

                            # MaxPlus.Core.EvalMAXScript('paramWire.connect {} {} "{}"'.format(srcStr, tgtStr, attributeName))

                        elif isinstance(opObject, Object3D):

                            if type(dccSceneItem) is list:
                                for i in xrange(1, len(dccSceneItem)):
                                    dccSceneItem[i].Select()
                                    MaxPlus.Core.EvalMAXScript('tgtOutputObj = selection[1]')
                                    dccSceneItem[i].Deselect()

                                    MaxPlus.Core.EvalMAXScript('tgtOutputMatCtrl = FabricMatrixController()')
                                    rt.tgtOutputObj.controller = rt.tgtOutputMatCtrl

                                    rt.tgtOutputMatCtrl.DFGAddPort("index",  # desiredPortName
                                                                   0,  # portType
                                                                   "UInt32",  # typeSpec
                                                                   portToConnect="outputValue",
                                                                   extDep="",
                                                                   metaData="{\"uiHidden\": \"true\"}",
                                                                   execPath="")

                                    rt.tgtOutputMatCtrl.DFGSetArgValue("index", i)

                                    rt.tgtOutputMatCtrl.DFGAddPort("inMatrices",  # desiredPortName
                                                                   0,  # portType
                                                                   portDataType,  # typeSpec
                                                                   portToConnect="",
                                                                   extDep="",
                                                                   metaData="",
                                                                   execPath="")

                                    arrayGetNodeName = rt.tgtOutputMatCtrl.DFGInstPreset("Fabric.Core.Array.Get",
                                                                      rt.Point2(40, 130),
                                                                      execPath="")

                                    rt.tgtOutputMatCtrl.DFGConnect("index",
                                                                   arrayGetNodeName + ".index",
                                                                   execPath="")

                                    rt.tgtOutputMatCtrl.DFGConnect("inMatrices",
                                                                   arrayGetNodeName + ".array",
                                                                   execPath="")

                                    rt.tgtOutputMatCtrl.DFGConnect(arrayGetNodeName + ".element",
                                                                   "outputValue",
                                                                   execPath="")

                                    rt.tgtOutputMatCtrl.ConnectArgs("inMatrices", rt.matCtrl, src)

                            else:
                                dccSceneItem.Select()
                                MaxPlus.Core.EvalMAXScript('tgtOutputObj = selection[1]')
                                dccSceneItem.Deselect()

                                MaxPlus.Core.EvalMAXScript('tgtOutputMatCtrl = FabricMatrixController()')
                                rt.tgtOutputObj.controller = rt.tgtOutputMatCtrl

                                rt.tgtOutputObj.controller = rt.tgtOutputMatCtrl

                                rt.tgtOutputMatCtrl.DFGAddPort("inMatrix",  # desiredPortName
                                                               0,  # portType
                                                               portDataType,  # typeSpec
                                                               portToConnect="outputValue",
                                                               extDep="",
                                                               metaData="",
                                                               execPath="")

                                rt.tgtOutputMatCtrl.ConnectArgs("inMatrix", rt.matCtrl, src)


                        elif isinstance(opObject, Xfo):
                            raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Xfo outputs types directly!")
                        elif isinstance(opObject, Mat44):
                            raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Mat44 types directly!")
                        else:
                            raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Python built-in types [%s] directly!" % (src, opObject.__class__.__name__))

                    if portDataType.endswith('[]'):
                        connectOutput(portName,
                                      connectionTargets[0]['opObject'],
                                      [x['dccSceneItem'] for x in connectionTargets])
                    else:
                        connectOutput(portName,
                                      connectionTargets['opObject'],
                                      connectionTargets['dccSceneItem'])

            # =============================================
            # Connect 'outputValue' port on Max controller
            # =============================================
            if ownerOutPortDataType.endswith('[]'):
                if isKLBased is False:
                    solverSolveNodeName = graphNodeName

                arrayGetNodeName = rt.matCtrl.DFGInstPreset("Fabric.Core.Array.Get",
                                                            rt.Point2(600, 200),
                                                            execPath="")

                rt.matCtrl.DFGConnect(solverSolveNodeName + "." + ownerOutPortName[:-1],
                                      arrayGetNodeName + ".array",
                                      execPath="")

                rt.matCtrl.DFGConnect(arrayGetNodeName + ".element",
                                      "outputValue",
                                      execPath="")

            else:
                if isKLBased is False:
                    solverSolveNodeName = graphNodeName

                rt.matCtrl.DFGConnect(solverSolveNodeName + "." + ownerOutPortName,
                                      "outputValue",
                                      execPath="")

            # Set Solver Operator Code
            if isKLBased is True:
                opSourceCode = kOperator.generateSourceCode()
                rt.matCtrl.DFGSetCode(opSourceCode, execPath=solverSolveNodeName)

        finally:
            pass

        return True

    # ==================
    # Attribute Methods
    # ==================
    def lockAttribute(self, kAttribute):
        """Locks attributes.

        Args:
            kAttribute (object): kraken attributes to lock.

        Returns:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kAttribute)

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

        # TODO: INSERT CODE TO LOCK ATTRIBUTE HERE

        # newDef = '\n'.join(defLines)
        # rt.CustAttributes.redefine(dataDef, newDef)

        parentDCCSceneItem.Deselect()

        return True

    def lockTransformAttrs(self, kSceneItem):
        """Locks flagged SRT attributes.

        Args:
            kSceneItem (Object): Kraken object to lock the SRT attributes on.

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
            MaxPlus.Point3(maxXfo.tr.x,
                           maxXfo.tr.y,
                           maxXfo.tr.z))

        dccSceneItem.SetWorldTM(mat3)

        order = ROT_ORDER_REMAP[kSceneItem.ro.order]

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

        raise NotImplementedError("'setMat44Attr' is not used in Kraken for 3dsMax")

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

        # pymxs.runtime.disableRefMsgs()
        MaxPlus.ViewportManager.DisableSceneRedraw()
        MaxPlus.SelectionManager.ClearNodeSelection()

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

        # pymxs.runtime.enableRefMsgs()
        MaxPlus.ViewportManager.EnableSceneRedraw()
        MaxPlus.ViewportManager.ForceCompleteRedraw()

        return True
