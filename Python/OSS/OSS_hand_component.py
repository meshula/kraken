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

class OSSHandComponent(BaseExampleComponent):
    """Hand Component"""

    def __init__(self, name='footBase', parent=None, data=None):

        super(OSSHandComponent, self).__init__(name=name, parent=parent, data=data)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.footSpaceInputTgt = self.createInput('footSpaceInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.ikGoalRefInputTgt = self.createInput('ikGoalRefInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.foot_cmpOut = self.createOutput('foot', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.toe_cmpOut = self.createOutput('toe', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.ikgoal_cmpOut = self.createOutput('ikgoal', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', value=1.0, dataType='Float', parent=self.cmpInputAttrGrp).getTarget()
        self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()

        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSHandComponentGuide(OSSHandComponent):
    """Hand Component Guide"""

    def __init__(self, name='foot', parent=None, data=None):

        Profiler.getInstance().push("Construct Hand Guide Component:" + name)
        super(OSSHandComponentGuide, self).__init__(name=name, parent=parent, data=data)


        # =========
        # Controls
        # ========

        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        # Guide Controls
        self.footCtrl = Control('foot', parent=self.ctrlCmpGrp, shape="sphere")
        self.toeCtrl = Control('toe', parent=self.ctrlCmpGrp, shape="sphere")
        self.toeTipCtrl = Control('toeTip', parent=self.ctrlCmpGrp, shape="sphere")
        self.heelPivotCtrl = Control('heelPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.toeTipPivotCtrl = Control('toeTipPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.innerPivotCtrl = Control('innerPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.outerPivotCtrl = Control('outerPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        if data is None:
            data = {
                    "name": name,
                    "location": "L",
                    "footXfo": Xfo(Vec3(1.85, 1.2, -1.2)),
                    "toeXfo": Xfo(Vec3(1.85, 0.4, 0.25)),
                    "toeTipXfo": Xfo(Vec3(1.85, 0.4, 1.5)),
                    "heelPivotXfo": Xfo(Vec3(1.85, 0.0, -1.6)),
                    "toeTipPivotXfo": Xfo(Vec3(1.85, 0.0, 1.5)),
                    "innerPivotXfo": Xfo(Vec3(1., 0.0, 0.25)),
                    "outerPivotXfo": Xfo(Vec3(2.67, 0.0, 0.25)),
                    "globalComponentCtrlSize": 1.0
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

        data = super(OSSHandComponentGuide, self).saveData()

        data['footXfo'] = self.footCtrl.xfo
        data['toeXfo'] = self.toeCtrl.xfo
        data['toeTipXfo'] = self.toeTipCtrl.xfo
        data['heelPivotXfo'] = self.heelPivotCtrl.xfo
        data['toeTipPivotXfo'] = self.toeTipPivotCtrl.xfo
        data['innerPivotXfo'] = self.innerPivotCtrl.xfo
        data['outerPivotXfo'] = self.outerPivotCtrl.xfo

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSHandComponentGuide, self).loadData( data )

        if "footXfo" in data.keys():
            self.footCtrl.xfo = data['footXfo']
        if "toeXfo" in data.keys():
            self.toeCtrl.xfo = data['toeXfo']
        if "toeTipXfo" in data.keys():
            self.toeTipCtrl.xfo = data['toeTipXfo']
        if "heelPivotXfo" in data.keys():
            self.heelPivotCtrl.xfo = data['heelPivotXfo']
        if "toeTipPivotXfo" in data.keys():
            self.toeTipPivotCtrl.xfo = data['toeTipPivotXfo']
        if "innerPivotXfo" in data.keys():
            self.innerPivotCtrl.xfo = data['innerPivotXfo']
        if "outerPivotXfo" in data.keys():
            self.outerPivotCtrl.xfo = data['outerPivotXfo']


        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.footCtrl.scalePoints(globalScaleVec)
        self.toeCtrl.scalePoints(globalScaleVec)
        self.toeTipCtrl.scalePoints(globalScaleVec)
        self.heelPivotCtrl.scalePoints(globalScaleVec)
        self.toeTipPivotCtrl.scalePoints(globalScaleVec)
        self.innerPivotCtrl.scalePoints(globalScaleVec)
        self.outerPivotCtrl.scalePoints(globalScaleVec)

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

        footPosition = self.footCtrl.xfo.tr
        toePosition = self.toeCtrl.xfo.tr
        toeTipPosition = self.toeTipCtrl.xfo.tr
        heelPivotPosition = self.heelPivotCtrl.xfo.tr
        toeTipPivotPosition = self.toeTipPivotCtrl.xfo.tr
        innerPivotPosition = self.innerPivotCtrl.xfo.tr
        outerPivotPosition = self.outerPivotCtrl.xfo.tr



        # Get lengths
        footLen = footPosition.subtract(toePosition).length()
        toeLen = toePosition.subtract(toeTipPosition).length()

        footXfo = Xfo()
        footXfo.tr = footPosition

        heelPivotXfo = Xfo()
        heelPivotXfo.tr = heelPivotPosition

        toeTipPivotXfo = Xfo()
        toeTipPivotXfo.tr = toeTipPivotPosition

        innerPivotXfo = Xfo()
        innerPivotXfo.tr = innerPivotPosition

        outerPivotXfo = Xfo()
        outerPivotXfo.tr = outerPivotPosition

        # Calculate Hand Xfo
        footToToe = toePosition.subtract(footPosition).unit()

        toeXfo = Xfo(self.toeCtrl.xfo)

        toePivotXfo = Xfo(toeXfo)


        heelPivotXfo.aimAt(aimPos=toeTipPivotPosition, upPos=footPosition, aimAxis=(0, 0, 1), upAxis=(0, 1, 0))
        # In the complete guide system, have live constraint for toe upvec, this assumes foot is higher than toe
        toeXfo.aimAt(aimPos=toeTipPosition, upPos=footPosition, aimAxis=boneAxis, upAxis=upAxis)
        # Same here
        footXfo.aimAt(aimPos=toeXfo.tr, upPos=toeTipPosition, aimAxis=boneAxis, upAxis=upAxis)

        toeTipPivotXfo.ori = heelPivotXfo.ori
        innerPivotXfo.ori = heelPivotXfo.ori
        outerPivotXfo.ori = heelPivotXfo.ori
        toePivotXfo.ori = heelPivotXfo.ori

        data['footXfo'] = footXfo
        data['toeXfo'] = toeXfo
        data['footLen'] = footLen
        data['toeLen'] = toeLen
        data['heelPivotXfo'] = heelPivotXfo
        data['toePivotXfo'] = toePivotXfo
        data['toeTipPivotXfo'] = toeTipPivotXfo
        data['innerPivotXfo'] = innerPivotXfo
        data['outerPivotXfo'] = outerPivotXfo

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

    def __init__(self, name='leg', parent=None, data=None):

        Profiler.getInstance().push("Construct MainSrt Rig Component:" + name)
        super(OSSHandComponentRig, self).__init__(name=name, parent=parent, data=data)


        # =========
        # Controls
        # =========
        # FK Hand
        self.footCtrlSpace = CtrlSpace('foot', parent=self.ctrlCmpGrp)
        self.footCtrl = Control('foot', parent=self.footCtrlSpace, shape="cube")
        self.footCtrl.alignOnXAxis()

        # FK Toe
        self.toeCtrlSpace = CtrlSpace('toe', parent=self.footCtrl)
        self.toeCtrl = Control('toe', parent=self.toeCtrlSpace, shape="cube")
        self.toeCtrl.alignOnXAxis()

        # =========
        # Mocap
        # =========
        # Mocap Hand
        self.foot_mocap = Control('foot_mocap', parent=self.footCtrlSpace, shape="cube")
        self.foot_mocap.alignOnXAxis()
        # Mocap Toe
        self.toe_mocapSpace = CtrlSpace('toe_mocap', parent=self.foot_mocap)
        self.toe_mocap = Control('toe_mocap', parent=self.toe_mocapSpace, shape="cube")
        self.toe_mocap.alignOnXAxis()




        # Rig Ref objects

        # Add Component Params to IK control
        footSettingsAttrGrp = AttributeGroup("DisplayInfo_HandSettings", parent=self.footCtrl)
        footDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=footSettingsAttrGrp)
        footMocapInputAttr = ScalarAttribute('footMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=footSettingsAttrGrp)
        footIKInputAttr = ScalarAttribute('footIK', value=1.0, minValue=0.0, maxValue=1.0, parent=footSettingsAttrGrp)
        footRockerInputAttr = ScalarAttribute('footRocker', value=0.0, minValue=-180.0, maxValue=180.0, parent=footSettingsAttrGrp)
        ballBreakInputAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=footSettingsAttrGrp)
        footTiltInputAttr = ScalarAttribute('footTilt', value=0.0, minValue=-180, maxValue=180.0, parent=footSettingsAttrGrp)

        self.drawDebugInputAttr.connect(footDrawDebugInputAttr)


        self.ikGoalRefLocator = Locator('ikGoalRef', parent=self.ikGoalRefInputTgt)
        self.ikGoalRefLocator.setShapeVisibility(False)

        # =========
        # Locators for foot pivot
        # =========
        self.toeJointLocator = Locator('toeJoint', parent=self.ikGoalRefInputTgt)
        #self.toeJointLocator.setVisibility(False) # does not seem to work, but setShapeVisibility does
        self.toeJointLocator.setShapeVisibility(False)
        self.footJointLocator = Locator('footJoint', parent=self.ikGoalRefInputTgt)
        self.footJointLocator.setShapeVisibility(False)
        self.heelPivotLocator = Locator('heelPivot', parent=self.ikGoalRefInputTgt)
        self.heelPivotLocator.setShapeVisibility(False)
        self.toePivotLocator = Locator('toePivot', parent=self.ikGoalRefInputTgt)
        self.toePivotLocator.setShapeVisibility(False)
        self.toeTipPivotLocator = Locator('toeTipPivot', parent=self.ikGoalRefInputTgt)
        self.toeTipPivotLocator.setShapeVisibility(False)
        self.innerPivotLocator = Locator('innerPivot', parent=self.ikGoalRefInputTgt)
        self.innerPivotLocator.setShapeVisibility(False)
        self.outerPivotLocator = Locator('outerPivot', parent=self.ikGoalRefInputTgt)
        self.outerPivotLocator.setShapeVisibility(False)


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getLocation()+self.getName(), self, parent=deformersLayer)

        self.footDef = Joint('foot', parent=self.defCmpGrp)
        self.footDef.setComponent(self)

        self.toeDef = Joint('toe', parent=self.defCmpGrp)
        self.toeDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs


        # ===============
        # Add KL Ops
        # ===============

        # Add HandRocker KL Op
        self.footRockerKLOp = KLOperator(self.getLocation()+self.getName()+'HandRockerKLOp', 'OSS_HandRockerSystem', 'OSS_Kraken')
        self.addOperator(self.footRockerKLOp)
        # Add Att Inputs
        self.footRockerKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.footRockerKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.footRockerKLOp.setInput('rightSide', self.rightSideInputAttr)
        self.footRockerKLOp.setInput('footRocker', footRockerInputAttr)
        self.footRockerKLOp.setInput('ballBreak', ballBreakInputAttr)
        self.footRockerKLOp.setInput('footTilt', footTiltInputAttr)
        # Add Xfo Inputs
        self.footRockerKLOp.setInput('ikCtrl', self.ikGoalRefLocator)
        self.footRockerKLOp.setInput('heelPivot', self.heelPivotLocator)
        self.footRockerKLOp.setInput('ballPivot', self.toePivotLocator)
        self.footRockerKLOp.setInput('toePivot', self.toeTipPivotLocator)
        self.footRockerKLOp.setInput('footJointLoc', self.footJointLocator)
        self.footRockerKLOp.setInput('toeJointLoc', self.toeJointLocator)
        self.footRockerKLOp.setInput('innerPivotLoc', self.innerPivotLocator)
        self.footRockerKLOp.setInput('outerPivotLoc', self.outerPivotLocator)
        # Add Xfo Outputs
        #self.legEndXfo_cmpOut = self.createOutput('legEndXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.footRockerHand_out = Locator('footRockerHand_out', parent=self.outputHrcGrp)
        self.footRockerToe_out = Locator('footRockerToe_out', parent=self.outputHrcGrp)
        self.footRockerKLOp.setOutput('ikGoal', self.ikgoal_cmpOut)
        self.footRockerKLOp.setOutput('footJoint', self.footRockerHand_out)
        self.footRockerKLOp.setOutput('toeJoint', self.footRockerToe_out)



        self.footCtrlSpaceConstraint = self.footCtrlSpace.constrainTo(self.footSpaceInputTgt, maintainOffset=True)


        # Wait, can this be a hier blend op?
        # Add Hand Blend KL Op
        self.IKHandBlendKLOp = KLOperator(self.getLocation()+self.getName()+'IKHandBlendKLOp', 'OSS_IKHandBlendSolver', 'OSS_Kraken')
        self.addOperator(self.IKHandBlendKLOp)
        # Add Att Inputs
        self.IKHandBlendKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.IKHandBlendKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.IKHandBlendKLOp.setInput('blend', footIKInputAttr)
        # Add Xfo Inputs)
        self.IKHandBlendKLOp.setInput('ikHand', self.footRockerHand_out)
        self.IKHandBlendKLOp.setInput('fkHand', self.footCtrl)
        self.IKHandBlendKLOp.setInput('ikToe', self.footRockerToe_out)
        self.IKHandBlendKLOp.setInput('fkToe', self.toeCtrl)
        # Add Xfo Outputs
        self.IKHandBlendKLOpHand_out = Locator('IKHandBlendKLOpHand_out', parent=self.outputHrcGrp)
        self.IKHandBlendKLOpToe_out = Locator('IKHandBlendKLOpToe_out', parent=self.outputHrcGrp)
        self.IKHandBlendKLOp.setOutput('foot', self.IKHandBlendKLOpHand_out)
        self.IKHandBlendKLOp.setOutput('toe', self.IKHandBlendKLOpToe_out)


        # Add Hand Toe HierBlend Solver for Mocap
        self.foot_mocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'foot_mocapHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.foot_mocapHierBlendSolver)
        self.foot_mocapHierBlendSolver.setInput('blend', footMocapInputAttr)
        self.foot_mocapHierBlendSolver.setInput('parentIndexes', [-1, 0])
        # Add Att Inputs
        self.foot_mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.foot_mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.foot_mocapHierBlendSolver.setInput('hierA', [self.IKHandBlendKLOpHand_out, self.IKHandBlendKLOpToe_out])
        self.foot_mocapHierBlendSolver.setInput('hierB', [self.foot_mocap, self.toe_mocap])
        # Add Xfo Outputs
        self.foot_mocapHierBlendSolver.setOutput('hierOut', [self.foot_cmpOut, self.toe_cmpOut])


        # Add Deformer Joint Constrain
        self.outputsToDeformersKLOp = KLOperator(self.getLocation()+self.getName()+'DeformerJointsKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)
        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.foot_cmpOut, self.toe_cmpOut])
        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [self.footDef, self.toeDef])



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

        super(OSSHandComponentRig, self).loadData( data )


        # TODO: make this a property of the component
        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping["NEGX"]



        self.footCtrlSpace.xfo = data['footXfo']
        self.footCtrl.xfo = data['footXfo']
        self.footCtrl.scalePointsOnAxis(data['footLen'], boneAxisStr)

        self.toeCtrlSpace.xfo = data['toeXfo']
        self.toeCtrl.xfo = data['toeXfo']
        self.toeCtrl.scalePointsOnAxis(data['toeLen'], boneAxisStr)


        self.foot_mocap.xfo = data['footXfo']
        self.foot_mocap.scalePointsOnAxis(data['footLen'], boneAxisStr)

        self.toe_mocapSpace.xfo = data['toeXfo']
        self.toe_mocap.xfo = data['toeXfo']
        self.toe_mocap.scalePointsOnAxis(data['toeLen'], boneAxisStr)


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

        self.toeJointLocator.xfo = data["toeXfo"]
        self.footJointLocator.xfo = data["footXfo"]
        self.heelPivotLocator.xfo = data["heelPivotXfo"]
        self.toeTipPivotLocator.xfo = data["toeTipPivotXfo"]
        self.innerPivotLocator.xfo = data["innerPivotXfo"]
        self.outerPivotLocator.xfo = data["outerPivotXfo"]
        self.toePivotLocator.xfo = data["toePivotXfo"]

        # Eval Constraints
        self.footCtrlSpaceConstraint.evaluate()

        # Eval Operators
        self.evalOperators()

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.footCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.toeCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSHandComponentGuide)
ks.registerComponent(OSSHandComponentRig)
