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

import traceback

COMPONENT_NAME = "foot"

class OSSFootComponent(BaseExampleComponent):
    """Foot Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        super(OSSFootComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.footSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.foot_cmpOut = self.createOutput('foot', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.ball_cmpOut = self.createOutput('ball', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
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


class OSSFootComponentGuide(OSSFootComponent):
    """Foot Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Foot Guide Component:" + name)
        super(OSSFootComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)
        self.ikHandleSizeInputAttr = ScalarAttribute('ikHandleSize', value=1, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        # Guide Controls
        self.footCtrl = Control('foot', parent=self.ctrlCmpGrp, shape="sphere")
        self.ballCtrl = Control('ball', parent=self.ctrlCmpGrp, shape="sphere")
        self.ballTipCtrl = Control('ballTip', parent=self.ctrlCmpGrp, shape="sphere")
        self.heelPivotCtrl = Control('heelPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.ballTipPivotCtrl = Control('ballTipPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.innerPivotCtrl = Control('innerPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.outerPivotCtrl = Control('outerPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.handleCtrl = Control('handle', parent=self.ctrlCmpGrp, shape="cross")


        data = {
                "name": name,
                "location": "L",
                "footXfo": Xfo(Vec3(1.85, 1.2, -1.2)),
                "ballXfo": Xfo(Vec3(1.85, 0.4, 0.25)),
                "ballTipXfo": Xfo(Vec3(1.85, 0.4, 1.5)),
                "heelPivotXfo": Xfo(Vec3(1.85, 0.0, -1.6)),
                "ballTipPivotXfo": Xfo(Vec3(1.85, 0.0, 1.5)),
                "innerPivotXfo": Xfo(Vec3(1., 0.0, 0.25)),
                "outerPivotXfo": Xfo(Vec3(2.67, 0.0, 0.25)),
                "handleXfo" : Xfo(Vec3(1.85, 0.0, -1.6)),
               }

        self.loadData(data)

        Profiler.getInstance().pop()


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.


        Return:
        The JSON data object

        """

        data = super(OSSFootComponentGuide, self).saveData()

        data['footXfo'] = self.footCtrl.xfo
        data['ballXfo'] = self.ballCtrl.xfo
        data['ballTipXfo'] = self.ballTipCtrl.xfo
        data['heelPivotXfo'] = self.heelPivotCtrl.xfo
        data['ballTipPivotXfo'] = self.ballTipPivotCtrl.xfo
        data['innerPivotXfo'] = self.innerPivotCtrl.xfo
        data['outerPivotXfo'] = self.outerPivotCtrl.xfo
        data['handleXfo'] = self.handleCtrl.xfo

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

        super(OSSFootComponentGuide, self).loadData( data )

        if "footXfo" in data.keys():
            self.footCtrl.xfo = data['footXfo']
        if "ballXfo" in data.keys():
            self.ballCtrl.xfo = data['ballXfo']
        if "ballTipXfo" in data.keys():
            self.ballTipCtrl.xfo = data['ballTipXfo']
        if "heelPivotXfo" in data.keys():
            self.heelPivotCtrl.xfo = data['heelPivotXfo']
        if "ballTipPivotXfo" in data.keys():
            self.ballTipPivotCtrl.xfo = data['ballTipPivotXfo']
        if "innerPivotXfo" in data.keys():
            self.innerPivotCtrl.xfo = data['innerPivotXfo']
        if "outerPivotXfo" in data.keys():
            self.outerPivotCtrl.xfo = data['outerPivotXfo']
        if "handleXfo" in data.keys():
            self.handleCtrl.xfo = data['handleXfo']


        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.footCtrl.scalePoints(globalScaleVec)
        self.ballCtrl.scalePoints(globalScaleVec)
        self.ballTipCtrl.scalePoints(globalScaleVec)
        self.heelPivotCtrl.scalePoints(globalScaleVec)
        self.ballTipPivotCtrl.scalePoints(globalScaleVec)
        self.innerPivotCtrl.scalePoints(globalScaleVec)
        self.outerPivotCtrl.scalePoints(globalScaleVec)
        self.handleCtrl.scalePoints(globalScaleVec)

        self.handleCtrl.scalePoints(Vec3(data["ikHandleSize"], data["ikHandleSize"], data["ikHandleSize"]))

        return True



    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSFootComponentGuide, self).getRigBuildData()

        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping[boneAxisStr]

        upAxisStr = "POSY"
        if self.getLocation() == 'R':
            upAxisStr = "NEGY"
        upAxis = axisStrToTupleMapping[upAxisStr]


        # Values

        footPosition = self.footCtrl.xfo.tr
        ballPosition = self.ballCtrl.xfo.tr
        ballTipPosition = self.ballTipCtrl.xfo.tr
        heelPivotPosition = self.heelPivotCtrl.xfo.tr
        ballTipPivotPosition = self.ballTipPivotCtrl.xfo.tr
        innerPivotPosition = self.innerPivotCtrl.xfo.tr
        outerPivotPosition = self.outerPivotCtrl.xfo.tr



        # Get lengths
        footLen = footPosition.subtract(ballPosition).length()
        ballLen = ballPosition.subtract(ballTipPosition).length()

        footXfo = Xfo()
        footXfo.tr = footPosition

        heelPivotXfo = Xfo()
        heelPivotXfo.tr = heelPivotPosition

        ballTipPivotXfo = Xfo()
        ballTipPivotXfo.tr = ballTipPivotPosition

        innerPivotXfo = Xfo()
        innerPivotXfo.tr = innerPivotPosition

        outerPivotXfo = Xfo()
        outerPivotXfo.tr = outerPivotPosition

        # Calculate Foot Xfo
        footToBall = ballPosition.subtract(footPosition).unit()

        ballXfo = Xfo(self.ballCtrl.xfo)

        ballPivotXfo = Xfo(ballXfo)


        heelPivotXfo.aimAt(aimPos=ballTipPivotPosition, upPos=footPosition, aimAxis=(0, 0, 1), upAxis=(0, 1, 0))
        # In the complete guide system, have live constraint for ball upvec, this assumes foot is higher than ball
        ballXfo.aimAt(aimPos=ballTipPosition, upPos=footPosition, aimAxis=boneAxis, upAxis=upAxis)
        # Same here
        footXfo.aimAt(aimPos=ballXfo.tr, upPos=ballTipPosition, aimAxis=boneAxis, upAxis=upAxis)

        ballTipPivotXfo.ori = heelPivotXfo.ori
        innerPivotXfo.ori = heelPivotXfo.ori
        outerPivotXfo.ori = heelPivotXfo.ori
        ballPivotXfo.ori = heelPivotXfo.ori

        handleXfo = self.handleCtrl.xfo

        data['footXfo'] = footXfo
        data['ballXfo'] = ballXfo
        data['footLen'] = footLen
        data['ballLen'] = ballLen
        data['heelPivotXfo'] = heelPivotXfo
        data['ballPivotXfo'] = ballPivotXfo
        data['ballTipPivotXfo'] = ballTipPivotXfo
        data['innerPivotXfo'] = innerPivotXfo
        data['outerPivotXfo'] = outerPivotXfo
        data['handleXfo'] = handleXfo

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

        return OSSFootComponentRig


class OSSFootComponentRig(OSSFootComponent):
    """Foot Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Leg Rig Component:" + name)
        super(OSSFootComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========

        # IK Handle
        self.handleCtrlSpace = CtrlSpace("footIK", parent=self.ctrlCmpGrp)
        self.handleCtrl = Control("footIK", parent=self.handleCtrlSpace, shape="cross")

        # FK Foot
        self.footCtrlSpace = CtrlSpace('foot', parent=self.ctrlCmpGrp)
        self.footCtrl = Control('foot', parent=self.footCtrlSpace, shape="cube")
        self.footCtrl.alignOnXAxis()

        # FK Ball
        self.ballCtrlSpace = CtrlSpace('ball', parent=self.footCtrl)
        self.ballCtrl = Control('ball', parent=self.ballCtrlSpace, shape="cube")
        self.ballCtrl.alignOnXAxis()

        # =========
        # Mocap
        # =========
        # Mocap Foot
        self.foot_mocap = Control('foot_mocap', parent=self.footCtrlSpace, shape="cube")
        self.foot_mocap.alignOnXAxis()
        # Mocap Ball
        self.ball_mocapSpace = CtrlSpace('ball_mocap', parent=self.foot_mocap)
        self.ball_mocap = Control('ball_mocap', parent=self.ball_mocapSpace, shape="cube")
        self.ball_mocap.alignOnXAxis()


        # Rig Ref objects

        # Add Component Params to IK control
        handleCtrlAttrGrp = AttributeGroup("DisplayInfo_FootSettings", parent=self.handleCtrl)
        footDrawDebugAttr = BoolAttribute('drawDebug', value=False, parent=handleCtrlAttrGrp)
        footMocapAttr = ScalarAttribute('mocap', value=0.0, minValue=0.0, maxValue=1.0, parent=handleCtrlAttrGrp)
        footIKAttr = ScalarAttribute('footIK', value=1.0, minValue=0.0, maxValue=1.0, parent=handleCtrlAttrGrp)
        footRockerAttr = ScalarAttribute('footRocker', value=0.0, minValue=-180.0, maxValue=180.0, parent=handleCtrlAttrGrp)
        ballBreakAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=handleCtrlAttrGrp)
        footTiltAttr = ScalarAttribute('footTilt', value=0.0, minValue=-180, maxValue=180.0, parent=handleCtrlAttrGrp)

        self.ikBlendAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=handleCtrlAttrGrp)
        self.ikBlend_cmpOutAttr.connect(self.ikBlendAttr)
        self.limbMocapAttr = ScalarAttribute('limbMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=handleCtrlAttrGrp)
        self.limbMocap_cmpOutAttr.connect(self.limbMocapAttr)
        self.softDistAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=handleCtrlAttrGrp)
        self.softDist_cmpOutAttr.connect(self.softDistAttr)
        self.stretchAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=handleCtrlAttrGrp)
        self.stretch_cmpOutAttr.connect(self.stretchAttr)


        self.drawDebugInputAttr.connect(footDrawDebugAttr)


        self.ikGoalRefLocator = Locator('ikGoalRef', parent=self.handleCtrl)
        self.ikGoalRefLocator.setShapeVisibility(False)

        # =========
        # Locators for foot pivot
        # =========
        self.ballJointLocator = Locator('ballJoint', parent=self.handleCtrl)
        #self.ballJointLocator.setVisibility(False) # does not seem to work, but setShapeVisibility does
        self.ballJointLocator.setShapeVisibility(False)
        self.footJointLocator = Locator('footJoint', parent=self.handleCtrl)
        self.footJointLocator.setShapeVisibility(False)
        self.heelPivotLocator = Locator('heelPivot', parent=self.handleCtrl)
        self.heelPivotLocator.setShapeVisibility(False)
        self.ballPivotLocator = Locator('ballPivot', parent=self.handleCtrl)
        self.ballPivotLocator.setShapeVisibility(False)
        self.ballTipPivotLocator = Locator('ballTipPivot', parent=self.handleCtrl)
        self.ballTipPivotLocator.setShapeVisibility(False)
        self.innerPivotLocator = Locator('innerPivot', parent=self.handleCtrl)
        self.innerPivotLocator.setShapeVisibility(False)
        self.outerPivotLocator = Locator('outerPivot', parent=self.handleCtrl)
        self.outerPivotLocator.setShapeVisibility(False)


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getLocation()+self.getName(), self, parent=deformersLayer)

        self.footDef = Joint('foot', parent=self.defCmpGrp)
        self.footDef.setComponent(self)

        self.ballDef = Joint('ball', parent=self.defCmpGrp)
        self.ballDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        self.handleCtrlSpaceConstraint = self.handleCtrlSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        self.footCtrlSpaceConstraint = self.footCtrlSpace.constrainTo(self.footSpaceInputTgt, maintainOffset=True)

        # Constraint outputs
        self.ikgoal_cmpOutConstraint = self.ikgoal_cmpOut.constrainTo(self.handleCtrl, maintainOffset=False)


        # ===============
        # Add KL Ops
        # ===============

        # Add FootRocker KL Op
        self.footRockerKLOp = KLOperator(self.getLocation()+self.getName()+'FootRockerKLOp', 'OSS_FootRockerSystem', 'OSS_Kraken')
        self.addOperator(self.footRockerKLOp)
        # Add Att Inputs
        self.footRockerKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.footRockerKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.footRockerKLOp.setInput('rightSide', self.rightSideInputAttr)
        self.footRockerKLOp.setInput('footRocker', footRockerAttr)
        self.footRockerKLOp.setInput('ballBreak', ballBreakAttr)
        self.footRockerKLOp.setInput('footTilt', footTiltAttr)
        # Add Xfo Inputs
        self.footRockerKLOp.setInput('ikCtrl', self.ikGoalRefLocator)
        self.footRockerKLOp.setInput('heelPivot', self.heelPivotLocator)
        self.footRockerKLOp.setInput('ballPivot', self.ballPivotLocator)
        self.footRockerKLOp.setInput('toePivot', self.ballTipPivotLocator)
        self.footRockerKLOp.setInput('footJointLoc', self.footJointLocator)
        self.footRockerKLOp.setInput('ballJointLoc', self.ballJointLocator)
        self.footRockerKLOp.setInput('innerPivotLoc', self.innerPivotLocator)
        self.footRockerKLOp.setInput('outerPivotLoc', self.outerPivotLocator)
        # Add Xfo Outputs
        #self.legEndXfo_cmpOut = self.createOutput('legEndXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.footRockerFoot_out = Locator('footRockerFoot_out', parent=self.outputHrcGrp)
        self.footRockerBall_out = Locator('footRockerBall_out', parent=self.outputHrcGrp)
        self.footRockerKLOp.setOutput('ikGoal', self.ikgoal_cmpOut)
        self.footRockerKLOp.setOutput('footJoint', self.footRockerFoot_out)
        self.footRockerKLOp.setOutput('ballJoint', self.footRockerBall_out)





        # Wait, can this be a hier blend op?  Don't like having this explicit OSS_IKFootBlendSolver Op
        # Add Foot Blend KL Op, no footBlend puts the position of the fk always at the ikOSS_IKFootBlendSolver Op pos, so maybe another kind of network
        self.IKFootBlendKLOp = KLOperator(self.getLocation()+self.getName()+'IKFootBlendKLOp', 'OSS_IKFootBlendSolver', 'OSS_Kraken')
        self.addOperator(self.IKFootBlendKLOp)
        # Add Att Inputs
        self.IKFootBlendKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.IKFootBlendKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.IKFootBlendKLOp.setInput('blend', footIKAttr)
        # Add Xfo Inputs)
        self.IKFootBlendKLOp.setInput('ikFoot', self.footRockerFoot_out)
        self.IKFootBlendKLOp.setInput('fkFoot', self.footCtrl)
        self.IKFootBlendKLOp.setInput('ikBall', self.footRockerBall_out)
        self.IKFootBlendKLOp.setInput('fkBall', self.ballCtrl)
        # Add Xfo Outputs
        self.IKFootBlendKLOpFoot_out = Locator('IKFootBlendKLOpFoot_out', parent=self.outputHrcGrp)
        self.IKFootBlendKLOpBall_out = Locator('IKFootBlendKLOpBall_out', parent=self.outputHrcGrp)
        self.IKFootBlendKLOp.setOutput('foot', self.IKFootBlendKLOpFoot_out)
        self.IKFootBlendKLOp.setOutput('ball', self.IKFootBlendKLOpBall_out)


        # Add Foot Ball HierBlend Solver for Mocap
        self.foot_mocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'foot_mocapHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.foot_mocapHierBlendSolver)
        self.foot_mocapHierBlendSolver.setInput('blend', footMocapAttr)
        self.foot_mocapHierBlendSolver.setInput('parentIndexes', [-1, 0])
        # Add Att Inputs
        self.foot_mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.foot_mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.foot_mocapHierBlendSolver.setInput('hierA', [self.IKFootBlendKLOpFoot_out, self.IKFootBlendKLOpBall_out])
        self.foot_mocapHierBlendSolver.setInput('hierB', [self.foot_mocap, self.ball_mocap])
        # Add Xfo Outputs
        self.foot_mocapHierBlendSolver.setOutput('hierOut', [self.foot_cmpOut, self.ball_cmpOut])


        # Add Deformer Joint Constrain
        self.outputsToDeformersKLOp = KLOperator(self.getLocation()+self.getName()+'DeformerJointsKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)
        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.foot_cmpOut, self.ball_cmpOut])
        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [self.footDef, self.ballDef])



        Profiler.getInstance().pop()

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

        super(OSSFootComponentRig, self).loadData( data )


        # TODO: make this a property of the component
        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping["NEGX"]


        self.handleCtrlSpace.xfo = data['handleXfo']
        #self.handleCtrlSpace.xfo.aimAt(aimVector=Vec3(0, 1, 0), upPos=self.ballCtrl.xfo.tr, aimAxis=(0, 1, 0), upAxis=(0, 0, 1))
        self.handleCtrl.xfo = self.handleCtrlSpace.xfo

        self.footCtrlSpace.xfo = data['footXfo']
        self.footCtrl.xfo = data['footXfo']
        self.footCtrl.scalePointsOnAxis(data['footLen'], boneAxisStr)

        self.ballCtrlSpace.xfo = data['ballXfo']
        self.ballCtrl.xfo = data['ballXfo']
        self.ballCtrl.scalePointsOnAxis(data['ballLen'], boneAxisStr)


        self.foot_mocap.xfo = data['footXfo']
        self.foot_mocap.scalePointsOnAxis(data['footLen'], boneAxisStr)

        self.ball_mocapSpace.xfo = data['ballXfo']
        self.ball_mocap.xfo = data['ballXfo']
        self.ball_mocap.scalePointsOnAxis(data['ballLen'], boneAxisStr)


        if self.getLocation() == "R":
            pass
            #self.legIKCtrl.rotatePoints(0, 90, 0)
            #self.legIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.legIKCtrl.rotatePoints(0, -90, 0)
            #self.legIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))


        self.rightSideInputAttr.setValue(self.getLocation() == 'R')

        self.footSpaceInputTgt.xfo = data["footXfo"]
        self.footSpaceInputTgt.xfo.ori = Xfo(data["heelPivotXfo"]).ori

        self.ballJointLocator.xfo = data["ballXfo"]
        self.footJointLocator.xfo = data["footXfo"]
        self.heelPivotLocator.xfo = data["heelPivotXfo"]
        self.ballTipPivotLocator.xfo = data["ballTipPivotXfo"]
        self.innerPivotLocator.xfo = data["innerPivotXfo"]
        self.outerPivotLocator.xfo = data["outerPivotXfo"]
        self.ballPivotLocator.xfo = data["ballPivotXfo"]


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


        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.footCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.ballCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.handleCtrl.scalePoints(globalScale)
        self.handleCtrl.scalePoints(Vec3(data["ikHandleSize"], data["ikHandleSize"], data["ikHandleSize"]))

        """
        footPlane = Control("TMP", shape="square")
        footPlane.alignOnZAxis()
        footPlane.scalePoints(Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], 1.0))
        # Damn, can't get the foot length because it is on another component
        # Can we do this with just inputs?  We'd have to guarantee that everything was in the correct pose first
        #footPlane.scalePointsOnAxis(self.handleCtrl.xfo.tr.subtract(self.ballTipPivotLocator.xfo.tr).length(), "POSZ")
        self.handleCtrl.appendCurveData(footPlane.getCurveData())
        """


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSFootComponentGuide)
ks.registerComponent(OSSFootComponentRig)
