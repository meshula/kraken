"""Kraken SI - SI Builder module.

Classes:
Builder -- Component representation.

"""

import json
import logging

from kraken.log import getLogger

from kraken.core.maths import Math_radToDeg, RotationOrder
from kraken.core.kraken_system import ks
from kraken.core.configs.config import Config
from kraken.core.builder import Builder

from kraken.core.maths import Vec2, Vec3, Xfo, Mat44, Math_radToDeg, RotationOrder
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.attributes.attribute import Attribute

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad

from kraken.plugins.si_plugin.utils import *


logger = getLogger('kraken')
logger.setLevel(logging.INFO)

# Rotation order remapping
# Softimage's enums don't map directly to the Fabric rotation orders
#
# Fabric | Softimage
# -------------------
# 0 ZYX  | 5 ZYX
# 1 XZY  | 1 XZY
# 2 YXZ  | 2 YXZ
# 3 YZX  | 3 YZX
# 4 XYZ  | 0 XYZ
# 5 ZXY  | 4 ZXY

ROT_ORDER_REMAP = {
    0: 5,
    1: 1,
    2: 2,
    3: 3,
    4: 0,
    5: 4
}


class Builder(Builder):
    """Builder object for building Kraken objects in Softimage."""

    def __init__(self):
        super(Builder, self).__init__()

    def deleteBuildElements(self):
        """Clear out all dcc built elements from the scene if exist."""

        si.SetValue("preferences.scripting.cmdlog", False, "")

        for builtElement in self._buildElements:
            if builtElement['src'].isTypeOf('Attribute'):
                continue

            node = builtElement['tgt']
            try:
                if node is not None and node.Parent.Name == 'Scene_Root':
                    si.DeleteObj("B:" + node.FullName)
                    si.Desktop.RedrawUI()
            except:
                continue

        self._buildElements = []

        si.SetValue("preferences.scripting.cmdlog", True, "")

        return

    # ========================
    # SceneItem Build Methods
    # ========================
    def buildContainer(self, kSceneItem, buildName):
        """Builds a container / namespace object.

        Args:
            kSceneItem (object): kSceneItem that represents a container to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = parentDCCSceneItem.AddModel(None, buildName)
        dccSceneItem.Name = buildName

        # Add custom param set to indicate that this object is the top level
        # Kraken Rig object

        if kSceneItem.isTypeOf('Rig'):
            dccSceneItem.AddProperty("CustomParameterSet", False, 'krakenRig')

            # Put Rig Data on DCC Item
            metaData = kSceneItem.getMetaData()
            if 'guideData' in metaData:
                pureJSON = metaData['guideData']

                rigData = dccSceneItem.AddProperty("UserDataBlob", False, 'krakenRigData')
                rigData.Value = json.dumps(pureJSON, indent=2)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildLayer(self, kSceneItem, buildName):
        """Builds a layer object.

        Args:
            kSceneItem (object): kSceneItem that represents a layer to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = parentDCCSceneItem.AddModel(None, buildName)
        dccSceneItem.Name = buildName
        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildHierarchyGroup(self, kSceneItem, buildName):
        """Builds a hierarchy group object.

        Args:
            kSceneItem (object): kSceneItem that represents a group to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: DCC Scene Item that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = parentDCCSceneItem.AddNull()
        dccSceneItem.Name = buildName

        lockObjXfo(dccSceneItem)

        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildGroup(self, kSceneItem, buildName):
        """Builds a locator / null object.

        Args:
            kSceneItem (object): kSceneItem that represents a group to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = parentDCCSceneItem.AddNull()
        dccSceneItem.Name = buildName
        dccSceneItem.Parameters('primary_icon').Value = 0
        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildJoint(self, kSceneItem, buildName):
        """Builds a joint object.

        Args:
            kSceneItem (object): kSceneItem that represents a joint to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: DCC Scene Item that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = parentDCCSceneItem.AddNull()
        dccSceneItem.Parameters('primary_icon').Value = 2
        dccSceneItem.Parameters('size').Value = kSceneItem.getRadius()

        dccSceneItem.Name = buildName
        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildLocator(self, kSceneItem, buildName):
        """Builds a locator / null object.

        Args:
            kSceneItem (object): kSceneItem that represents a locator / null
                to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = parentDCCSceneItem.AddNull()
        dccSceneItem.Name = buildName
        self._registerSceneItemPair(kSceneItem, dccSceneItem)

        return dccSceneItem

    def buildCurve(self, kSceneItem, buildName):
        """Builds a Curve object.

        Args:
            kSceneItem (object): kSceneItem that represents a curve to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = None

        # Format points for Softimage
        curveData = kSceneItem.getCurveData()

        curvePoints = []
        for eachSubCurve in curveData:
            subCurvePoints = eachSubCurve["points"]

            formattedPoints = []
            for i in xrange(3):
                axisPositions = []
                for p, eachPnt in enumerate(subCurvePoints):
                    if p < len(subCurvePoints):
                        axisPositions.append(eachPnt[i])

                formattedPoints.append(axisPositions)

            formattedPoints.append([1.0] * len(subCurvePoints))
            curvePoints.append(formattedPoints)

        # Build the curve
        for i, eachSubCurve in enumerate(curvePoints):
            closedSubCurve = curveData[i]["closed"]

            # Create knots
            if closedSubCurve is True:
                knots = list(xrange(len(eachSubCurve[0]) + 1))
            else:
                knots = list(xrange(len(eachSubCurve[0])))

            if i == 0:
                dccSceneItem = parentDCCSceneItem.AddNurbsCurve(
                    list(eachSubCurve),
                    knots,
                    closedSubCurve,
                    1,
                    constants.siNonUniformParameterization,
                    constants.siSINurbs)

                self._registerSceneItemPair(kSceneItem, dccSceneItem)
            else:
                dccSceneItem.ActivePrimitive.Geometry.AddCurve(
                    eachSubCurve,
                    knots,
                    closedSubCurve,
                    1,
                    constants.siNonUniformParameterization)

        dccSceneItem.Name = buildName

        return dccSceneItem

    def buildControl(self, kSceneItem, buildName):
        """Builds a Control object.

        Args:
            kSceneItem (object): kSceneItem that represents a control to be
                built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kSceneItem.getParent())

        if parentDCCSceneItem is None:
            parentDCCSceneItem = si.ActiveProject3.ActiveScene.Root

        dccSceneItem = None

        # Format points for Softimage
        curveData = kSceneItem.getCurveData()

        curvePoints = []
        for eachSubCurve in curveData:
            subCurvePoints = eachSubCurve["points"]

            formattedPoints = []
            for i in xrange(3):
                axisPositions = []
                for p, eachPnt in enumerate(subCurvePoints):
                    if p < len(subCurvePoints):
                        axisPositions.append(eachPnt[i])

                formattedPoints.append(axisPositions)

            formattedPoints.append([1.0] * len(subCurvePoints))
            curvePoints.append(formattedPoints)

        # Build the curve
        for i, eachSubCurve in enumerate(curvePoints):
            closedSubCurve = curveData[i]["closed"]

            # Create knots
            if closedSubCurve is True:
                knots = list(xrange(len(eachSubCurve[0]) + 1))
            else:
                knots = list(xrange(len(eachSubCurve[0])))

            if i == 0:
                dccSceneItem = parentDCCSceneItem.AddNurbsCurve(
                    list(eachSubCurve),
                    knots,
                    closedSubCurve,
                    1,
                    constants.siNonUniformParameterization,
                    constants.siSINurbs)

                self._registerSceneItemPair(kSceneItem, dccSceneItem)
            else:
                dccSceneItem.ActivePrimitive.Geometry.AddCurve(
                    eachSubCurve,
                    knots,
                    closedSubCurve,
                    1,
                    constants.siNonUniformParameterization)

        dccSceneItem.Name = buildName

        return dccSceneItem

    # ========================
    # Attribute Build Methods
    # ========================
    def buildBoolAttribute(self, kAttribute):
        """Builds a Bool attribute.

        Args:
            kAttribute (object): kAttribute that represents a boolean attribute
            to be built.

        Returns:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = Dispatch(self.getDCCSceneItem(kAttribute.getParent()))
        dccSceneItem = parentDCCSceneItem.AddParameter2(
            kAttribute.getName(),
            constants.siBool,
            kAttribute.getValue(),
            "",
            "",
            "",
            "",
            constants.siClassifUnknown,
            2053,
            kAttribute.getName())

        dccSceneItem.Animatable = kAttribute.getAnimatable()
        dccSceneItem.Keyable = kAttribute.getKeyable()
        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildScalarAttribute(self, kAttribute):
        """Builds a Float attribute.

        Args:
            kAttribute (object): kAttribute that represents a float attribute to be built.

        Returns:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = Dispatch(self.getDCCSceneItem(kAttribute.getParent()))
        dccSceneItem = parentDCCSceneItem.AddParameter2(
            kAttribute.getName(),
            constants.siDouble,
            kAttribute.getValue(),
            kAttribute.getMin(),
            kAttribute.getMax(),
            kAttribute.getUIMin(),
            kAttribute.getUIMax(),
            constants.siClassifUnknown,
            2053,
            kAttribute.getName())

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildIntegerAttribute(self, kAttribute):
        """Builds a Integer attribute.

        Args:
            kAttribute (object): kAttribute that represents a integer attribute to be built.

        Returns:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = Dispatch(self.getDCCSceneItem(kAttribute.getParent()))
        dccSceneItem = parentDCCSceneItem.AddParameter2(
            kAttribute.getName(),
            constants.siInt4,
            kAttribute.getValue(),
            kAttribute.getMin(),
            kAttribute.getMax(),
            kAttribute.getUIMin(),
            kAttribute.getUIMax(),
            constants.siClassifUnknown,
            2053,
            kAttribute.getName())

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildStringAttribute(self, kAttribute):
        """Builds a String attribute.

        Args:
            kAttribute (object): kAttribute that represents a string attribute to be built.

        Returns:
            bool: True if successful.

        """

        if kAttribute.getParent().getName() == 'implicitAttrGrp':
            return False

        parentDCCSceneItem = Dispatch(self.getDCCSceneItem(kAttribute.getParent()))
        dccSceneItem = parentDCCSceneItem.AddParameter2(
            kAttribute.getName(),
            constants.siString,
            kAttribute.getValue(),
            "",
            "",
            "",
            "",
            constants.siClassifUnknown,
            2053,
            kAttribute.getName())

        self._registerSceneItemPair(kAttribute, dccSceneItem)

        return True

    def buildAttributeGroup(self, kAttributeGroup):
        """Builds attribute groups on the DCC object.

        Args:
            kAttributeGroup (object): Kraken object to build the attribute group on.

        Returns:
            bool: True if successful.

        """

        parentDCCSceneItem = self.getDCCSceneItem(kAttributeGroup.getParent())

        groupName = kAttributeGroup.getName()
        if groupName == "implicitAttrGrp":
            return False

        dccSceneItem = parentDCCSceneItem.AddProperty("CustomParameterSet", False, groupName)
        self._registerSceneItemPair(kAttributeGroup, dccSceneItem)

        return True

    def connectAttribute(self, kAttribute):
        """Connects the driver attribute to this one.

        Args:
            kAttribute (object): Attribute to connect.

        Returns:
            bool: True if successful.

        """

        if kAttribute.isConnected() is True:

            # Detect if driver is visibility attribute and map to correct DCC attribute
            driverAttr = kAttribute.getConnection()
            if driverAttr.getName() == 'visibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                driver = dccItem.Properties("Visibility").Parameters("viewvis")

            elif driverAttr.getName() == 'shapeVisibility' and driverAttr.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(driverAttr.getParent().getParent())
                driver = dccItem.Properties("Visibility").Parameters("viewvis")

            else:
                driver = self.getDCCSceneItem(kAttribute.getConnection())

            # Detect if the driven attribute is a visibility attribute and map to correct DCC attribute
            if kAttribute.getName() == 'visibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                driven = dccItem.Properties("Visibility").Parameters("viewvis")

            elif kAttribute.getName() == 'shapeVisibility' and kAttribute.getParent().getName() == 'implicitAttrGrp':
                dccItem = self.getDCCSceneItem(kAttribute.getParent().getParent())
                driven = dccItem.Properties("Visibility").Parameters("viewvis")
            else:
                driven = self.getDCCSceneItem(kAttribute)


            driven.AddExpression(driver.FullName)

        return True

    # =========================
    # Constraint Build Methods
    # =========================
    def buildOrientationConstraint(self, kConstraint, buildName):
        """Builds an orientation constraint represented by the kConstraint.

        Args:
            kConstraint (object): Kraken constraint object to build.

        Returns:
            object: dccSceneItem that was created.

        """

        constraineeDCCSceneItem = self.getDCCSceneItem(kConstraint.getConstrainee())

        constrainers = getCollection()
        for eachConstrainer in kConstraint.getConstrainers():
            constrainers.AddItems(self.getDCCSceneItem(eachConstrainer))

        dccSceneItem = constraineeDCCSceneItem.Kinematics.AddConstraint(
            "Orientation",
            constrainers,
            kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:

            order = ROT_ORDER_REMAP[kConstraint.getConstrainee().ro.order]

            offsetXfo = kConstraint.computeOffset()
            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            dccSceneItem.Parameters('offx').Value = Math_radToDeg(offsetAngles.x)
            dccSceneItem.Parameters('offy').Value = Math_radToDeg(offsetAngles.y)
            dccSceneItem.Parameters('offz').Value = Math_radToDeg(offsetAngles.z)

        si.SetUserKeyword(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPoseConstraint(self, kConstraint, buildName):
        """Builds an pose constraint represented by the kConstraint.

        Args:
            kConstraint (object): kraken constraint object to build.

        Returns:
            bool: True if successful.

        """

        dccConstrainee = self.getDCCSceneItem(kConstraint.getConstrainee())

        constrainingObjs = getCollection()
        for eachConstrainer in kConstraint.getConstrainers():
            constrainer = self.getDCCSceneItem(eachConstrainer)
            constrainingObjs.AddItems(constrainer)

        dccSceneItem = dccConstrainee.Kinematics.AddConstraint(
            "Pose",
            constrainingObjs,
            kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:

            order = ROT_ORDER_REMAP[kConstraint.getConstrainee().ro.order]

            offsetXfo = kConstraint.computeOffset()
            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            dccSceneItem.Parameters('sclx').Value = offsetXfo.sc.x
            dccSceneItem.Parameters('scly').Value = offsetXfo.sc.y
            dccSceneItem.Parameters('sclz').Value = offsetXfo.sc.z
            dccSceneItem.Parameters('rotx').Value = Math_radToDeg(offsetAngles.x)
            dccSceneItem.Parameters('roty').Value = Math_radToDeg(offsetAngles.y)
            dccSceneItem.Parameters('rotz').Value = Math_radToDeg(offsetAngles.z)
            dccSceneItem.Parameters('posx').Value = offsetXfo.tr.x
            dccSceneItem.Parameters('posy').Value = offsetXfo.tr.y
            dccSceneItem.Parameters('posz').Value = offsetXfo.tr.z

        si.SetUserKeyword(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPositionConstraint(self, kConstraint, buildName):
        """Builds an position constraint represented by the kConstraint.

        Args:
            kConstraint (object): kraken constraint object to build.

        Returns:
            bool: True if successful.

        """

        dccConstrainee = self.getDCCSceneItem(kConstraint.getConstrainee())

        constrainers = getCollection()
        for eachConstrainer in kConstraint.getConstrainers():
            constrainers.AddItems(self.getDCCSceneItem(eachConstrainer))

        dccSceneItem = dccConstrainee.Kinematics.AddConstraint(
            "Position",
            constrainers,
            kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:
            offsetXfo = kConstraint.computeOffset()

            dccSceneItem.Parameters('off1x').Value = offsetXfo.tr.x
            dccSceneItem.Parameters('off1y').Value = offsetXfo.tr.y
            dccSceneItem.Parameters('off1z').Value = offsetXfo.tr.z

        si.SetUserKeyword(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildScaleConstraint(self, kConstraint, buildName):
        """Builds an scale constraint represented by the kConstraint.

        Args:
            kConstraint (object): kraken constraint object to build.

        Returns:
            bool: True if successful.

        """

        dccConstrainee = self.getDCCSceneItem(kConstraint.getConstrainee())

        constrainers = getCollection()
        for eachConstrainer in kConstraint.getConstrainers():
            constrainers.AddItems(self.getDCCSceneItem(eachConstrainer))

        dccSceneItem = dccConstrainee.Kinematics.AddConstraint(
            "Scaling",
            constrainers,
            kConstraint.getMaintainOffset())

        if kConstraint.getMaintainOffset() is True:
            offsetXfo = kConstraint.computeOffset()

            dccSceneItem.Parameters('offx').Value = offsetXfo.sc.x
            dccSceneItem.Parameters('offy').Value = offsetXfo.sc.y
            dccSceneItem.Parameters('offz').Value = offsetXfo.sc.z

        si.SetUserKeyword(dccSceneItem, buildName)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem


    # =========================
    # Operator Builder Methods
    # =========================
    def buildKLOperator(self, kOperator, buildName):
        """Builds KL Operators on the components.

        Args:
            kOperator (object): kraken operator that represents a KL operator.
            buildName (str): The name to use on the built object.

        Returns:
            bool: True if successful.

        """

        return self.buildCanvasOperator(kOperator, buildName, isKLBased=True)

    def buildCanvasOperator(self, kOperator, buildName, isKLBased=False):
        """Builds Canvas Operators on the components.

        Args:
            kOperator (object): kraken operator that represents a Splice operator.
            buildName (str): The name to use on the built object.
            isKLBased (bool): Whether the solver is based on a KL object.

        Returns:
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

        def addPortConnection(canvasOpPath, portName, portDataType, portConnectionType):

            if portDataType in ('Execute',
                                'EvalContext',
                                'DrawingHandle',
                                'InlineDebugShape'):
                return

            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

            if portConnectionType == 'In':
                connectedObjects = kOperator.getInput(portName)

                if type(connectedObjects) == list:
                    if portDataType[:-2] in ('Xfo', 'Mat44'):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        portmapDefinition = portName + "|XSI Port"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)

                        arrayInputString = ';'.join([self.getDCCSceneItem(x).FullName + ".kine.global" for x in connectedObjects])

                        si.FabricCanvasOpConnectPort(
                            canvasOpPath,
                            portName,
                            arrayInputString)
                else:
                    if isinstance(connectedObjects, Attribute):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                        dccSceneItem = self.getDCCSceneItem(connectedObjects)
                        portmapDefinition = portName + "|XSI Parameter"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                        parameter = canvasOp.Parameters(portName)

                        if parameter is not None:
                            parameter.AddExpression(dccSceneItem.FullName)
                    elif isinstance(connectedObjects, Object3D):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        portmapDefinition = portName + "|XSI Port"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)

                        dccSceneItem = self.getDCCSceneItem(connectedObjects)
                        si.FabricCanvasOpConnectPort(
                            canvasOpPath,
                            portName,
                            dccSceneItem.FullName + ".kine.global")
                    elif isinstance(connectedObjects, Xfo):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                        si.FabricCanvasSetArgValue(canvasOp, portName, portDataType, connectedObjects.getRTVal().getJSON().getSimpleType())
                    elif isinstance(connectedObjects, Mat44):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                        si.FabricCanvasSetArgValue(canvasOp, portName, portDataType, connectedObjects.getRTVal().getJSON().getSimpleType())
                    elif isinstance(connectedObjects, Vec2):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                        si.FabricCanvasSetArgValue(canvasOp, portName, portDataType, connectedObjects.getRTVal().getJSON().getSimpleType())
                    elif isinstance(connectedObjects, Vec3):
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                        si.FabricCanvasSetArgValue(canvasOp, portName, portDataType, connectedObjects.getRTVal().getJSON().getSimpleType())
                    else:
                        if portName in ('frame', 'time'):
                            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                            portmapDefinition = portName + "|XSI Parameter"
                            si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                            parameter = canvasOp.Parameters(portName)
                            if parameter is not None:
                                if portName == 'time':
                                    parameter.AddExpression("T")
                                elif portName == 'frame':
                                    parameter.AddExpression("Fc")

                        else:
                            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                            validatePortValue(connectedObjects, portName, portDataType)
                            si.FabricCanvasSetArgValue(canvasOp, portName, portDataType, connectedObjects)

            elif portConnectionType in ('Out', 'IO'):
                connectedObjects = kOperator.getOutput(portName)

                if type(connectedObjects) == list:
                    if portDataType[:-2] in ('Xfo', 'Mat44'):

                        for i in xrange(len(connectedObjects)):
                            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                            portmapDefinition = portName + str(i) + "|XSI Port"
                            si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)

                            dccSceneItem = self.getDCCSceneItem(connectedObjects[i])
                            si.FabricCanvasOpConnectPort(
                                canvasOpPath,
                                portName + str(i),
                                dccSceneItem.FullName + ".kine.global")
                else:
                    dccSceneItem = self.getDCCSceneItem(connectedObjects)

                    if isinstance(connectedObjects, Attribute):
                        portmapDefinition = portName + "|XSI Port"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        outParamProp = canvasOp.Parent3DObject.Properties("_CanvasOut_" + portName)
                        parameter = outParamProp.Parameters('value')

                        if hasattr(connectedObjects, "getName"):
                            # Handle output connections to visibility attributes.
                            if connectedObjects.getName() == 'visibility' and connectedObjects.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(connectedObjects.getParent().getParent())
                                dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                            elif connectedObjects.getName() == 'shapeVisibility' and connectedObjects.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(connectedObjects.getParent().getParent())
                                dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')

                        dccSceneItem.AddExpression(parameter.FullName)

                    elif isinstance(connectedObjects, Object3D):
                        portmapDefinition = portName + "|XSI Port"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)

                        si.FabricCanvasOpConnectPort(
                        canvasOpPath,
                        portName,
                        dccSceneItem.FullName + ".kine.global")

            else:
                raise Exception("Operator 'addPortConnection':'" + kOperator.getName() + " has an invalid 'portConnectionType': " + portConnectionType)

            return

        canvasOpPath = None
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

                # Find operatorOwner to attach Splice Operator to.
                ownerOutPortIndex = findPortOfType(['Mat44', 'Mat44[]'], ['Out', 'IO'])
                if ownerOutPortIndex is -1:
                    raise Exception("Solver '" + kOperator.getName() + "' has no Mat44 outputs!")

                ownerArg = ports[ownerOutPortIndex]
                ownerArgName = ownerArg.name.getSimpleType()
                ownerArgDataType = ownerArg.dataType.getSimpleType()
                # ownerArgConnectionType = ownerArg.connectionType.getSimpleType()

                if ownerArgDataType == 'Mat44[]':
                    operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerArgName)[0])
                    ownerArgName = ownerArgName + str(0)
                else:
                    operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerArgName))

                # Create Canvas Operator
                canvasOpPath = str(si.FabricCanvasOpApply(operatorOwner.FullName, "", True, "", ""))
                canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                canvasOp.Name = buildName
                self._registerSceneItemPair(kOperator, canvasOp)

                config = Config.getInstance()
                nameTemplate = config.getNameTemplate()
                typeTokens = nameTemplate['types']
                opTypeToken = typeTokens.get(type(kOperator).__name__, 'op')
                solverNodeName = '_'.join([kOperator.getName(), opTypeToken])
                solverSolveNodeName = '_'.join([kOperator.getName(), 'solve', opTypeToken])

                si.FabricCanvasSetExtDeps(canvasOpPath, "", kOperator.getExtension())

                solverTypeName = kOperator.getSolverTypeName()

                # Create Solver Function Node
                dfgEntry = "dfgEntry {\n  solver = " + solverTypeName + "();\n}"
                solverNodeCode = "{}\n\n{}".format('require ' + kOperator.getExtension() + ';', dfgEntry)

                si.FabricCanvasAddFunc(canvasOpPath,
                                       "",
                                       solverNodeName,
                                       solverNodeCode,
                                       "-220",
                                       "100")

                si.FabricCanvasAddPort(canvasOpPath,
                                       solverNodeName,
                                       "solver",
                                       "Out",
                                       solverTypeName,
                                       "",
                                       kOperator.getExtension())

                solverVarName = si.FabricCanvasAddVar(canvasOpPath,
                                                      "",
                                                      "solverVar",
                                                      solverTypeName,
                                                      kOperator.getExtension(),
                                                      "-75",
                                                      "100")

                si.FabricCanvasConnect(canvasOpPath,
                                       "",
                                       solverNodeName + ".solver",
                                       solverVarName + ".value")

                # Crate Solver "Solve" Function Node
                si.FabricCanvasAddFunc(canvasOpPath,
                                       "",
                                       solverSolveNodeName,
                                       "dfgEntry {}"
                                       "100",
                                       "100")

                si.FabricCanvasAddPort(canvasOpPath,
                                       solverSolveNodeName,
                                       "solver",
                                       "IO",
                                       solverTypeName,
                                       "",
                                       kOperator.getExtension())

                si.FabricCanvasConnect(canvasOpPath,
                                       "",
                                       solverVarName + ".value",
                                       solverSolveNodeName + ".solver")

                si.FabricCanvasConnect(canvasOpPath,
                                       "",
                                       solverSolveNodeName + ".solver",
                                       "exec")

                # Generate the operator source code.
                opSourceCode = kOperator.generateSourceCode()
                si.FabricCanvasSetCode(canvasOpPath, solverSolveNodeName, opSourceCode)

            else:
                host = ks.getCoreClient().DFG.host
                opBinding = host.createBindingToPreset(kOperator.getPresetPath())
                node = opBinding.getExec()
                portCount = node.getExecPortCount()

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

                # Create Splice Operator
                canvasOpPath = str(si.FabricCanvasOpApply(operatorOwner.FullName, "", True, "", ""))
                canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                canvasOp.Name = buildName
                self._registerSceneItemPair(kOperator, canvasOp)

                si.FabricCanvasSetExtDeps(canvasOpPath, "", "Kraken")

                uniqueNodeName = si.FabricCanvasInstPreset(canvasOpPath, "", kOperator.getPresetPath(), "400", "0")
                solverSolveNodeName = uniqueNodeName

            # Create operator ports and internal connections
            for i in xrange(portCount):
                if isKLBased is True:
                    port = ports[i]
                    portName = port.name.getSimpleType()
                    portDataType = port.dataType.getSimpleType()
                    portConnectionType = port.connectionType.getSimpleType()
                else:
                    portName = node.getExecPortName(i)
                    rtVal = opBinding.getArgValue(portName)
                    portDataType = rtVal.getTypeName().getSimpleType()
                    portConnectionType = portTypeMap[node.getExecPortType(i)]

                aCount = 0  # Store how many array nodes have been created.
                if portConnectionType == 'In':
                    if isKLBased is True:
                        si.FabricCanvasAddPort(canvasOpPath, solverSolveNodeName, portName, "In", portDataType, "")

                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "In", portDataType, "")
                    si.FabricCanvasConnect(canvasOpPath, "", portName, solverSolveNodeName + "." + portName)

                elif portConnectionType in ('IO', 'Out'):

                    if portDataType.endswith('[]'):
                        connectedObjects = kOperator.getOutput(portName)

                        arrayNode = si.FabricCanvasAddFunc(
                            canvasOpPath,
                            "",
                            portName + "_DecomposeArray",
                            "dfgEntry {}",
                            "800",
                            str(aCount * 100))

                        aCount += 1

                        si.FabricCanvasAddPort(canvasOpPath, arrayNode, portName, "In", portDataType, "")
                        arrayNodeCode = "dfgEntry { \n"
                        for j in xrange(len(connectedObjects)):
                            si.FabricCanvasAddPort(
                                canvasOpPath,
                                arrayNode,
                                portName + str(j),
                                "Out",
                                portDataType[:-2],
                                "",
                                "")

                            arrayNodeCode += "  " + portName + str(j) + " = " + portName + "[" + str(j) + "];\n"

                        arrayNodeCode += "}"

                        si.FabricCanvasAddPort(canvasOpPath,
                                               solverSolveNodeName,
                                               portName,
                                               "Out",
                                               portDataType,
                                               "")

                        si.FabricCanvasSetCode(canvasOpPath,
                                               arrayNode,
                                               arrayNodeCode)

                        si.FabricCanvasConnect(canvasOpPath,
                                               "",
                                               solverSolveNodeName + "." + portName,
                                               arrayNode + "." + portName)

                        for j in xrange(len(connectedObjects)):
                            si.FabricCanvasAddPort(canvasOpPath, "", portName + str(j), "Out", portDataType[:-2], "")
                            si.FabricCanvasConnect(canvasOpPath, "", arrayNode + "." + portName + str(j), portName + str(j))

                    else:
                        if isKLBased is True:
                            si.FabricCanvasAddPort(canvasOpPath, solverSolveNodeName, portName, "Out", portDataType, "")

                        if portDataType not in ('Execute', 'DrawingHandle'):
                            si.FabricCanvasAddPort(canvasOpPath, "", portName, "Out", portDataType, "")

                        if portDataType in ('Execute', 'DrawingHandle') and portName == 'exec':
                            pass
                        elif portDataType in ('Execute', 'DrawingHandle') and portName != 'exec':
                            si.FabricCanvasConnect(canvasOpPath, "", solverSolveNodeName + "." + portName, "exec")
                        else:
                            si.FabricCanvasConnect(canvasOpPath, "", solverSolveNodeName + "." + portName, portName)

                else:
                    raise Exception("Operator:'" + solverSolveNodeName + " has an invalid 'portConnectionType': " + portConnectionType)

            # Make connections from DCC objects to operator ports
            for i in xrange(portCount):
                if isKLBased is True:
                    port = ports[i]
                    portName = port.name.getSimpleType()
                    portDataType = port.dataType.getSimpleType()
                    portConnectionType = port.connectionType.getSimpleType()
                else:
                    portName = node.getExecPortName(i)
                    rtVal = opBinding.getArgValue(portName)
                    portDataType = rtVal.getTypeName().getSimpleType()
                    portConnectionType = portTypeMap[node.getExecPortType(i)]

                if portConnectionType == 'In':
                    addPortConnection(canvasOpPath, portName, portDataType, portConnectionType)

                elif portConnectionType in ('IO', 'Out'):
                    addPortConnection(canvasOpPath, portName, portDataType, portConnectionType)
                else:
                    raise Exception("Operator:'" + solverSolveNodeName + " has an invalid 'portConnectionType': " + portConnectionType)

        finally:
            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
            if canvasOp is not None:
                canvasOp.Parameters('graphExecMode').Value = 0

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

        if kAttribute.getName() in ('visibility', 'ShapeVisibility'):
            dccSceneItem = self.getDCCSceneItem(kAttribute.getParent().getParent())

            if kAttribute.getName() == 'visibility':
                visAttr = dccSceneItem.Properties("Visibility").Parameters("viewvis")
                visAttr.SetLock(constants.siLockLevelManipulation)
            elif kAttribute.getName() == 'ShapeVisibility':
                visAttr = dccSceneItem.Properties("Visibility").Parameters("viewvis")
                visAttr.SetLock(constants.siLockLevelManipulation)
            else:
                pass

        else:
            dccSceneItem = self.getDCCSceneItem(kAttribute)
            dccSceneItem.SetLock(constants.siLockLevelManipulation)

        return True

    def lockTransformAttrs(self, kSceneItem):
        """Locks flagged SRT attributes.

        Args:
            kSceneItem (object): kraken object to lock the SRT attributes on.

        Returns:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        # Lock Rotation
        if kSceneItem.testFlag("lockXRotation") is True:
            dccSceneItem.Kinematics.Local.Parameters('rotx').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('rotx').SetCapabilityFlag(constants.siKeyable, False)

        if kSceneItem.testFlag("lockYRotation") is True:
            dccSceneItem.Kinematics.Local.Parameters('roty').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('roty').SetCapabilityFlag(constants.siKeyable, False)

        if kSceneItem.testFlag("lockZRotation") is True:
            dccSceneItem.Kinematics.Local.Parameters('rotz').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('rotz').SetCapabilityFlag(constants.siKeyable, False)

        # Lock Scale
        if kSceneItem.testFlag("lockXScale") is True:
            dccSceneItem.Kinematics.Local.Parameters('sclx').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('sclx').SetCapabilityFlag(constants.siKeyable, False)

        if kSceneItem.testFlag("lockYScale") is True:
            dccSceneItem.Kinematics.Local.Parameters('scly').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('scly').SetCapabilityFlag(constants.siKeyable, False)

        if kSceneItem.testFlag("lockZScale") is True:
            dccSceneItem.Kinematics.Local.Parameters('sclz').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('sclz').SetCapabilityFlag(constants.siKeyable, False)

        # Lock Translation
        if kSceneItem.testFlag("lockXTranslation") is True:
            dccSceneItem.Kinematics.Local.Parameters('posx').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('posx').SetCapabilityFlag(constants.siKeyable, False)

        if kSceneItem.testFlag("lockYTranslation") is True:
            dccSceneItem.Kinematics.Local.Parameters('posy').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('posy').SetCapabilityFlag(constants.siKeyable, False)

        if kSceneItem.testFlag("lockZTranslation") is True:
            dccSceneItem.Kinematics.Local.Parameters('posz').SetLock(constants.siLockLevelManipulation)
            dccSceneItem.Kinematics.Local.Parameters('posz').SetCapabilityFlag(constants.siKeyable, False)

        return True

    # ===================
    # Visibility Methods
    # ===================
    def setVisibility(self, kSceneItem):
        """Sets the visibility of the object after its been created.

        Args:
            kSceneItem (object): kraken object to set the visibility on.

        Returns:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        # Set Visibility
        visAttr = kSceneItem.getVisibilityAttr()
        if visAttr.isConnected() is False and kSceneItem.getVisibility() is False:
            dccSceneItem.Properties("Visibility").Parameters("viewvis").Value = False

        # Set Shape Visibility
        shapeVisAttr = kSceneItem.getShapeVisibilityAttr()
        if shapeVisAttr.isConnected() is False and kSceneItem.getShapeVisibility() is False:
            dccSceneItem.Properties("Visibility").Parameters("viewvis").Value = False

        return True

    # ================
    # Display Methods
    # ================
    def setObjectColor(self, kSceneItem):
        """Sets the color on the dccSceneItem.

        Args:
            kSceneItem (object): kraken object to set the color on.

        Returns:
            bool: True if successful.

        """

        colors = self.config.getColors()
        dccSceneItem = self.getDCCSceneItem(kSceneItem)
        buildColor = self.getBuildColor(kSceneItem)

        if buildColor is not None:
            displayProperty = dccSceneItem.AddProperty("Display Property")

            # Object color is set as a string
            if type(buildColor) is str:

                # Color in config is stored as rgb scalar values in a list
                if type(colors[buildColor]) is list:
                    displayProperty.Parameters("wirecolorr").Value = colors[buildColor][0]
                    displayProperty.Parameters("wirecolorg").Value = colors[buildColor][1]
                    displayProperty.Parameters("wirecolorb").Value = colors[buildColor][2]

                # Color in config is stored as a Color object
                elif type(colors[buildColor]).__name__ == 'Color':
                    displayProperty.Parameters("wirecolorr").Value = colors[buildColor].r
                    displayProperty.Parameters("wirecolorg").Value = colors[buildColor].g
                    displayProperty.Parameters("wirecolorb").Value = colors[buildColor].b

                else:
                    raise TypeError(kSceneItem.getPath() + " has an invalid type: '" + type(colors[buildColor]).__name__ + "'")

            # Object color is set as a Color object
            elif type(buildColor).__name__ == 'Color':
                displayProperty.Parameters("wirecolorr").Value = buildColor.r
                displayProperty.Parameters("wirecolorg").Value = buildColor.g
                displayProperty.Parameters("wirecolorb").Value = buildColor.b

        return True

    # ==================
    # Transform Methods
    # ==================
    def setTransform(self, kSceneItem):
        """Translates the transform to Softimage transform.

        Args:
            kSceneItem (object): object to set the transform on.

        Returns:
            bool: True if successful.

        """

        dccSceneItem = self.getDCCSceneItem(kSceneItem)

        order = ROT_ORDER_REMAP[kSceneItem.ro.order]
        dccSceneItem.Kinematics.Local.Parameters('rotorder').Value = order

        xfo = XSIMath.CreateTransform()
        sc = XSIMath.CreateVector3(kSceneItem.xfo.sc.x,
                                   kSceneItem.xfo.sc.y,
                                   kSceneItem.xfo.sc.z)

        quat = XSIMath.CreateQuaternion(kSceneItem.xfo.ori.w,
                                        kSceneItem.xfo.ori.v.x,
                                        kSceneItem.xfo.ori.v.y,
                                        kSceneItem.xfo.ori.v.z)

        tr = XSIMath.CreateVector3(kSceneItem.xfo.tr.x,
                                   kSceneItem.xfo.tr.y,
                                   kSceneItem.xfo.tr.z)

        xfo.SetScaling(sc)
        xfo.SetRotationFromQuaternion(quat)
        xfo.SetTranslation(tr)

        dccSceneItem.Kinematics.Global.PutTransform2(None, xfo)

        return True

    def setMat44Attr(self, dccSceneItemName, attr, mat44):
        """Sets a matrix attribute directly with values from a fabric Mat44.

        Note: Fabric and Softimage's matrix row orders are reversed, so we
        transpose the matrix first.

        Args:
            dccSceneItemName (str): name of dccSceneItem.
            attr (str): name of matrix attribute to set.
            mat44 (Mat44): matrix value.

        Return:
            bool: True if successful.

        """

        xfo = XSIMath.CreateTransform()

        mat44 = mat44.transpose()
        matrix = []
        rows = [mat44.row0, mat44.row1, mat44.row2, mat44.row3]
        for row in rows:
            matrix.extend([row.x, row.y, row.z, row.t])

        xfo.SetMatrix4(matrix)

        dccSceneItem.Kinematics.Global.PutTransform2(None, xfo)

        return True

    # ==============
    # Build Methods
    # ==============
    def _preBuild(self, kSceneItem):
        """Pre-Build commands.

        Args:
            kSceneItem (object): kraken kSceneItem object to build.

        Returns:
            bool: True if successful.

        """

        si.SetValue("preferences.scripting.cmdlog", False, "")

        return True

    def _postBuild(self, kSceneItem):
        """Post-Build commands.

        Args:
            kSceneItem (object): kraken kSceneItem object to run post-build
                operations on.

        Returns:
            bool: True if successful.

        """

        super(Builder, self)._postBuild(kSceneItem)

        # Find all Canvas Ops and set to only execute if necessary
        nameTemplate = self.config.getNameTemplate()
        sep = nameTemplate['separator']
        klOpToken = nameTemplate['types'].get('KLOperator', None)
        canvasOpToken = nameTemplate['types'].get('CanvasOperator', None)

        if klOpToken is None or canvasOpToken is None:
            logger.warn("'KLOperator' or 'CanvasOperator' tokens not found in Config!")
        else:
            klOpName = klOpToken
            canvasOpName = canvasOpToken

            # Find all Canvas Ops and set to only execute if necessary
            klOps = si.FindObjects2(constants.siCustomOperatorID).Filter('', '', '*' + klOpName + '*')
            canvasOps = si.FindObjects2(constants.siCustomOperatorID).Filter('', '', '*' + canvasOpName + '*')

            fabricOps = getCollection()
            fabricOps.AddItems(klOps)
            fabricOps.AddItems(canvasOps)
            for op in fabricOps:
                op.Parameters('graphExecMode').Value = 1

        return True
