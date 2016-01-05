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

class OSSLimbComponent(BaseExampleComponent):
    """Limb Component"""

    def __init__(self, name='limbBase', parent=None):

        super(OSSLimbComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.legPelvisInputTgt = self.createInput('pelvisInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        # This is the actual ik goal as offset by another component like the foot
        self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.ikgoalRef_cmpOut = self.createOutput('ikgoalRef', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Output Xfos
        self.upleg_cmpOut = self.createOutput('upleg', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.loleg_cmpOut = self.createOutput('loleg', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.ankle_cmpOut = self.createOutput('ankle', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        # Not sure how to deal with this, if we don't want another component like the foot to offset the ik goal,
        # then can we just connect this output to its own input.  It actually would not create a cycle in the real graph
        # don't think we can make default connections like this right now anyways
        self.ikgoal_cmpOut = self.createOutput('ikgoal', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', value=1.0, dataType='Float', parent=self.cmpInputAttrGrp).getTarget()
        self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()

        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSLimbComponentGuide(OSSLimbComponent):
    """Limb Component Guide"""

    def __init__(self, name='limb', parent=None, data=None):

        Profiler.getInstance().push("Construct Leg Guide Component:" + name)
        super(OSSLimbComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        # Guide Controls
        self.uplegCtrl = Control('upleg', parent=self.ctrlCmpGrp, shape="sphere")
        self.lolegCtrl = Control('loleg', parent=self.ctrlCmpGrp, shape="sphere")
        self.ankleCtrl = Control('ankle', parent=self.ctrlCmpGrp, shape="sphere")

        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        self.useOtherIKGoalInput = BoolAttribute('useOtherIKGoal', value=False, parent=guideSettingsAttrGrp)


        if data is None:
            data = {
                    "name": name,
                    "location": "L",
                    "uplegXfo": Xfo(Vec3(0.9811, 9.769, -0.4572)),
                    "lolegXfo": Xfo(Vec3(1.4488, 5.4418, -0.5348)),
                    "ankleXfo": Xfo(Vec3(1.85, 1.2, -1.2)),
                    "useOtherIKGoalInput": 0,
                    "globalComponentCtrlSize": 1.0,
                   }

        self.loadData(data)

        """
        Possible way to change the inputs/outputs based on component settings.  Need to change rig.py _makeConnections not raise
        an exception, though.  Not sure it should raise an exception anyway.....
        if not self.useOtherIKGoalInput.getValue():
            self.removeOutputByName('ikgoalRef')
        """

        Profiler.getInstance().pop()


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.


        Return:
        The JSON data object

        """

        data = super(OSSLimbComponentGuide, self).saveData()

        data['uplegXfo'] = self.uplegCtrl.xfo
        data['lolegXfo'] = self.lolegCtrl.xfo
        data['ankleXfo'] = self.ankleCtrl.xfo
        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSLimbComponentGuide, self).loadData( data )


        if "uplegXfo" in data.keys():
            self.uplegCtrl.xfo = data['uplegXfo']
        if "lolegXfo" in data.keys():
            self.lolegCtrl.xfo = data['lolegXfo']
        if "ankleXfo" in data.keys():
            self.ankleCtrl.xfo = data['ankleXfo']

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.uplegCtrl.scalePoints(globalScaleVec)
        self.lolegCtrl.scalePoints(globalScaleVec)
        self.ankleCtrl.scalePoints(globalScaleVec)

        return True



    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSLimbComponentGuide, self).getRigBuildData()

        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping[boneAxisStr]

        upAxisStr = "POSY"
        if self.getLocation() == 'R':
            upAxisStr = "NEGY"
        upAxis = axisStrToTupleMapping[upAxisStr]


        # Values
        uplegPosition = self.uplegCtrl.xfo.tr
        lolegPosition = self.lolegCtrl.xfo.tr
        anklePosition = self.ankleCtrl.xfo.tr

        # Calculate Upleg Xfo
        uplegXfo = Xfo(self.uplegCtrl.xfo)
        # upAxis neg Y assumes the loleg is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #uplegXfo.aimAt(self.lolegCtrl.xfo.tr, upPos=self.ankleCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis.negate())
        uplegXfo.aimAt(aimPos=self.lolegCtrl.xfo.tr, upPos=self.ankleCtrl.xfo.tr, aimAxis=boneAxis, upAxis=tuple([-x for x in upAxis]))


        # Calculate loleg Xfo
        lolegXfo = Xfo(self.lolegCtrl.xfo)
        # upAxis neg Y assumes the loleg is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #lolegXfo.aimAt(self.toeCtrl.xfo.tr, upPos=self.uplegCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis.negate())
        lolegXfo.aimAt(aimPos=self.ankleCtrl.xfo.tr, upPos=self.uplegCtrl.xfo.tr, aimAxis=boneAxis, upAxis=tuple([-x for x in upAxis]))

        # Get lengths
        uplegLen = uplegPosition.subtract(lolegPosition).length()
        lolegLen = lolegPosition.subtract(anklePosition).length()

        handleXfo = Xfo()
        handleXfo.tr = anklePosition

        ankleXfo = Xfo()
        ankleXfo.tr = anklePosition
        # ankleXfo.ori = lolegXfo.ori


        upVXfo = Xfo()
        offset = [x * uplegLen * 2 for x in upAxis]

        upVXfo.tr = lolegXfo.transformVector(Vec3(offset[0], offset[1], offset[2]))



        data['uplegXfo'] = uplegXfo
        data['lolegXfo'] = lolegXfo
        data['handleXfo'] = handleXfo
        data['ankleXfo'] = ankleXfo
        data['upVXfo'] = upVXfo
        data['uplegLen'] = uplegLen
        data['lolegLen'] = lolegLen

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

        return OSSLimbComponentRig


class OSSLimbComponentRig(OSSLimbComponent):
    """Limb Component"""

    def __init__(self, name='leg', parent=None):

        Profiler.getInstance().push("Construct Leg Rig Component:" + name)
        super(OSSLimbComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # upleg
        self.uplegFKCtrlSpace = CtrlSpace('upleg', parent=self.ctrlCmpGrp)
        self.uplegFKCtrl = Control('upleg', parent=self.uplegFKCtrlSpace, shape="cube")
        #self.setCurveData
        self.uplegFKCtrl.alignOnXAxis()

        # loleg
        self.lolegFKCtrlSpace = CtrlSpace('loleg', parent=self.uplegFKCtrl)
        self.lolegFKCtrl = Control('loleg', parent=self.lolegFKCtrlSpace, shape="cube")
        self.lolegFKCtrl.alignOnXAxis()

        # Ankle
        self.legIKCtrlSpace = CtrlSpace('footIK', parent=self.ctrlCmpGrp)
        self.legIKCtrl = Control('footIK', parent=self.legIKCtrlSpace, shape="cross")

        # =========
        # Mocap
        # =========
        # Mocap upleg
        self.upleg_mocap = Control('upleg_mocap', parent=self.uplegFKCtrlSpace, shape="cube")
        self.upleg_mocap.alignOnXAxis()
        # Mocap loleg
        self.loleg_mocapSpace = CtrlSpace('loleg_mocap', parent=self.upleg_mocap)
        self.loleg_mocap = Control('loleg_mocap', parent=self.loleg_mocapSpace, shape="cube")
        self.loleg_mocap.alignOnXAxis()
        # Mocap Ankle
        self.legend_mocapSpace = CtrlSpace('legend_mocap', parent=self.loleg_mocap)
        self.legend_mocap = Locator('legend_mocap', parent=self.legend_mocapSpace)


        # Add Component Params to IK control
        legSettingsAttrGrp = AttributeGroup("DisplayInfo_LegSettings", parent=self.legIKCtrl)
        legDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=legSettingsAttrGrp)
        self.legBone0LenInputAttr = ScalarAttribute('bone0Len', value=1.0, parent=legSettingsAttrGrp)
        self.legBone1LenInputAttr = ScalarAttribute('bone1Len', value=1.0, parent=legSettingsAttrGrp)
        legIKBlendInputAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        legMocapInputAttr = ScalarAttribute('legMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        footMocapInputAttr = ScalarAttribute('footMocap', value=0.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        footIKInputAttr = ScalarAttribute('footIK', value=1.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        #legSoftIKInputAttr = BoolAttribute('softIK', value=True, parent=legSettingsAttrGrp)
        legSoftDistInputAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=legSettingsAttrGrp)
        legStretchBlendInputAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        footRockerInputAttr = ScalarAttribute('footRocker', value=0.0, minValue=-180.0, maxValue=180.0, parent=legSettingsAttrGrp)
        ballBreakInputAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=legSettingsAttrGrp)
        footTiltInputAttr = ScalarAttribute('footTilt', value=0.0, minValue=-180, maxValue=180.0, parent=legSettingsAttrGrp)

        self.drawDebugInputAttr.connect(legDrawDebugInputAttr)

        # UpV
        self.legUpVCtrlSpace = CtrlSpace('legUpV', parent=self.ctrlCmpGrp)
        self.legUpVCtrl = Control('legUpV', parent=self.legUpVCtrlSpace, shape="triangle")
        self.legUpVCtrl.alignOnZAxis()
        self.legUpVCtrlMasterSpace = CtrlSpace('legIKMaster', parent=self.globalSRTInputTgt)
        self.legUpVCtrlIKSpace = CtrlSpace('legUpVIK', parent=self.legIKCtrl)

        upVAttrGrp = AttributeGroup("UpVAttrs", parent=self.legUpVCtrl)
        upVSpaceBlendInputAttr = ScalarAttribute('IKFootSpace', value=0.0, minValue=0.0, maxValue=1.0, parent=upVAttrGrp)



        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getLocation()+self.getName(), self, parent=deformersLayer)

        self.uplegDef = Joint('upleg', parent=self.defCmpGrp)
        self.uplegDef.setComponent(self)

        self.lolegDef = Joint('loleg', parent=self.defCmpGrp)
        self.lolegDef.setComponent(self)

        self.ankleDef = Joint('ankle', parent=self.defCmpGrp)
        self.ankleDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.legIKCtrlSpaceInputConstraint = self.legIKCtrlSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        self.legRootInputConstraint = self.uplegFKCtrlSpace.constrainTo(self.legPelvisInputTgt, maintainOffset=True)
        self.ikGoalRefInputConstraint = self.ikgoalRef_cmpOut.constrainTo(self.legIKCtrl, maintainOffset=True)



        # Blend the Spaces (should make this a sub proc)
        self.legUpVSpaceHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'UpVSpace_HierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.legUpVSpaceHierBlendSolver)
        self.legUpVSpaceHierBlendSolver.setInput('blend', upVSpaceBlendInputAttr)
        upVSpaceBlendInputAttr.setValue(0.5)
        self.legUpVSpaceHierBlendSolver.setInput('parentIndexes', [-1])
        # Add Att Inputs
        self.legUpVSpaceHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.legUpVSpaceHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.legUpVSpaceHierBlendSolver.setInput('hierA', [self.legUpVCtrlMasterSpace])
        self.legUpVSpaceHierBlendSolver.setInput('hierB', [self.legUpVCtrlIKSpace])
        # Add Xfo Outputs
        self.legUpVSpaceHierBlendSolver.setOutput('hierOut', [self.legUpVCtrlSpace])



        # ===============
        # Add KL Ops
        # ===============


        # Add FK/IK Blend Leg KL Op
        self.legIKKLOp = KLOperator(self.getLocation()+self.getName()+'IKFKTwoBoneIKSolver', 'OSS_TwoBoneIKSolver', 'OSS_Kraken')
        self.addOperator(self.legIKKLOp)
        # Add Att Inputs
        self.legIKKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.legIKKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.legIKKLOp.setInput('bone0Len', self.legBone0LenInputAttr)
        self.legIKKLOp.setInput('bone1Len', self.legBone1LenInputAttr)
        self.legIKKLOp.setInput('ikBlend', legIKBlendInputAttr)
        #self.legIKKLOp.setInput('Mocap', legMocapInputAttr)
        self.legIKKLOp.setInput('softDist', legSoftDistInputAttr)
        self.legIKKLOp.setInput('stretch', legStretchBlendInputAttr)
        self.legIKKLOp.setInput('rightSide', self.rightSideInputAttr)
        # Add Xfo Inputs
        self.legIKKLOp.setInput('root', self.legPelvisInputTgt)
        self.legIKKLOp.setInput('bone0FK', self.uplegFKCtrl)
        self.legIKKLOp.setInput('bone1FK', self.lolegFKCtrl)
        self.legIKKLOp.setInput('ikHandle', self.ikgoal_cmpIn)
        self.legIKKLOp.setInput('upV', self.legUpVCtrl)
        # Add Xfo Outputs
        self.legIKKLOp_bone0_out = Locator('legIKKLOp_bone0_out', parent=self.outputHrcGrp)
        self.legIKKLOp_bone1_out = Locator('legIKKLOp_bone1_out', parent=self.outputHrcGrp)
        self.legIKKLOp_bone2_out = Locator('legIKKLOp_bone2_out', parent=self.outputHrcGrp)
        self.legIKKLOp.setOutput('bone0Out', self.legIKKLOp_bone0_out)
        self.legIKKLOp.setOutput('bone1Out', self.legIKKLOp_bone1_out)
        self.legIKKLOp.setOutput('bone2Out', self.legIKKLOp_bone2_out)


        # Add Leg HierBlend Solver for Mocap
        self.legMocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'legMocapHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.legMocapHierBlendSolver)
        self.legMocapHierBlendSolver.setInput('blend', legMocapInputAttr)
        self.legMocapHierBlendSolver.setInput('parentIndexes', [-1, 0, 1])
        # Add Att Inputs
        self.legMocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.legMocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.legMocapHierBlendSolver.setInput('hierA', [self.legIKKLOp_bone0_out, self.legIKKLOp_bone1_out, self.legIKKLOp_bone2_out])
        self.legMocapHierBlendSolver.setInput('hierB', [self.upleg_mocap, self.loleg_mocap, self.legend_mocap])
        # Add Xfo Outputs
        self.legMocapHierBlendSolver.setOutput('hierOut', [self.upleg_cmpOut, self.loleg_cmpOut, self.ankle_cmpOut])


        # Add Deformer Joint Constrain
        self.outputsToDeformersKLOp = KLOperator(self.getLocation()+self.getName()+'DeformerJointsKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)
        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.upleg_cmpOut, self.loleg_cmpOut, self.ankle_cmpOut])
        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [self.uplegDef, self.lolegDef, self.ankleDef])



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

        super(OSSLimbComponentRig, self).loadData( data )


        # TODO: make this a property of the component
        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping["NEGX"]


        #Upleg
        self.uplegFKCtrlSpace.xfo = data['uplegXfo']
        self.uplegFKCtrl.xfo = data['uplegXfo']
        self.uplegFKCtrl.scalePointsOnAxis(data['uplegLen'], boneAxisStr)

        self.upleg_cmpOut.xfo = data['uplegXfo']
        self.loleg_cmpOut.xfo = data['lolegXfo']
        self.ikgoal_cmpOut.xfo = data['ankleXfo']
        self.ikgoal_cmpIn.xfo = data['ankleXfo']

        # Loleg
        self.lolegFKCtrlSpace.xfo = data['lolegXfo']
        self.lolegFKCtrl.xfo = data['lolegXfo']
        self.lolegFKCtrl.scalePointsOnAxis(data['lolegLen'], boneAxisStr)

        self.upleg_mocap.xfo = data['uplegXfo']
        self.upleg_mocap.scalePointsOnAxis(data['uplegLen'], boneAxisStr)

        self.loleg_mocapSpace.xfo = data['lolegXfo']
        self.loleg_mocap.xfo = data['lolegXfo']
        self.loleg_mocap.scalePointsOnAxis(data['lolegLen'], boneAxisStr)

        self.legend_mocapSpace.xfo = data['ankleXfo']
        self.legend_mocap.xfo = data['ankleXfo']
        self.legend_mocap.xfo.ori = self.loleg_mocap.xfo.ori

        #ACK, can't access the foot heel pivot guide to set the ik control pos and ori.  Damn
        #Until later when we have better guide rigs setups, assume world Y up and Z forward to toe
        self.legIKCtrlSpace.xfo = data['ankleXfo']
        #self.legIKCtrlSpace.xfo.aimAt(aimVector=Vec3(0, 1, 0), upPos=self.toeCtrl.xfo.tr, aimAxis=(0, 1, 0), upAxis=(0, 0, 1))
        self.legIKCtrl.xfo = self.legIKCtrlSpace.xfo
        self.ikgoalRef_cmpOut.xfo = self.legIKCtrlSpace.xfo
        #self.legIKTarget.xfo.tr = data['ankleXfo'].tr


        if self.getLocation() == "R":
            pass
            #self.legIKCtrl.rotatePoints(0, 90, 0)
            #self.legIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.legIKCtrl.rotatePoints(0, -90, 0)
            #self.legIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))

        self.legUpVCtrlIKSpace.xfo = data['upVXfo']
        self.legUpVCtrl.xfo = data['upVXfo']
        self.legUpVCtrlMasterSpace.xfo = data['upVXfo']

        self.rightSideInputAttr.setValue(self.getLocation() == 'R')
        self.legBone0LenInputAttr.setMin(0.0)
        self.legBone0LenInputAttr.setMax(data['uplegLen'] * 3.0)
        self.legBone0LenInputAttr.setValue(data['uplegLen'])
        self.legBone1LenInputAttr.setMin(0.0)
        self.legBone1LenInputAttr.setMax(data['lolegLen'] * 3.0)
        self.legBone1LenInputAttr.setValue(data['lolegLen'])

        self.legPelvisInputTgt.xfo = data['uplegXfo']

        # Eval Constraints
        self.legIKCtrlSpaceInputConstraint.evaluate()
        self.legRootInputConstraint.evaluate()
        self.ikGoalRefInputConstraint.evaluate()

        # Eval Operators
        self.evalOperators()

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.uplegFKCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.lolegFKCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.legIKCtrl.scalePoints(globalScale)
        self.legUpVCtrl.scalePoints(globalScale)

        footPlane = Control("TMP", shape="square")
        footPlane.alignOnZAxis()
        footPlane.scalePoints(Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], 1.0))
        # Damn, can't get the foot length because it is on another component
        # Can we do this with just inputs?  We'd have to guarantee that everything was in the correct pose first
        #footPlane.scalePointsOnAxis(self.legIKCtrl.xfo.tr.subtract(self.toeTipPivotLocator.xfo.tr).length(), "POSZ")
        self.legIKCtrl.appendCurveData(footPlane.getCurveData())



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSLimbComponentGuide)
ks.registerComponent(OSSLimbComponentRig)
