import re

from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo, axisStrToTupleMapping
from kraken.core.maths.xfo import xfoFromDirAndUpV
import kraken.core.maths.euler as euler

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

COMPONENT_NAME = "hand"

class OSSHandComponent(BaseExampleComponent):
    """Hand Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        super(OSSHandComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.handSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.hand_cmpOut = self.createOutput('hand', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.palm_cmpOut = self.createOutput('palm', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.ikgoal_cmpOut = self.createOutput('ikgoal', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', value=1.0, dataType='Float', parent=self.cmpInputAttrGrp).getTarget()
        self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()
        self.ikBlend_cmpOutAttr = self.createOutput('ikBlend', dataType='Float', value=1.0, parent=self.cmpOutputAttrGrp).getTarget()
        self.limbMocap_cmpOutAttr = self.createOutput('limbMocap', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()
        self.softDist_cmpOutAttr = self.createOutput('softDist', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()
        self.stretch_cmpOutAttr = self.createOutput('stretch', dataType='Float', value=0.0, parent=self.cmpOutputAttrGrp).getTarget()
        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSHandComponentGuide(OSSHandComponent):
    """Hand Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Hand Guide Component:" + name)
        super(OSSHandComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.0, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)
        self.ikHandleSizeInputAttr = ScalarAttribute('ikHandleSize', value=1, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)
        #self.numDigits = IntegerAttribute('numDigits', value=5, minValue=1, maxValue=20, parent=guideSettingsAttrGrp)
        self.digit3SegmentNames = StringAttribute('Digit3SegmentNames', value="index middle ring pinky", parent=guideSettingsAttrGrp)
        self.digit2SegmentNames = StringAttribute('Digit2SegmentNames', value="thumb", parent=guideSettingsAttrGrp)
        self.digit1SegmentNames = StringAttribute('Digit1SegmentNames', value="", parent=guideSettingsAttrGrp)

        self.digit3SegmentNames.setValueChangeCallback(self.updateDigit3SegmentControls)
        self.digit2SegmentNames.setValueChangeCallback(self.updateDigit2SegmentControls)
        self.digit1SegmentNames.setValueChangeCallback(self.updateDigit1SegmentControls)

        # Guide Controls
        self.handCtrl = Control('hand', parent=self.ctrlCmpGrp, shape="sphere")
        self.palmCtrl = Control('palm', parent=self.ctrlCmpGrp, shape="sphere")
        self.palmTipCtrl = Control('palmTip', parent=self.ctrlCmpGrp, shape="sphere")
        self.handleCtrl = Control('handle', parent=self.ctrlCmpGrp, shape="cross")

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
        #Reset all shapes, but really we should just recreate all controls from loadData instead of init
        for ctrl in self.getAllHierarchyNodes(classType=Control):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSHandComponentGuide, self).loadData( data )

        if "handXfo" in data.keys():
            self.handCtrl.xfo = data['handXfo']
        if "palmXfo" in data.keys():
            self.palmCtrl.xfo = data['palmXfo']
        if "palmTipXfo" in data.keys():
            self.palmTipCtrl.xfo = data['palmTipXfo']
        if "handleXfo" in data.keys():
            self.handleCtrl.xfo = data['handleXfo']


        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.handCtrl.scalePoints(globalScaleVec)
        self.palmCtrl.scalePoints(globalScaleVec)
        self.palmTipCtrl.scalePoints(globalScaleVec)
        self.handleCtrl.scalePoints(globalScaleVec)

        self.handleCtrl.scalePoints(Vec3(data["ikHandleSize"], data["ikHandleSize"], data["ikHandleSize"]))

        for ctrlListName in ["digit3SegmentCtrls", "digit2SegmentCtrls", "digit1SegmentCtrls"]:
            ctrls = getattr(self, ctrlListName)
            if ctrlListName+"Xfos" in data.keys():
                for i in xrange(len(data[ctrlListName+"Xfos"])):
                    if i < len(ctrls):
                        ctrls[i].xfo = data[ctrlListName+"Xfos"][i]
        return True



    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSHandComponentGuide, self).getRigBuildData()

        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping[boneAxisStr]

        upAxisStr = "POSY"
        if self.getLocation() == 'R':
            upAxisStr = "NEGY"
        upAxis = axisStrToTupleMapping[upAxisStr]


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
        palmXfo.aimAt(aimPos=palmTipPosition, upVector=handXfo.ori.getYaxis(), aimAxis=boneAxis, upAxis=upAxis)
        # Same here
        handXfo.aimAt(aimPos=palmXfo.tr, upVector=handXfo.ori.getYaxis(), aimAxis=boneAxis, upAxis=upAxis)

        handleXfo = self.handleCtrl.xfo

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
        self.handleCtrlSpace = CtrlSpace("handIK", parent=self.ctrlCmpGrp)
        self.handleCtrl = Control("handIK", parent=self.handleCtrlSpace, shape="cross")

        # FK Hand
        self.handCtrlSpace = CtrlSpace('hand', parent=self.ctrlCmpGrp)
        self.handCtrl = Control('hand', parent=self.handCtrlSpace, shape="cube")
        self.handCtrl.alignOnXAxis()

        # FK palm
        self.palmCtrlSpace = CtrlSpace('palm', parent=self.handCtrl)
        self.palmCtrl = Control('palm', parent=self.palmCtrlSpace, shape="cube")
        self.palmCtrl.alignOnXAxis()

        # IK Hand
        self.handIKCtrlSpace = CtrlSpace('handIK', parent=self.handleCtrl)

        # IK palm
        self.palmCtrlSpace = CtrlSpace('palmIK', parent=self.handIKCtrlSpace)





        # Rig Ref objects

        # Add Component Params to IK control
        self.handleCtrlAttrGrp = AttributeGroup("DisplayInfo_HandSettings", parent=self.handleCtrl)
        handDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=self.handleCtrlAttrGrp)
        handIKInputAttr = ScalarAttribute('handIK', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        #ballBreakInputAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=self.handleCtrlAttrGrp)
        #HandTiltInputAttr = ScalarAttribute('handTilt', value=0.0, minValue=-180, maxValue=180.0, parent=self.handleCtrlAttrGrp)

        self.drawDebugInputAttr.connect(handDrawDebugInputAttr)

        self.ikBlendAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.ikBlend_cmpOutAttr.connect(self.ikBlendAttr)
        # Need a more elegant way to drive attrs on another component, especially this one where we don't even know if the limb has mocap
        self.limbMocapAttr = ScalarAttribute('limbMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.limbMocap_cmpOutAttr.connect(self.limbMocapAttr)
        self.softDistAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=self.handleCtrlAttrGrp)
        self.softDist_cmpOutAttr.connect(self.softDistAttr)
        self.stretchAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.stretch_cmpOutAttr.connect(self.stretchAttr)


        self.ikGoalRefLocator = Locator('ikGoalRef', parent=self.handleCtrl)
        self.ikGoalRefLocator.setShapeVisibility(False)


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getLocation()+self.getName(), self, parent=deformersLayer)

        self.handDef = Joint('hand', parent=self.defCmpGrp)
        self.handDef.setComponent(self)

        self.palmDef = Joint('palm', parent=self.defCmpGrp)
        self.palmDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        self.handCtrlSpaceConstraint = self.handCtrlSpace.constrainTo(self.handSpaceInputTgt, maintainOffset=True)
        self.handleCtrlSpaceConstraint = self.handleCtrlSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        # Constraint outputs
        self.ikgoal_cmpOutConstraint = self.ikgoal_cmpOut.constrainTo(self.handleCtrl, maintainOffset=False)



        # Create IK joints (until footrocker system is integrated)
        self.ikHandLocator = Locator('ikHand', parent=self.handCtrlSpace)
        self.ikPalmLocator = Locator('ikPalm', parent=self.ikHandLocator)


        # ===============
        # Add KL Ops
        # ===============




        # Wait, can this be a hier blend op?
        # Add Hand Blend KL Op
        self.IKHandBlendKLOp = KLOperator(self.getLocation()+self.getName()+'IKHandBlendKLOp', 'OSS_IKFootBlendSolver', 'OSS_Kraken')
        self.addOperator(self.IKHandBlendKLOp)
        # Add Att Inputs
        self.IKHandBlendKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.IKHandBlendKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.IKHandBlendKLOp.setInput('blend', handIKInputAttr)
        # Add Xfo Inputs)
        self.IKHandBlendKLOp.setInput('ikFoot', self.handIKCtrlSpace)
        self.IKHandBlendKLOp.setInput('fkFoot', self.handCtrl)
        self.IKHandBlendKLOp.setInput('ikBall', self.palmCtrlSpace)
        self.IKHandBlendKLOp.setInput('fkBall', self.palmCtrl)
        # Add Xfo Outputs
        self.IKHandBlendKLOpHand_out = Locator('IKHandBlendKLOpHand_out', parent=self.outputHrcGrp)
        self.IKHandBlendKLOpPalm_out = Locator('IKHandBlendKLOpPalm_out', parent=self.outputHrcGrp)
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


        for i, digitName in enumerate(digitNameList):
            parent = self.palm_cmpOut
            newCtrls = []
            newDefs = []
            for j, segment in enumerate(segments):
                #Eventually, we need outputs and ports for this component for each digit segment
                #spineOutput = ComponentOutput(digitName+"_"+segment, parent=self.outputHrcGrp)

                if segment == "end":
                    continue  # don't create control for end (but we need it to loop through control positions correctly)
                newCtrlSpace = CtrlSpace(digitName+"_"+segment, parent=parent)
                newCtrl = Control(digitName+"_"+segment, parent=newCtrlSpace, shape="square")
                newCtrl.rotatePoints(0,0,90)
                newCtrl.scalePoints(globalScale)
                newCtrls.append(newCtrl)

                newDef = Joint(digitName+"_"+segment, parent=self.defCmpGrp)
                newDefs.append(newDef)

                parent = newCtrl
                ctrlListName = "digit"+str(numSegments)+"SegmentCtrls"

                if (ctrlListName+"Xfos") in data.keys():

                    index = i*len(segments) + j

                    if (i*numSegments + j) < len(data[ctrlListName+"Xfos"]):
                        newCtrlSpace.xfo = data[ctrlListName+"Xfos"][index]
                        newCtrl.xfo = data[ctrlListName+"Xfos"][index]

            # Add Deformer Joint Constrain
            outputsToDeformersKLOp = KLOperator(self.getLocation()+self.getName()+digitName+'DeformerJointsKLOp', 'MultiPoseConstraintSolver', 'Kraken')
            self.addOperator(outputsToDeformersKLOp)
            # Add Att Inputs
            outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
            outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            outputsToDeformersKLOp.setInput('constrainers', newCtrls)
            # Add Xfo Outputs
            outputsToDeformersKLOp.setOutput('constrainees', newDefs)

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

        # TODO: make this a property of the component
        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping["NEGX"]


        self.handleCtrlSpace.xfo = data['handleXfo']
        #self.handleCtrlSpace.xfo.aimAt(aimVector=Vec3(0, 1, 0), upPos=self.palmCtrl.xfo.tr, aimAxis=(0, 1, 0), upAxis=(0, 0, 1))
        self.handleCtrl.xfo = self.handleCtrlSpace.xfo

        self.handCtrlSpace.xfo = data['handXfo']
        self.handCtrl.xfo = data['handXfo']
        self.handCtrl.scalePointsOnAxis(data['handLen'], boneAxisStr)

        self.palmCtrlSpace.xfo = data['palmXfo']
        self.palmCtrl.xfo = data['palmXfo']
        self.palmCtrl.scalePointsOnAxis(data['palmLen'], boneAxisStr)

        self.handIKCtrlSpace.xfo = self.handCtrl.xfo
        self.palmCtrlSpace.xfo = self.palmCtrl.xfo

        self.ikHandLocator = data['handXfo']
        self.ikPalmLocator = data['palmXfo']


        if self.getLocation() == "R":
            pass
            #self.legIKCtrl.rotatePoints(0, 90, 0)
            #self.legIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.legIKCtrl.rotatePoints(0, -90, 0)
            #self.legIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))


        self.rightSideInputAttr.setValue(self.getLocation() == 'R')

        self.createControls(3, data["Digit3SegmentNames"], data)
        self.createControls(2, data["Digit2SegmentNames"], data)
        self.createControls(1, data["Digit1SegmentNames"], data)

        if self.mocap:
            self.mocapInputAttr = ScalarAttribute('mocap', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
            # =========
            # Mocap
            # =========
            # Mocap Hand
            self.handMocapCtrl = Control('hand_mocap', parent=self.handCtrlSpace, shape="cube")
            self.handMocapCtrl.alignOnXAxis()
            self.handMocapCtrl.xfo = data['handXfo']
            self.handMocapCtrl.scalePointsOnAxis(data['handLen'], boneAxisStr)

            # Mocap palm
            self.palmMocapCtrlSpace = CtrlSpace('palm_mocap', parent=self.handMocapCtrl)
            self.palmMocapCtrlSpace.xfo = data['palmXfo']
            self.palmMocapCtrl = Control('palm_mocap', parent=self.palmMocapCtrlSpace, shape="cube")
            self.palmMocapCtrl.xfo = data['palmXfo']
            self.palmMocapCtrl.alignOnXAxis()
            self.palmMocapCtrl.scalePointsOnAxis(data['palmLen'], boneAxisStr)




            # Add Hand palm HierBlend Solver for Mocap
            self.mocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'mocapHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.mocapHierBlendSolver)
            self.mocapHierBlendSolver.setInput('blend', self.mocapInputAttr)
            self.mocapHierBlendSolver.setInput('parentIndexes', [-1, 0])
            # Add Att Inputs
            self.mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            self.mocapHierBlendSolver.setInput('hierA',
                [
                self.IKHandBlendKLOpHand_out,
                self.IKHandBlendKLOpPalm_out
                ],
            )
            self.mocapHierBlendSolver.setInput('hierB',
                [
                self.handMocapCtrl,
                self.palmMocapCtrl,
                ]
            )
            #Create some nodes just for the oupt of the blend.
            #Wish we could just make direct connections....

            self.handMocapCtrl_link = CtrlSpace('handMocapCtrl_link', parent=self.outputHrcGrp)
            self.palmMocapCtrl_link = CtrlSpace('palmMocapCtrl_link', parent=self.outputHrcGrp)

            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.handMocapCtrl_link,
                self.palmMocapCtrl_link,
                ]
            )
            self.handOutputTgtConstraint = self.hand_cmpOut.constrainTo(self.handMocapCtrl_link)
            self.palmOutputTgtConstraint = self.palm_cmpOut.constrainTo(self.palmMocapCtrl_link)
        else:
            self.handOutputTgtConstraint = self.hand_cmpOut.constrainTo(self.IKHandBlendKLOpHand_out)
            self.palmOutputTgtConstraint = self.palm_cmpOut.constrainTo(self.IKHandBlendKLOpPalm_out)


        # Add Deformer Joint Constrain
        self.outputsToDeformersKLOp = KLOperator(self.getLocation()+self.getName()+'DeformerJointsKLOpBlach', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)
        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.hand_cmpOut, self.palm_cmpOut])
        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [self.handDef, self.palmDef])

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
        self.handOutputTgtConstraint.evaluate()
        self.palmOutputTgtConstraint.evaluate()


        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.handCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.palmCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.handleCtrl.scalePoints(globalScale)
        self.handleCtrl.scalePoints(Vec3(data["ikHandleSize"], data["ikHandleSize"], data["ikHandleSize"]))

        """
        HandPlane = Control("TMP", shape="square")
        HandPlane.alignOnZAxis()
        HandPlane.scalePoints(Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], 1.0))
        # Damn, can't get the Hand length because it is on another component
        # Can we do this with just inputs?  We'd have to guarantee that everything was in the correct pose first
        #HandPlane.scalePointsOnAxis(self.handleCtrl.xfo.tr.subtract(self.palmTipPivotLocator.xfo.tr).length(), "POSZ")
        self.handleCtrl.appendCurveData(HandPlane.getCurveData())
        """


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
