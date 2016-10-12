from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV, aimAt
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
from kraken.core.objects.locator import Locator

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "headNeck"

class OSSHeadNeckComponent(OSS_Component):
    """Neck Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSHeadNeckComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.worldSRTInputTgt = self.createInput('worldSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.neckBaseOutputTgt = self.createOutput('neckBase', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.headOutputTgt = self.createOutput('head', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.neckVertebraeOutput = self.createOutput('neckVertebrae', dataType='Xfo[]')


class OSSHeadNeckComponentGuide(OSSHeadNeckComponent):
    """Neck Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct HeadNeck Guide Component:" + name)
        super(OSSHeadNeckComponentGuide, self).__init__(name, parent)

        self.constrainBaseToControl = BoolAttribute('constrainBaseToControl', value=False, parent=self.guideSettingsAttrGrp)
        self.constrainEndToControl = BoolAttribute('constrainEndToControl', value=False, parent=self.guideSettingsAttrGrp)

        # =========
        # Controls
        # ========
        # Guide Controls
        self.neckHandleCtrl = Control('neckHandlePosition', parent=self.ctrlCmpGrp, shape='null')
        self.neckCtrl = Control('neckPosition', parent=self.ctrlCmpGrp, shape='circle')
        self.neckCtrl.scalePoints(Vec3(2, 2, 2))
        self.neckCtrl.setColor('red')
        self.headCtrl = Control('headPosition', parent=self.ctrlCmpGrp, shape='cube')
        self.headHandleCtrl = Control('headHandlePosition', parent=self.ctrlCmpGrp, shape='null')

        self.numDeformersAttr = IntegerAttribute('numDeformers', value=4, minValue=0, maxValue=20, parent=self.guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        #self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
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
        for ctrl in self.getHierarchyNodes(classType="Control"):
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
        self.neckCtrl = FKControl('neck', parent=self.ctrlCmpGrp, shape="square", scale=2.5)
        self.neckCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["ZYX"])  #Set with component settings later
        self.neckCtrlSpace = self.neckCtrl.insertCtrlSpace()

        # Head
        self.headCtrl = FKControl('head', parent=self.neckCtrl, shape="halfCircle", scale=2)
        self.headCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["XZY"])  #Set with component settings later
        self.headCtrlSpace  = self.headCtrl.insertCtrlSpace()



        self.neckMidCtrl = FKControl('neckMid', parent=self.neckCtrl, shape="circle", scale=6)
        self.neckMidCtrl.ro = RotationOrder(rotationOrderStrToIntMapping["XZY"])  #Set with component settings later
        #self.headCtrl.rotatePoints(0, 0, 90)
        self.neckMidCtrlSpace  = self.neckMidCtrl.insertCtrlSpace()


        # Neck handle
        self.neckHandleCtrlSpace = CtrlSpace('neckHandle', parent=self.neckMidCtrl)
        # Head handle
        self.headHandleCtrlSpace = CtrlSpace('headHandle', parent=self.neckMidCtrl)

        headNeckSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.headCtrl)
        self.headAlignToWorldSpaceAttr = ScalarAttribute('alignToWorld', value=0.0, minValue=0.0, maxValue=1.0, parent=headNeckSettingsAttrGrp)
        self.HeadAlignIkSpaceAttr = ScalarAttribute('headIK', value=0.0, minValue=0.0, maxValue=1.0, parent=headNeckSettingsAttrGrp)


        # Head Aim
        self.headSpace = CtrlSpace('head', parent=self.globalSRTInputTgt)
        self.headWorldRef  = CtrlSpace('headWorldRef', parent=self.ctrlCmpGrp)
        self.headFKToWorldRef  = CtrlSpace('FKToWorldRef', parent=self.neckCtrl)
        self.headFKRef  = CtrlSpace('headFKRef', parent=self.neckCtrl)
        self.headIKRef = CtrlSpace('headIKRef', parent=self.neckCtrl)
        self.headIKCtrlSpace = CtrlSpace('headIK', parent=self.ctrlCmpGrp)
        self.headIKCtrl = IKControl('head', parent=self.headIKCtrlSpace, shape="square")
        self.headIKCtrl.setColor('red')
        self.headIKCtrl.rotatePoints(90,0,0)
        self.headIKCtrl.lockScale(x=True, y=True, z=True)
        self.headIKCtrl.lockRotation(x=True, y=True, z=True)

        self.headIKUpVSpace = CtrlSpace('headUpV', parent=self.globalSRTInputTgt)
        self.headIKUpV = Control('headUpV', parent=self.headIKUpVSpace, shape="circle")
        self.headIKUpV.lockScale(x=True, y=True, z=True)
        self.headIKUpV.lockRotation(x=True, y=True, z=True)


        # ==========
        # Deformers
        # ==========
        self.deformerJoints = []
        self.neckOutputs = []
        #self.setNumDeformers(1)

        self.controlInputs = []
        self.controlRestInputs = []

        self.alignSpaces = []
        self.alignWeights = []
        self.params = []
        self.rigControlAligns = []

        self.rigidIDs = []
        self.rigidMat44s = []
        self.rigidAligns = []

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
        self.headIKUpVSpaceConstraint = self.headIKUpVSpace.constrainTo(self.headFKRef, constraintType="Position", maintainOffset=True)




        # ===============
        # Add Fabric Ops
        # ===============
        # Add Neck Canvas Op
        self.NURBSNeckKLOp = KLOperator('NURBSNeckKLOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')

        self.addOperator(self.NURBSNeckKLOp)

        self.NURBSNeckKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.NURBSNeckKLOp.setInput('drawDebug', self.drawDebugInputAttr)

        self.NURBSNeckKLOp.setInput('alignX', 1 )
        self.NURBSNeckKLOp.setInput('alignY', 2 )
        self.NURBSNeckKLOp.setInput('alignZ', 3 )
        self.NURBSNeckKLOp.setInput('degree', 3)
        self.NURBSNeckKLOp.setInput('keepArcLength', 0.0)
        self.NURBSNeckKLOp.setInput('compressionAmt', 0)
        self.NURBSNeckKLOp.setInput('followCurveTangent', 1.0)
        self.NURBSNeckKLOp.setInput('followCurveNormal', 1.0)
        self.NURBSNeckKLOp.setInput('useLocalNormal', 0.0)
        self.NURBSNeckKLOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.NURBSNeckKLOp.setInput('parent', self.ctrlCmpGrp)
        # atVec should be optional
        self.NURBSNeckKLOp.setInput('atVec', self.ctrlCmpGrp)
        self.NURBSNeckKLOp.setInput('controlAligns', self.rigControlAligns)
        self.NURBSNeckKLOp.setInput('controls', self.controlInputs)
        self.NURBSNeckKLOp.setInput('controlsRest', self.controlRestInputs)
        self.NURBSNeckKLOp.setInput('rigidIDs', [0,5])
        self.NURBSNeckKLOp.setInput('rigidMat44s', self.rigidMat44s)
        self.NURBSNeckKLOp.setInput('rigidAligns', self.rigidAligns)

        self.NURBSNeckKLOp.setInput('params', self.params )
        self.NURBSNeckKLOp.setOutput('outputs', self.neckOutputs)

        # ===============
        # Add Fabric Ops
        # ===============

        # Add Spine Canvas Op
        self.HeadAimKLOp = KLOperator('HeadAimKLOp', 'OSS_AimKLSolver', 'OSS_Kraken')
        self.addOperator(self.HeadAimKLOp)

        # Add Att Inputs
        self.HeadAimKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.HeadAimKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.HeadAimKLOp.setInput('blend',  0)

        self.HeadAimKLOp.setInput('rest', self.headFKRef)
        self.HeadAimKLOp.setInput('ik', self.headIKCtrl)
        # Add Xfo Inputs
        self.HeadAimKLOp.setInput('up', self.headIKUpV)
        self.HeadAimKLOp.setOutput('result', self.headIKRef)



        # Add Spine Canvas Op
        # Add Att Inputs
        self.alignHeadToWorldOp = self.blend_two_xfos(
            self.headFKToWorldRef,
            self.headFKRef, self.headWorldRef,
            parentSpace = self.neckCtrl,
            blendTranslate=0,
            blendRotate=self.headAlignToWorldSpaceAttr,
            blendScale=0,
            name= 'alignHeadToWorldOp')


        self.alignHeadToIKOp = self.blend_two_xfos(
            self.headCtrlSpace,
            self.headFKToWorldRef, self.headIKRef,
            parentSpace = self.neckCtrl,
            blendTranslate=0,
            blendRotate=self.HeadAlignIkSpaceAttr,
            blendScale=0,
            name= 'alignHeadToIKOp')


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
            #Need dynamic ports branch to be able to see this updated in Graph
            neckOutput = self.createOutput(name, dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            self.neckOutputs.append(neckOutput)

        parent = self.deformersParent
        for i in xrange(numDeformers):
            if i == numDeformers-1:
                name = 'head'
            else:
                name = 'neck' + str(i + 1).zfill(2)
            if i > 0:
                parent = self.deformerJoints[-1]
            neckDef = Joint(name, parent=parent)
            neckDef.setComponent(self)
            self.deformerJoints.append(neckDef)
            if i == 0:
                self.parentSpaceInputTgt.childJoints = [neckDef]

        # Determine params for number of Deformers
        a = 0.0
        b = 1.0
        for i in range(numDeformers):
            ratio = float(i) / float(numDeformers-1)
            self.params.append((1.0-ratio)*a + ratio*b)
            self.rigControlAligns.append(Vec3(1,2,3))
        if hasattr(self, 'NURBSNeckKLOp'):  # Check in case this is ever called from Guide callback
            self.NURBSNeckKLOp.setInput('params',  self.params)


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
        self.headCtrl.xfo.tr = headPosition
        self.headIKRef.xfo.tr = headPosition
        self.headFKRef.xfo.tr = headPosition
        self.headFKToWorldRef.xfo.tr = headPosition
        self.headWorldRef.xfo.tr = headPosition

        neckMidXfo = self.neckHandleCtrlSpace.xfo.linearInterpolate(self.headHandleCtrlSpace.xfo, 0.5)
        self.neckMidCtrlSpace.xfo = neckMidXfo
        self.neckMidCtrl.xfo = neckMidXfo

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
        self.controlInputs.append(self.headCtrl)

        self.controlRestInputs.append(self.neckCtrl.xfo)
        self.controlRestInputs.append(self.neckHandleCtrlSpace.xfo)
        self.controlRestInputs.append(self.headHandleCtrlSpace.xfo)
        self.controlRestInputs.append(self.headCtrl.xfo)

        self.rigidMat44s.append(self.controlInputs[0])
        self.rigidMat44s.append(self.controlInputs[-1])
        self.rigidAligns.append(Vec3(-2,1,3))
        self.rigidAligns.append(Vec3(-2,1,3))


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
            self.neckMocapCtrl.setColor("mediumpurple")
            self.neckMocapCtrl.xfo.tr = neckPosition

            self.neckMocapCtrlSpace = self.neckMocapCtrl.insertCtrlSpace()
            self.neckMocapCtrlSpaceConstraint = self.neckMocapCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

            # Neck handle
            self.neckHandleMocapCtrlSpace = CtrlSpace('neckHandle', parent=self.neckMocapCtrlSpace)
            self.neckHandleMocapCtrlSpace.xfo.tr = neckHandlePosition

            # Head
            self.headMocapCtrl = MCControl('head', parent=self.neckMocapCtrl, shape="circle")
            self.headMocapCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
            self.headMocapCtrl.setColor("mediumpurple")
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

       # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.NURBSNeckKLOp.evaluate()
        self.alignHeadToWorldOp.evaluate()
        self.alignHeadToIKOp.evaluate()

        self.neckBaseOutputTgt.constrainTo(self.neckOutputs[0]).evaluate()

        #self.headOutputConstraint = self.headOutputTgt.constrainTo(self.neckOutputs[-1])
        # We might want to put this as feature of operator.  Certainly this should be a blend...
        # self.headOutputTgt.xfo.tr = self.headCtrl.xfo.tr
        # aimAt(self.headOutputTgt.xfo, aimVector=Vec3(0, 1, 0), upVector=Vec3(0, 0, 1), aimAxis=(1, 0, 0), upAxis=(0, 0, 1))

        self.headOutputTgt.constrainTo(self.headCtrl, maintainOffset=True).evaluate()

        for i in xrange(len(self.neckOutputs)-1):
            constraint = self.deformerJoints[i].constrainTo(self.neckOutputs[i])
            constraint.evaluate()

        #Really
        #Hard-coded for now....
        self.deformerJoints[-1].xfo.tr = self.headCtrl.xfo.tr
        aimAt(self.deformerJoints[-1].xfo, aimVector=Vec3(0, 1, 0), upVector=Vec3(0, 0, 1), aimAxis=(1, 0, 0), upAxis=(0, 0, 1))
        self.deformerJoints[-1].constrainTo(self.headCtrl, maintainOffset=True).evaluate()

        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.

        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()

        self.neckBaseOutputTgt.parentJoint =  self.deformerJoints[0]
        self.headOutputTgt.parentJoint =  self.deformerJoints[-1]


        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.headCtrl.rotatePoints(-90, 0, 0)
        self.headCtrl.scalePoints(Vec3(1, -1, 1))
        self.headCtrl.translatePoints(Vec3(0.0, 2.25, 0.0))
        self.neckCtrl.translatePoints(Vec3(0.0, 1.0, 0.0))
        self.neckCtrl.scalePoints(globalScale)
        self.headCtrl.scalePoints(globalScale)

        self.headIKCtrl.getVisibilityAttr().connect(self.HeadAlignIkSpaceAttr, lock=True)
        self.headIKUpV.getVisibilityAttr().connect(self.HeadAlignIkSpaceAttr, lock=True)




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSHeadNeckComponentGuide)
ks.registerComponent(OSSHeadNeckComponentRig)
