from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import *

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.components.component_output import ComponentOutput
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.transform import Transform
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.layer import Layer
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
# from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component


COMPONENT_NAME = "spine"

class OSSSpineComponent(OSS_Component):
    """Spine Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSSpineComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========


        # Declare Output Xfos
        self.hipsOutputTgt = self.createOutput('hips', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.pelvisOutputTgt = self.createOutput('pelvis', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.spineEndOutputTgt = self.createOutput('spineEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.spineVertebraeOutput = self.createOutput('spineVertebrae', dataType='Xfo[]')

        # Declare Input Attrs

        # Declare Output Attrs



class OSSSpineComponentGuide(OSSSpineComponent):
    """Spine Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Spine Guide Component:" + name)
        super(OSSSpineComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # ========
        self.numDeformersAttr = IntegerAttribute('numDeformers', value=6, minValue=0, maxValue=20, parent=self.guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        #self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
        self.mocapInputAttr = None
        # Guide Controls


        self.pelvisCtrl = Control('pelvisPosition', parent=self.ctrlCmpGrp, shape='null')
        self.torsoCtrl = Control('torsoPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.chestCtrl = Control('chestPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.upChestCtrl = Control('upChestPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.neckCtrl = Control('neckPosition', parent=self.ctrlCmpGrp, shape='null')



        data = {
            'pelvisPosition': Vec3(0.0, 9, 0),
            'torsoPosition': Vec3(0.0, 10, 0),
            'chestPosition': Vec3(0.0, 12, 0),
            'upChestPosition': Vec3(0.0, 14, 0),
            'neckPosition': Vec3(0.0, 15, 0),
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

        data = super(OSSSpineComponentGuide, self).saveData()

        data['pelvisPosition'] = self.pelvisCtrl.xfo.tr
        data['torsoPosition'] = self.torsoCtrl.xfo.tr
        data['chestPosition'] = self.chestCtrl.xfo.tr
        data['upChestPosition'] = self.upChestCtrl.xfo.tr
        data['neckPosition'] = self.neckCtrl.xfo.tr

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

        #saveData() will grab the guide settings values (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSSpineComponentGuide, self).loadData( data )

        self.pelvisCtrl.xfo.tr = data["pelvisPosition"]
        self.torsoCtrl.xfo.tr = data["torsoPosition"]
        self.chestCtrl.xfo.tr = data["chestPosition"]
        self.upChestCtrl.xfo.tr = data["upChestPosition"]
        self.neckCtrl.xfo.tr = data["neckPosition"]

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec = Vec3(globalScale, globalScale, globalScale)

        self.pelvisCtrl.scalePoints(globalScaleVec)
        self.torsoCtrl.scalePoints(globalScaleVec)
        self.chestCtrl.scalePoints(globalScaleVec)
        self.upChestCtrl.scalePoints(globalScaleVec)
        self.neckCtrl.scalePoints(globalScaleVec)

        return True


    def updateMocap(self, mocap):
        """ Callback to changing the component setting 'useOtherIKGoalInput'
        Really, we should build this ability into the system, to add/remove input attrs based on guide setting bools.
        That way, we don't have to write these callbacks.
        """
        if mocap:
            if self.mocapInputAttr is None:
                self.mocapInputAttr = self.createInput('mocap', dataType='Float', parent=self.cmpInputAttrGrp)
                self.mocap = True

        else:
            if self.mocapInputAttr is not None:
                self.deleteInput('mocap', parent=self.cmpInputAttrGrp)
                self.mocapInputAttr = None
                self.mocap = False


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSSpineComponentGuide, self).getRigBuildData()

        data['pelvisPosition'] = self.pelvisCtrl.xfo.tr
        data['torsoPosition'] = self.torsoCtrl.xfo.tr
        data['chestPosition'] = self.chestCtrl.xfo.tr
        data['upChestPosition'] = self.upChestCtrl.xfo.tr
        data['neckPosition'] = self.neckCtrl.xfo.tr

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

        return OSSSpineComponentRig


class OSSSpineComponentRig(OSSSpineComponent):
    """Spine Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Spine Rig Component:" + name)
        super(OSSSpineComponentRig, self).__init__(name, parent)

        self.mocap = False
        # =========
        # Controls
        # =========



        # hips
        self.hipsCtrl = FKControl('hips', parent=self.ctrlCmpGrp, shape="squarePointed")
        self.hipsCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.hipsCtrl.rotatePoints(0, -90.0, 0)
        self.hipsCtrl.scalePoints(Vec3(4.5, 3.0, 3.0))
        self.hipsCtrlSpace = self.hipsCtrl.insertCtrlSpace()

        # Pelvis
        self.pelvisCtrlSpace = CtrlSpace('pelvis', parent=self.hipsCtrl)
        # self.pelvisCtrl = Control('pelvis', parent=self.pelvisCtrlSpace, shape="cube")
        # self.pelvisCtrl.setColor("green")
        # self.pelvisCtrl.scalePoints(Vec3(1, 1, 1))

        # Torso
        self.torsoCtrl = FKControl('torso', parent=self.ctrlCmpGrp, shape="squarePointed")
        self.torsoCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.torsoCtrl.rotatePoints(0, -90.0, 0)
        self.torsoCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.torsoCtrlSpace = self.torsoCtrl.insertCtrlSpace()


        # Chest
        self.chestCtrl = FKControl('chest', parent=self.torsoCtrl, shape="squarePointed")
        self.chestCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.chestCtrl.rotatePoints(0, -90.0, 0)
        self.chestCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.chestCtrlSpace = self.chestCtrl.insertCtrlSpace()

        # UpChest
        self.upChestCtrl = FKControl('upChest', parent=self.chestCtrl, shape="squarePointed")
        self.upChestCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.upChestCtrl.rotatePoints(0, -90.0, 0)
        self.upChestCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.upChestCtrlSpace = self.upChestCtrl.insertCtrlSpace()
        self.upChestCtrlResult = Transform('upChest_result', parent=self.ctrlCmpGrp)
        self.upChestCtrlResult.xfo = Xfo(self.upChestCtrl.xfo)


        # chest Aim
        chestNeckSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.upChestCtrl)
        self.chestAlignToWorldSpaceAttr = ScalarAttribute('alignToWorld', value=0.0, minValue=0.0, maxValue=1.0, parent=chestNeckSettingsAttrGrp)
        self.chestAlignIkSpaceAttr = ScalarAttribute('alignToChestIK', value=0.0, minValue=0.0, maxValue=1.0, parent=chestNeckSettingsAttrGrp)
        self.chestIKAttr = ScalarAttribute('chestIK', value=0.0, minValue=0.0, maxValue=1.0, parent=chestNeckSettingsAttrGrp)


        self.chestWorldRef = CtrlSpace('chestWorldRef', parent=self.ctrlCmpGrp)
        self.chestFKToWorldRef = CtrlSpace('FKToWorldRef', parent=self.ctrlCmpGrp)
        self.chestFKRef = CtrlSpace('chestFKRef', parent=self.chestCtrl)
        self.upChestIKRef = CtrlSpace('upChestIKRef', parent=self.ctrlCmpGrp)
        self.upChestIKCtrlSpace = CtrlSpace('upChestIK', parent=self.ctrlCmpGrp)
        self.upChestIKCtrl = IKControl('chest', parent=self.upChestIKCtrlSpace, shape="square")
        self.upChestIKCtrl.setColor('red')
        self.upChestIKCtrl.rotatePoints(90,0,0)
        self.upChestIKCtrl.scalePoints(Vec3(3,3,3))
        self.upChestIKCtrl.lockScale(x=True, y=True, z=True)
        self.upChestIKCtrl.lockRotation(x=True, y=True, z=True)

        self.upChestIKUpVSpace = CtrlSpace('chestUpV', parent=self.globalSRTInputTgt)
        self.upChestIKUpV = Control('chestUpV', parent=self.upChestIKUpVSpace, shape="circle")
        self.upChestIKUpV.scalePoints(Vec3(3,3,3))
        self.upChestIKUpV.lockScale(x=True, y=True, z=True)
        self.upChestIKUpV.lockRotation(x=True, y=True, z=True)

        # Neck
        self.neckCtrlSpace = CtrlSpace('neck', parent=self.ctrlCmpGrp)
        self.neckCtrlSpace.constrainTo(self.upChestCtrlResult, maintainOffset=True)


        # ==========
        # Deformers
        # ==========

        self.deformerJoints = []
        self.spineOutputs = []

        self.controlInputs = []
        self.controlRestInputs = []

        self.spineOutputs = []
        self.params = []
        self.rigControlAligns = []

        self.rigidIDs = []
        self.rigidMat44s = []
        self.rigidAligns = []
        #self.setNumDeformers(1)

        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.spineVertebraeOutput.setTarget(self.spineOutputs)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.hipsCtrlSpaceConstraint = self.hipsCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.torsoCtrlSpaceConstraint = self.torsoCtrlSpace.constrainTo(self.parentSpaceInputTgt)


        # ===============
        # Add Fabric Ops
        # ===============
        # Add Spine Canvas Op

        self.NURBSSpineKLOp = KLOperator('spine', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.NURBSSpineKLOp)

        self.NURBSSpineKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.NURBSSpineKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.NURBSSpineKLOp.setInput('alignX', 1 )
        self.NURBSSpineKLOp.setInput('alignY', 2 )
        self.NURBSSpineKLOp.setInput('alignZ', 3 )
        self.NURBSSpineKLOp.setInput('degree', 3)
        self.NURBSSpineKLOp.setInput('keepArcLength', 0.0)
        self.NURBSSpineKLOp.setInput('compressionAmt', 0.4)
        self.NURBSSpineKLOp.setInput('followCurveTangent', 1.0)
        self.NURBSSpineKLOp.setInput('followCurveNormal', 1.0)
        self.NURBSSpineKLOp.setInput('useLocalNormal', 0.0)
        self.NURBSSpineKLOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.NURBSSpineKLOp.setInput('parent', self.ctrlCmpGrp)
        # atVec should be optional
        self.NURBSSpineKLOp.setInput('atVec', self.ctrlCmpGrp)
        self.NURBSSpineKLOp.setInput('controlAligns', self.rigControlAligns)
        self.NURBSSpineKLOp.setInput('controls', self.controlInputs)
        self.NURBSSpineKLOp.setInput('controlsRest', self.controlRestInputs)
        self.NURBSSpineKLOp.setInput('rigidIDs', [0,5])
        self.NURBSSpineKLOp.setInput('rigidMat44s', self.rigidMat44s)
        self.NURBSSpineKLOp.setInput('rigidAligns', self.rigidAligns)

        self.NURBSSpineKLOp.setInput('params', self.params )

        self.NURBSSpineKLOp.setOutput('outputs', self.spineOutputs)

        # establish params between 0 and 1 (for now)

        Profiler.getInstance().pop()


    def setNumDeformers(self, numDeformers):

        for output in reversed(self.spineOutputs):
            output.getParent().removeChild(output)
        del self.spineOutputs[:] #Clear since this array obj is tied to output already

        for joint in reversed(self.deformerJoints):
            joint.getParent().removeChild(joint)
        del self.deformerJoints[:] #Clear since this array obj is tied to output already

        # Add new deformers and outputs
        for i in xrange(len(self.spineOutputs), numDeformers):
            if i == 0:
                name = "pelvis"
                self.spineOutputs.append(self.pelvisOutputTgt)
            else:
                name = 'spine' + str(i).zfill(2)
                #Need dynamic ports branch to be able to see this updated in Graph
                spineOutput = self.createOutput(name, dataType='Xfo', parent=self.outputHrcGrp).getTarget()
                self.spineOutputs.append(spineOutput)

        parent = self.deformersParent
        for i in xrange(len(self.deformerJoints), numDeformers):
            if i == 0:
                name = "pelvis"
            else:
                name = 'spine' + str(i).zfill(2)
                parent = self.deformerJoints[-1]
            spineDef = Joint(name, parent=parent)
            spineDef.setComponent(self)
            self.deformerJoints.append(spineDef)
            if name == "pelvis":
                self.parentSpaceInputTgt.childJoints = [spineDef]


        # Determine params for number of Deformers
        a = 0.0
        b = 1.0
        for i in range(numDeformers):
            ratio = float(i) / float(numDeformers-1)
            self.params.append((1.0-ratio)*a + ratio*b)
            self.rigControlAligns.append(Vec3(1,2,3))
        if hasattr(self, 'NURBSSpineKLOp'):  # Check in case this is ever called from Guide callback
            self.NURBSSpineKLOp.setInput('params',  self.params)

        return True


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSSpineComponentRig, self).loadData( data )

        pelvisPosition = data['pelvisPosition']
        torsoPosition = data['torsoPosition']
        chestPosition = data['chestPosition']
        upChestPosition = data['upChestPosition']
        neckPosition = data['neckPosition']
        numDeformers = data['numDeformers']

        self.mocap = bool(data["mocap"])

        self.pelvisCtrlSpace.xfo.tr = pelvisPosition

        self.hipsCtrlSpace.xfo.tr = torsoPosition
        self.hipsCtrl.xfo.tr = torsoPosition


        self.torsoCtrlSpace.xfo.tr = torsoPosition
        self.torsoCtrl.xfo.tr = torsoPosition

        self.chestCtrlSpace.xfo.tr = chestPosition
        self.chestCtrl.xfo.tr = chestPosition

        self.upChestCtrlSpace.xfo.tr = upChestPosition
        self.upChestCtrl.xfo.tr = upChestPosition

        self.neckCtrlSpace.xfo.tr = neckPosition
        # self.neckCtrl.xfo.tr = neckPosition

        # Chest LookAt/Aim Controls
        self.chestFKRef.xfo = self.upChestCtrlSpace.xfo
        length = upChestPosition.distanceTo(torsoPosition) * 3
        self.upChestIKCtrlSpace.xfo.ori = self.upChestCtrlSpace.xfo.ori
        self.upChestIKCtrlSpace.xfo.tr = self.upChestCtrlSpace.xfo.tr.add(Vec3(0, 0, length))
        self.upChestIKCtrl.xfo = self.upChestIKCtrlSpace.xfo

        self.upChestIKUpV.xfo.ori = self.upChestCtrlSpace.xfo.ori
        self.upChestIKUpV.xfo.tr = self.upChestCtrlSpace.xfo.tr.add(Vec3(0, length, 0))

        # Do we want this to be world up or hips up?
        self.chestIKUpVSpaceConstraint = self.upChestIKUpVSpace.constrainTo(self.hipsCtrl, maintainOffset=True)

        # Add Aim Op
        self.chestAimKLOp = KLOperator('chestAimKLOp', 'OSS_AimKLSolver', 'OSS_Kraken')
        self.addOperator(self.chestAimKLOp)

        # Add Att Inputs
        self.chestAimKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.chestAimKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.chestAimKLOp.setInput('blend',  0)
        # Add Xfo Inputs
        self.chestAimKLOp.setInput('rest', self.chestFKRef)
        self.chestAimKLOp.setInput('ik', self.upChestIKCtrl)
        self.chestAimKLOp.setInput('up', self.upChestIKUpV)
        # Outputs
        self.chestAimKLOp.setOutput('result', self.upChestIKRef)


        # Add Blend Op
        # Add Att Inputs
        self.alignchestToWorldOp = self.blend_two_xfos(
            self.chestFKToWorldRef,
            self.chestFKRef, self.chestWorldRef,
            blendTranslate=0,
            blendRotate=self.chestAlignToWorldSpaceAttr,
            blendScale=0,
            name='alignchestToWorldOp')

        self.upChestCtrlSpace.setParent(self.ctrlCmpGrp)

        self.alignchestToIKOp = self.blend_two_xfos(
            self.upChestCtrlSpace,
            self.chestFKToWorldRef, self.upChestIKRef,
            blendTranslate=0,
            blendRotate=self.chestAlignIkSpaceAttr,
            blendScale=0,
            name='alignchestToIKOp')



        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        self.pelvisHeight = pelvisPosition.subtract(torsoPosition)
        self.hipsCtrl.translatePoints( self.pelvisHeight - Vec3(0,2,0))

        self.controlInputs.append(self.pelvisCtrlSpace)
        self.controlInputs.append(self.torsoCtrl)
        self.controlInputs.append(self.chestCtrl)
        self.controlInputs.append(self.upChestCtrlResult)
        self.controlInputs.append(self.neckCtrlSpace)

        self.controlRestInputs.append(self.pelvisCtrlSpace.xfo)
        self.controlRestInputs.append(self.torsoCtrl.xfo)
        self.controlRestInputs.append(self.chestCtrl.xfo)
        self.controlRestInputs.append(self.upChestCtrlResult.xfo)
        self.controlRestInputs.append(self.neckCtrlSpace.xfo)

        self.rigidMat44s.append(self.controlInputs[0])
        self.rigidMat44s.append(self.controlInputs[-1])
        self.rigidAligns.append(Vec3(-2,1,3))
        self.rigidAligns.append(Vec3(-2,1,3))


        # Constrain Outputs
        self.spineEndOutputConstraint = self.spineEndOutputTgt.constrainTo(self.spineOutputs[-1])

        if self.mocap:

            self.mocapInputAttr = self.createInput('mocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            height = 2.0

            # hips
            self.hipsMocapCtrl = MCControl('hips', parent=self.ctrlCmpGrp, shape="circle")
            self.hipsMocapCtrl.scalePoints(Vec3(4.5, height, 2.5))
            self.hipsMocapCtrl.setColor("mediumpurple")
            self.hipsMocapCtrl.xfo.tr = pelvisPosition
            self.hipsMocapCtrlSpace = self.hipsMocapCtrl.insertCtrlSpace()

            self.pelvisMocapCtrl = MCControl('pelvis', parent=self.hipsMocapCtrl, shape="circle")
            self.pelvisMocapCtrl.scalePoints(Vec3(4.5, height, 2.5))
            self.pelvisMocapCtrl.setColor("mediumpurple")
            self.pelvisMocapCtrl.xfo.tr = pelvisPosition
            self.pelvisMocapCtrlSpace = self.pelvisMocapCtrl.insertCtrlSpace()

            # Torso
            self.torsoMocapCtrl = MCControl('torso', parent=self.hipsMocapCtrl, shape="circle")
            self.torsoMocapCtrl.scalePoints(Vec3(5.0, height, 3.0))
            self.torsoMocapCtrl.setColor("mediumpurple")

            self.torsoMocapCtrl.xfo.tr = torsoPosition
            self.torsoMocapCtrlSpace = self.torsoMocapCtrl.insertCtrlSpace()

            # Chest
            self.chestMocapCtrl = MCControl('chest', parent=self.torsoMocapCtrl, shape="circle")
            self.chestMocapCtrl.scalePoints(Vec3(5.0, height, 3.0))
            self.chestMocapCtrl.setColor("mediumpurple")
            self.chestMocapCtrl.xfo.tr = chestPosition
            self.chestMocapCtrlSpace = self.chestMocapCtrl.insertCtrlSpace()

            # UpChest
            self.upChestMocapCtrl = MCControl('upChest', parent=self.chestMocapCtrl, shape="circle")
            self.upChestMocapCtrl.scalePoints(Vec3(5.0, height, 3.0))
            self.upChestMocapCtrl.setColor("mediumpurple")
            self.upChestMocapCtrl.xfo.tr = upChestPosition
            self.upChestMocapCtrlSpace = self.upChestMocapCtrl.insertCtrlSpace()

            # Neck
            self.neckMocapCtrlSpace = CtrlSpace('neckPosition', parent=self.upChestMocapCtrl)
            self.neckMocapCtrlSpace.xfo.tr = neckPosition

            # ==============
            # Constrain I/O
            # ==============
            # Constraint inputs

            # Blend anim and mocap together
            self.mocapHierBlendSolver = KLOperator(self.getName()+'mocap', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.mocapHierBlendSolver)
            self.mocapHierBlendSolver.setInput('blend', self.mocapInputAttr)  # connect this to attr
            # Add Att Inputs
            self.mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            self.mocapHierBlendSolver.setInput('hierA',
                [
                self.hipsCtrl,
                self.pelvisCtrlSpace,
                self.torsoCtrl,
                self.chestCtrl,
                self.upChestCtrl,
                self.neckCtrlSpace
                ],
            )

            self.mocapHierBlendSolver.setInput('hierB',
                [
                self.hipsMocapCtrl,
                self.pelvisMocapCtrlSpace,
                self.torsoMocapCtrl,
                self.chestMocapCtrl,
                self.upChestMocapCtrl,
                self.neckMocapCtrlSpace
                ]
            )
            #Create some nodes just for the ouput of the blend.
            #Wish we could just make direct connections....

            self.hipsCtrl_link = Transform('hipsCtrl_link', parent=self.outputHrcGrp)
            self.pelvisCtrlSpace_link = Transform('pelvisCtrlSpace_link', parent=self.outputHrcGrp)
            self.torsoCtrl_link = Transform('torsoCtrl_link', parent=self.outputHrcGrp)
            self.chestCtrl_link = Transform('chestCtrl_link', parent=self.outputHrcGrp)
            self.upChestCtrl_link = Transform('upChestCtrl_link', parent=self.outputHrcGrp)
            self.neckCtrlSpace_link = Transform('neckCtrlSpace_link', parent=self.outputHrcGrp)

            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.hipsCtrl_link,
                self.pelvisCtrlSpace_link,
                self.torsoCtrl_link,
                self.chestCtrl_link,
                self.upChestCtrl_link,
                self.neckCtrlSpace_link
                ]
            )
            self.mocapHierBlendSolver.setInput("parentIndexes", [-1, 0, 0, 2, 3, 4])
            self.mocapHierBlendSolver.evaluate()

            # Add Xfo Outputs
            self.mcControlInputs = []
            self.NURBSSpineKLOp.setInput('controls', self.mcControlInputs)
            self.mcControlInputs.append(self.pelvisCtrlSpace_link)
            self.mcControlInputs.append(self.torsoCtrl_link)
            self.mcControlInputs.append(self.chestCtrl_link)
            self.mcControlInputs.append(self.upChestCtrl_link)
            self.mcControlInputs.append(self.neckCtrlSpace_link)

            self.hipsOutputConstraint = self.hipsOutputTgt.constrainTo(self.hipsCtrl_link)
            #self.pelvisOutputConstraint = self.pelvisOutputTgt.constrainTo(self.pelvisCtrlSpace_link)
        else:     # Constraint outputs
            self.hipsOutputConstraint = self.hipsOutputTgt.constrainTo(self.hipsCtrl)
            #self.pelvisOutputConstraint = self.pelvisOutputTgt.constrainTo(self.pelvisCtrlSpace)


        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()

        for i in xrange(len(self.spineOutputs)):
            constraint = self.deformerJoints[i].constrainTo(self.spineOutputs[i])
            constraint.evaluate()


        #self.spineEndOutputTgt.xfo = Xfo(self.spineOutputs[-1].xfo)


        self.chestIKOp = self.blend_two_xfos(
            self.upChestCtrlResult,
            self.upChestCtrl, self.upChestIKRef,
            blendTranslate=0,
            blendRotate=self.chestIKAttr,
            blendScale=0,
            name='chestIKAttrOp')

        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.hipsCtrlSpaceConstraint.evaluate()
        self.torsoCtrlSpaceConstraint.evaluate()
        self.hipsOutputConstraint.evaluate()
        #self.spineBaseOutputConstraint.evaluate()
        #self.pelvisOutputConstraint.evaluate()
        self.spineEndOutputConstraint.evaluate()

        self.hipsOutputTgt.parentJoint = self.deformerJoints[0]
        self.pelvisOutputTgt.parentJoint = self.deformerJoints[0]
        self.spineEndOutputTgt.parentJoint = self.deformerJoints[-1]

        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


        chestIKVisAddAttr = self.createScalarAttribute(name="chestIKVisAdd", groupName="__vis__", kObject=self.upChestIKCtrl)
        self.addSolver = self.createSimpleMathSolver(self.chestAlignIkSpaceAttr, self.chestIKAttr, mode="ADD", output=chestIKVisAddAttr)
        visAttr = self.createScalarAttribute(name="chestIKVis", groupName="__vis__", kObject=self.upChestIKCtrl)
        self.aimVisConditionSolver = self.createConditionSolver(chestIKVisAddAttr, 1.0, 0.0, name="aimVis", result=visAttr)
        self.upChestIKCtrl.getVisibilityAttr().connect(visAttr, lock=True)
        self.upChestIKUpV.getVisibilityAttr().connect(visAttr, lock=True)

        # ====================
        # Extra Shape Mods
        # ====================
        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.hipsCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.torsoCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.chestCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.upChestCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], 1.0, data['globalComponentCtrlSize']))

        if self.mocap:
            self.hipsMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.pelvisMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.torsoMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.chestMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.upChestMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], 1.0, data['globalComponentCtrlSize']))

        self.evalOperators()
        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSpineComponentGuide)
ks.registerComponent(OSSSpineComponentRig)
