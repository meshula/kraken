"""Kraken Maya - Maya Builder module.

Classes:
Builder -- Component representation.

"""

import json
import logging

from kraken.log import getLogger

from kraken.core.kraken_system import ks

from kraken.core.maths import Vec2, Vec3, Xfo, Mat44, Math_radToDeg, RotationOrder

from kraken.core.builder import Builder
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.attributes.attribute import Attribute
from kraken.plugins.maya_plugin.utils import *

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad

import maya.cmds as cmds

logger = getLogger('kraken')
logger.setLevel(logging.INFO)


class Builder(Builder):
    """Builder object for building Kraken objects in Maya."""

    def __init__(self):
        super(Builder, self).__init__()

    def deleteBuildElements(self):
        """Clear out all dcc built elements from the scene if exist."""

        for builtElement in self._buildElements:
            if builtElement['src'].isTypeOf('Attribute'):
                continue

            node = builtElement['tgt']
            if node.exists():
                pm.delete(node)

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

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

        if kSceneItem.isTypeOf('Rig'):
            krakenRigAttr = dccSceneItem.addAttr('krakenRig',
                                                 niceName='krakenRig',
                                                 attributeType="bool",
                                                 defaultValue=True,
                                                 keyable=False)

            dccSceneItem.attr('krakenRig').setLocked(True)

            # Put Rig Data on DCC Item
            metaData = kSceneItem.getMetaData()
            if 'guideData' in metaData:
                pureJSON = metaData['guideData']

                krakenRigDataAttr = dccSceneItem.addAttr('krakenRigData',
                                                     niceName='krakenRigData',
                                                     dataType="string",
                                                     keyable=False)

                dccSceneItem.attr('krakenRigData').set(json.dumps(pureJSON, indent=2))
                dccSceneItem.attr('krakenRigData').setLocked(True)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

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

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

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

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

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

        dccSceneItem = pm.group(name="group", em=True)
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

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

        pm.select(parentNode)
        dccSceneItem = pm.joint(name="joint")
        pm.rename(dccSceneItem, buildName)

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

        dccSceneItem = pm.spaceLocator(name="locator")
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

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

        # Format points for Maya
        curveData = kSceneItem.getCurveData()

        # Scale, rotate, translation shape
        curvePoints = []
        for eachSubCurve in curveData:
            formattedPoints = eachSubCurve["points"]
            curvePoints.append(formattedPoints)

        mainCurve = None
        for i, eachSubCurve in enumerate(curvePoints):
            closedSubCurve = curveData[i]["closed"]
            degreeSubCurve = curveData[i]["degree"]

            currentSubCurve = pm.curve(per=False,
                                       point=curvePoints[i],
                                       degree=degreeSubCurve)

            if closedSubCurve:
                pm.closeCurve(currentSubCurve,
                              preserveShape=True,
                              replaceOriginal=True)

            if mainCurve is None:
                mainCurve = currentSubCurve

            if i > 0:
                pm.parent(currentSubCurve.getShape(),
                          mainCurve,
                          relative=True,
                          shape=True)

                pm.delete(currentSubCurve)

        dccSceneItem = mainCurve
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

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

        # Format points for Maya
        curveData = kSceneItem.getCurveData()

        # Scale, rotate, translation shape
        curvePoints = []
        for eachSubCurve in curveData:
            formattedPoints = eachSubCurve["points"]
            curvePoints.append(formattedPoints)

        mainCurve = None
        for i, eachSubCurve in enumerate(curvePoints):
            closedSubCurve = curveData[i]["closed"]
            degreeSubCurve = curveData[i]["degree"]

            currentSubCurve = pm.curve(per=False,
                                       point=curvePoints[i],
                                       degree=degreeSubCurve)

            if closedSubCurve:
                pm.closeCurve(currentSubCurve,
                              preserveShape=True,
                              replaceOriginal=True)

            if mainCurve is None:
                mainCurve = currentSubCurve

            if i > 0:
                pm.parent(currentSubCurve.getShape(),
                          mainCurve,
                          relative=True,
                          shape=True)

                pm.delete(currentSubCurve)

        dccSceneItem = mainCurve
        pm.parent(dccSceneItem, parentNode)
        pm.rename(dccSceneItem, buildName)

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
        parentDCCSceneItem.addAttr(kAttribute.getName(),
                                   niceName=kAttribute.getName(),
                                   attributeType="bool",
                                   defaultValue=kAttribute.getValue(),
                                   keyable=True)

        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())
        dccSceneItem.setLocked(kAttribute.getLock())
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
        parentDCCSceneItem.addAttr(kAttribute.getName(),
                                   niceName=kAttribute.getName(),
                                   attributeType="float",
                                   defaultValue=kAttribute.getValue(),
                                   keyable=True)

        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())

        if kAttribute.getMin() is not None:
            dccSceneItem.setMin(kAttribute.getMin())

        if kAttribute.getMax() is not None:
            dccSceneItem.setMax(kAttribute.getMax())

        if kAttribute.getUIMin() is not None:
            dccSceneItem.setSoftMin(kAttribute.getUIMin())

        if kAttribute.getUIMax() is not None:
            dccSceneItem.setSoftMax(kAttribute.getUIMax())

        dccSceneItem.setLocked(kAttribute.getLock())
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

        mininum = kAttribute.getMin()
        if mininum == None:
            mininum = 0

        maximum = kAttribute.getMax()
        if maximum == None:
            maximum = kAttribute.getValue() * 2

        parentDCCSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
        parentDCCSceneItem.addAttr(kAttribute.getName(), niceName=kAttribute.getName(), attributeType="long", defaultValue=kAttribute.getValue(), minValue=mininum, maxValue=maximum, keyable=True)
        parentDCCSceneItem.attr(kAttribute.getName())
        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())

        if kAttribute.getMin() is not None:
            dccSceneItem.setMin(kAttribute.getMin())

        if kAttribute.getMax() is not None:
            dccSceneItem.setMax(kAttribute.getMax())

        if kAttribute.getUIMin() is not None:
            dccSceneItem.setSoftMin(kAttribute.getUIMin())

        if kAttribute.getUIMax() is not None:
            dccSceneItem.setSoftMax(kAttribute.getUIMax())

        dccSceneItem.setLocked(kAttribute.getLock())
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
        parentDCCSceneItem.addAttr(kAttribute.getName(),
                                   niceName=kAttribute.getName(),
                                   dataType="string")

        dccSceneItem = parentDCCSceneItem.attr(kAttribute.getName())
        dccSceneItem.set(kAttribute.getValue())
        dccSceneItem.setLocked(kAttribute.getLock())
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

        groupName = kAttributeGroup.getName()
        if groupName == "implicitAttrGrp":
            return False

        parentDCCSceneItem.addAttr(groupName,
                                   niceName=groupName,
                                   attributeType="enum",
                                   enumName="-----",
                                   keyable=True)

        dccSceneItem = parentDCCSceneItem.attr(groupName)
        pm.setAttr(parentDCCSceneItem + "." + groupName, lock=True)

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
                driver = dccItem.attr('visibility')

            elif driverAttr.getName() == 'shapeVisibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                shape = dccItem.getShape()
                driver = shape.attr('visibility')

            else:
                driver = self.getDCCSceneItem(kAttribute.getConnection())

            # Detect if the driven attribute is a visibility attribute and map
            # to correct DCC attribute
            if kAttribute.getName() == 'visibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                driven = dccItem.attr('visibility')

            elif kAttribute.getName() == 'shapeVisibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                shape = dccItem.getShape()
                driven = shape.attr('visibility')
            else:
                driven = self.getDCCSceneItem(kAttribute)

            pm.connectAttr(driver, driven, force=True)

        return True

    # =========================
    # Constraint Build Methods
    # =========================
    def buildOrientationConstraint(self, kConstraint):
        """Builds an orientation constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())
        dccSceneItem = pm.orientConstraint(
            [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
            constraineeDCCSceneItem,
            name=kConstraint.getName() + "_ori_cns",
            maintainOffset=kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:

            # Maya's rotation order enums:
            # 0 XYZ
            # 1 YZX
            # 2 ZXY
            # 3 XZY
            # 4 YXZ <-- 5 in Fabric
            # 5 ZYX <-- 4 in Fabric
            order = kConstraint.getConstrainee().ro.order
            if order == 4:
                order = 5
            elif order == 5:
                order = 4

            offsetXfo = kConstraint.computeOffset()
            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            dccSceneItem.attr('offset').set([offsetAngles.x,
                                             offsetAngles.y,
                                             offsetAngles.z])

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPoseConstraint(self, kConstraint):
        """Builds an pose constraint represented by the kConstraint.

        Args:
            kConstraint (Object): kraken constraint object to build.

        Return:
            bool: True if successful.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())
        dccSceneItem = pm.parentConstraint(
            [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
            constraineeDCCSceneItem,
            name=kConstraint.getName() + "_par_cns",
            maintainOffset=kConstraint.getMaintainOffset())

        scaleConstraint = pm.scaleConstraint(
            [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
            constraineeDCCSceneItem,
            name=kConstraint.getName() + "_scl_cns",
            maintainOffset=kConstraint.getMaintainOffset())

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
                0: 4,
                1: 3,
                2: 5,
                3: 1,
                4: 0,
                5: 2
            }

            order = rotOrderRemap[kConstraint.getConstrainee().ro.order]
            # if order == 4:
            #     order = 5
            # elif order == 5:
            #     order = 4

            offsetXfo = kConstraint.computeOffset()
            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            # Set offsets on parent constraint
            dccSceneItem.target[0].targetOffsetTranslate.set([offsetXfo.tr.x,
                                                              offsetXfo.tr.y,
                                                              offsetXfo.tr.z])

            dccSceneItem.target[0].targetOffsetRotate.set(
                [Math_radToDeg(offsetAngles.x),
                 Math_radToDeg(offsetAngles.y),
                 Math_radToDeg(offsetAngles.z)])

            # Set offsets on the scale constraint
            scaleConstraint.offset.set([offsetXfo.sc.x,
                                        offsetXfo.sc.y,
                                        offsetXfo.sc.z])

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPositionConstraint(self, kConstraint):
        """Builds an position constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            bool: True if successful.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())
        dccSceneItem = pm.pointConstraint(
            [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
            constraineeDCCSceneItem,
            name=kConstraint.getName() + "_pos_cns",
            maintainOffset=kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:
            offsetXfo = kConstraint.computeOffset()

            # Set offsets on the scale constraint
            dccSceneItem.offset.set([offsetXfo.tr.x,
                                     offsetXfo.tr.y,
                                     offsetXfo.tr.z])

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildScaleConstraint(self, kConstraint):
        """Builds an scale constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            bool: True if successful.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())
        dccSceneItem = pm.scaleConstraint(
            [self.getDCCSceneItem(x) for x in kConstraint.getConstrainers()],
            constraineeDCCSceneItem,
            name=kConstraint.getName() + "_scl_cns",
            maintainOffset=kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:
            offsetXfo = kConstraint.computeOffset()

            # Set offsets on the scale constraint
            dccSceneItem.offset.set([offsetXfo.sc.x,
                                     offsetXfo.sc.y,
                                     offsetXfo.sc.z])

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

        pm.connectAttr(connectionTargetDCCSceneItem,
                       targetDCCSceneItem,
                       force=True)

        return True

    # =========================
    # Operator Builder Methods
    # =========================
    def buildKLOperator(self, kOperator):
        """Builds KL Operators on the components.

        Args:
            kOperator (Object): Kraken operator that represents a KL
                operator.

        Return:
            bool: True if successful.

        """

        # Code to build KL and Canvas based Operators has been merged.
        # It's important to note here that the 'isKLBased' argument is set
        # to true.
        self.buildCanvasOperator(kOperator, isKLBased=True)

        return True

    def buildCanvasOperator(self, kOperator, isKLBased=False):
        """Builds Canvas Operators on the components.

        Args:
            kOperator (object): Kraken operator that represents a Canvas
                operator.
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
            if isKLBased is False:
                host = ks.getCoreClient().DFG.host
                opBinding = host.createBindingToPreset(kOperator.getPresetPath())
                node = opBinding.getExec()

                portTypeMap = {
                    0: 'In',
                    1: 'IO',
                    2: 'Out'
                }

            # Create Canvas Operator
            canvasNode = pm.createNode('canvasNode', name=kOperator.getName())
            self._registerSceneItemPair(kOperator, pm.PyNode(canvasNode))


            if isKLBased is True:

                pm.FabricCanvasSetExtDeps(mayaNode=canvasNode,
                                      execPath="",
                                      extDep=kOperator.getExtension())

                solverTypeName = kOperator.getSolverTypeName()

                pm.FabricCanvasAddFunc(mayaNode=canvasNode,
                                       execPath="",
                                       title=kOperator.getName(),
                                       code="dfgEntry {}", xPos="100", yPos="100")

                pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                       execPath=kOperator.getName(),
                                       desiredPortName="solver",
                                       portType="IO",
                                       typeSpec=solverTypeName,
                                       connectToPortPath="",
                                       extDep=kOperator.getExtension())

                pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                       execPath="",
                                       desiredPortName="solver",
                                       portType="IO",
                                       typeSpec=solverTypeName,
                                       connectToPortPath="",
                                       extDep=kOperator.getExtension())

                pm.FabricCanvasConnect(mayaNode=canvasNode,
                                       execPath="",
                                       srcPortPath="solver",
                                       dstPortPath=kOperator.getName() + ".solver")

                pm.FabricCanvasConnect(mayaNode=canvasNode,
                                       execPath="",
                                       srcPortPath=kOperator.getName() + ".solver",
                                       dstPortPath="solver")
            else:
                pm.FabricCanvasSetExtDeps(mayaNode=canvasNode,
                                          execPath="",
                                          extDep="Kraken")

                graphNodeName = pm.FabricCanvasInstPreset(
                    mayaNode=canvasNode,
                    execPath="",
                    presetPath=kOperator.getPresetPath(),
                    xPos="100",
                    yPos="100")

            portCount = 0
            if isKLBased is True:
                portCount = len(kOperator.getSolverArgs())
            else:
                portCount = node.getExecPortCount()

            arraySizes = {}
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
                        pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                           execPath="",
                                           desiredPortName=portName,
                                           portType="In",
                                           typeSpec=portDataType,
                                           connectToPortPath="")

                        pm.FabricCanvasAddPort(mayaNode=canvasNode,
                                               execPath=kOperator.getName(),
                                               desiredPortName=portName,
                                               portType="In",
                                               typeSpec=portDataType,
                                               connectToPortPath="")

                        pm.FabricCanvasConnect(mayaNode=canvasNode,
                                               execPath="",
                                               srcPortPath=portName,
                                               dstPortPath=kOperator.getName() + "." + portName)

                    else:
                        pm.FabricCanvasAddPort(
                            mayaNode=canvasNode,
                            execPath="",
                            desiredPortName=portName,
                            portType="In",
                            typeSpec=portDataType,
                            connectToPortPath="")

                        pm.FabricCanvasConnect(
                            mayaNode=canvasNode,
                            execPath="",
                            srcPortPath=portName,
                            dstPortPath=graphNodeName + "." + portName)

                elif portConnectionType in ['IO', 'Out']:
                    if isKLBased is True:
                        pm.FabricCanvasAddPort(
                            mayaNode=canvasNode,
                            execPath="",
                            desiredPortName=portName,
                            portType="Out",
                            typeSpec=portDataType,
                            connectToPortPath="")

                        pm.FabricCanvasAddPort(
                            mayaNode=canvasNode,
                            execPath=kOperator.getName(),
                            desiredPortName=portName,
                            portType="Out",
                            typeSpec=portDataType,
                            connectToPortPath="")

                        pm.FabricCanvasConnect(
                            mayaNode=canvasNode,
                            execPath="",
                            srcPortPath=kOperator.getName() + "." + portName,
                            dstPortPath=portName)
                    else:
                        pm.FabricCanvasAddPort(
                            mayaNode=canvasNode,
                            execPath="",
                            desiredPortName=portName,
                            portType="Out",
                            typeSpec=portDataType,
                            connectToPortPath="")

                        pm.FabricCanvasConnect(
                            mayaNode=canvasNode,
                            execPath="",
                            srcPortPath=graphNodeName + "." + portName,
                            dstPortPath=portName)
                else:
                    raise Exception("Invalid connection type:" + portConnectionType)

                if portDataType == 'EvalContext':
                    continue
                elif portDataType == 'DrawingHandle':
                    continue
                elif portDataType == 'InlineDebugShape':
                    continue

                if portName == 'time':
                    pm.expression(o=canvasNode + '.time', s=canvasNode + '.time = time;')
                    continue
                if portName == 'frame':
                    pm.expression(o=canvasNode + '.frame', s=canvasNode + '.frame = frame;')
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
                    if portConnectionType in ['IO', 'Out']:
                        arraySizes[portName] = len(connectedObjects)

                    connectionTargets = []
                    for i in xrange(len(connectedObjects)):
                        opObject = connectedObjects[i]
                        dccSceneItem = self.getDCCSceneItem(opObject)

                        if hasattr(opObject, "getName"):
                            # Handle output connections to visibility attributes.
                            if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                dccSceneItem = dccItem.attr('visibility')
                            elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                shape = dccItem.getShape()
                                dccSceneItem = shape.attr('visibility')

                        connectionTargets.append(
                            {
                                'opObject': opObject,
                                'dccSceneItem': dccSceneItem
                            })
                else:
                    if connectedObjects is None:
                        if isKLBased:
                            opType = kOperator.getExtension()+":"+kOperator.getSolverTypeName()
                        else:
                            opType = kOperator.getPresetPath()
                        logger.warning("Operator '" + kOperator.getName() +
                                       "' of type '" + opType +
                                       "' port '" + portName + "' not connected.")
                        continue

                    opObject = connectedObjects
                    dccSceneItem = self.getDCCSceneItem(opObject)
                    if hasattr(opObject, "getName"):
                        # Handle output connections to visibility attributes.
                        if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                            dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                            dccSceneItem = dccItem.attr('visibility')
                        elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                            dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                            shape = dccItem.getShape()
                            dccSceneItem = shape.attr('visibility')

                    connectionTargets = {
                        'opObject': opObject,
                        'dccSceneItem': dccSceneItem
                    }

                # Add the Canvas Port for each port.
                if portConnectionType == 'In':

                    def connectInput(tgt, opObject, dccSceneItem):
                        if isinstance(opObject, Attribute):
                            pm.connectAttr(dccSceneItem, tgt)
                        elif isinstance(opObject, Object3D):
                            pm.connectAttr(dccSceneItem.attr('worldMatrix'), tgt)
                        elif isinstance(opObject, Xfo):
                            self.setMat44Attr(tgt.partition(".")[0], tgt.partition(".")[2], opObject.toMat44())
                        elif isinstance(opObject, Mat44):
                            self.setMat44Attr(tgt.partition(".")[0], tgt.partition(".")[2], opObject)
                        elif isinstance(opObject, Vec2):
                            pm.setAttr(tgt, opObject.x, opObject.y, type="double2")
                        elif isinstance(opObject, Vec3):
                            pm.setAttr(tgt, opObject.x, opObject.y, opObject.z, type="double3")
                        else:
                            validatePortValue(opObject, portName, portDataType)

                            pm.setAttr(tgt, opObject)

                    if portDataType.endswith('[]'):
                        for i in xrange(len(connectionTargets)):
                            connectInput(
                                canvasNode + "." + portName + '[' + str(i) + ']',
                                connectionTargets[i]['opObject'],
                                connectionTargets[i]['dccSceneItem'])
                    else:
                        connectInput(
                            canvasNode + "." + portName,
                            connectionTargets['opObject'],
                            connectionTargets['dccSceneItem'])

                elif portConnectionType in ['IO', 'Out']:

                    def connectOutput(src, opObject, dccSceneItem):
                        if isinstance(opObject, Attribute):
                            pm.connectAttr(src, dccSceneItem)
                        elif isinstance(opObject, Object3D):
                            decomposeNode = pm.createNode('decomposeMatrix')
                            pm.connectAttr(src,
                                           decomposeNode.attr("inputMatrix"),
                                           force=True)

                            decomposeNode.attr("outputRotate").connect(dccSceneItem.attr("rotate"))
                            decomposeNode.attr("outputScale").connect(dccSceneItem.attr("scale"))
                            decomposeNode.attr("outputTranslate").connect(dccSceneItem.attr("translate"))
                        elif isinstance(opObject, Xfo):
                            raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Xfo outputs types directly!")
                        elif isinstance(opObject, Mat44):
                            raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Mat44 types directly!")
                        else:
                            raise NotImplementedError("Kraken Canvas Operator cannot set object [%s] outputs with Python built-in types [%s] directly!" % (src, opObject.__class__.__name__))

                    if portDataType.endswith('[]'):
                        for i in xrange(len(connectionTargets)):
                            connectOutput(
                                str(canvasNode + "." + portName) + '[' + str(i) + ']',
                                connectionTargets[i]['opObject'],
                                connectionTargets[i]['dccSceneItem'])
                    else:
                        connectOutput(
                            str(canvasNode + "." + portName),
                            connectionTargets['opObject'],
                            connectionTargets['dccSceneItem'])

            if isKLBased is True:
                opSourceCode = kOperator.generateSourceCode(arraySizes=arraySizes)
                pm.FabricCanvasSetCode(mayaNode=canvasNode,
                                       execPath=kOperator.getName(),
                                       code=opSourceCode)

        finally:
            pass

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

        # Lock Rotation
        if kSceneItem.testFlag("lockXRotation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'rx',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockYRotation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'ry',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockZRotation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'rz',
                lock=True,
                keyable=False,
                channelBox=False)


        # Lock Scale
        if kSceneItem.testFlag("lockXScale") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'sx',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockYScale") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'sy',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockZScale") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'sz',
                lock=True,
                keyable=False,
                channelBox=False)


        # Lock Translation
        if kSceneItem.testFlag("lockXTranslation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'tx',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockYTranslation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'ty',
                lock=True,
                keyable=False,
                channelBox=False)

        if kSceneItem.testFlag("lockZTranslation") is True:
            pm.setAttr(
                dccSceneItem.longName() + "." + 'tz',
                lock=True,
                keyable=False,
                channelBox=False)

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
            dccSceneItem.visibility.set(False)

        # Set Shape Visibility
        shapeVisAttr = kSceneItem.getShapeVisibilityAttr()
        if shapeVisAttr.isConnected() is False and kSceneItem.getShapeVisibility() is False:
            # Get shape node, if it exists, hide it.
            shape = dccSceneItem.getShape()
            if shape is not None:
                shape.visibility.set(False)

        return True

    # ================
    # Display Methods
    # ================
    def setObjectColor(self, kSceneItem):
        """Sets the color on the dccSceneItem.

        Args:
            kSceneItem (Object): kraken object to set the color on.

        Return:
            bool: True if successful.

        """

        colors = self.config.getColors()
        dccSceneItem = self.getDCCSceneItem(kSceneItem)
        buildColor = self.getBuildColor(kSceneItem)

        if buildColor is not None:
            dccSceneItem.overrideEnabled.set(True)
            dccSceneItem.overrideColor.set(colors[buildColor][0])

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

        quat = dt.Quaternion(kSceneItem.xfo.ori.v.x,
                             kSceneItem.xfo.ori.v.y,
                             kSceneItem.xfo.ori.v.z,
                             kSceneItem.xfo.ori.w)

        dccSceneItem.setScale(dt.Vector(
            kSceneItem.xfo.sc.x,
            kSceneItem.xfo.sc.y,
            kSceneItem.xfo.sc.z))

        dccSceneItem.setTranslation(dt.Vector(
            kSceneItem.xfo.tr.x,
            kSceneItem.xfo.tr.y,
            kSceneItem.xfo.tr.z),
            "world")

        dccSceneItem.setRotation(quat, "world")

        # Maya's rotation order enums:
        # 0 XYZ
        # 1 YZX
        # 2 ZXY
        # 3 XZY
        # 4 YXZ <-- 5 in Fabric
        # 5 ZYX <-- 4 in Fabric
        order = kSceneItem.ro.order
        if order == 4:
            order = 5
        elif order == 5:
            order = 4

        #  Maya api is one off from Maya's own node enum pyMel uses API
        dccSceneItem.setRotationOrder(order + 1, False)

        pm.select(clear=True)

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

        mat44 = mat44.transpose()
        matrix = []
        rows = [mat44.row0, mat44.row1, mat44.row2, mat44.row3]
        for row in rows:
            matrix.extend([row.x, row.y, row.z, row.t])

        cmds.setAttr(dccSceneItemName + "." + attr, matrix, type="matrix")

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

    def _postBuild(self):
        """Post-Build commands.

        Return:
            bool: True if successful.

        """

        return True
