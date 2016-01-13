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
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        # If the useOtherIKGoalInput is True, this will be actual ik goal as offset by another component like the foot
        self.ikgoal_cmpIn = None

        # Declare Output Xfos
        self.uplimb_cmpOut = self.createOutput('uplimb', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.lolimb_cmpOut = self.createOutput('lolimb', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.endlimb_cmpOut = self.createOutput('endlimb', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
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

    def __init__(self, name='limb', parent=None):

        Profiler.getInstance().push("Construct Limb Guide Component:" + name)
        super(OSSLimbComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.useOtherIKGoalInput = BoolAttribute('useOtherIKGoal', value=True, parent=guideSettingsAttrGrp)
        self.uplimbName = StringAttribute('uplimbName', value="uplimb", parent=guideSettingsAttrGrp)
        self.lolimbName = StringAttribute('lolimbName', value="lolimb", parent=guideSettingsAttrGrp)
        self.ikHandleName = StringAttribute('ikHandleName', value="limbIK", parent=guideSettingsAttrGrp)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)


        # Guide Controls
        self.uplimbCtrl = Control('uplimb', parent=self.ctrlCmpGrp, shape="sphere")
        self.lolimbCtrl = Control('lolimb', parent=self.ctrlCmpGrp, shape="sphere")
        self.handleCtrl = Control('handle', parent=self.ctrlCmpGrp, shape="cross")

        self.useOtherIKGoalInput.setValueChangeCallback(self.updateUseOtherIKGoal)
        self.useOtherIKGoalInput.setUpdateNode(True)


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
        for ctrl in self.getAllHierarchyNodes(classType=Control):
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
            self.updateUseOtherIKGoal(data["useOtherIKGoalInput"])

        return True


    def updateUseOtherIKGoal(self, useOtherIKGoal):
        """ Callback to changing the component setting 'useOtherIKGoalInput' """

        if useOtherIKGoal:
            if self.ikgoal_cmpIn is None:
                self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        else:
            if self.ikgoal_cmpIn is not None:
                self.removeInputByName('ikGoalInput')
                self.ikgoal_cmpIn = None





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
        uplimbPosition = self.uplimbCtrl.xfo.tr
        lolimbPosition = self.lolimbCtrl.xfo.tr
        handlePosition = self.handleCtrl.xfo.tr

        # Calculate uplimb Xfo
        uplimbXfo = Xfo(self.uplimbCtrl.xfo)
        # upAxis neg Y assumes the lolimb is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #uplimbXfo.aimAt(self.lolimbCtrl.xfo.tr, upPos=self.handleCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis.negate())
        uplimbXfo.aimAt(aimPos=self.lolimbCtrl.xfo.tr, upPos=self.handleCtrl.xfo.tr, aimAxis=boneAxis, upAxis=tuple([-x for x in upAxis]))


        # Calculate lolimb Xfo
        lolimbXfo = Xfo(self.lolimbCtrl.xfo)
        # upAxis neg Y assumes the lolimb is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #lolimbXfo.aimAt(self.toeCtrl.xfo.tr, upPos=self.uplimbCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis.negate())
        lolimbXfo.aimAt(aimPos=self.handleCtrl.xfo.tr, upPos=self.uplimbCtrl.xfo.tr, aimAxis=boneAxis, upAxis=tuple([-x for x in upAxis]))

        # Get lengths
        uplimbLen = uplimbPosition.subtract(lolimbPosition).length()
        lolimbLen = lolimbPosition.subtract(handlePosition).length()

        handleXfo = self.handleCtrl.xfo

        upVXfo = Xfo()
        offset = [x * uplimbLen * 2 for x in upAxis]

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

    def __init__(self, name='limb', parent=None):

        Profiler.getInstance().push("Construct Limb Rig Component:" + name)
        super(OSSLimbComponentRig, self).__init__(name, parent)


    def createControls(self, data):

        name = data["name"]
        uplimbName = data['uplimbName']
        lolimbName = data['lolimbName']
        ikHandleName = data['ikHandleName']

        self.useOtherIKGoal = data['useOtherIKGoal']
        if self.useOtherIKGoal:
            self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # =========
        # Controls
        # =========
        # uplimb
        self.uplimbFKCtrlSpace = CtrlSpace(uplimbName, parent=self.ctrlCmpGrp)
        self.uplimbFKCtrl = Control(uplimbName, parent=self.uplimbFKCtrlSpace, shape="cube")
        self.uplimbFKCtrl.alignOnXAxis()

        # lolimb
        self.lolimbFKCtrlSpace = CtrlSpace(lolimbName, parent=self.uplimbFKCtrl)
        self.lolimbFKCtrl = Control(lolimbName, parent=self.lolimbFKCtrlSpace, shape="cube")
        self.lolimbFKCtrl.alignOnXAxis()

        # handle
        self.limbIKCtrlSpace = CtrlSpace(ikHandleName, parent=self.ctrlCmpGrp)
        if self.useOtherIKGoal: #Do not use this as a control, hide it
            self.limbIKCtrl = Locator(uplimbName, parent=self.limbIKCtrlSpace)
        else:
            self.limbIKCtrl = Control(uplimbName, parent=self.limbIKCtrlSpace, shape="cross")

        # =========
        # Mocap
        # =========
        # Mocap uplimb
        self.uplimb_mocap = Control(uplimbName+'_mocap', parent=self.uplimbFKCtrlSpace, shape="cube")
        self.uplimb_mocap.alignOnXAxis()
        # Mocap lolimb
        self.lolimb_mocapSpace = CtrlSpace(lolimbName+'_mocap', parent=self.uplimb_mocap)
        self.lolimb_mocap = Control(lolimbName+'_mocap', parent=self.lolimb_mocapSpace, shape="cube")
        self.lolimb_mocap.alignOnXAxis()
        # Mocap handle
        self.endlimb_mocapSpace = CtrlSpace(name+'end_mocap', parent=self.lolimb_mocap)
        self.endlimb_mocap = Locator(name+'end_mocap', parent=self.endlimb_mocapSpace)


        # Add Component Params to IK control
        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.limbIKCtrl)
        limbDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=limbSettingsAttrGrp)
        self.limbBone0LenInputAttr = ScalarAttribute('bone0Len', value=1.0, parent=limbSettingsAttrGrp)
        self.limbBone1LenInputAttr = ScalarAttribute('bone1Len', value=1.0, parent=limbSettingsAttrGrp)
        limbIKBlendInputAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        limbMocapInputAttr = ScalarAttribute(name+'Mocap', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        limbSoftDistInputAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=limbSettingsAttrGrp)
        limbStretchBlendInputAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)


        self.drawDebugInputAttr.connect(limbDrawDebugInputAttr)

        # UpV
        self.limbUpVCtrlSpace = CtrlSpace(name+'UpV', parent=self.ctrlCmpGrp)
        self.limbUpVCtrl = Control(name+'UpV', parent=self.limbUpVCtrlSpace, shape="triangle")
        self.limbUpVCtrl.alignOnZAxis()

        self.limbUpVCtrlMasterSpace = CtrlSpace(name+'IKMaster', parent=self.globalSRTInputTgt)

        parent = self.limbIKCtrl
        if self.useOtherIKGoal:
            parent = self.ikgoal_cmpIn
        self.limbUpVCtrlIKSpace = CtrlSpace(name+'UpVIK', parent=parent)

        upVAttrGrp = AttributeGroup("UpVAttrs", parent=self.limbUpVCtrl)
        upVSpaceBlendInputAttr = ScalarAttribute(ikHandleName+'Space', value=0.0, minValue=0.0, maxValue=1.0, parent=upVAttrGrp)



        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getLocation()+self.getName(), self, parent=deformersLayer)

        self.uplimbDef = Joint(uplimbName, parent=self.defCmpGrp)
        self.uplimbDef.setComponent(self)

        self.lolimbDef = Joint(lolimbName, parent=self.defCmpGrp)
        self.lolimbDef.setComponent(self)

        self.limbendDef = Joint(name+'end', parent=self.defCmpGrp)
        self.limbendDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.limbIKCtrlSpaceInputConstraint = self.limbIKCtrlSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        self.parentSpaceInputConstraint = self.uplimbFKCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)


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
        self.limbIKKLOp.setInput('ikBlend', limbIKBlendInputAttr)
        self.limbIKKLOp.setInput('softDist', limbSoftDistInputAttr)
        self.limbIKKLOp.setInput('stretch', limbStretchBlendInputAttr)
        self.limbIKKLOp.setInput('rightSide', self.rightSideInputAttr)
        # Add Xfo Inputs
        self.limbIKKLOp.setInput('root', self.parentSpaceInputTgt)
        self.limbIKKLOp.setInput('bone0FK', self.uplimbFKCtrl)
        self.limbIKKLOp.setInput('bone1FK', self.lolimbFKCtrl)
        self.limbIKKLOp.setInput('upV', self.limbUpVCtrl)

        if self.ikgoal_cmpIn:
           self.limbIKKLOp.setInput('ikHandle', self.ikgoal_cmpIn)
        else:
            self.limbIKKLOp.setInput('ikHandle', self.limbIKCtrl)

        # Add Xfo Outputs
        self.limbIKKLOp_bone0_out = Locator('limbIKKLOp_bone0_out', parent=self.outputHrcGrp)
        self.limbIKKLOp_bone1_out = Locator('limbIKKLOp_bone1_out', parent=self.outputHrcGrp)
        self.limbIKKLOp_bone2_out = Locator('limbIKKLOp_bone2_out', parent=self.outputHrcGrp)
        self.limbIKKLOp.setOutput('bone0Out', self.limbIKKLOp_bone0_out)
        self.limbIKKLOp.setOutput('bone1Out', self.limbIKKLOp_bone1_out)
        self.limbIKKLOp.setOutput('bone2Out', self.limbIKKLOp_bone2_out)


        # Add Limb HierBlend Solver for Mocap
        self.limbMocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'limbMocapHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.limbMocapHierBlendSolver)
        self.limbMocapHierBlendSolver.setInput('blend', limbMocapInputAttr)
        self.limbMocapHierBlendSolver.setInput('parentIndexes', [-1, 0, 1])
        # Add Att Inputs
        self.limbMocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.limbMocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.limbMocapHierBlendSolver.setInput('hierA', [self.limbIKKLOp_bone0_out, self.limbIKKLOp_bone1_out, self.limbIKKLOp_bone2_out])
        self.limbMocapHierBlendSolver.setInput('hierB', [self.uplimb_mocap, self.lolimb_mocap, self.endlimb_mocap])
        # Add Xfo Outputs
        self.limbMocapHierBlendSolver.setOutput('hierOut', [self.uplimb_cmpOut, self.lolimb_cmpOut, self.endlimb_cmpOut])


        # Add Deformer Joint Constrain
        self.outputsToDeformersKLOp = KLOperator(self.getLocation()+self.getName()+'DeformerJointsKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)
        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.uplimb_cmpOut, self.lolimb_cmpOut, self.endlimb_cmpOut])
        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [self.uplimbDef, self.lolimbDef, self.limbendDef])



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

        self.createControls(data)

        # TODO: make this a property of the component
        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping["NEGX"]


        #uplimb
        self.uplimbFKCtrlSpace.xfo = data['uplimbXfo']
        self.uplimbFKCtrl.xfo = data['uplimbXfo']
        self.uplimbFKCtrl.scalePointsOnAxis(data['uplimbLen'], boneAxisStr)

        self.uplimb_cmpOut.xfo = data['uplimbXfo']
        self.lolimb_cmpOut.xfo = data['lolimbXfo']
        self.ikgoal_cmpOut.xfo = data['handleXfo']
        if self.ikgoal_cmpIn:
            self.ikgoal_cmpIn.xfo = data['handleXfo']

        # lolimb
        self.lolimbFKCtrlSpace.xfo = data['lolimbXfo']
        self.lolimbFKCtrl.xfo = data['lolimbXfo']
        self.lolimbFKCtrl.scalePointsOnAxis(data['lolimbLen'], boneAxisStr)

        self.uplimb_mocap.xfo = data['uplimbXfo']
        self.uplimb_mocap.scalePointsOnAxis(data['uplimbLen'], boneAxisStr)

        self.lolimb_mocapSpace.xfo = data['lolimbXfo']
        self.lolimb_mocap.xfo = data['lolimbXfo']
        self.lolimb_mocap.scalePointsOnAxis(data['lolimbLen'], boneAxisStr)

        self.endlimb_mocapSpace.xfo = data['handleXfo']
        self.endlimb_mocap.xfo = data['handleXfo']
        self.endlimb_mocap.xfo.ori = self.lolimb_mocap.xfo.ori

        #Until later when we have better guide rigs setups, assume world Y up and Z forward to toe
        self.limbIKCtrlSpace.xfo = data['handleXfo']
        #self.limbIKCtrlSpace.xfo.aimAt(aimVector=Vec3(0, 1, 0), upPos=self.toeCtrl.xfo.tr, aimAxis=(0, 1, 0), upAxis=(0, 0, 1))
        self.limbIKCtrl.xfo = self.limbIKCtrlSpace.xfo


        if self.getLocation() == "R":
            pass
            #self.limbIKCtrl.rotatePoints(0, 90, 0)
            #self.limbIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.limbIKCtrl.rotatePoints(0, -90, 0)
            #self.limbIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))

        self.limbUpVCtrlIKSpace.xfo = data['upVXfo']
        self.limbUpVCtrl.xfo = data['upVXfo']
        self.limbUpVCtrlMasterSpace.xfo = data['upVXfo']

        self.rightSideInputAttr.setValue(self.getLocation() == 'R')
        self.limbBone0LenInputAttr.setMin(0.0)
        self.limbBone0LenInputAttr.setMax(data['uplimbLen'] * 3.0)
        self.limbBone0LenInputAttr.setValue(data['uplimbLen'])
        self.limbBone1LenInputAttr.setMin(0.0)
        self.limbBone1LenInputAttr.setMax(data['lolimbLen'] * 3.0)
        self.limbBone1LenInputAttr.setValue(data['lolimbLen'])

        self.parentSpaceInputTgt.xfo = data['uplimbXfo']

        # Eval Constraints
        self.limbIKCtrlSpaceInputConstraint.evaluate()
        self.parentSpaceInputConstraint.evaluate()

        # Eval Operators
        self.evalOperators()

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.uplimbFKCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.lolimbFKCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        if not self.useOtherIKGoal:
            self.limbIKCtrl.scalePoints(globalScale)
        self.limbUpVCtrl.scalePoints(globalScale)



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSLimbComponentGuide)
ks.registerComponent(OSSLimbComponentRig)
