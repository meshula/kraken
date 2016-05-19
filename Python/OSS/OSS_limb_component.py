from kraken.core.maths import Vec3, AXIS_NAME_TO_TUPLE_MAP, AXIS_NAME_TO_INT_MAP
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

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "limb"

# Sweet Sweet
class OSSLimbComponent(OSS_Component):
    """Limb Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        super(OSSLimbComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        # If the useOtherIKGoalInput is True, this will be actual ik goal as offset by another component like the foot
        self.ikgoal_cmpIn = None

        # Declare Output Xfos
        self.uplimb_cmpOut = self.createOutput('uplimb', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.lolimb_cmpOut = self.createOutput('lolimb', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.endlimb_cmpOut = self.createOutput('endlimb', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()


class OSSLimbComponentGuide(OSSLimbComponent):
    """Limb Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Limb Guide Component:" + name)
        super(OSSLimbComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        # Guide Settings
        self.useOtherIKGoalInput = BoolAttribute('useOtherIKGoal', value=True, parent=self.guideSettingsAttrGrp)
        self.uplimbName = StringAttribute('uplimbName', value="uplimb", parent=self.guideSettingsAttrGrp)
        self.lolimbName = StringAttribute('lolimbName', value="lolimb", parent=self.guideSettingsAttrGrp)
        self.ikHandleName = StringAttribute('ikHandleName', value="limbIK", parent=self.guideSettingsAttrGrp)

        # Guide Controls
        self.uplimbCtrl = Control('uplimb', parent=self.ctrlCmpGrp, shape="sphere")
        self.lolimbCtrl = Control('lolimb', parent=self.ctrlCmpGrp, shape="sphere")
        self.handleCtrl = Control('handle', parent=self.ctrlCmpGrp, shape="jack")

        self.useOtherIKGoalInput.setValueChangeCallback(self.updateUseOtherIKGoal)
        #self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )

        self.limbMocapInputAttr = None

        data = {
                "name": name,
                "location": "L",
                "uplimbXfo": Xfo(Vec3(0.9811, 9.769, -0.4572)),
                "lolimbXfo": Xfo(Vec3(1.4488, 5.4418, -0.5348)),
                "handleXfo": Xfo(Vec3(1.85, 1.2, -1.2)),
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

        data = super(OSSLimbComponentGuide, self).saveData()

        data['uplimbXfo'] = self.uplimbCtrl.xfo
        data['lolimbXfo'] = self.lolimbCtrl.xfo
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
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSLimbComponentGuide, self).loadData(data)

        if "uplimbXfo" in data.keys():
            self.uplimbCtrl.xfo = data['uplimbXfo']
        if "lolimbXfo" in data.keys():
            self.lolimbCtrl.xfo = data['lolimbXfo']
        if "handleXfo" in data.keys():
            self.handleCtrl.xfo = data['handleXfo']

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.uplimbCtrl.scalePoints(globalScaleVec)
        self.lolimbCtrl.scalePoints(globalScaleVec)
        self.handleCtrl.scalePoints(globalScaleVec)

        # maybe roll this into a createControls() function like in the Rig object?
        if "uplimbName" in data.keys():
            self.uplimbCtrl.setName(data['uplimbName'])
        if "lolimbName" in data.keys():
            self.lolimbCtrl.setName(data['lolimbName'])
        if "ikHandleName" in data.keys():
            self.handleCtrl.setName(data['ikHandleName'])

        if "useOtherIKGoalInput" in data.keys():
            self.updateUseOtherIKGoal(bool(data["useOtherIKGoalInput"]))

        return True


    def updateMocap(self, mocap):
        """ Callback to changing the component setting 'useOtherIKGoalInput'
        Really, we should build this ability into the system, to add/remove input attrs based on guide setting bools.
        That way, we don't have to write these callbacks.
        """
        if mocap:
            if self.limbMocapInputAttr is None:
                self.limbMocapInputAttr = self.createInput('limbMocap', dataType='Float', parent=self.cmpInputAttrGrp)
                self.mocap = True

        else:
            if self.limbMocapInputAttr is not None:
                # self.deleteInput('limbMocap', parent=self.cmpInputAttrGrp)
                self.limbMocapInputAttr = None
                self.mocap = False



    def updateUseOtherIKGoal(self, useOtherIKGoal):
        """ Callback to changing the component setting 'useOtherIKGoalInput' """

        if useOtherIKGoal:
            if self.ikgoal_cmpIn is None:
                self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
                self.ikBlendAttr = self.createInput('ikBlend', dataType='Float', parent=self.cmpInputAttrGrp)
                self.softDistAttr = self.createInput('softDist', dataType='Float', parent=self.cmpInputAttrGrp)
                self.stretchAttr = self.createInput('stretch', dataType='Float', parent=self.cmpInputAttrGrp)
        else:
            if self.ikgoal_cmpIn is not None:
                # self.deleteInput('ikGoalInput', parent=self.inputHrcGrp)
                # self.deleteInput('ikBlend', parent=self.cmpInputAttrGrp)
                # self.deleteInput('softDist', parent=self.cmpInputAttrGrp)
                # self.deleteInput('stretch', parent=self.cmpInputAttrGrp)
                self.ikgoal_cmpIn = None


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSLimbComponentGuide, self).getRigBuildData()

        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]

        # Values
        uplimbPosition = self.uplimbCtrl.xfo.tr
        lolimbPosition = self.lolimbCtrl.xfo.tr
        handlePosition = self.handleCtrl.xfo.tr

        # Calculate uplimb Xfo
        uplimbXfo = Xfo(self.uplimbCtrl.xfo)
        # self.upAxis neg Y assumes the lolimb is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #aimAt(uplimbXfo, self.lolimbCtrl.xfo.tr, upPos=self.handleCtrl.xfo.tr, aimAxis=self.boneAxis, upAxis=self.upAxis.negate())
        aimAt(uplimbXfo, aimPos=self.lolimbCtrl.xfo.tr, upPos=self.handleCtrl.xfo.tr, aimAxis=self.boneAxis, upAxis=tuple([-x for x in self.upAxis]))


        # Calculate lolimb Xfo
        lolimbXfo = Xfo(self.lolimbCtrl.xfo)
        # self.upAxis neg Y assumes the lolimb is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #aimAt(lolimbXfo, self.toeCtrl.xfo.tr, upPos=self.uplimbCtrl.xfo.tr, aimAxis=self.boneAxis, upAxis=self.upAxis.negate())
        aimAt(lolimbXfo, aimPos=self.handleCtrl.xfo.tr, upPos=self.uplimbCtrl.xfo.tr, aimAxis=self.boneAxis, upAxis=tuple([-x for x in self.upAxis]))

        # Get lengths
        uplimbLen = uplimbPosition.subtract(lolimbPosition).length()
        lolimbLen = lolimbPosition.subtract(handlePosition).length()

        handleXfo = self.handleCtrl.xfo

        upVXfo = Xfo()
        offset = [x * uplimbLen * 2 for x in self.upAxis]

        upVXfo.tr = lolimbXfo.transformVector(Vec3(offset[0], offset[1], offset[2]))

        data['uplimbXfo'] = uplimbXfo
        data['lolimbXfo'] = lolimbXfo
        data['handleXfo'] = handleXfo
        data['upVXfo'] = upVXfo
        data['uplimbLen'] = uplimbLen
        data['lolimbLen'] = lolimbLen

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

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Limb Rig Component:" + name)
        super(OSSLimbComponentRig, self).__init__(name, parent)


    def createControls(self, data):

        name = data["name"]
        uplimbName = data['uplimbName']
        lolimbName = data['lolimbName']
        ikHandleName = data['ikHandleName']

        self.useOtherIKGoal = bool(data['useOtherIKGoal'])
        self.mocap = bool(data["mocap"])

        # =========
        # Controls
        # =========
        # uplimb
        self.uplimbFKCtrl = FKControl(uplimbName, parent=self.ctrlCmpGrp, shape="cube")
        self.uplimbFKCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["YXZ"])  #Set with component settings later
        self.uplimbFKCtrl.xfo = data['uplimbXfo']
        self.uplimbFKCtrlSpace = self.uplimbFKCtrl.insertCtrlSpace()

        # lolimb
        self.lolimbFKCtrl = FKControl(lolimbName, parent=self.uplimbFKCtrl)
        self.lolimbFKCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["XZY"])  #Set with component settings later
        self.lolimbFKCtrl.xfo = data['lolimbXfo']
        self.lolimbFKCtrlSpace = self.lolimbFKCtrl.insertCtrlSpace()

        box = False
        if box:
            for ctrl in [self.uplimbFKCtrl, self.lolimbFKCtrl]:
                ctrl.setShape("cube")
                ctrl.alignOnXAxis()
            self.uplimbFKCtrl.scalePointsOnAxis(data['uplimbLen'], self.boneAxisStr)
            self.lolimbFKCtrl.scalePointsOnAxis(data['lolimbLen'], self.boneAxisStr)
        else:
            self.uplimbFKCtrl.setShape("square")
            self.lolimbFKCtrl.setShape("squarePointed")
            for ctrl in [self.uplimbFKCtrl, self.lolimbFKCtrl]:
                if self.getLocation() == 'R':
                    ctrl.scalePoints(Vec3(-1,-1,-1))
                ctrl.rotatePoints(-90,0,90)


        self.limbIKCtrlSpace = CtrlSpace(ikHandleName, parent=self.ctrlCmpGrp)
        self.limbIKCtrlSpace.xfo = data['handleXfo']
        # hand
        if self.useOtherIKGoal: #Do not use this as a control, hide it
            self.limbIKCtrl = Transform(ikHandleName, parent=self.limbIKCtrlSpace)
        else:
            self.limbIKCtrl = IKControl(ikHandleName, parent=self.limbIKCtrlSpace, shape="jack")
        self.limbIKCtrl.xfo = data['handleXfo']


        # Add Component Params to IK control
        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.limbIKCtrl)


        if self.mocap:
                self.limbMocapInputAttr = self.createInput('limbMocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()

        if self.useOtherIKGoal:
            self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
            self.limbIKCtrl.constrainTo(self.ikgoal_cmpIn, maintainOffset=True)
            self.ikBlendAttr = self.createInput('ikBlend', dataType='Float', value=1.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            self.softDistAttr = self.createInput('softDist', dataType='Float', value=0.0, minValue=0.0, parent=self.cmpInputAttrGrp).getTarget()
            self.stretchAttr = self.createInput('stretch', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
        else:
            self.ikgoal_cmpIn = None
            self.ikBlendAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
            self.softDistAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=limbSettingsAttrGrp)
            self.stretchAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)

        self.limbBone0LenInputAttr = ScalarAttribute('bone0Len', value=1.0, parent=limbSettingsAttrGrp)
        self.limbBone1LenInputAttr = ScalarAttribute('bone1Len', value=1.0, parent=limbSettingsAttrGrp)
        self.limbDrawDebugAttr = BoolAttribute('drawDebug', value=False, parent=limbSettingsAttrGrp)

        self.drawDebugInputAttr.connect(self.limbDrawDebugAttr)



        # =========
        # Mocap
        # =========
        if self.mocap:
            # Mocap uplimb
            self.uplimb_mocap = MCControl(uplimbName, parent=self.uplimbFKCtrlSpace, shape="cube")
            #rotation order should stay consistent no matter what ro the controls have
            self.uplimb_mocap.xfo = data['uplimbXfo']
            self.uplimb_mocap.alignOnXAxis()
            self.uplimb_mocap.scalePointsOnAxis(data['uplimbLen'], self.boneAxisStr)


            # Mocap lolimb
            self.lolimb_mocap = MCControl(lolimbName, parent=self.uplimb_mocap, shape="cube")
            self.lolimb_mocap.xfo = data['lolimbXfo']
            self.lolimb_mocap.alignOnXAxis()
            self.lolimb_mocap.scalePointsOnAxis(data['lolimbLen'], self.boneAxisStr)
            self.lolimb_mocap.insertCtrlSpace()
            # Mocap handle
            self.endlimb_mocap = Transform(name+'end', parent=self.lolimb_mocap)
            self.endlimb_mocap.xfo = data['handleXfo']
            self.endlimb_mocap.xfo.ori = self.lolimb_mocap.xfo.ori
            self.endlimb_mocap.insertCtrlSpace()


        # UpV
        self.limbUpVCtrl = Control(name+'UpV', parent=self.ctrlCmpGrp, shape="triangle")
        self.limbUpVCtrl.xfo = data['upVXfo']
        self.limbUpVCtrl.alignOnZAxis()
        self.limbUpVCtrlSpace = self.limbUpVCtrl.insertCtrlSpace()


        self.limbUpVCtrlIKSpace = CtrlSpace(name+'UpVIK', parent=self.ctrlCmpGrp)
        self.limbUpVCtrlIKSpace.xfo = data['upVXfo']
        if self.useOtherIKGoal:
            self.limbUpVCtrlIKSpaceConstraint = self.limbUpVCtrlIKSpace.constrainTo(self.ikgoal_cmpIn, maintainOffset=True)
        else:
            self.limbUpVCtrlIKSpaceConstraint = self.limbUpVCtrlIKSpace.constrainTo(self.limbIKCtrl, maintainOffset=True)


        self.limbUpVCtrlMasterSpace = CtrlSpace(name+'IKMaster', parent=self.ctrlCmpGrp)
        self.limbUpVCtrlMasterSpace.xfo = data['upVXfo']
        self.limbUpVCtrlMasterSpaceConstraint = self.limbUpVCtrlMasterSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)

        upVAttrGrp = AttributeGroup("UpVAttrs", parent=self.limbUpVCtrl)
        upVSpaceBlendInputAttr = ScalarAttribute(ikHandleName+'Space', value=0.0, minValue=0.0, maxValue=1.0, parent=upVAttrGrp)



        # ==========
        # Deformers
        # ==========

        self.uplimbDef = Joint(uplimbName, parent=self.deformersParent)
        self.uplimbDef.setComponent(self)

        self.lolimbDef = Joint(lolimbName, parent=self.uplimbDef)
        self.lolimbDef.setComponent(self)

        self.limbendDef = Joint(name+'end', parent=self.lolimbDef)
        self.limbendDef.setComponent(self)

        self.parentSpaceInputTgt.childJoints = [self.uplimbDef]


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.limbIKCtrlSpaceInputConstraint = self.limbIKCtrlSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        self.uplimbFKCtrlSpaceConstraint = self.uplimbFKCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)


        # Blend the Spaces (should make this a sub proc)
        self.limbUpVSpaceHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'UpVSpace_HierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.limbUpVSpaceHierBlendSolver)
        self.limbUpVSpaceHierBlendSolver.setInput('blend', upVSpaceBlendInputAttr)
        upVSpaceBlendInputAttr.setValue(0.5)
        self.limbUpVSpaceHierBlendSolver.setInput('parentIndexes', [-1])
        # Add Att Inputs
        self.limbUpVSpaceHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.limbUpVSpaceHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.limbUpVSpaceHierBlendSolver.setInput('hierA', [self.limbUpVCtrlMasterSpace])
        self.limbUpVSpaceHierBlendSolver.setInput('hierB', [self.limbUpVCtrlIKSpace])
        # Add Xfo Outputs
        self.limbUpVSpaceHierBlendSolver.setOutput('hierOut', [self.limbUpVCtrlSpace])



        # ===============
        # Add KL Ops
        # ===============


        # Add FK/IK Blend Limb KL Op
        self.limbIKKLOp = KLOperator(self.getLocation()+self.getName()+'IKFKTwoBoneIKSolver', 'OSS_TwoBoneIKSolver', 'OSS_Kraken')
        self.addOperator(self.limbIKKLOp)
        # Add Att Inputs
        self.limbIKKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.limbIKKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.limbIKKLOp.setInput('bone0Len', self.limbBone0LenInputAttr)
        self.limbIKKLOp.setInput('bone1Len', self.limbBone1LenInputAttr)
        self.limbIKKLOp.setInput('ikBlend', self.ikBlendAttr)
        self.limbIKKLOp.setInput('softDist', self.softDistAttr)
        self.limbIKKLOp.setInput('stretch', self.stretchAttr)
        # Add Xfo Inputs
        self.limbIKKLOp.setInput('root', self.uplimbFKCtrlSpace)
        self.limbIKKLOp.setInput('bone0FK', self.uplimbFKCtrl)
        self.limbIKKLOp.setInput('bone1FK', self.lolimbFKCtrl)
        self.limbIKKLOp.setInput('upV', self.limbUpVCtrl)
        self.limbIKKLOp.setInput('boneAxis', AXIS_NAME_TO_INT_MAP[self.boneAxisStr])
        self.limbIKKLOp.setInput('upAxis', AXIS_NAME_TO_INT_MAP[self.upAxisStr])
        self.limbIKKLOp.setInput('ikHandle', self.limbIKCtrl)



        if self.mocap:

            # Add Xfo Outputs
            self.limbIKKLOp_bone0_out = Transform('limbIKKLOp_bone0_out', parent=self.outputHrcGrp)
            self.limbIKKLOp_bone1_out = Transform('limbIKKLOp_bone1_out', parent=self.outputHrcGrp)
            self.limbIKKLOp_bone2_out = Transform('limbIKKLOp_bone2_out', parent=self.outputHrcGrp)
            self.limbIKKLOp.setOutput('bone0Out', self.limbIKKLOp_bone0_out)
            self.limbIKKLOp.setOutput('bone1Out', self.limbIKKLOp_bone1_out)
            self.limbIKKLOp.setOutput('bone2Out', self.limbIKKLOp_bone2_out)

            # Add Limb HierBlend Solver for Mocap
            self.limbMocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'limbMocapHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.limbMocapHierBlendSolver)
            self.limbMocapHierBlendSolver.setInput('blend', self.limbMocapInputAttr)
            self.limbMocapHierBlendSolver.setInput('parentIndexes', [-1, 0, 1])
            # Add Att Inputs
            self.limbMocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.limbMocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            self.limbMocapHierBlendSolver.setInput('hierA', [self.limbIKKLOp_bone0_out, self.limbIKKLOp_bone1_out, self.limbIKKLOp_bone2_out])
            self.limbMocapHierBlendSolver.setInput('hierB', [self.uplimb_mocap, self.lolimb_mocap, self.endlimb_mocap])
            # Add Xfo Outputs
            self.limbMocapHierBlendSolver.setOutput('hierOut', [self.uplimb_cmpOut, self.lolimb_cmpOut, self.endlimb_cmpOut])
        else:
            self.limbIKKLOp.setOutput('bone0Out', self.uplimb_cmpOut)
            self.limbIKKLOp.setOutput('bone1Out', self.lolimb_cmpOut)
            self.limbIKKLOp.setOutput('bone2Out', self.endlimb_cmpOut)


        # Add Deformer Joint Constrain
        self.uplimbDef.constrainTo(self.uplimb_cmpOut).evaluate()
        self.uplimb_cmpOut.parentJoint = self.uplimbDef

        self.lolimbDef.constrainTo(self.lolimb_cmpOut).evaluate()
        self.lolimb_cmpOut.parentJoint = self.lolimbDef

        self.limbendDef.constrainTo(self.endlimb_cmpOut).evaluate()
        self.endlimb_cmpOut.parentJoint = self.limbendDef



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
        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]

        self.createControls(data)






        if self.getLocation() == "R":
            pass
            #self.limbIKCtrl.rotatePoints(0, 90, 0)
            #self.limbIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.limbIKCtrl.rotatePoints(0, -90, 0)
            #self.limbIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))



        self.limbBone0LenInputAttr.setMin(0.0)
        self.limbBone0LenInputAttr.setMax(data['uplimbLen'] * 3.0)
        self.limbBone0LenInputAttr.setValue(data['uplimbLen'])
        self.limbBone1LenInputAttr.setMin(0.0)
        self.limbBone1LenInputAttr.setMax(data['lolimbLen'] * 3.0)
        self.limbBone1LenInputAttr.setValue(data['lolimbLen'])




        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()

        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        # None
        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.uplimbFKCtrl.scalePoints(Vec3(1, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.lolimbFKCtrl.scalePoints(Vec3(1, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))

        # self.uplimbFKCtrl.rotatePoints(0, -90, 0)
        # self.lolimbFKCtrl.rotatePoints(0, -90, 0)
        if not self.useOtherIKGoal:
            self.limbIKCtrl.scalePoints(globalScale)
        self.limbUpVCtrl.scalePoints(globalScale)



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSLimbComponentGuide)
ks.registerComponent(OSSLimbComponentRig)
