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
from kraken.core.objects.space import Space
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

        # =========
        # Controls
        # =========



        # hips
        self.hipsCtrl = FKControl('hips', parent=self.ctrlCmpGrp, shape="squarePointed")
        self.hipsCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.hipsCtrl.rotatePoints(0, -90.0, 0)
        self.hipsCtrl.scalePoints(Vec3(4.5, 3.0, 3.0))
        self.hipsSpace = self.hipsCtrl.insertSpace()

        # Pelvis
        self.pelvisSpace = Space('pelvis', parent=self.hipsCtrl)
        # self.pelvisCtrl = Control('pelvis', parent=self.pelvisSpace, shape="cube")
        # self.pelvisCtrl.setColor("green")
        # self.pelvisCtrl.scalePoints(Vec3(1, 1, 1))

        # Torso
        self.torsoCtrl = FKControl('torso', parent=self.ctrlCmpGrp, shape="squarePointed")
        self.torsoCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.torsoCtrl.rotatePoints(0, -90.0, 0)
        self.torsoCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.torsoSpace = self.torsoCtrl.insertSpace()


        # Chest
        self.chestCtrl = FKControl('chest', parent=self.torsoCtrl, shape="squarePointed")
        self.chestCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.chestCtrl.rotatePoints(0, -90.0, 0)
        self.chestCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.chestSpace = self.chestCtrl.insertSpace()

        # UpChest
        self.upChestCtrl = FKControl('upChest', parent=self.chestCtrl, shape="squarePointed")
        self.upChestCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZYX"])  #Set with component settings later
        self.upChestCtrl.rotatePoints(0, -90.0, 0)
        self.upChestCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.upChestSpace = self.upChestCtrl.insertSpace()
        self.upChestCtrlResult = Transform('upChest_result', parent=self.ctrlCmpGrp)
        self.upChestCtrlResult.xfo = self.upChestCtrl.xfo


        # chest Aim
        chestNeckSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.upChestCtrl)
        self.chestAlignToWorldSpaceAttr = ScalarAttribute('alignToWorld', value=0.0, minValue=0.0, maxValue=1.0, parent=chestNeckSettingsAttrGrp)
        self.chestAlignIkSpaceAttr = ScalarAttribute('alignToChestIK', value=0.0, minValue=0.0, maxValue=1.0, parent=chestNeckSettingsAttrGrp)
        self.chestIKAttr = ScalarAttribute('chestIK', value=0.0, minValue=0.0, maxValue=1.0, parent=chestNeckSettingsAttrGrp)


        self.chestWorldRef = Space('chestWorldRef', parent=self.ctrlCmpGrp)
        self.chestFKToWorldRef = Space(self.getName()+'FKToWorldRef', parent=self.ctrlCmpGrp)
        self.chestFKRef = Space('chestFKRef', parent=self.chestCtrl)
        self.upChestIKRef = Space('upChestIKRef', parent=self.ctrlCmpGrp)
        self.upChestIKSpace = Space('upChestIK', parent=self.ctrlCmpGrp)
        self.upChestIKCtrl = IKControl('chest', parent=self.upChestIKSpace, shape="square")
        self.upChestIKCtrl.setColor('red')
        self.upChestIKCtrl.rotatePoints(90,0,0)
        self.upChestIKCtrl.scalePoints(Vec3(3,3,3))
        self.upChestIKCtrl.lockScale(x=True, y=True, z=True)
        self.upChestIKCtrl.lockRotation(x=True, y=True, z=True)

        self.upChestIKUpVSpace = Space('chestUpV', parent=self.globalSRTInputTgt)
        self.upChestIKUpV = Control('chestUpV', parent=self.upChestIKUpVSpace, shape="circle")
        self.upChestIKUpV.scalePoints(Vec3(3,3,3))
        self.upChestIKUpV.lockScale(x=True, y=True, z=True)
        self.upChestIKUpV.lockRotation(x=True, y=True, z=True)

        # Neck
        self.spineNeckSpace = Space('spineNeck', parent=self.ctrlCmpGrp)
        self.spineNeckSpace.constrainTo(self.upChestCtrlResult, maintainOffset=True)


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
        self.hipsSpaceConstraint = self.hipsSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.torsoSpaceConstraint = self.torsoSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

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

        self.pelvisSpace.xfo.tr = pelvisPosition

        self.hipsSpace.xfo.tr = torsoPosition
        self.hipsCtrl.xfo.tr = torsoPosition


        self.torsoSpace.xfo.tr = torsoPosition
        self.torsoCtrl.xfo.tr = torsoPosition

        self.chestSpace.xfo.tr = chestPosition
        self.chestCtrl.xfo.tr = chestPosition

        self.upChestSpace.xfo.tr = upChestPosition
        self.upChestCtrl.xfo.tr = upChestPosition

        self.spineNeckSpace.xfo.tr = neckPosition
        # self.neckCtrl.xfo.tr = neckPosition

        # Chest LookAt/Aim Controls
        self.chestFKRef.xfo = self.upChestSpace.xfo
        length = upChestPosition.distanceTo(torsoPosition) * 3
        self.upChestIKSpace.xfo.ori = self.upChestSpace.xfo.ori
        self.upChestIKSpace.xfo.tr = self.upChestSpace.xfo.tr.add(Vec3(0, 0, length))
        self.upChestIKCtrl.xfo = self.upChestIKSpace.xfo

        self.upChestIKUpV.xfo.ori = self.upChestSpace.xfo.ori
        self.upChestIKUpV.xfo.tr = self.upChestSpace.xfo.tr.add(Vec3(0, length, 0))

        # Do we want this to be world up or hips up?
        self.chestIKUpVSpaceConstraint = self.upChestIKUpVSpace.constrainTo(self.hipsCtrl, maintainOffset=True)

        # Add Aim Op
        self.chestAimKLOp = KLOperator('chestAimKLOp', 'OSS_AimKLSolver', 'OSS_Kraken')
        self.addOperator(self.chestAimKLOp)

        # Add Att Inputs
        self.chestAimKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.chestAimKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.chestAimKLOp.setInput('blend',  1)
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

        self.upChestSpace.setParent(self.ctrlCmpGrp)

        self.alignchestToIKOp = self.blend_two_xfos(
            self.upChestSpace,
            self.chestFKToWorldRef, self.upChestIKRef,
            blendTranslate=0,
            blendRotate=self.chestAlignIkSpaceAttr,
            blendScale=0,
            name='alignchestToIKOp')



        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        self.pelvisHeight = pelvisPosition.subtract(torsoPosition)
        self.hipsCtrl.translatePoints( self.pelvisHeight - Vec3(0,2,0))

        self.controlInputs.append(self.pelvisSpace)
        self.controlInputs.append(self.torsoCtrl)
        self.controlInputs.append(self.chestCtrl)
        self.controlInputs.append(self.upChestCtrlResult)
        self.controlInputs.append(self.spineNeckSpace)

        self.controlRestInputs.append(self.pelvisSpace.xfo)
        self.controlRestInputs.append(self.torsoCtrl.xfo)
        self.controlRestInputs.append(self.chestCtrl.xfo)
        self.controlRestInputs.append(self.upChestCtrlResult.xfo)
        self.controlRestInputs.append(self.spineNeckSpace.xfo)

        self.rigidMat44s.append(self.controlInputs[0])
        self.rigidMat44s.append(self.controlInputs[-1])
        self.rigidAligns.append(Vec3(-2,1,3))
        self.rigidAligns.append(Vec3(-2,1,3))


        # Constrain Outputs
        self.spineEndOutputConstraint = self.spineEndOutputTgt.constrainTo(self.spineOutputs[-1])
        self.hipsOutputConstraint = self.hipsOutputTgt.constrainTo(self.hipsCtrl)


        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()

        for i in xrange(len(self.spineOutputs)):
            constraint = self.deformerJoints[i].constrainTo(self.spineOutputs[i])
            constraint.evaluate()


        #self.spineEndOutputTgt.xfo = self.spineOutputs[-1].xfo


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
        self.hipsSpaceConstraint.evaluate()
        self.torsoSpaceConstraint.evaluate()
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

        self.evalOperators()
        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSpineComponentGuide)
ks.registerComponent(OSSSpineComponentRig)
