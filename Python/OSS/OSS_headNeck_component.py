from kraken.core.maths import Vec3
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.euler import rotationOrderStrToIntMapping

from kraken.core.objects.components.base_example_component import BaseExampleComponent

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
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *

COMPONENT_NAME = "headNeck"

class OSSHeadNeckComponent(BaseExampleComponent):
    """Neck Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSHeadNeckComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.neckBaseOutputTgt = self.createOutput('neckBase', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.neckEndOutputTgt = self.createOutput('neckEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.neckVertebraeOutput = self.createOutput('neckVertebrae', dataType='Xfo[]')

        # Declare Input Attrs
        self.buildWithCanvasOps = self.createInput('buildWithCanvasOps', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)

class OSSHeadNeckComponentGuide(OSSHeadNeckComponent):
    """Neck Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct HeadNeck Guide Component:" + name)
        super(OSSHeadNeckComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # ========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        # Guide Controls
        self.neckHandleCtrl = Control('neckHandlePosition', parent=self.ctrlCmpGrp, shape='null')
        self.neckCtrl = Control('neckPosition', parent=self.ctrlCmpGrp, shape='circle')
        self.neckCtrl.scalePoints(Vec3(2, 2, 2))
        self.neckCtrl.setColor('red')
        self.headCtrl = Control('headPosition', parent=self.ctrlCmpGrp, shape='cube')
        self.headHandleCtrl = Control('headHandlePosition', parent=self.ctrlCmpGrp, shape='null')
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        self.numDeformersAttr = IntegerAttribute('numDeformers', value=4, minValue=0, maxValue=20, parent=guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
        self.mocapInputAttr = None

        data = {
            'name': name,
            'location': 'M',
            'neckPosition': Vec3(0.0, 15, 0),
            'neckHandlePosition': Vec3(0.0, 15.25, 0),
            'headHandlePosition': Vec3(0.0, 17.75, 0),
            'headPosition': Vec3(0.0, 18, 0),
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

        data = super(OSSHeadNeckComponentGuide, self).saveData()

        data['neckPosition'] = self.neckCtrl.xfo.tr
        data['neckHandlePosition'] = self.neckHandleCtrl.xfo.tr
        data['headHandlePosition'] = self.headHandleCtrl.xfo.tr
        data['headPosition'] = self.headCtrl.xfo.tr

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

        super(OSSHeadNeckComponentGuide, self).loadData( data )

        self.neckCtrl.xfo.tr = data["neckPosition"]
        self.neckHandleCtrl.xfo.tr = data["neckHandlePosition"]
        self.headHandleCtrl.xfo.tr = data["headHandlePosition"]
        self.headCtrl.xfo.tr = data["headPosition"]

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.neckCtrl.scalePoints(globalScaleVec)
        self.headCtrl.scalePoints(globalScaleVec)

        return True


    def updateMocap(self, mocap):
        """ Callback to changing the component setting 'useOtherIKGoalInput'
        Really, we should build this ability into the system, to add/remove input attrs based on guide setting bools.
        That way, we don't have to write these callbacks.
        """
        if mocap:
            if self.mocapInputAttr is None:
                self.mocapInputAttr = self.createInput('mocap', dataType='Float', parent=self.cmpInputAttrGrp)

        else:
            if self.mocapInputAttr is not None:
                self.deleteInput('mocap', parent=self.cmpInputAttrGrp)
                self.mocapInputAttr = None


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSHeadNeckComponentGuide, self).getRigBuildData()

        data['neckPosition'] = self.neckCtrl.xfo.tr
        data['neckHandlePosition'] = self.neckHandleCtrl.xfo.tr
        data['headHandlePosition'] = self.headHandleCtrl.xfo.tr
        data['headPosition'] = self.headCtrl.xfo.tr
        data['numDeformers'] = self.numDeformersAttr.getValue()

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

        return OSSHeadNeckComponentRig


class OSSHeadNeckComponentRig(OSSHeadNeckComponent):
    """Neck Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Neck Rig Component:" + name)
        super(OSSHeadNeckComponentRig, self).__init__(name, parent)

        self.mocap = False
        # =========
        # Controls
        # =========
        # COG

        # Neck
        self.neckCtrl = FKControl('neck', parent=self.ctrlCmpGrp, shape="square")
        self.neckCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["ZYX"])  #Set with component settings later
        self.neckCtrl.scalePoints(Vec3(2.5, 2.5, 2.5))
        self.neckCtrlSpace = self.neckCtrl.insertCtrlSpace()

        # Neck handle
        self.neckHandleCtrlSpace = CtrlSpace('neckHandle', parent=self.neckCtrlSpace)

        # Head
        self.headCtrl = FKControl('head', parent=self.neckCtrl, shape="square")
        self.headCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["XZY"])  #Set with component settings later
        #self.headCtrl.rotatePoints(0, 0, 90)
        self.headCtrl.scalePoints(Vec3(6.0, 6.0, 6.0))
        self.headCtrlSpace  = self.headCtrl.insertCtrlSpace()

        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.headCtrl)
        self.HeadAlignFkSpaceAttr = ScalarAttribute('headFK', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        self.HeadAlignIkSpaceAttr = ScalarAttribute('headIK', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        self.HeadAlignWorldSpaceAttr = ScalarAttribute('headWorld', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)

        # Head handle
        self.headAlignSpace = CtrlSpace('headAlign', parent=self.headCtrl)
        self.headHandleCtrlSpace = CtrlSpace('headHandle', parent=self.headAlignSpace)


        # Head Aim
        self.headSpace = CtrlSpace('head', parent=self.globalSRTInputTgt)
        self.headIKCtrlSpace = CtrlSpace('headIK', parent=self.globalSRTInputTgt)
        self.headIKCtrl = IKControl('head', parent=self.headIKCtrlSpace, shape="square")
        self.headIKCtrl.setColor('red')
        self.headIKCtrl.rotatePoints(90,0,0)
        self.headIKCtrl.lockScale(x=True, y=True, z=True)
        self.headIKCtrl.lockRotation(x=True, y=True, z=True)

        self.headIKUpVSpace = CtrlSpace('headUpV', parent=self.globalSRTInputTgt)
        self.headIKUpV = Control('headUpV', parent=self.headIKUpVSpace, shape="circle")
        self.headIKUpV.lockScale(x=True, y=True, z=True)
        self.headIKUpV.lockRotation(x=True, y=True, z=True)


        self.headWorldCtrl = IKControl('headWorld', parent=self.globalSRTInputTgt, shape="square")
        self.headWorldCtrl.setColor('blue')
        self.headWorldCtrl.scalePoints(Vec3(7.0, 7.0, 7.0))
        self.headWorldCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["XZY"])  #Set with component settings later
        self.headWorldCtrlSpace  = self.headWorldCtrl.insertCtrlSpace()


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.addItem("defCmpGrp", self.defCmpGrp)
        self.deformerJoints = []
        self.neckOutputs = []
        self.setNumDeformers(1)

        self.controlInputs = []
        self.controlRestInputs = []

        self.alignSpaces = []
        self.alignWeights = []

        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.neckVertebraeOutput.setTarget(self.neckOutputs)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.neckCtrlSpaceConstraint = self.neckCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.headIKUpVSpaceConstraint = self.headIKUpVSpace.constrainTo(self.headCtrl, constraintType="Position", maintainOffset=True)

        self.headWorldSpaceConstraint = self.headWorldCtrlSpace.constrainTo(self.headCtrl, constraintType="Position", maintainOffset=True)



        # ===============
        # Add Fabric Ops
        # ===============
        # Add Neck Canvas Op
        self.NURBSNeckKLOp = KLOperator('NURBSNeckKLOp', 'OSS_NURBSSpineKLSolver', 'OSS_Kraken')

        self.addOperator(self.NURBSNeckKLOp)

        self.NURBSNeckKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.NURBSNeckKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.NURBSNeckKLOp.setInput('numDeformers',  1)
        self.NURBSNeckKLOp.setInput('compressionAmt', 0)
        self.NURBSNeckKLOp.setInput('controls', self.controlInputs)
        self.NURBSNeckKLOp.setInput('controlsRest', self.controlRestInputs)
        self.NURBSNeckKLOp.setOutput('outputs', self.neckOutputs)
        self.buildWithCanvasOps = False
        if self.buildWithCanvasOps:
            # ===============
            # Add Fabric Ops
            # ===============
            # Add Spine Canvas Op
            self.HeadAlignCanvasOp = CanvasOperator('HeadAlignCanvasOp', 'OSS.Solvers.AlignSolver')
            self.addOperator(self.HeadAlignCanvasOp)

            # Add Att Inputs
            self.HeadAlignCanvasOp.setInput('drawDebug', self.drawDebugInputAttr)
            self.HeadAlignCanvasOp.setInput('rigScale', self.rigScaleInputAttr)
            self.HeadAlignCanvasOp.setInput('translationAmt',  0)
            self.HeadAlignCanvasOp.setInput('rotationAmt',  1)
            self.HeadAlignCanvasOp.setInput('scaleAmt',  0)
            self.HeadAlignCanvasOp.setInput('atAxis',  0)
            self.HeadAlignCanvasOp.setInput('upAxis',  1)
            self.HeadAlignCanvasOp.setInput('mat44Parent',  self.headCtrl)

            self.HeadAlignCanvasOp.setInput('spaces', self.alignSpaces)
            self.HeadAlignCanvasOp.setInput('spaceWeights', self.alignWeights)

            self.HeadAlignCanvasOp.setOutput('result', self.headAlignSpace)


            # Add Aim Splice Op
            # =================
            # self.headIKCanvasOp = KLOperator('headIKCanvasOp', 'DirectionConstraintSolver', 'Kraken')
            self.headIKCanvasOp = CanvasOperator('headIKCanvasOp', 'Kraken.Solvers.DirectionConstraintSolver')
            self.addOperator(self.headIKCanvasOp)

            # Add Att Inputs
            self.headIKCanvasOp.setInput('drawDebug', self.drawDebugInputAttr)
            self.headIKCanvasOp.setInput('rigScale', self.rigScaleInputAttr)

            # Add Xfo Inputs
            self.headIKCanvasOp.setInput('position', self.headCtrl)
            self.headIKCanvasOp.setInput('upVector', self.headIKUpV)
            self.headIKCanvasOp.setInput('atVector', self.headIKCtrl)

            # Add Xfo Outputs
            self.headIKCanvasOp.setOutput('constrainee', self.headSpace)


        # Add Deformer Splice Op
        self.deformersToOutputsKLOp = KLOperator('neckDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.deformersToOutputsKLOp)

        # Add Att Inputs
        self.deformersToOutputsKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.deformersToOutputsKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setInput('constrainers', self.neckOutputs)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setOutput('constrainees', self.deformerJoints)



        Profiler.getInstance().pop()


    def setNumDeformers(self, numDeformers):

        for output in reversed(self.neckOutputs):
            output.getParent().removeChild(output)
        del self.neckOutputs[:] #Clear since this array obj is tied to output already

        for joint in reversed(self.deformerJoints):
            joint.getParent().removeChild(joint)
        del self.deformerJoints[:] #Clear since this array obj is tied to output already

        # Add new deformers and outputs
        for i in xrange(numDeformers):
            name = 'neck' + str(i + 1).zfill(2)
            neckOutput = ComponentOutput(name, parent=self.outputHrcGrp)
            self.neckOutputs.append(neckOutput)

        for i in xrange(numDeformers):

            if i == numDeformers-1:
                name = 'head'
            else:
                name = 'neck' + str(i + 1).zfill(2)
            neckDef = Joint(name, parent=self.defCmpGrp)
            neckDef.setComponent(self)

            self.deformerJoints.append(neckDef)

        if hasattr(self, 'NURBSNeckKLOp'):  # Check in case this is ever called from Guide callback
            self.NURBSNeckKLOp.setInput('numDeformers',  numDeformers)

        return True


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSHeadNeckComponentRig, self).loadData( data )

        neckPosition = data['neckPosition']
        neckHandlePosition = data['neckHandlePosition']
        headHandlePosition = data['headHandlePosition']
        headPosition = data['headPosition']
        numDeformers = data['numDeformers']

        self.mocap = bool(data["mocap"])

        self.neckCtrlSpace.xfo.tr = neckPosition
        self.neckCtrl.xfo.tr = neckPosition
        self.neckHandleCtrlSpace.xfo.tr = neckHandlePosition
        self.headHandleCtrlSpace.xfo.tr = headHandlePosition
        self.headCtrlSpace.xfo.tr = headPosition
        self.headAlignSpace.xfo.tr = headPosition
        self.headCtrl.xfo.tr = headPosition

        self.headWorldCtrlSpace.xfo.tr = headPosition
        self.headWorldCtrl.xfo.tr = headPosition

        # Head LookAt/Aim Controls
        self.headIKCtrlSpace.xfo.ori = self.headCtrlSpace.xfo.ori
        self.headIKCtrlSpace.xfo.tr = self.headCtrlSpace.xfo.tr.add(Vec3(0, 0, 30))
        self.headIKCtrl.xfo = self.headIKCtrlSpace.xfo

        self.headIKUpV.xfo.ori = self.headCtrlSpace.xfo.ori
        self.headIKUpV.xfo.tr = self.headCtrlSpace.xfo.tr.add(Vec3(0, 30, 0))

        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        self.controlInputs.append(self.neckCtrl)
        self.controlInputs.append(self.neckHandleCtrlSpace)
        self.controlInputs.append(self.headHandleCtrlSpace)
        self.controlInputs.append(self.headAlignSpace)

        self.controlRestInputs.append(self.neckCtrl.xfo)
        self.controlRestInputs.append(self.neckHandleCtrlSpace.xfo)
        self.controlRestInputs.append(self.headHandleCtrlSpace.xfo)
        self.controlRestInputs.append(self.headAlignSpace.xfo)


        self.alignSpaces.append(self.headCtrl)
        self.alignSpaces.append(self.headSpace)
        self.alignSpaces.append(self.headWorldCtrl)

        self.alignWeights.append(self.HeadAlignFkSpaceAttr)
        self.alignWeights.append(self.HeadAlignIkSpaceAttr)
        self.alignWeights.append(self.HeadAlignWorldSpaceAttr)


        if self.mocap:

            self.mocapInputAttr = self.createInput('mocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()


            self.neckCtrlSpace.xfo.tr = neckPosition
            self.neckCtrl.xfo.tr = neckPosition
            self.neckHandleCtrlSpace.xfo.tr = neckHandlePosition
            self.headHandleCtrlSpace.xfo.tr = headHandlePosition
            self.headCtrlSpace.xfo.tr = headPosition
            self.headCtrl.xfo.tr = headPosition


            # Neck
            self.neckMocapCtrl = MCControl('neck', parent=self.ctrlCmpGrp, shape="circle")
            self.neckMocapCtrl.scalePoints(Vec3(5.0, 5.0, 5.0))
            self.neckMocapCtrl.setColor("purpleLight")
            self.neckMocapCtrl.xfo.tr = neckPosition

            self.neckMocapCtrlSpace = self.neckMocapCtrl.insertCtrlSpace()
            self.neckMocapCtrlSpaceConstraint = self.neckMocapCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

            # Neck handle
            self.neckHandleMocapCtrlSpace = CtrlSpace('neckHandle', parent=self.neckMocapCtrlSpace)
            self.neckHandleMocapCtrlSpace.xfo.tr = neckHandlePosition

            # Head
            self.headMocapCtrl = MCControl('head', parent=self.neckMocapCtrl, shape="circle")
            self.headMocapCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
            self.headMocapCtrl.setColor("purpleLight")
            self.headMocapCtrl.xfo.tr = headPosition

            self.headMocapCtrlSpace = self.headMocapCtrl.insertCtrlSpace()

            # Head handle
            self.headHandleMocapCtrlSpace = CtrlSpace('headHandle_mocap', parent=self.headMocapCtrl)
            self.headHandleMocapCtrlSpace.xfo.tr = headHandlePosition

            # Blend anim and mocap together
            self.mocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'mocap_HierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.mocapHierBlendSolver)
            self.mocapHierBlendSolver.setInput('blend', self.mocapInputAttr)  # connect this to attr
            # Add Att Inputs
            self.mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            self.mocapHierBlendSolver.setInput('hierA',
                [
                self.neckCtrl,
                self.neckHandleCtrlSpace,
                self.headCtrl,
                self.headHandleCtrlSpace,
                ],
            )

            self.mocapHierBlendSolver.setInput('hierB',
                [
                self.neckMocapCtrl,
                self.neckHandleMocapCtrlSpace,
                self.headMocapCtrl,
                self.headHandleMocapCtrlSpace
                ]
            )
            self.mocapHierBlendSolver.setInput('parentIndexes', [-1, 0, 0, 2])

            #Create some nodes just for the oupt of the blend.
            #Wish we could just make direct connections....

            self.neckCtrlSpace_link = CtrlSpace('neckCtrlSpace_link', parent=self.outputHrcGrp)
            self.neckHandleCtrlSpace_link = CtrlSpace('neckHandleCtrlSpace_link', parent=self.outputHrcGrp)
            self.headCtrlSpace_link = CtrlSpace('headCtrlSpace_link', parent=self.outputHrcGrp)
            self.headHandleCtrlSpace_link = CtrlSpace('headHandleCtrlSpace_link', parent=self.outputHrcGrp)


            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.neckCtrlSpace_link,
                self.neckHandleCtrlSpace_link,
                self.headCtrlSpace_link,
                self.headHandleCtrlSpace_link
                ]
            )
            self.mocapHierBlendSolver.evaluate()

            # Add Xfo Outputs
            self.NURBSNeckKLOp.setInput('neck', self.neckCtrlSpace_link)
            self.NURBSNeckKLOp.setInput('head', self.headCtrlSpace_link)
            self.NURBSNeckKLOp.setInput('neckHandle', self.neckHandleCtrlSpace_link)
            self.NURBSNeckKLOp.setInput('headHandle', self.headHandleCtrlSpace_link)

        self.neckBaseOutputConstraint = self.neckBaseOutputTgt.constrainTo(self.neckOutputs[0])
        self.neckEndOutputConstraint = self.neckEndOutputTgt.constrainTo(self.neckOutputs[-1])

        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.NURBSNeckKLOp.evaluate()

        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.neckBaseOutputConstraint.evaluate()
        self.neckEndOutputConstraint.evaluate()
        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])


        self.headCtrl.rotatePoints(-90, 0, 0)
        self.headCtrl.translatePoints(Vec3(0, 1.5, 0.0))
        self.neckCtrl.scalePoints(globalScale)
        self.headCtrl.scalePoints(globalScale)

        self.headWorldCtrl.rotatePoints(-90, 0, 0)
        self.headWorldCtrl.translatePoints(Vec3(0, 1.5, 0.0))
        self.headWorldCtrl.scalePoints(globalScale)

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSHeadNeckComponentGuide)
ks.registerComponent(OSSHeadNeckComponentRig)
