from kraken.core.maths import Vec3

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
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.layer import Layer
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


class OSSNeckComponent(BaseExampleComponent):
    """Neck Component"""

    def __init__(self, name="neckBase", parent=None):
        super(OSSNeckComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.neckParentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

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

class OSSNeckComponentGuide(OSSNeckComponent):
    """Neck Component Guide"""

    def __init__(self, name='neck', parent=None):

        Profiler.getInstance().push("Construct Neck Guide Component:" + name)
        super(OSSNeckComponentGuide, self).__init__(name, parent)

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

        data = {
            'name': name,
            'location': 'M',
            'neckPosition': Vec3(0.0, 15, 0),
            'neckHandlePosition': Vec3(0.0, 15.25, 0),
            'headHandlePosition': Vec3(0.0, 17.75, 0),
            'headPosition': Vec3(0.0, 18, 0),
        }

        # Now, add the guide settings attributes to the data (happens in saveData)
        data.update(self.saveData())

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

        data = super(OSSNeckComponentGuide, self).saveData()

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

        super(OSSNeckComponentGuide, self).loadData( data )

        self.neckCtrl.xfo.tr = data["neckPosition"]
        self.neckHandleCtrl.xfo.tr = data["neckHandlePosition"]
        self.headHandleCtrl.xfo.tr = data["headHandlePosition"]
        self.headCtrl.xfo.tr = data["headPosition"]

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.neckCtrl.scalePoints(globalScaleVec)
        self.headCtrl.scalePoints(globalScaleVec)

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSNeckComponentGuide, self).getRigBuildData()

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

        return OSSNeckComponentRig


class OSSNeckComponentRig(OSSNeckComponent):
    """Neck Component"""

    def __init__(self, name="neck", parent=None):

        Profiler.getInstance().push("Construct Neck Rig Component:" + name)
        super(OSSNeckComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # COG
        print self.ctrlCmpGrp


        # Neck
        self.neckCtrlSpace = CtrlSpace('neck', parent=self.ctrlCmpGrp)
        self.neckCtrl = Control('neck', parent=self.neckCtrlSpace, shape="square")
        self.neckCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))

        # Neck handle
        self.neckHandleCtrlSpace = CtrlSpace('neckHandle', parent=self.neckCtrlSpace)

        # Head
        self.headCtrlSpace = CtrlSpace('head', parent=self.neckCtrl)
        self.headCtrl = Control('head', parent=self.headCtrlSpace, shape="circle")
        self.headCtrl.scalePoints(Vec3(6.0, 6.0, 6.0))
        self.headCtrl.setColor("orange")

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
        self.neckSrtInputConstraint = PoseConstraint('_'.join([self.neckCtrlSpace.getName(), 'To', self.neckParentSpaceInputTgt.getName()]))
        self.neckSrtInputConstraint.addConstrainer(self.neckParentSpaceInputTgt)
        self.neckSrtInputConstraint.setMaintainOffset(True)
        self.neckCtrlSpace.addConstraint(self.neckSrtInputConstraint)

        self.neckBaseOutputConstraint = PoseConstraint('_'.join([self.neckBaseOutputTgt.getName(), 'To', 'neckBase']))
        self.neckBaseOutputConstraint.addConstrainer(self.neckOutputs[0])
        self.neckBaseOutputTgt.addConstraint(self.neckBaseOutputConstraint)

        self.neckEndOutputConstraint = PoseConstraint('_'.join([self.neckEndOutputTgt.getName(), 'To', 'neckEnd']))
        self.neckEndOutputConstraint.addConstrainer(self.neckOutputs[0])
        self.neckEndOutputTgt.addConstraint(self.neckEndOutputConstraint)


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

        super(OSSNeckComponentRig, self).loadData( data )

        neckPosition = data['neckPosition']
        neckHandlePosition = data['neckHandlePosition']
        headHandlePosition = data['headHandlePosition']
        headPosition = data['headPosition']
        numDeformers = data['numDeformers']

        self.neckCtrlSpace.xfo.tr = neckPosition
        self.neckCtrl.xfo.tr = neckPosition
        self.neckHandleCtrlSpace.xfo.tr = neckHandlePosition
        self.headHandleCtrlSpace.xfo.tr = headHandlePosition
        self.headCtrlSpace.xfo.tr = headPosition
        self.headCtrl.xfo.tr = headPosition


        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        # Updating constraint to use the updated last output.
        self.neckEndOutputConstraint.setConstrainer(self.neckOutputs[-1], index=0)


        # ====================
        # Evaluate Splice Ops
        # ====================
        # evaluate the neck op so that all the output transforms are updated.
        self.ZSplineNeckCanvasOp.evaluate()

        # evaluate the constraint op so that all the joint transforms are updated.
        self.deformersToOutputsKLOp.evaluate()

        # evaluate the constraints to ensure the outputs are now in the correct location.
        self.neckBaseOutputConstraint.evaluate()
        self.neckEndOutputConstraint.evaluate()

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        # self.neckCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], 1.0, data['globalComponentCtrlSize']))


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSNeckComponentGuide)
ks.registerComponent(OSSNeckComponentRig)
