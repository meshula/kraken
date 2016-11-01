from kraken.core.maths import *
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
from kraken.core.objects.locator import Locator

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

        self.endTwistParent_cmpIn = self.createInput('endTwistParent', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

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
        self.untwistUplimb = BoolAttribute('untwistUplimb', value=False, parent=self.guideSettingsAttrGrp)
        self.addPartialJoints = BoolAttribute('addPartialJoints', value=False, parent=self.guideSettingsAttrGrp)
        self.addMidControlsInput = BoolAttribute('addMidControls', value=True, parent=self.guideSettingsAttrGrp)
        self.useOtherIKGoalInput = BoolAttribute('useOtherIKGoal', value=True, parent=self.guideSettingsAttrGrp)
        self.uplimbName = StringAttribute('uplimbName', value="uplimb", parent=self.guideSettingsAttrGrp)
        self.lolimbName = StringAttribute('lolimbName', value="lolimb", parent=self.guideSettingsAttrGrp)
        self.ikHandleName = StringAttribute('ikHandleName', value="limbIK", parent=self.guideSettingsAttrGrp)
        self.addTwistJoints = BoolAttribute('addTwistJoints', value=False, parent=self.guideSettingsAttrGrp)
        self.uplimbNumTwistJoints = IntegerAttribute('uplimbNumTwistJoints', value=5, minValue=2, maxValue=20, parent=self.guideSettingsAttrGrp)
        self.lolimbNumTwistJoints = IntegerAttribute('lolimbNumTwistJoints', value=5, minValue=2, maxValue=20, parent=self.guideSettingsAttrGrp)


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
        data['globalComponentCtrlSize'] = self.globalComponentCtrlSizeInputAttr.getValue()

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

        globalScale = data['globalComponentCtrlSize']
        self.globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.uplimbCtrl.scalePoints(self.globalScaleVec)
        self.lolimbCtrl.scalePoints(self.globalScaleVec)
        self.handleCtrl.scalePoints(self.globalScaleVec)

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
                self.softIKAttr = self.createInput('softIK', dataType='Float', parent=self.cmpInputAttrGrp)
                self.squashhAttr = self.createInput('squash', dataType='Float', parent=self.cmpInputAttrGrp)
                self.stretchAttr = self.createInput('stretch', dataType='Float', parent=self.cmpInputAttrGrp)
        else:
            if self.ikgoal_cmpIn is not None:
                # self.deleteInput('ikGoalInput', parent=self.inputHrcGrp)
                # self.deleteInput('ikBlend', parent=self.cmpInputAttrGrp)
                # self.deleteInput('softIK', parent=self.cmpInputAttrGrp)
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
        data['upVXfo']    = upVXfo
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
        self.uplimbName = data['uplimbName']
        self.lolimbName = data['lolimbName']
        self.ikHandleName = data['ikHandleName']

        self.useOtherIKGoal = bool(data['useOtherIKGoal'])
        self.mocap = bool(data["mocap"])

        globalScale = data['globalComponentCtrlSize']
        self.globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.untwistUplimb = bool(data['untwistUplimb'])  #This should be a simple method instead
        self.addPartialJoints = bool(data['addPartialJoints'])  #This should be a simple method instead
        self.addTwistJoints = bool(data['addTwistJoints'])  #This should be a simple method instead
        self.addMidControls = bool(data['addMidControls'])  #This should be a simple method instead
        self.addTwistJointsORaddMidControls = bool(data['addTwistJoints']) or bool(data['addMidControls'])

        # =========
        # Controls
        # =========
        # World and Parent Space for Aligns (add more if needed)
        self.uplimbWorldSpace = CtrlSpace(self.uplimbName + 'WorldSpace', parent=self.ctrlCmpGrp)
        self.uplimbParentSpace = CtrlSpace(self.uplimbName + 'ParentSpace', parent=self.ctrlCmpGrp)
        self.uplimbWorldSpace.xfo  = data['uplimbXfo']
        self.uplimbParentSpace.xfo = data['uplimbXfo']

        # uplimb
        self.uplimbFKCtrlSpace = CtrlSpace(self.uplimbName, parent=self.ctrlCmpGrp)
        self.uplimbFKCtrl = FKControl(self.uplimbName, parent=self.uplimbFKCtrlSpace, shape="cube")
        self.uplimbFKCtrl.xfo = data['uplimbXfo']
        self.uplimbFKCtrlSpace.xfo = data['uplimbXfo']
        self.uplimbFKCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["YXZ"])  #Set with component settings later

        if self.untwistUplimb:
            # We should be able to insert a space to any kind of 3D object, not just controls
            self.uplimbUntwistBase = CtrlSpace(name=self.uplimbName+"UntwistBase", parent=self.uplimbParentSpace)
            self.uplimbUntwistBase.xfo = data['uplimbXfo']

        # lolimb
        self.lolimbFKCtrlSpace = CtrlSpace(self.lolimbName, parent=self.uplimbFKCtrl)
        self.lolimbFKCtrl = FKControl(self.lolimbName, parent=self.lolimbFKCtrlSpace)
        self.lolimbFKCtrlSpace.xfo = data['lolimbXfo']
        self.lolimbFKCtrl.xfo = data['lolimbXfo']
        self.lolimbFKCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["YXZ"])  #Set with component settings later


        # lolimbIK
        self.lolimbIKCtrlSpace = CtrlSpace(self.lolimbName+'IK', parent=self.ctrlCmpGrp)
        self.lolimbIKCtrl = FKControl(self.lolimbName+'IK', parent=self.lolimbIKCtrlSpace, shape="circle", scale=globalScale*0.8)
        self.lolimbIKCtrlSpace.xfo = data['lolimbXfo']
        self.lolimbIKCtrl.xfo = data['lolimbXfo']
        self.lolimbIKCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["XZY"])  #Set with component settings later
        self.lolimbIKCtrl.lockRotation(x=True, y=True, z=True)
        self.lolimbIKCtrl.lockScale(x=True, y=True, z=True)
        self.lolimbIKCtrl.rotatePoints(0, 0, 90)

        # MidCtrls (Bend/Bow) Creation - may need to make this an option
        # uplimbMid
        if self.addMidControls:
            self.uplimbMidCtrlSpace = CtrlSpace(self.uplimbName+'Mid', parent=self.ctrlCmpGrp)
            self.uplimbMidCtrl = FKControl(self.uplimbName+'Mid', parent=self.uplimbMidCtrlSpace, shape="circle", scale=globalScale*1.0)
            self.lolimbMidCtrlSpace = CtrlSpace(self.lolimbName+'Mid', parent=self.ctrlCmpGrp)
            self.lolimbMidCtrl = FKControl(self.lolimbName+'Mid', parent=self.lolimbMidCtrlSpace, shape="circle", scale=globalScale*0.8)

            for ctrl in [self.uplimbMidCtrl, self.uplimbMidCtrlSpace]:
                ctrl.xfo = data['uplimbXfo']
                ctrl.xfo.tr = data['uplimbXfo'].tr.linearInterpolate(data['lolimbXfo'].tr, 0.5)
            # lolimbMid
            for ctrl in [self.lolimbMidCtrl, self.lolimbMidCtrlSpace]:
                ctrl.xfo = data['lolimbXfo']
                ctrl.xfo.tr = data['lolimbXfo'].tr.linearInterpolate(data['handleXfo'].tr, 0.5)

            for ctrl in [self.uplimbMidCtrl, self.lolimbMidCtrl]:
                ctrl.lockRotation(x=True, y=True, z=True)
                ctrl.lockScale(x=True, y=True, z=True)
                ctrl.rotatePoints(0, 0, 90)

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


        self.limbIKCtrlSpace = CtrlSpace(self.ikHandleName, parent=self.ctrlCmpGrp)
        self.limbIKCtrlSpace.xfo = data['handleXfo']

        # hand
        if self.useOtherIKGoal: #Do not use this as a control, hide it
            self.limbIKCtrl = Transform(self.ikHandleName, parent=self.limbIKCtrlSpace)
        else:
            self.limbIKCtrl = IKControl(self.ikHandleName, parent=self.limbIKCtrlSpace, shape="jack")
        self.limbIKCtrl.xfo = data['handleXfo']


        # Add Component Params to IK control
        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.limbIKCtrl)


        if self.mocap:
                self.limbMocapInputAttr = self.createInput('limbMocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()

        if self.useOtherIKGoal:
            self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
            self.limbIKCtrl.constrainTo(self.ikgoal_cmpIn, maintainOffset=True)
            self.ikBlendAttr = self.createInput('ikBlend', dataType='Float', value=1.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            self.softIKAttr = self.createInput('softIK', dataType='Float', value=0.0, minValue=0.0, parent=self.cmpInputAttrGrp).getTarget()
            self.squashAttr = self.createInput('squash', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            self.stretchAttr = self.createInput('stretch', dataType='Float', value=1.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
        else:
            self.ikgoal_cmpIn = None
            self.ikBlendAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
            self.softIKAttr = ScalarAttribute('softIK', value=0.0, minValue=0.0, parent=limbSettingsAttrGrp)
            self.squashAttr = ScalarAttribute('squash', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
            self.stretchAttr = ScalarAttribute('stretch', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)

        self.limbBone0LenInputAttr = ScalarAttribute('bone0Len', value=1.0, parent=limbSettingsAttrGrp)
        self.limbBone1LenInputAttr = ScalarAttribute('bone1Len', value=1.0, parent=limbSettingsAttrGrp)
        self.limbDrawDebugAttr = BoolAttribute('drawDebug', value=True, parent=limbSettingsAttrGrp)

        self.drawDebugInputAttr.connect(self.limbDrawDebugAttr)



        # =========
        # Mocap
        # =========
        if self.mocap:
            # Mocap uplimb
            self.uplimb_mocap = MCControl(self.uplimbName, parent=self.uplimbFKCtrlSpace, shape="cube")
            #rotation order should stay consistent no matter what ro the controls have
            self.uplimb_mocap.xfo = data['uplimbXfo']
            self.uplimb_mocap.alignOnXAxis()
            self.uplimb_mocap.scalePointsOnAxis(data['uplimbLen'], self.boneAxisStr)


            # Mocap lolimb
            self.lolimb_mocap = MCControl(self.lolimbName, parent=self.uplimb_mocap, shape="cube")
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
        upVSpaceBlendInputAttr = ScalarAttribute(self.ikHandleName+'Space', value=0.0, minValue=0.0, maxValue=1.0, parent=upVAttrGrp)


        # ==========
        # Deformers
        # ==========

        self.uplimbDef = Joint(self.uplimbName, parent=self.deformersParent)
        self.uplimbDef.setComponent(self)

        self.lolimbDef = Joint(self.lolimbName, parent=self.uplimbDef)
        self.lolimbDef.setComponent(self)
        # Don't want to change RO for fbx output right now
        # self.lolimbDef.ro = RotationOrder(rotationOrderStrToIntMapping["YXZ"])  #Set with component settings later

        self.limbendDef = Joint(name+'end', parent=self.lolimbDef)
        self.limbendDef.setComponent(self)

        self.parentSpaceInputTgt.childJoints = [self.uplimbDef]


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        # self.uplimbFKCtrlSpaceConstraint = self.uplimbFKCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        self.uplimbParentSpaceConstraint     = self.uplimbParentSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.uplimbWorldSpaceConstraint      = self.uplimbWorldSpace.constrainTo(self.ctrlCmpGrp, maintainOffset=True)

        # Blend the Spaces (should make this a sub proc)
        self.limbUpVSpaceHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'UpVSpace_HierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.limbUpVSpaceHierBlendSolver)
        self.limbUpVSpaceHierBlendSolver.setInput('blend', upVSpaceBlendInputAttr)
        upVSpaceBlendInputAttr.setValue(0.0)
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

        # WorldSpace Blend Aim
        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_Settings", parent=self.uplimbFKCtrl)
        self.worldSpaceAttr  = ScalarAttribute('alignToWorld', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)

        self.armAlignOp = self.blend_two_xfos(
            self.uplimbFKCtrlSpace,
            self.uplimbParentSpace, self.uplimbWorldSpace,
            blendTranslate=0,
            blendRotate=self.worldSpaceAttr,
            blendScale=0,
            blend=self.worldSpaceAttr,
            name= self.uplimbName + 'BlendKLOp')

        # Add FK/IK Blend Limb KL Op
        self.limbIKKLOp = KLOperator(self.getLocation()+self.getName()+'IKFKTwoBoneIKSolver', 'OSS_TwoBoneIKSolver', 'OSS_Kraken')
        self.addOperator(self.limbIKKLOp)
        # Add Att Inputs
        self.limbIKKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.limbIKKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.limbIKKLOp.setInput('bone0Len', self.limbBone0LenInputAttr)
        self.limbIKKLOp.setInput('bone1Len', self.limbBone1LenInputAttr)
        self.limbIKKLOp.setInput('ikBlend', self.ikBlendAttr)
        self.limbIKKLOp.setInput('softIK', self.softIKAttr)
        self.limbIKKLOp.setInput('squash', self.squashAttr)
        self.limbIKKLOp.setInput('stretch', self.stretchAttr)
        # Add Xfo Inputs
        self.limbIKKLOp.setInput('root', self.uplimbFKCtrlSpace)
        self.limbIKKLOp.setInput('bone0FK', self.uplimbFKCtrl)
        self.limbIKKLOp.setInput('bone1FK', self.lolimbFKCtrl)
        self.limbIKKLOp.setInput('upV', self.limbUpVCtrl)
        self.limbIKKLOp.setInput('boneAxis', AXIS_NAME_TO_INT_MAP[self.boneAxisStr])
        self.limbIKKLOp.setInput('upAxis', AXIS_NAME_TO_INT_MAP[self.upAxisStr])
        self.limbIKKLOp.setInput('ikHandle', self.limbIKCtrl)

        # Add lolimb IK
        self.limbIKKLOp.setOutput('bone0Out', self.uplimb_cmpOut)
        self.limbIKKLOp.setOutput('bone1Out', self.lolimbIKCtrlSpace)
        self.limbIKKLOp.setOutput('bone2Out', self.endlimb_cmpOut)



        # MidCtrl (Bend/Bow) Creation - may need to make this an option
        if self.addMidControls:
            sourceA = self.uplimb_cmpOut
            sourceB = self.lolimbIKCtrl
            self.uplimbMidCtrlRigOp = KLOperator(self.uplimbName + "MidBlendOp", 'OSS_BlendTRSConstraintSolver', 'OSS_Kraken')
            self.addOperator(self.uplimbMidCtrlRigOp)
            self.uplimbMidCtrlRigOp.setInput('blendTranslate', 0.5)
            self.uplimbMidCtrlRigOp.setInput('blendRotate', 0)
            self.uplimbMidCtrlRigOp.setInput('blendScale', 0.5)
            self.uplimbMidCtrlRigOp.setInput('constrainerTranslateA', sourceA)
            self.uplimbMidCtrlRigOp.setInput('constrainerTranslateB', sourceB)
            self.uplimbMidCtrlRigOp.setInput('constrainerRotateA', sourceA)
            self.uplimbMidCtrlRigOp.setInput('constrainerRotateB', sourceB)
            self.uplimbMidCtrlRigOp.setInput('constrainerScaleA', sourceA)
            self.uplimbMidCtrlRigOp.setInput('constrainerScaleB', sourceB)
            self.uplimbMidCtrlRigOp.setOutput('result', self.uplimbMidCtrlSpace)

            sourceA = self.lolimbIKCtrl
            sourceB = self.endlimb_cmpOut
            self.lolimbMidCtrlRigOp = KLOperator(self.lolimbName + "MidBlendOp", 'OSS_BlendTRSConstraintSolver', 'OSS_Kraken')
            self.addOperator(self.lolimbMidCtrlRigOp)
            self.lolimbMidCtrlRigOp.setInput('blendTranslate', 0.5)
            self.lolimbMidCtrlRigOp.setInput('blendRotate', 0)
            self.lolimbMidCtrlRigOp.setInput('blendScale', 0.5)
            self.lolimbMidCtrlRigOp.setInput('constrainerTranslateA', sourceA)
            self.lolimbMidCtrlRigOp.setInput('constrainerTranslateB', sourceB)
            self.lolimbMidCtrlRigOp.setInput('constrainerRotateA', sourceA)
            self.lolimbMidCtrlRigOp.setInput('constrainerRotateB', sourceB)
            self.lolimbMidCtrlRigOp.setInput('constrainerScaleA', sourceA)
            self.lolimbMidCtrlRigOp.setInput('constrainerScaleB', sourceB)
            self.lolimbMidCtrlRigOp.setOutput('result', self.lolimbMidCtrlSpace)


        # Mocap
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
            self.limbMocapHierBlendSolver.setOutput('hierOut', [self.uplimb_cmpOut, self.lolimbIKCtrlSpace, self.endlimb_cmpOut])
        else:
            self.limbIKKLOp.setOutput('bone0Out', self.uplimb_cmpOut)
            self.limbIKKLOp.setOutput('bone1Out', self.lolimbIKCtrlSpace)
            self.limbIKKLOp.setOutput('bone2Out', self.endlimb_cmpOut)

        if self.untwistUplimb:
            uplimbSolverOut = self.createOutput(self.uplimbName+"uplimbSolverOut", dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            self.limbIKKLOp.setOutput('bone0Out', uplimbSolverOut)

            self.untwistKLOp = KLOperator(self.getLocation()+self.getName()+'OSS_UntwistSolver', 'OSS_UntwistSolver', 'OSS_Kraken')
            self.addOperator(self.untwistKLOp)
            self.untwistKLOp.setInput('drawDebug', self.drawDebugInputAttr)
            self.untwistKLOp.setInput('rigScale', self.rigScaleInputAttr)
            self.untwistKLOp.setInput('inMatrix', uplimbSolverOut)
            self.untwistKLOp.setInput('inBaseMatrix', self.uplimbUntwistBase)
            self.untwistKLOp.setInput('axis', AXIS_NAME_TO_INT_MAP[self.boneAxisStr])
            self.untwistKLOp.setOutput('untwistedMatrix', self.uplimb_cmpOut)




        # Add lolimb IK Constrain
        self.lolimb_cmpOut.constrainTo(self.lolimbIKCtrl).evaluate()

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

        self.drawDebugInputAttr.setValue(True)

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

        if self.addTwistJointsORaddMidControls:
            boneAxisVec = AXIS_NAME_TO_VEC3_MAP[self.boneAxisStr]
            upAxisVec = AXIS_NAME_TO_VEC3_MAP[self.upAxisStr]
            sideAxisVec = boneAxisVec.cross(upAxisVec)
            sideAxisStr = TUPLE_TO_AXIS_NAME_MAP[sideAxisVec.x, sideAxisVec.y, sideAxisVec.z]


            uplimbStartTwistXfo = self.createOutput(self.uplimbName+"StartTwist", dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            uplimbStartTwistXfo.xfo = Xfo(self.uplimb_cmpOut.xfo)
            uplimbStartTwistXfo.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)


            lolimbEndTwistXfo = self.createOutput(self.lolimbName+"EndTwist", dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            lolimbEndTwistXfo.xfo = Xfo(self.endlimb_cmpOut.xfo)
            if self.useOtherIKGoal:
                lolimbEndTwistXfo.constrainTo(self.endTwistParent_cmpIn, maintainOffset=True)
            else:
                lolimbEndTwistXfo.constrainTo(self.endlimb_cmpOut, maintainOffset=True)

            if self.addMidControls:
               self.uplimbTwInputs = [self.uplimb_cmpOut, self.uplimbMidCtrl, self.lolimb_cmpOut]
               self.lolimbTwInputs = [self.lolimb_cmpOut, self.lolimbMidCtrl, lolimbEndTwistXfo]
            else:
               self.uplimbTwInputs = [self.uplimb_cmpOut, self.lolimb_cmpOut]
               self.lolimbTwInputs = [self.lolimb_cmpOut, lolimbEndTwistXfo]

            self.uplimbTwistKLOp = self.createTwistJoints(
                self.uplimbName+"_twist",
                self.uplimbDef,
                self.uplimbTwInputs,
                numDeformers=int(data['uplimbNumTwistJoints']),
                #skipStart=True,
                aimAxisStr=self.boneAxisStr,  #This would be an offset to the ctrlAxis
                sideAxisStr=self.upAxisStr.replace("POS", "NEG"),
                #ctrlAimAxisStr=self.boneAxisStr,  # Don't invert the Xaxis of the control - remember this is relative to existing ctrls
                ctrlNormalAxisStr=self.upAxisStr)  #We want the normal to the curve to be in Y so MAP this (Z default to Y)


            self.lolimbTwistKLOp = self.createTwistJoints(
                self.lolimbName+"_twist",
                self.lolimbDef,
                self.lolimbTwInputs,
                numDeformers=int(data['lolimbNumTwistJoints']),
                #skipStart=True,
                aimAxisStr=self.boneAxisStr,  #This would be an offset to the ctrlAxis
                sideAxisStr=self.upAxisStr.replace("POS", "NEG"),
                #ctrlAimAxisStr=self.boneAxisStr, # Don't invert the Xaxis of the control - remember this is relative to existing ctrls
                ctrlNormalAxisStr=self.upAxisStr)

            self.uplimbTwistKLOp.evaluate
            self.lolimbTwistKLOp.evaluate

        if self.addPartialJoints:

            if self.untwistUplimb:
                uplimbBaseRotate = self.uplimbUntwistBase
            else:
                uplimbBaseRotate = self.uplimbFKCtrlSpace

            uplimbPartialDef = self.createPartialJoint(self.uplimbDef, baseTranslate=self.uplimbDef, baseRotate=uplimbBaseRotate, parent=self.uplimbDef.getParent())

            lolimbPartialConstrainer = self.uplimb_cmpOut
            if self.addTwistJointsORaddMidControls:
                lolimbPartialConstrainer = self.uplimbTwistKLOp.getOutput("outputs")[-1]  #Use the last twist joint to blend ori from

            #Re-write the PartialJointBlend solver and python function to better accommodate random inputs.
            # We actually want to blend between the end of the uplimb twist and the start of the lolimb twist - because of scale interp
            lolimbTargetDef = self.lolimbDef
            if self.addTwistJointsORaddMidControls:
               lolimbTargetDef = self.lolimbTwistKLOp.getOutput("outputs")[0]  #Use the last twist joint to blend ori from

            lolimb_ik_base = Locator(self.lolimbDef.getName()+"_ik_base_null" , parent=self.ctrlCmpGrp)
            lolimb_ik_base.setShapeVisibility(False)
            lolimb_ik_base.xfo = Xfo(self.lolimb_cmpOut.xfo) #should be up to date by now, keep orientation of lolimb in relation to uplimb
            lolimb_ik_base.constrainTo(lolimbPartialConstrainer, maintainOffset=True)
            lolimbPartialDef = self.createPartialJoint(lolimbTargetDef,
                name=self.lolimbDef.getName()+"_part",
                baseTranslate=lolimbTargetDef,
                baseRotate=lolimb_ik_base,
                baseScale=lolimb_ik_base,
                parent=self.lolimbDef.getParent())

            self.parentSpaceInputTgt.childJoints.append(uplimbPartialDef)

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info

        self.lolimbFKCtrl.scalePoints(Vec3(1, self.globalScaleVec.y, self.globalScaleVec.z))
        self.uplimbFKCtrl.scalePoints(Vec3(1, self.globalScaleVec.y, self.globalScaleVec.z))

        # self.uplimbFKCtrl.rotatePoints(0, -90, 0)
        # self.lolimbFKCtrl.rotatePoints(0, -90, 0)
        if not self.useOtherIKGoal:
            self.limbIKCtrl.scalePoints(self.globalScaleVec)
        self.limbUpVCtrl.scalePoints(self.globalScaleVec)

        self.connectReverse(self.ikBlendAttr, self.uplimbFKCtrl.getVisibilityAttr())
        self.connectReverse(self.ikBlendAttr, self.lolimbFKCtrl.getVisibilityAttr())





from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSLimbComponentGuide)
ks.registerComponent(OSSLimbComponentRig)
