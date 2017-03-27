import re

from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV, aimAt
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import *


from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute


from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.transform import Transform
from kraken.core.objects.joint import Joint
from kraken.core.objects.space import Space
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component


COMPONENT_NAME = "hand"

class OSSHandComponent(OSS_Component):
    """Hand Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        super(OSSHandComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.hand_cmpOut = self.createOutput('hand', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.palm_cmpOut = self.createOutput('palm', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.ikgoal_cmpOut = self.createOutput('ikgoal', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs

        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()
        self.ikBlend_cmpOutAttr = self.createOutput('ikBlend', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()
        #self.limbMocap_cmpOutAttr = self.createOutput('limbMocap', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()
        self.softIK_cmpOutAttr = self.createOutput('softIK', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()
        self.stretch_cmpOutAttr = self.createOutput('stretch', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()



class OSSHandComponentGuide(OSSHandComponent):
    """Hand Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Hand Guide Component:" + name)
        super(OSSHandComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        # Guide Settings
        self.addPartialJoints = BoolAttribute('addPartialJoints', value=False, parent=self.guideSettingsAttrGrp)
        self.ikHandleSizeInputAttr = ScalarAttribute('ikHandleSize', value=1, minValue=0.0,   maxValue=50.0, parent=self.guideSettingsAttrGrp)
        #self.numDigits = IntegerAttribute('numDigits', value=5, minValue=1, maxValue=20, parent=self.guideSettingsAttrGrp)
        self.digit3SegmentNames = StringAttribute('Digit3SegmentNames', value="index middle ring pinky", parent=self.guideSettingsAttrGrp)
        self.digit2SegmentNames = StringAttribute('Digit2SegmentNames', value="thumb", parent=self.guideSettingsAttrGrp)
        self.digit1SegmentNames = StringAttribute('Digit1SegmentNames', value="", parent=self.guideSettingsAttrGrp)


        self.digit3SegmentNames.setValueChangeCallback(self.updateDigit3SegmentControls)
        self.digit2SegmentNames.setValueChangeCallback(self.updateDigit2SegmentControls)
        self.digit1SegmentNames.setValueChangeCallback(self.updateDigit1SegmentControls)

        # Guide Controls
        self.handCtrl = Control('hand', parent=self.ctrlCmpGrp, shape="sphere")
        self.palmCtrl = Control('palm', parent=self.ctrlCmpGrp, shape="sphere")
        self.palmCtrl.setShapeVisibility(False)  # For now, until this is an option
        self.palmCtrl.lockRotation(True, True, True)
        self.palmCtrl.lockScale(True, True, True)
        # self.palmCtrl.lockTranslation(True, True, True)
        self.palmTipCtrl = Control('palmTip', parent=self.ctrlCmpGrp, shape="sphere")
        self.handleCtrl = Control('handle', parent=self.ctrlCmpGrp, shape="jack")

        self.digit3SegmentCtrls = []
        self.digit2SegmentCtrls = []
        self.digit1SegmentCtrls = []

        data = {
                "name": name,
                "location": "L",
                "handXfo": Xfo(Vec3(1.85, 1.2, -1.2)),
                "palmXfo": Xfo(Vec3(1.85, 0.4, 0.25)),
                "palmTipXfo": Xfo(Vec3(1.85, 0.4, 1.5)),
                "handleXfo" : Xfo(Vec3(1.85, 0.0, -1.6)),
               }

        self.loadData(data)

        Profiler.getInstance().pop()


    # ==========
    # Callbacks
    # ==========
    def updateNumDigitsControls(self, numSegments, controlsList, digitNames):
        """Load a saved guide representation from persisted data.

        Arguments:
        numDigits -- object, The number of palm/toes

        Return:
        True if successful.

        """

        self.controlXforms = []

        # Store current values if guide controls already exist
        current = 0
        for i, ctrl in enumerate(controlsList):

            if ctrl.getParent() is self.palmCtrl:
                self.controlXforms.append([ctrl.xfo])
                current = len(self.controlXforms) -1
            else:
                self.controlXforms[current].append(ctrl.xfo)


        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        # Lets build all new digits
        digitNameList = getDigitNameList(digitNames)

        if not digitNameList:  # Nothing to build
            return True

        segments = ["palm", "base", "mid", "tip", "end"]
        if numSegments == 2:
            segments.remove("mid")
        elif numSegments == 1:
            segments.remove("mid")
            segments.remove("tip")

        offset = 0.0
        for i, digitName in enumerate(digitNameList):
            parent = self.palmCtrl
            for j, segment in enumerate(segments):
                newCtrl = Control(digitName+"_"+segment, parent=parent, shape="sphere")
                #newCtrl.scalePoints(Vec3(0.25, 0.25, 0.25))
                if j == 0:
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(10, 0.0, -offset)))
                    offset += 10.0
                else:
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(10.0, 0.0, 0.0)))

                controlsList.append(newCtrl)
                parent = newCtrl

                if i < len(self.controlXforms):
                    if j < len(self.controlXforms[i]):
                        newCtrl.xfo = self.controlXforms[i][j]
        return True


    def updateDigit3SegmentControls(self, digitNames):
        self.updateNumDigitsControls(3, self.digit3SegmentCtrls, digitNames)

    def updateDigit2SegmentControls(self, digitNames):
        self.updateNumDigitsControls(2, self.digit2SegmentCtrls, digitNames)

    def updateDigit1SegmentControls(self, digitNames):
        self.updateNumDigitsControls(1, self.digit1SegmentCtrls, digitNames)


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.


        Return:
        The JSON data object

        """

        data = super(OSSHandComponentGuide, self).saveData()

        data['handXfo'] = self.handCtrl.xfo
        data['palmXfo'] = self.palmCtrl.xfo
        data['palmTipXfo'] = self.palmTipCtrl.xfo
        data['handleXfo'] = self.handleCtrl.xfo


        for ctrlListName in ["digit3SegmentCtrls", "digit2SegmentCtrls", "digit1SegmentCtrls"]:
            ctrls = getattr(self, ctrlListName)
            xfos = []
            for i in xrange(len(ctrls)):
                xfos.append(ctrls[i].xfo)
            data[ctrlListName+"Xfos"] = xfos



        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSHandComponentGuide, self).loadData( data )


        #Reset all shapes, but really we should just recreate all controls from loadData instead of init
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        # TODO: make this a property of the component
        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]

        if "handXfo" in data.keys():
            self.handCtrl.xfo = data['handXfo']
        if "palmXfo" in data.keys():
            self.palmCtrl.xfo = data['palmXfo']
        if "palmTipXfo" in data.keys():
            self.palmTipCtrl.xfo = data['palmTipXfo']
        if "handleXfo" in data.keys():
            self.handleCtrl.xfo = data['handleXfo']


        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        self.globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.handCtrl.scalePoints(self.globalScaleVec)
        self.palmCtrl.scalePoints(self.globalScaleVec)
        self.palmTipCtrl.scalePoints(self.globalScaleVec)
        self.handleCtrl.scalePoints(self.globalScaleVec)

        self.handleCtrl.scalePoints(Vec3(data["ikHandleSize"], data["ikHandleSize"], data["ikHandleSize"]))

        for ctrlListName in ["digit3SegmentCtrls", "digit2SegmentCtrls", "digit1SegmentCtrls"]:
            ctrls = getattr(self, ctrlListName)
            if ctrlListName+"Xfos" in data.keys():
                for i in xrange(len(data[ctrlListName+"Xfos"])):
                    if i < len(ctrls):
                        ctrls[i].xfo = data[ctrlListName+"Xfos"][i]
                        ctrls[i].scalePoints(self.globalScaleVec)
        return True



    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSHandComponentGuide, self).getRigBuildData()



        # Values

        HandPosition = self.handCtrl.xfo.tr
        palmPosition = self.palmCtrl.xfo.tr
        palmTipPosition = self.palmTipCtrl.xfo.tr


        # Get lengths
        handLen = HandPosition.subtract(palmPosition).length()
        palmLen = palmPosition.subtract(palmTipPosition).length()

        handXfo = Xfo()
        handXfo.tr = HandPosition

        # Calculate Hand Xfo
        HandTopalm = palmPosition.subtract(HandPosition).unit()

        palmXfo = Xfo(self.palmCtrl.xfo)


        # In the complete guide system, have live constraint for palm upvec, this assumes Hand is higher than palm
        #upvec hard-coded for now.  Really, we should have an upVector in the guide setup
        aimAt(palmXfo, aimPos=palmTipPosition, upVector=handXfo.ori.getYaxis(), aimAxis=self.boneAxis, upAxis=self.upAxis)
        # Same here
        aimAt(handXfo, aimPos=palmXfo.tr, upVector=handXfo.ori.getYaxis(), aimAxis=self.boneAxis, upAxis=self.upAxis)

        handleXfo = self.handleCtrl.xfo
        # Not great.  This assumes that guide ctrl has been mirrored from left side
        # Another case where the guide system should feed in correct values
        #if self.getLocation() == 'R':
        #    handleXfo.ori = handleXfo.ori.mirror(0)

        data['handXfo'] = handXfo
        data['palmXfo'] = palmXfo
        data['handLen'] = handLen
        data['palmLen'] = palmLen
        data['handleXfo'] = handleXfo


        for ctrlListName in ["digit3SegmentCtrls", "digit2SegmentCtrls", "digit1SegmentCtrls"]:
            ctrls = getattr(self, ctrlListName)
            xfos = []
            for i in xrange(len(ctrls)):
                xfos.append(ctrls[i].xfo)
            data[ctrlListName+"Xfos"] = xfos

        return data

    # ==============
    # Class Methods
    # ==============
    @classmethod
    def getComponentType(cls):
        """Enables introspection of the class prior to construction to determine if it is a guide component.

        Return:
        The true if this component is a guide component.

        """

        return 'Guide'

    @classmethod
    def getRigComponentClass(cls):
        """Returns the corresponding rig component class for this guide component class

        Return:
        The rig component class.

        """

        return OSSHandComponentRig


class OSSHandComponentRig(OSSHandComponent):
    """Hand Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Leg Rig Component:" + name)
        super(OSSHandComponentRig, self).__init__(name, parent)

        self.mocap = False

        # =========
        # Controls
        # =========

        # IK Handle
        self.handleCtrl = IKControl("hand", parent=self.ctrlCmpGrp, shape="jack")
        self.handleCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZXY"])  #Set with component settings later careful when combining with foot!
        self.handleSpace = self.handleCtrl.insertSpace(name="hand_ik") # To avoid clashes
        self.handleIKSpace = Space('handIK', parent=self.handleCtrl)

        # FK Hand
        self.handCtrl = FKControl('hand', parent=self.ctrlCmpGrp, shape="cube")
        self.handCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.handCtrl.alignOnXAxis()
        self.handSpace = self.handCtrl.insertSpace(name="hand_fk")

        # FK palm
        self.palmCtrl = FKControl('palm', parent=self.handCtrl, shape="cube")
        self.palmCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.palmCtrl.alignOnXAxis()
        self.palmSpace = self.palmCtrl.insertSpace()

        # IK palm
        self.palmIKSpace = Space('palmIK', parent=self.handleIKSpace)


        # Rig Ref objects

        # Add Component Params to IK control
        self.handleCtrlAttrGrp = AttributeGroup("DisplayInfo_HandSettings", parent=self.handleCtrl)
        #ballBreakInputAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=self.handleCtrlAttrGrp)
        #HandTiltInputAttr = ScalarAttribute('handTilt', value=0.0, minValue=-180, maxValue=180.0, parent=self.handleCtrlAttrGrp)

        self.ikBlendAttr = ScalarAttribute('ikBlend', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.ikBlend_cmpOutAttr.connect(self.ikBlendAttr)
        self.handIKInputAttr = ScalarAttribute('handIK', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)

        # Need a more elegant way to drive attrs on another component, especially this one where we don't even know if the limb has mocap
        #self.limbMocapAttr = ScalarAttribute('limbMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        #self.limbMocap_cmpOutAttr.connect(self.limbMocapAttr)
        self.softIKAttr = ScalarAttribute('softIK', value=0.0, minValue=0.0, parent=self.handleCtrlAttrGrp)
        self.softIK_cmpOutAttr.connect(self.softIKAttr)
        self.stretchAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.stretch_cmpOutAttr.connect(self.stretchAttr)

        self.ikGoalRefTransform = Transform('ikGoalRef', parent=self.handleCtrl)

        handDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=self.handleCtrlAttrGrp)
        self.drawDebugInputAttr.connect(handDrawDebugInputAttr)
        # ==========
        # Deformers
        # ==========

        self.handDef = Joint('hand', parent=self.deformersParent)
        self.handDef.setComponent(self)
        self.handDef.constrainTo(self.hand_cmpOut, maintainOffset=False)
        self.hand_cmpOut.parentJoint =  self.handDef

        self.palmDef = Joint('palm', parent=self.handDef)
        self.palmDef.setComponent(self)
        self.palmDef.constrainTo(self.palmCtrl)
        self.palm_cmpOut.parentJoint =  self.palmDef

        self.parentSpaceInputTgt.childJoints = [self.handDef]

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        self.handSpaceConstraint = self.handSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.handleSpaceConstraint = self.handleSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        # Constraint outputs
        self.ikgoal_cmpOutConstraint = self.ikgoal_cmpOut.constrainTo(self.handleCtrl, maintainOffset=False)



        # Create IK joints (until footrocker system is integrated)
        self.ikHandTransform = Transform('ikHand', parent=self.handSpace)
        self.ikPalmTransform = Transform('ikPalm', parent=self.ikHandTransform)


        # ===============
        # Add KL Ops
        # ===============

        # Wait, can this be a hier blend op?
        # Add Hand Blend KL Op
        self.IKHandBlendKLOp = KLOperator(self.getName(), 'OSS_IKFootBlendSolver', 'OSS_Kraken')
        self.addOperator(self.IKHandBlendKLOp)
        # Add Att Inputs
        self.IKHandBlendKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.IKHandBlendKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.IKHandBlendKLOp.setInput('blend', self.handIKInputAttr)
        # Add Xfo Inputs)
        self.IKHandBlendKLOp.setInput('ikFoot', self.handleIKSpace)
        self.IKHandBlendKLOp.setInput('fkFoot', self.handCtrl)
        self.IKHandBlendKLOp.setInput('ikBall', self.palmIKSpace)
        self.IKHandBlendKLOp.setInput('fkBall', self.palmCtrl)
        # Add Xfo Outputs
        self.IKHandBlendKLOpHand_out = Transform('IKHandBlendKLOpHand_out', parent=self.outputHrcGrp)
        self.IKHandBlendKLOpPalm_out = Transform('IKHandBlendKLOpPalm_out', parent=self.outputHrcGrp)
        self.IKHandBlendKLOp.setOutput('foot', self.IKHandBlendKLOpHand_out)
        self.IKHandBlendKLOp.setOutput('ball', self.IKHandBlendKLOpPalm_out)


        Profiler.getInstance().pop()


    def createControls(self, numSegments, digitNames, data):

        digitNameList = getDigitNameList(digitNames)

        segments = ["palm", "base", "mid", "tip", "end"]
        if numSegments == 2:
            segments.remove("mid")
        elif numSegments == 1:
            segments.remove("mid")
            segments.remove("tip")

        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.handCtrl.xfo.ori.getZaxis()

        upVectorAxisStr = self.upAxisStr[-1]
        upVectorFunction = getattr(self.handCtrl.xfo.ori, "get"+upVectorAxisStr+"axis")
        upVector = upVectorFunction()
        if self.upAxisStr.startswith("NEG"):
            upVector = upVector.negate()


        for i, digitName in enumerate(digitNameList):
            parent = self.palm_cmpOut
            defParent = self.handDef
            digiSegCtrls = []
            digiSegDefs = []
            for j, segment in enumerate(segments):
                #Eventually, we need outputs and ports for this component for each digit segment
                #spineOutput = ComponentOutput(digitName+"_"+segment, parent=self.outputHrcGrp)

                if segment == "end":
                    continue  # don't create control for end (but we need it to loop through control positions correctly)
                digiSegCtrl = FKControl(digitName+"_"+segment, parent=parent, shape="square")
                digiSegCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["XZY"])  #Set with component settings later
                digiSegCtrl.rotatePoints(0,0,90)
                digiSegCtrl.scalePoints(globalScale)
                digiSegCtrls.append(digiSegCtrl)

                digiSegDef = Joint(digitName+"_"+segment, parent=defParent)
                digiSegDef.setComponent(self)
                digiSegDefs.append(digiSegDef)

                defParent = digiSegDef

                parent = digiSegCtrl
                ctrlListName = "digit"+str(numSegments)+"SegmentCtrls"

                if (ctrlListName+"Xfos") in data.keys():

                    index = i*len(segments) + j

                    if (i*numSegments + j) < len(data[ctrlListName+"Xfos"]):
                        digiSegCtrl.xfo = data[ctrlListName+"Xfos"][index]

            #Aim Control at child
            for j in range(len(digiSegCtrls)):

                if j == len(digiSegCtrls) - 1:
                    digiSegCtrls[j].xfo.ori = digiSegCtrls[j-1].xfo.ori
                else:
                    aimAt(digiSegCtrls[j].xfo, aimPos=digiSegCtrls[j+1].xfo.tr, upVector=upVector, aimAxis=self.boneAxis, upAxis=self.upAxis)

                digiSegCtrls[j].insertSpace()
                digiSegDefs[j].constrainTo(digiSegCtrls[j]).evaluate()

                if self.addPartialJoints:
                    twistXfo = self.createOutput(digiSegDefs[j].getName()+"_partial", dataType='Xfo', parent=self.outputHrcGrp).getTarget()
                    twistXfo.xfo = digiSegDefs[j].xfo
                    twistXfo.constrainTo(digiSegDefs[j].getParent(), maintainOffset=True)
                    self.createPartialJoint(digiSegDefs[j], baseTranslate=twistXfo, baseRotate=twistXfo, parent=digiSegDefs[j].getParent())



        return True




    # =============
    # Data Methods
    # =============
    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSHandComponentRig, self).loadData( data )

        self.mocap = bool(data["mocap"])

        self.addPartialJoints = bool(data['addPartialJoints'])  #This should be a simple method instead

        # TODO: make this a property of the component
        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]


        self.handleSpace.xfo = data['handleXfo']
        #aimAt(self.handleSpace.xfo., aimVector=Vec3(0, 1, 0), upPos=self.palmCtrl.xfo.tr, aimAxis=(0, 1, 0), upAxis=(0, 0, 1))
        self.handleCtrl.xfo = self.handleSpace.xfo

        self.handSpace.xfo = data['handXfo']
        self.handCtrl.xfo = data['handXfo']
        self.handCtrl.scalePointsOnAxis(data['handLen'], self.boneAxisStr)

        self.palmSpace.xfo = data['palmXfo']
        self.palmCtrl.xfo = data['palmXfo']
        self.palmCtrl.scalePointsOnAxis(data['palmLen'] / 5.0, self.boneAxisStr)

        self.handleIKSpace.xfo = self.handCtrl.xfo
        self.palmIKSpace.xfo = self.palmCtrl.xfo

        self.ikHandTransform = data['handXfo']
        self.ikPalmTransform = data['palmXfo']


        if self.getLocation() == "R":
            pass
            #self.legIKCtrl.rotatePoints(0, 90, 0)
            #self.legIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.legIKCtrl.rotatePoints(0, -90, 0)
            #self.legIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))


        self.createControls(3, data["Digit3SegmentNames"], data)
        self.createControls(2, data["Digit2SegmentNames"], data)
        self.createControls(1, data["Digit1SegmentNames"], data)

        self.connectReverse(self.handIKInputAttr, self.handCtrl.getVisibilityAttr())

        self.hand_cmpOutConstraint = self.hand_cmpOut.constrainTo(self.IKHandBlendKLOpHand_out)
        self.palm_cmpOutConstraint = self.palm_cmpOut.constrainTo(self.IKHandBlendKLOpPalm_out)



        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()
        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()
        self.ikgoal_cmpOutConstraint.evaluate()
        self.hand_cmpOutConstraint.evaluate()
        self.palm_cmpOutConstraint.evaluate()


        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.handCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize']*2, data['globalComponentCtrlSize']))
        self.palmCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize']*2, data['globalComponentCtrlSize']))
        self.handleCtrl.scalePoints(globalScale)
        self.handleCtrl.scalePoints(Vec3(data["ikHandleSize"], data["ikHandleSize"], data["ikHandleSize"]))

        """
        HandPlane = Control("TMP", shape="square")
        HandPlane.alignOnZAxis()
        HandPlane.scalePoints(Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], 1.0))
        # Damn, can't get the Hand length because it is on another component
        # Can we do this with just inputs?  We'd have to guarantee that everything was in the correct pose first
        #HandPlane.scalePointsOnAxis(self.handleCtrl.xfo.tr.subtract(self.palmTipPivotTransform.xfo.tr).length(), "POSZ")
        self.handleCtrl.appendCurveData(HandPlane.getCurveData())
        """
        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)


def getDigitNameList(digitNames):
    """ tokenizes string argument, returns a list"""

    digitNameList = re.split(r'[ ,:;]+', digitNames)

    # These checks should actually prevent the component_inspector from closing maybe?
    for name in digitNameList:
        if name and not re.match(r'^[\w_]+$', name):
            # Eventaully specific exception just for component class that display component name, etc.
            raise ValueError("digitNames \""+name+"\" contains non-alphanumeric characters in component \""+self.getName()+"\"")

    digitNameList = [x for x in digitNameList if x != ""]

    if not digitNameList:
        return []

    if len(digitNameList) > len(set(digitNameList)):
        raise ValueError("Duplicate names in digitNames in component \""+self.getName()+"\"")

    return digitNameList

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSHandComponentGuide)
ks.registerComponent(OSSHandComponentRig)
