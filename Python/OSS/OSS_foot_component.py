from kraken.core.maths import Vec3, AXIS_NAME_TO_TUPLE_MAP
from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV, aimAt
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.euler import rotationOrderStrToIntMapping

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
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control
from kraken.core.objects.transform import Transform

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *

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
        self.handleCtrl = Control('handle', parent=self.ctrlCmpGrp, shape="jack")


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
        for ctrl in self.getHierarchyNodes(classType=Control):
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

        # TODO: make this a property of the component
        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]


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


        aimAt(heelPivotXfo, aimPos=ballTipPivotPosition, upPos=footPosition, aimAxis=(0, 0, 1), upAxis=(0, 1, 0))
        # In the complete guide system, have live constraint for ball upvec, this assumes foot is higher than ball
        aimAt(ballXfo, aimPos=ballTipPosition, upPos=footPosition, aimAxis=self.boneAxis, upAxis=self.upAxis)
        # Same here
        aimAt(footXfo, aimPos=ballXfo.tr, upPos=ballTipPosition, aimAxis=self.boneAxis, upAxis=self.upAxis)

        ballTipPivotXfo.ori = heelPivotXfo.ori
        innerPivotXfo.ori = heelPivotXfo.ori
        outerPivotXfo.ori = heelPivotXfo.ori
        ballPivotXfo.ori = heelPivotXfo.ori

        handleXfo = self.handleCtrl.xfo
        # Not great.  This assumes that guide ctrl has been mirrored from left side
        # Another case where the guide system should feed in correct values
        if self.getLocation() == 'R':
            handleXfo.ori = handleXfo.ori.mirror(0)

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

        self.mocap = False

        # =========
        # Controls
        # =========

        # IK Handle
        self.handleCtrl = IKControl("foot", parent=self.ctrlCmpGrp, shape="jack")
        self.handleCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["ZXY"])  #Set with component settings later careful when combining with foot!
        self.handleCtrlSpace = self.handleCtrl.insertCtrlSpace()

        # FK Foot
        self.footCtrl = FKControl('foot', parent=self.ctrlCmpGrp, shape="cube")
        self.footCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["ZYX"])  #Set with component settings later
        self.footCtrlSpace = self.footCtrl.insertCtrlSpace()

        # FK Ball
        self.ballCtrl = FKControl('ball', parent=self.footCtrl, shape="cube")
        self.ballCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["ZYX"])  #Set with component settings later
        self.ballCtrlSpace = self.ballCtrl.insertCtrlSpace()



        # Rig Ref objects

        # Add Component Params to IK control
        self.handleCtrlAttrGrp = AttributeGroup("DisplayInfo_FootSettings", parent=self.handleCtrl)
        self.ikBlendAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.ikBlend_cmpOutAttr.connect(self.ikBlendAttr)


        footIKAttr = ScalarAttribute('footIK', value=1.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        footRockerAttr = ScalarAttribute('footRocker', value=0.0, minValue=-180.0, maxValue=180.0, parent=self.handleCtrlAttrGrp)
        ballBreakAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=self.handleCtrlAttrGrp)
        footTiltAttr = ScalarAttribute('footTilt', value=0.0, minValue=-180, maxValue=180.0, parent=self.handleCtrlAttrGrp)


        self.softDistAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=self.handleCtrlAttrGrp)
        self.softDist_cmpOutAttr.connect(self.softDistAttr)
        self.stretchAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.stretch_cmpOutAttr.connect(self.stretchAttr)

        drawDebugAttr = BoolAttribute('drawDebug', value=False, parent=self.handleCtrlAttrGrp)
        self.drawDebugInputAttr.connect(drawDebugAttr)

        self.limbMocapAttr = ScalarAttribute('limbMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)
        self.limbMocap_cmpOutAttr.connect(self.limbMocapAttr)

        self.ikGoalRefTransform = Transform('ikGoalRef', parent=self.handleCtrl)

        # =========
        # Nulls for foot pivot
        # =========
        self.ballJointTransform = Transform('ballJoint', parent=self.handleCtrl)
        self.footJointTransform = Transform('footJoint', parent=self.handleCtrl)
        self.heelPivotTransform = Transform('heelPivot', parent=self.handleCtrl)
        self.ballPivotTransform = Transform('ballPivot', parent=self.handleCtrl)
        self.ballTipPivotTransform = Transform('ballTipPivot', parent=self.handleCtrl)
        self.innerPivotTransform = Transform('innerPivot', parent=self.handleCtrl)
        self.outerPivotTransform = Transform('outerPivot', parent=self.handleCtrl)


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
        #self.ikgoal_cmpOutConstraint = self.ikgoal_cmpOut.constrainTo(self.handleCtrl, maintainOffset=False)


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
        self.footRockerKLOp.setInput('ikCtrl', self.ikGoalRefTransform)
        self.footRockerKLOp.setInput('heelPivot', self.heelPivotTransform)
        self.footRockerKLOp.setInput('ballPivot', self.ballPivotTransform)
        self.footRockerKLOp.setInput('toePivot', self.ballTipPivotTransform)
        self.footRockerKLOp.setInput('footJointLoc', self.footJointTransform)
        self.footRockerKLOp.setInput('ballJointLoc', self.ballJointTransform)
        self.footRockerKLOp.setInput('innerPivotLoc', self.innerPivotTransform)
        self.footRockerKLOp.setInput('outerPivotLoc', self.outerPivotTransform)
        # Add Xfo Outputs
        #self.legEndXfo_cmpOut = self.createOutput('legEndXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.footRockerFoot_out = Transform('footRockerFoot_out', parent=self.outputHrcGrp)
        self.footRockerBall_out = Transform('footRockerBall_out', parent=self.outputHrcGrp)
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
        self.IKFootBlendKLOpFoot_out = Transform('IKFootBlendKLOpFoot_out', parent=self.outputHrcGrp)
        self.IKFootBlendKLOpBall_out = Transform('IKFootBlendKLOpBall_out', parent=self.outputHrcGrp)
        self.IKFootBlendKLOp.setOutput('foot', self.IKFootBlendKLOpFoot_out)
        self.IKFootBlendKLOp.setOutput('ball', self.IKFootBlendKLOpBall_out)




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

        self.mocap = bool(data["mocap"])

        # TODO: make this a property of the component
        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]


        self.handleCtrl.xfo = data['handleXfo']
        self.handleCtrlSpace.xfo = Xfo(self.handleCtrl.xfo)

        self.footCtrl.xfo = data['footXfo']
        self.footCtrl.alignOnXAxis()
        self.footCtrl.scalePointsOnAxis(data['footLen'], self.boneAxisStr)
        self.footCtrlSpace.xfo = Xfo(self.footCtrl.xfo)

        self.ballCtrl.xfo = data['ballXfo']
        self.ballCtrl.alignOnXAxis()
        self.ballCtrl.scalePointsOnAxis(data['ballLen'], self.boneAxisStr)
        self.ballCtrlSpace.xfo = Xfo(self.ballCtrl.xfo)

        self.ikGoalRefTransform.xfo = data['handleXfo']

        if self.getLocation() == "R":
            pass
            #self.legIKCtrl.rotatePoints(0, 90, 0)
            #self.legIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.legIKCtrl.rotatePoints(0, -90, 0)
            #self.legIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))


        self.rightSideInputAttr.setValue(self.getLocation() == 'R')


        if self.mocap:
            self.mocapInputAttr = ScalarAttribute('mocap', value=0.0, minValue=0.0, maxValue=1.0, parent=self.handleCtrlAttrGrp)



            # Mocap Foot
            self.footMocapCtrl = MCControl('foot', parent=self.footCtrlSpace, shape="cube")
            self.footMocapCtrl.alignOnXAxis()
            self.footMocapCtrl.xfo = data['footXfo']
            self.footMocapCtrl.scalePointsOnAxis(data['footLen'], self.boneAxisStr)


            # Mocap Ball
            self.ballMocapCtrl = MCControl('ball', parent=self.footMocapCtrl, shape="cube")
            self.ballMocapCtrl.xfo = data['ballXfo']
            self.ballMocapCtrl.alignOnXAxis()
            self.ballMocapCtrl.scalePointsOnAxis(data['ballLen'], self.boneAxisStr)
            self.ballMocapCtrlSpace = self.ballMocapCtrl.insertCtrlSpace()


            # Add Foot Ball HierBlend Solver for Mocap
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
                self.IKFootBlendKLOpFoot_out,
                self.IKFootBlendKLOpBall_out
                ],
            )
            self.mocapHierBlendSolver.setInput('hierB',
                [
                self.footMocapCtrl,
                self.ballMocapCtrl,
                ]
            )
            #Create some nodes just for the oupt of the blend.
            #Wish we could just make direct connections....

            self.footMocapCtrl_link = CtrlSpace('footMocapCtrl_link', parent=self.outputHrcGrp)
            self.ballMocapCtrl_link = CtrlSpace('ballMocapCtrl_link', parent=self.outputHrcGrp)

            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.footMocapCtrl_link,
                self.ballMocapCtrl_link,
                ]
            )
            self.footOutputTgtConstraint = self.foot_cmpOut.constrainTo(self.footMocapCtrl_link)
            self.ballOutputTgtConstraint = self.ball_cmpOut.constrainTo(self.ballMocapCtrl_link)
        else:
            self.footOutputTgtConstraint = self.foot_cmpOut.constrainTo(self.IKFootBlendKLOpFoot_out)
            self.ballOutputTgtConstraint = self.ball_cmpOut.constrainTo(self.IKFootBlendKLOpBall_out)





        self.footSpaceInputTgt.xfo = data["footXfo"]
        self.footSpaceInputTgt.xfo.ori = Xfo(data["heelPivotXfo"]).ori

        self.ballJointTransform.xfo = data["ballXfo"]
        self.footJointTransform.xfo = data["footXfo"]
        self.heelPivotTransform.xfo = data["heelPivotXfo"]
        self.ballTipPivotTransform.xfo = data["ballTipPivotXfo"]
        self.innerPivotTransform.xfo = data["innerPivotXfo"]
        self.outerPivotTransform.xfo = data["outerPivotXfo"]
        self.ballPivotTransform.xfo = data["ballPivotXfo"]






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
        self.footOutputTgtConstraint.evaluate()
        self.ballOutputTgtConstraint.evaluate()

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
        #footPlane.scalePointsOnAxis(self.handleCtrl.xfo.tr.subtract(self.ballTipPivotTransform.xfo.tr).length(), "POSZ")
        self.handleCtrl.appendCurveData(footPlane.getCurveData())
        """


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSFootComponentGuide)
ks.registerComponent(OSSFootComponentRig)
