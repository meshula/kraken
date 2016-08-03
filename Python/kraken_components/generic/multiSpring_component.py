import math

from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.xfo import xfoFromDirAndUpV

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.position_constraint import PositionConstraint
from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.components.component_output import ComponentOutput
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.layer import Layer
from kraken.core.objects.control import Control

from kraken.core.objects.operators.canvas_operator import CanvasOperator
from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


class MultiSpringComponent(BaseExampleComponent):
    """Multi Spring Base"""

    def __init__(self, name='MultiSpringBase', parent=None):

        super(MultiSpringComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.rootInputTgt = self.createInput('rootInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.boneOutputs = self.createOutput('boneOutputs', dataType='Xfo[]')

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


class MultiSpringComponentGuide(MultiSpringComponent):
    """MultiSpring Component Guide"""

    def __init__(self, name='MultiSpring', parent=None):

        Profiler.getInstance().push("Construct FKCHain Guide Component:" + name)
        super(MultiSpringComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # =========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.numSprings = IntegerAttribute('numSprings', value=5, minValue=1, maxValue=100, parent=guideSettingsAttrGrp)
        self.numSprings.setValueChangeCallback(self.updateNumJointControls)

        self.springCtrls = []

        numSprings = self.numSprings.getValue()
        springXfos = self.generateGuideXfos(numSprings)

        for i in xrange(numSprings):
            newCtrl = Control('spring' + str(i + 1).zfill(2), parent=self.ctrlCmpGrp, shape="squarePointed")
            newCtrl.alignOnXAxis()
            self.springCtrls.append(newCtrl)

        data = {
           "location": "L",
           "springXfos": springXfos,
           "numSprings": self.numSprings.getValue()
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

        data = super(MultiSpringComponentGuide, self).saveData()

        springXfos = []
        for i in xrange(len(self.springCtrls)):
            springXfos.append(self.springCtrls[i].xfo)

        data['springXfos'] = springXfos

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(MultiSpringComponentGuide, self).loadData(data)

        for i in xrange(len(data['springXfos'])):
            self.springCtrls[i].xfo = data['springXfos'][i]

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(MultiSpringComponentGuide, self).getRigBuildData()

        numSprings = self.numSprings.getValue()
        boneXfos = []
        for i in xrange(numSprings):
            boneXfos.append(self.springCtrls[i].xfo)

        data['boneXfos'] = boneXfos
        data['numSprings'] = self.numSprings.getValue()

        return data


    # ==========
    # Callbacks
    # ==========
    def updateNumJointControls(self, numSprings):
        """Load a saved guide representation from persisted data.

        Arguments:
        numSprings -- object, The number of joints inthe chain.

        Return:
        True if successful.

        """

        if numSprings == 0:
            raise IndexError("'numSprings' must be > 0")

        if numSprings > len(self.springCtrls):
            for i in xrange(len(self.springCtrls), numSprings):

                newCtrl = Control('spring' + str(i + 1).zfill(2), parent=self.ctrlCmpGrp, shape="squarePointed")
                newCtrl.alignOnXAxis()
                self.springCtrls.append(newCtrl)

        elif numSprings < len(self.springCtrls):
            numExtraCtrls = len(self.springCtrls) - numSprings
            for i in xrange(numExtraCtrls):
                extraCtrl = self.springCtrls.pop()
                extraCtrl.getParent().removeChild(extraCtrl)

        # Reset the control positions based on new number of joints
        springXfos = self.generateGuideXfos(numSprings)
        for i in xrange(len(self.springCtrls)):
            self.springCtrls[i].xfo = springXfos[i]

        return True


    def generateGuideXfos(self, numSprings):
        """Generates the positions for the guide controls based on the number
        of joints.

        Args:
            numSprings (int): Number of joints to generate a transform for.

        Returns:
            list: Guide control positions.

        """

        guideXfos = []
        j = 0
        for i in xrange(numSprings):
            springXfo = Xfo()
            springXfo.tr.x = i % 5 * 2
            springXfo.tr.z = j * 2

            if i % 5 == 4:
                j += 1

            guideXfos.append(springXfo)

        return guideXfos


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

        return MultiSpringComponentRig


class MultiSpringComponentRig(MultiSpringComponent):
    """Multi Spring Rig"""

    def __init__(self, name='MultiSpring', parent=None):

        Profiler.getInstance().push("Construct Multi Spring Rig Component:" + name)
        super(MultiSpringComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Spring Ctrls
        self.mainSpringCtrl = Control('springSettings', parent=self.ctrlCmpGrp, shape='pin')

        self.springCtrlSpaces = []
        self.springCtrls = []
        self.setNumControls(1)

        # Add Component Params to FK control
        springSettingsAttrGrp = AttributeGroup("DisplayInfo_SpringSettings", parent=self.mainSpringCtrl)
        self.springDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=springSettingsAttrGrp)
        self.springtargetOffsetXInputAttr = ScalarAttribute('targetOffset_X', value=3.0, minValue=0.0, maxValue=10.0, parent=springSettingsAttrGrp)
        self.springtargetOffsetYInputAttr = ScalarAttribute('targetOffset_Y', value=0.0, minValue=0.0, maxValue=10.0, parent=springSettingsAttrGrp)
        self.springtargetOffsetZInputAttr = ScalarAttribute('targetOffset_Z', value=0.0, minValue=0.0, maxValue=10.0, parent=springSettingsAttrGrp)
        self.springFrameInputAttr = IntegerAttribute('frame', value=1, parent=springSettingsAttrGrp)
        self.springResetFrameInputAttr = IntegerAttribute('reset_frame', value=1, parent=springSettingsAttrGrp)
        self.springMassInputAttr = ScalarAttribute('mass', value=0.5, minValue=0.0, maxValue=20.0, parent=springSettingsAttrGrp)
        self.springSpringStrengthInputAttr = ScalarAttribute('springStrength', value=6.0, minValue=0.0, maxValue=20.0, parent=springSettingsAttrGrp)
        self.springDampingInputAttr = ScalarAttribute('damping', value=0.125, minValue=0.0, maxValue=5.0, parent=springSettingsAttrGrp)

        # Connect IO to controls
        self.drawDebugInputAttr.connect(self.springDrawDebugInputAttr)

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.addItem('defCmpGrp', self.defCmpGrp)
        self.deformerJoints = []
        self.boneOutputsTgt = []
        self.setNumDeformers(4)

        # =====================
        # Create Component I/O
        # =====================

        # Set IO Targets
        self.boneOutputs.setTarget(self.boneOutputsTgt)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.rootInputConstraint = PoseConstraint('_'.join([self.springCtrlSpaces[0].getName(), 'To', self.rootInputTgt.getName()]))
        self.rootInputConstraint.setMaintainOffset(True)
        self.rootInputConstraint.addConstrainer(self.rootInputTgt)
        self.springCtrlSpaces[0].addConstraint(self.rootInputConstraint)


        # ===============
        # Add Splice Ops
        # ===============
        # Add Solver Canvas Op
        self.springOp = CanvasOperator('springSolverOp', 'Kraken.Solvers.SpringOffsetSolver')
        self.addOperator(self.springOp)

        # Add Att Inputs
        self.springOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.springOp.setInput('rigScale', self.rigScaleInputAttr)
        self.springOp.setInput('targetOffset_X', self.springtargetOffsetXInputAttr)
        self.springOp.setInput('targetOffset_Y', self.springtargetOffsetYInputAttr)
        self.springOp.setInput('targetOffset_Z', self.springtargetOffsetZInputAttr)
        self.springOp.setInput('frame', self.springFrameInputAttr)
        self.springOp.setInput('reset_frame', self.springResetFrameInputAttr)
        self.springOp.setInput('mass', self.springMassInputAttr)
        self.springOp.setInput('spring_strength', self.springSpringStrengthInputAttr)
        self.springOp.setInput('damping', self.springDampingInputAttr)

        # Add Xfo Inputs
        self.springOp.setInput('inputs', self.springCtrls)

        # Add Xfo Outputs
        self.springOp.setOutput('outputs', self.boneOutputsTgt)

        # Add Deformer Splice Op
        self.deformersToOutputsKLOp = KLOperator('springDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.deformersToOutputsKLOp)

        # Add Att Inputs
        self.deformersToOutputsKLOp.setInput('drawDebug', False)
        self.deformersToOutputsKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.deformersToOutputsKLOp.setInput('constrainers', self.boneOutputsTgt)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setOutput('constrainees', self.deformerJoints)

        Profiler.getInstance().pop()


    def setNumControls(self, numControls):

        # Add more controls
        if numControls > len(self.springCtrlSpaces):
            for i in xrange(len(self.springCtrlSpaces), numControls):
                boneName = 'spring' + str(i + 1).zfill(2)
                boneFKCtrlSpace = CtrlSpace(boneName, parent=self.ctrlCmpGrp)

                boneFKCtrl = Control(boneName, parent=boneFKCtrlSpace, shape='squarePointed')
                boneFKCtrl.alignOnXAxis()

                self.springCtrlSpaces.append(boneFKCtrlSpace)
                self.springCtrls.append(boneFKCtrl)

        # Remove extra ctrls
        elif numControls < len(self.springCtrlSpaces):
            numExtraCtrls = len(self.springCtrls) - numControls
            for i in xrange(numExtraCtrls):
                extraCtrlSpace = self.springCtrlSpaces.pop()
                extraCtrl = self.springCtrls.pop()
                extraCtrlSpace.getParent().removeChild(extraCtrlSpace)
                extraCtrl.getParent().removeChild(extraCtrl)


    def setNumDeformers(self, numDeformers):

        # Add more deformers and outputs
        if numDeformers > len(self.boneOutputsTgt):
            for i in xrange(len(self.boneOutputsTgt), numDeformers):
                name = 'bone' + str(i + 1).zfill(2)

                legOutput = ComponentOutput(name, parent=self.outputHrcGrp)
                self.boneOutputsTgt.append(legOutput)

                boneDef = Joint(name, parent=self.defCmpGrp)
                boneDef.setComponent(self)
                self.deformerJoints.append(boneDef)

        # Remove extra deformers and outputs
        elif numDeformers < len(self.boneOutputsTgt):
            numExtraOutputs = len(self.boneOutputsTgt) - numDeformers
            numExtraDefs = len(self.deformerJoints) - numDeformers

            for i in xrange(numExtraOutputs):
                extraOutput = self.boneOutputsTgt.pop()
                extraDef = self.deformerJoints.pop()

                extraOutput.getParent().removeChild(extraOutput)
                extraDef.getParent().removeChild(extraDef)

        return True


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(MultiSpringComponentRig, self).loadData( data )

        boneXfos = data['boneXfos']
        numSprings = data['numSprings']

        # Add extra controls and outputs
        self.setNumControls(numSprings)
        self.setNumDeformers(numSprings)

        for i in xrange(numSprings):
            self.springCtrlSpaces[i].xfo = boneXfos[i]
            self.springCtrls[i].xfo = boneXfos[i]

        # ==========================
        # Create Output Constraints
        # ==========================

        # ============
        # Set IO Xfos
        # ============
        self.rootInputTgt.xfo = boneXfos[0]

        for i in xrange(numSprings):
            self.boneOutputsTgt[i].xfo = boneXfos[i]

        # =============
        # Set IO Attrs
        # =============

        # ====================
        # Evaluate Splice Ops
        # ====================
        # Eval Solver Ops
        self.springOp.evaluate()

        # evaluate the output splice op to evaluate with new outputs and deformers
        self.deformersToOutputsKLOp.evaluate()

        # evaluate the constraints to ensure the outputs are now in the correct location.
        self.rootInputConstraint.evaluate()


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(MultiSpringComponentGuide)
ks.registerComponent(MultiSpringComponentRig)
