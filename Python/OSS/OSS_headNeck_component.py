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
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.neckBaseOutputTgt = self.createOutput('neckBase', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.neckEndOutputTgt = self.createOutput('neckEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.neckVertebraeOutput = self.createOutput('neckVertebrae', dataType='Xfo[]')

        # Declare Input Attrs
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
        for ctrl in self.getAllHierarchyNodes(classType=Control):
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
        self.headCtrlSpace = self.headCtrl.insertCtrlSpace()

        # Head handle
        self.headHandleCtrlSpace = CtrlSpace('headHandle', parent=self.headCtrl)


        # ==========
        # Deformers
        # ==========

        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.deformerJoints = []
        self.neckOutputs = []
        self.setNumDeformers(1)


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




        # ===============
        # Add Fabric Ops
        # ===============
        # Add Neck Canvas Op
        self.ZSplineNeckCanvasOp = CanvasOperator('ZSplineNeckCanvasOp', 'OSS.Solvers.ZSplineNeckSolver')

        self.addOperator(self.ZSplineNeckCanvasOp)

        # Add Att Inputs
        self.ZSplineNeckCanvasOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.ZSplineNeckCanvasOp.setInput('rigScale', self.rigScaleInputAttr)
        self.ZSplineNeckCanvasOp.setInput('numDeformers',  1)
        # Add Xfo Inputs
        self.ZSplineNeckCanvasOp.setInput('neck', self.neckCtrl)
        self.ZSplineNeckCanvasOp.setInput('head', self.headCtrl)
        self.ZSplineNeckCanvasOp.setInput('neckHandle', self.neckHandleCtrlSpace)
        self.ZSplineNeckCanvasOp.setInput('headHandle', self.headHandleCtrlSpace)
        # temp now until handles are swapped


        # Add Xfo Outputs
        self.ZSplineNeckCanvasOp.setOutput('outputs', self.neckOutputs)

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

        # Add new deformers and outputs
        for i in xrange(len(self.neckOutputs), numDeformers):
            name = 'neck' + str(i + 1).zfill(2)
            neckOutput = ComponentOutput(name, parent=self.outputHrcGrp)
            self.neckOutputs.append(neckOutput)

        for i in xrange(len(self.deformerJoints), numDeformers):
            name = 'neck' + str(i + 1).zfill(2)
            neckDef = Joint(name, parent=self.defCmpGrp)
            neckDef.setComponent(self)
            self.deformerJoints.append(neckDef)

        if hasattr(self, 'ZSplineNeckCanvasOp'):  # Check in case this is ever called from Guide callback
            self.ZSplineNeckCanvasOp.setInput('numDeformers',  numDeformers)

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


        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)


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
            self.neckHandleMocapCtrlSpace.setSecondType(MCControl)
            self.neckHandleMocapCtrlSpace.xfo.tr = neckHandlePosition

            # Head
            self.headMocapCtrl = MCControl('head', parent=self.neckMocapCtrl, shape="circle")
            self.headMocapCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
            self.headMocapCtrl.setColor("purpleLight")
            self.headMocapCtrl.xfo.tr = headPosition

            self.headMocapCtrlSpace = self.headMocapCtrl.insertCtrlSpace()

            # Head handle
            self.headHandleMocapCtrlSpace = CtrlSpace('headHandle_mocap', parent=self.headMocapCtrl)
            self.headHandleMocapCtrlSpace.setSecondType(MCControl)
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
            self.ZSplineNeckCanvasOp.setInput('neck', self.neckCtrlSpace_link)
            self.ZSplineNeckCanvasOp.setInput('head', self.headCtrlSpace_link)
            self.ZSplineNeckCanvasOp.setInput('neckHandle', self.neckHandleCtrlSpace_link)
            self.ZSplineNeckCanvasOp.setInput('headHandle', self.headHandleCtrlSpace_link)


        self.neckBaseOutputConstraint = self.neckBaseOutputTgt.constrainTo(self.neckOutputs[0], maintainOffset=True)
        self.neckEndOutputConstraint = self.neckEndOutputTgt.constrainTo(self.neckOutputs[-1], maintainOffset=True)


        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important

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


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSHeadNeckComponentGuide)
ks.registerComponent(OSSHeadNeckComponentRig)
