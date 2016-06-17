"""Kraken SI - SI Builder module.

Classes:
Builder -- Component representation.

"""

import json
import logging

from kraken.log import getLogger

from kraken.core.maths import Math_radToDeg, RotationOrder
from kraken.core.kraken_system import ks
from kraken.core.builder import Builder

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad

from kraken.plugins.si_plugin.utils import *

logger = getLogger('kraken')
logger.setLevel(logging.INFO)


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
        dccSceneItem.Parameters('size').Value = 0.125
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
    def buildOrientationConstraint(self, kConstraint):
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

            # Softimage's rotation orders remapped
            # It appears Softimage uses the reversed orders
            # Not the same orders.
            rotOrderRemap = {
                0: 0,
                1: 3,
                2: 4,
                3: 1,
                4: 5,
                5: 2
            }

            order = rotOrderRemap[kConstraint.getConstrainee().ro.order]

            offsetXfo = kConstraint.computeOffset()
            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            dccSceneItem.Parameters('offx').Value = Math_radToDeg(offsetAngles.x)
            dccSceneItem.Parameters('offy').Value = Math_radToDeg(offsetAngles.y)
            dccSceneItem.Parameters('offz').Value = Math_radToDeg(offsetAngles.z)

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPoseConstraint(self, kConstraint):
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

            # Softimage's rotation orders
            #
            # 0 XYZ
            # 1 XZY
            # 2 YXZ
            # 3 YZX
            # 4 ZXY
            # 5 ZYX

            rotOrderRemap = {
                0: 4,
                1: 1,
                2: 2,
                3: 3,
                4: 5,
                5: 0
            }

            order = rotOrderRemap[kConstraint.getConstrainee().ro.order]

            offsetXfo = kConstraint.computeOffset()
            offsetAngles = offsetXfo.ori.toEulerAnglesWithRotOrder(
                RotationOrder(order))

            logger.inform([Math_radToDeg(offsetAngles.x),
                           Math_radToDeg(offsetAngles.y),
                           Math_radToDeg(offsetAngles.z)])

            dccSceneItem.Parameters('sclx').Value = offsetXfo.sc.x
            dccSceneItem.Parameters('scly').Value = offsetXfo.sc.y
            dccSceneItem.Parameters('sclz').Value = offsetXfo.sc.z
            dccSceneItem.Parameters('rotx').Value = Math_radToDeg(offsetAngles.x)
            dccSceneItem.Parameters('roty').Value = Math_radToDeg(offsetAngles.y)
            dccSceneItem.Parameters('rotz').Value = Math_radToDeg(offsetAngles.z)
            dccSceneItem.Parameters('posx').Value = offsetXfo.tr.x
            dccSceneItem.Parameters('posy').Value = offsetXfo.tr.y
            dccSceneItem.Parameters('posz').Value = offsetXfo.tr.z

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildPositionConstraint(self, kConstraint):
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

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    def buildScaleConstraint(self, kConstraint):
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

        self._registerSceneItemPair(kConstraint, dccSceneItem)

        return dccSceneItem

    # ========================
    # Component Build Methods
    # ========================
    def buildAttributeConnection(self, connectionInput):
        """Builds the link between the target and connection target.

        Args:
            connectionInput (object): kraken component input to build
                connections for.

        Returns:
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
        targetDCCSceneItem.AddExpression(connectionTargetDCCSceneItem.FullName)

        return True

    # =========================
    # Operator Builder Methods
    # =========================
    def buildKLOperator(self, kOperator):
        """Builds KL Operators on the components.

        Args:
            kOperator (object): kraken operator that represents a KL operator.

        Returns:
            bool: True if successful.

        """

        try:
            solverTypeName = kOperator.getSolverTypeName()
            args = kOperator.getSolverArgs()


            def findPortOfType(dataTypes, connectionTypes):
                for i in xrange(len(args)):
                    arg = args[i]
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

            ownerArg = args[ownerOutPortIndex]
            ownerArgName = ownerArg.name.getSimpleType()
            ownerArgDataType = ownerArg.dataType.getSimpleType()
            # ownerArgConnectionType = ownerArg.connectionType.getSimpleType()

            if ownerArgDataType == 'Mat44[]':
                operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerArgName)[0])
                ownerArgName = ownerArgName + str(0)
            else:
                operatorOwner = self.getDCCSceneItem(kOperator.getOutput(ownerArgName))


            # Create Splice Operator
            canvasOpPath = si.FabricCanvasOpApply(operatorOwner.FullName, "", True, "", "")
            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
            self._registerSceneItemPair(kOperator, canvasOp)

            si.FabricCanvasSetExtDeps(canvasOpPath, "", "Kraken")

            si.FabricCanvasAddFunc(canvasOpPath, "",
                                   kOperator.getName(),
                                   "dfgEntry {}",
                                   "400",
                                   "0")

            si.FabricCanvasAddPort(canvasOpPath,
                                   kOperator.getName(),
                                   "solver",
                                   "IO",
                                   solverTypeName,
                                   "",
                                   "Kraken")

            si.FabricCanvasAddPort(canvasOpPath,
                                   "",
                                   "solver",
                                   "IO",
                                   solverTypeName,
                                   "",
                                   "Kraken")

            si.FabricCanvasConnect(canvasOpPath,
                                   "",
                                   "solver",
                                   kOperator.getName() + ".solver")

            si.FabricCanvasConnect(canvasOpPath,
                                   "",
                                   kOperator.getName() + ".solver",
                                   "solver")


            def addCanvasPorts(canvasOpPath, portName, canvasGraphPort, portDataType, argConnectionType, dccSceneItem):

                if argConnectionType == 'In':
                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "In", portDataType, "")
                    si.FabricCanvasConnect(canvasOpPath, "", portName, canvasGraphPort)
                elif argConnectionType in ['IO', 'Out']:
                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "Out", portDataType, "")
                    si.FabricCanvasConnect(canvasOpPath, "", canvasGraphPort, portName)

                if portDataType == 'EvalContext':
                    return
                elif portDataType == 'DrawingHandle':
                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "Out", portDataType, canvasGraphPort, "", "")
                elif portDataType == 'InlineDebugShape':
                    return

                # Append the suffix based on the argument type, Softimage Only
                if portDataType in ('Xfo', 'Mat44'):
                    portmapDefinition = portName + "|XSI Port"

                    canvasOpPath2 = str(canvasOpPath) + ":"
                    si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                    canvasOpPath = str(canvasOpPath2)[:-1]

                    canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
                    si.FabricCanvasOpConnectPort(
                        canvasOpPath,
                        portName,
                        dccSceneItem.FullName + ".kine.global")

                elif portDataType in ['Scalar', 'Boolean', 'Integer']:

                    if argConnectionType == 'In':
                        portmapDefinition = portName + "|XSI Parameter"

                        canvasOpPath2 = str(canvasOpPath) + ":"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                        canvasOpPath = str(canvasOpPath2)[:-1]
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        parameter = canvasOp.Parameters(portName)
                        if parameter is not None:
                            if portName == 'time':
                                parameter.AddExpression("T")
                                return
                            if portName == 'frame':
                                parameter.AddExpression("Fc")
                                return
                            else:
                                parameter.AddExpression(dccSceneItem.FullName)

                    elif argConnectionType in ('Out', 'IO'):
                        portmapDefinition = portName + "|XSI Port"

                        canvasOpPath2 = str(canvasOpPath) + ":"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                        canvasOpPath = str(canvasOpPath2)[:-1]
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        outParamProp = canvasOp.Parent3DObject.Properties("_CanvasOut_" + portName)
                        parameter = outParamProp.Parameters('value')
                        dccSceneItem.AddExpression(parameter.FullName)

                    else:
                        raise NotImplementedError("'argConnectionType': " + argConnectionType + " is not supported!")

            arraySizes = {}
            # connect the operator to the objects in the DCC
            for i in xrange(len(args)):
                arg = args[i]
                argName = arg.name.getSimpleType()
                argDataType = arg.dataType.getSimpleType()
                argConnectionType = arg.connectionType.getSimpleType()

                canvasOpPath2 = str(canvasOpPath) + ":"

                if argDataType.endswith('[]'):
                    elementDataType = argDataType[:-2]
                    if argConnectionType == 'In':
                        connectedObjects = kOperator.getInput(argName)

                        arrayNode = si.FabricCanvasAddFunc(
                            canvasOpPath,
                            "",
                            argName + "_ComposeArray",
                            "dfgEntry {}",
                            "40",
                            str(i * 100))

                        si.FabricCanvasAddPort(
                            canvasOpPath,
                            arrayNode,
                            "array",
                            "Out",
                            argDataType,
                            "")

                        arrayNodeCode = "dfgEntry { \n  array.resize(" + str(len(connectedObjects)) + ");\n"
                        for j in range(len(connectedObjects)):
                            si.FabricCanvasAddPort(canvasOpPath,
                                                   arrayNode,
                                                   "value" + str(j),
                                                   "In",
                                                   elementDataType,
                                                   "",
                                                   "")

                            arrayNodeCode += "  array[" + str(j) + "] = value" + str(j) + ";\n"

                        arrayNodeCode += "}"

                        si.FabricCanvasSetCode(canvasOpPath,
                                               arrayNode,
                                               arrayNodeCode)

                        si.FabricCanvasAddPort(canvasOpPath,
                                               kOperator.getName(),
                                               argName,
                                               "In",
                                               argDataType,
                                               "")

                        si.FabricCanvasConnect(canvasOpPath,
                                               "",
                                               arrayNode + ".array",
                                               kOperator.getName() + "." + argName)

                    elif argConnectionType in ['IO', 'Out']:
                        connectedObjects = kOperator.getOutput(argName)

                        arrayNode = si.FabricCanvasAddFunc(
                            canvasOpPath,
                            "",
                            argName + "_DecomposeArray",
                            "dfgEntry {}",
                            "800",
                            str(i * 100))

                        si.FabricCanvasAddPort(canvasOpPath, arrayNode, "array", "In", argDataType, "")
                        arrayNodeCode = "dfgEntry { \n"
                        for j in xrange(len(connectedObjects)):
                            si.FabricCanvasAddPort(
                                canvasOpPath,
                                arrayNode,
                                "value" + str(j),
                                "Out",
                                elementDataType,
                                "",
                                "")

                            arrayNodeCode += "  value" + str(j) + " = array[" + str(j) + "];\n"

                        arrayNodeCode += "}"

                        si.FabricCanvasSetCode(canvasOpPath,
                                               arrayNode,
                                               arrayNodeCode)

                        si.FabricCanvasAddPort(canvasOpPath,
                                               kOperator.getName(),
                                               argName,
                                               "Out",
                                               argDataType,
                                               "")

                        si.FabricCanvasConnect(canvasOpPath,
                                               "",
                                               kOperator.getName() + "." + argName,
                                               arrayNode + ".array")

                        # OutArrays must be resized by the splice op.
                        arraySizes[argName] = len(connectedObjects)

                    for j in xrange(len(connectedObjects)):
                        dccSceneItem = self.getDCCSceneItem(connectedObjects[j])
                        if dccSceneItem is None:
                            if hasattr(opObject, "getName"):
                                # Handle output connections to visibility attributes.
                                if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                    dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                    dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                                elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                    dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                    dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                                else:
                                    raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + solverTypeName + "' arg:'" + argName + "' dcc item not found for item:" + connectedObjects[j].getPath())
                            elif portDataType in ('DrawingHandle'):
                                pass
                            else:
                                raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + solverTypeName + "' arg:'" + argName + "' dcc item not found for item:" + connectedObjects[j].getPath())

                        addCanvasPorts(canvasOpPath,
                                       argName + str(j),
                                       arrayNode + ".value" + str(j),
                                       elementDataType,
                                       argConnectionType,
                                       dccSceneItem)


                else:
                    if argConnectionType == 'In':
                        connectedObject = kOperator.getInput(argName)
                        si.FabricCanvasAddPort(canvasOpPath, kOperator.getName(), argName, "In", argDataType, "")
                    elif argConnectionType in ['IO', 'Out']:
                        connectedObject = kOperator.getOutput(argName)
                        si.FabricCanvasAddPort(canvasOpPath, kOperator.getName(), argName, "Out", argDataType, "")

                    dccSceneItem = self.getDCCSceneItem(connectedObject)
                    if dccSceneItem is None:
                        if hasattr(opObject, "getName"):
                            # Handle output connections to visibility attributes.
                            if opObject.getName() == 'visibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                            elif opObject.getName() == 'shapeVisibility' and opObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(opObject.getParent().getParent())
                                dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                            else:
                                raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + solverTypeName + "' arg:'" + argName + "' dcc item not found for item:" + connectedObjects[j].getPath())

                        else:
                            raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + solverTypeName + "' arg:'" + argName + "' dcc item not found for item:" + connectedObjects[j].getPath())

                    addCanvasPorts(canvasOpPath,
                                   argName,
                                   kOperator.getName() + "." + argName,
                                   argDataType,
                                   argConnectionType,
                                   dccSceneItem)

                canvasOpPath = canvasOpPath2[:-1]

            # Generate the operator source code.
            opSourceCode = kOperator.generateSourceCode(arraySizes=arraySizes)
            si.FabricCanvasSetCode(canvasOpPath, kOperator.getName(), opSourceCode)


        finally:
            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
            canvasOp.Parameters('graphExecMode').Value = 0

        return True

    def buildCanvasOperator(self, kOperator):
        """Builds Canvas Operators on the components.

        Args:
            kOperator (object): kraken operator that represents a Splice operator.

        Returns:
            bool: True if successful.

        """

        try:
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


            # Create Splice Operator
            canvasOpPath = si.FabricCanvasOpApply(operatorOwner.FullName, "", True, "", "")
            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
            self._registerSceneItemPair(kOperator, canvasOp)

            si.FabricCanvasSetExtDeps(canvasOpPath, "", "Kraken")
            uniqueNodeName = si.FabricCanvasInstPreset(canvasOpPath, "", kOperator.getPresetPath(), "400", "0")

            def addCanvasPorts(canvasOpPath, portName, canvasGraphPort, portDataType, argConnectionType, dccSceneItem):

                if argConnectionType == 'In':
                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "In", portDataType, "")
                    si.FabricCanvasConnect(canvasOpPath, "", portName, canvasGraphPort)
                elif argConnectionType in ['IO', 'Out']:
                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "Out", portDataType, "")
                    si.FabricCanvasConnect(canvasOpPath, "", canvasGraphPort, portName)

                if portDataType == 'EvalContext':
                    return
                elif portDataType == 'DrawingHandle':
                    si.FabricCanvasAddPort(canvasOpPath, "", portName, "Out", portDataType, canvasGraphPort, "", "")
                elif portDataType == 'InlineDebugShape':
                    return

                # Append the suffix based on the argument type, Softimage Only
                if portDataType in ('Xfo', 'Mat44'):
                    portmapDefinition = portName + "|XSI Port"

                    canvasOpPath2 = str(canvasOpPath) + ":"
                    si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                    canvasOpPath = str(canvasOpPath2)[:-1]
                    canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                    si.FabricCanvasOpConnectPort(
                        canvasOpPath,
                        portName,
                        dccSceneItem.FullName + ".kine.global")

                elif portDataType in ['Scalar', 'Boolean', 'Integer']:

                    if argConnectionType == 'In':
                        portmapDefinition = portName + "|XSI Parameter"

                        canvasOpPath2 = str(canvasOpPath) + ":"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                        canvasOpPath = str(canvasOpPath2)[:-1]
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        parameter = canvasOp.Parameters(portName)
                        if parameter is not None:
                            if portName == 'time':
                                parameter.AddExpression("T")
                                return
                            if portName == 'frame':
                                parameter.AddExpression("Fc")
                                return
                            else:
                                parameter.AddExpression(dccSceneItem.FullName)

                    elif argConnectionType in ('Out', 'IO'):
                        portmapDefinition = portName + "|XSI Port"

                        canvasOpPath2 = str(canvasOpPath) + ":"
                        si.FabricCanvasOpPortMapDefine(canvasOpPath, portmapDefinition)
                        canvasOpPath = str(canvasOpPath2)[:-1]
                        canvasOp = si.Dictionary.GetObject(canvasOpPath, False)

                        outParamProp = canvasOp.Parent3DObject.Properties("_CanvasOut_" + portName)
                        parameter = outParamProp.Parameters('value')
                        dccSceneItem.AddExpression(parameter.FullName)

                    else:
                        raise NotImplementedError("Argument '" + portName + "' connection type: '" + argConnectionType + " not supported!")


            # connect the operator to the objects in the DCC
            for i in xrange(node.getExecPortCount()):
                portName = node.getExecPortName(i)
                portConnectionType = portTypeMap[node.getExecPortType(i)]
                rtVal = opBinding.getArgValue(portName)
                portDataType = rtVal.getTypeName().getSimpleType()

                if portConnectionType not in ['In', 'IO', 'Out']:
                    raise Exception("Invalid connection type:" + portConnectionType)

                canvasOpPath2 = str(canvasOpPath) + ":"

                if portDataType.endswith('[]'):
                    elementDataType = portDataType[:-2]
                    if portConnectionType == 'In':
                        connectedObjects = kOperator.getInput(portName)
                        if connectedObjects is None:
                            continue

                        arrayNode = si.FabricCanvasAddFunc(
                            canvasOpPath,
                            "",
                            portName + "_ComposeArray",
                            "dfgEntry {}",
                            "40",
                            str(i * 100))

                        si.FabricCanvasAddPort(canvasOpPath,
                                               arrayNode,
                                               "array",
                                               "Out",
                                               portDataType,
                                               "")

                        arrayNodeCode = "dfgEntry { \n  array.resize(" + str(len(connectedObjects)) + ");\n"
                        for j in xrange(len(connectedObjects)):
                            si.FabricCanvasAddPort(canvasOpPath,
                                                   arrayNode,
                                                   "value" + str(j),
                                                   "In",
                                                   elementDataType,
                                                   "",
                                                   "")

                            arrayNodeCode += "  array[" + str(j) + "] = value" + str(j) + ";\n"

                        arrayNodeCode += "}"
                        si.FabricCanvasSetCode(canvasOpPath, arrayNode, arrayNodeCode)

                        si.FabricCanvasConnect(canvasOpPath,
                                               "",
                                               arrayNode + ".array",
                                               uniqueNodeName + "." + portName)

                    elif portConnectionType in ['IO', 'Out']:
                        connectedObjects = kOperator.getOutput(portName)
                        if connectedObjects is None:
                            continue

                        arrayNode = si.FabricCanvasAddFunc(
                            canvasOpPath,
                            "",
                            portName + "_DecomposeArray",
                            "dfgEntry {}",
                            "800",
                            str(i * 100))

                        si.FabricCanvasAddPort(canvasOpPath,
                                               arrayNode,
                                               "array",
                                               "In",
                                               portDataType,
                                               "")

                        arrayNodeCode = "dfgEntry { \n"
                        for j in xrange(len(connectedObjects)):
                            si.FabricCanvasAddPort(canvasOpPath,
                                                   arrayNode,
                                                   "value" + str(j),
                                                   "Out",
                                                   elementDataType,
                                                   "",
                                                   "")

                            arrayNodeCode += "  value" + str(j) + " = array[" + str(j) + "];\n"

                        arrayNodeCode += "}"
                        si.FabricCanvasSetCode(canvasOpPath,
                                               arrayNode,
                                               arrayNodeCode)

                        si.FabricCanvasConnect(canvasOpPath,
                                               "",
                                               uniqueNodeName + "." + portName,
                                               arrayNode + ".array")

                        # OutArrays must be resized by the splice op.
                        # arraySizes[portName] = len(connectedObjects)

                    for j in xrange(len(connectedObjects)):
                        dccSceneItem = self.getDCCSceneItem(connectedObjects[j])
                        if dccSceneItem is None:
                            if hasattr(connectedObjects[j], "getName"):
                                # Handle output connections to visibility attributes.
                                if connectedObjects[j].getName() == 'visibility' and connectedObjects[j].getParent().getName() == 'implicitAttrGrp':
                                    dccItem = self.getDCCSceneItem(connectedObjects[j].getParent().getParent())
                                    dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                                elif connectedObjects[j].getName() == 'shapeVisibility' and connectedObjects[j].getParent().getName() == 'implicitAttrGrp':
                                    dccItem = self.getDCCSceneItem(connectedObjects[j].getParent().getParent())
                                    dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                                else:
                                    raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + solverTypeName + "' arg:'" + argName + "' dcc item not found for item:" + connectedObjects[j].getPath())

                            else:
                                raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + solverTypeName + "' arg:'" + argName + "' dcc item not found for item:" + connectedObjects[j].getPath())

                        # Note: Need to find the operator each time as the
                        # operator is destroyed and recreated each time you add
                        # a new port.
                        canvasOp = si.Dictionary.GetObject(operatorOwner.Fullname + ".kine.global.CanvasOp", False)

                        addCanvasPorts(canvasOp,
                                       portName + str(j),
                                       arrayNode + ".value" + str(j),
                                       elementDataType,
                                       portConnectionType,
                                       dccSceneItem)

                else:
                    if portConnectionType == 'In':
                        connectedObject = kOperator.getInput(portName)
                    elif portConnectionType in ['IO', 'Out']:
                        connectedObject = kOperator.getOutput(portName)

                    if connectedObject is None and portDataType not in ('DrawingHandle'):
                        continue

                    dccSceneItem = self.getDCCSceneItem(connectedObject)
                    if dccSceneItem is None:
                        if hasattr(connectedObject, "getName"):
                            # Handle output connections to visibility attributes.
                            if connectedObject.getName() == 'visibility' and connectedObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(connectedObject.getParent().getParent())
                                dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                            elif connectedObject.getName() == 'shapeVisibility' and connectedObject.getParent().getName() == 'implicitAttrGrp':
                                dccItem = self.getDCCSceneItem(connectedObject.getParent().getParent())
                                dccSceneItem = dccItem.Properties('Visibility').Parameters('viewvis')
                            else:
                                raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + kOperator.getPresetPath() + "' port:'" + portName + "' dcc item not found.")
                        elif portDataType in ('DrawingHandle'):
                            pass
                        else:
                            raise Exception("Operator:'" + kOperator.getName() + "' of type:'" + kOperator.getPresetPath() + "' port:'" + portName + "' dcc item not found.")

                    addCanvasPorts(canvasOpPath, portName, uniqueNodeName + "." + portName, portDataType, portConnectionType, dccSceneItem)

                canvasOpPath = canvasOpPath2[:-1]

            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
            canvasOp.Parameters("graphExecMode").Value = 1
            canvasOp.Parameters("graphExecMode").Value = 0

        finally:
            canvasOp = si.Dictionary.GetObject(canvasOpPath, False)
            canvasOp.Parameters('graphExecMode').Value = 0

        return True

    # ==================
    # Parameter Methods
    # ==================
    def lockParameters(self, kSceneItem):
        """Locks flagged SRT parameters.

        Args:
            kSceneItem (object): kraken object to lock the SRT parameters on.

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
            displayProperty.Parameters("wirecolorr").Value = colors[buildColor][1][0]
            displayProperty.Parameters("wirecolorg").Value = colors[buildColor][1][1]
            displayProperty.Parameters("wirecolorb").Value = colors[buildColor][1][2]

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

        # Softimage's rotation orders remapped:
        rotOrderRemap = {
            0: 0,
            1: 3,
            2: 4,
            3: 1,
            4: 5,
            5: 2
        }

        order = rotOrderRemap[kSceneItem.ro.order]
        dccSceneItem.Kinematics.Local.Parameters('rotorder').Value = order

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

    def _postBuild(self):
        """Post-Build commands.

        Returns:
            bool: True if successful.

        """

        # Find all Canvas Ops and set to only execute if necessary
        canvasOps = si.FindObjects2(constants.siCustomOperatorID).Filter('CanvasOp')
        for op in canvasOps:
            op.Parameters('graphExecMode').Value = 1

        return True
