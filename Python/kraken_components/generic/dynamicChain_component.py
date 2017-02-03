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

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


class DynamicChainComponent(BaseExampleComponent):
    """FK Chain Base"""

    def __init__(self, name='DynamicChainBase', parent=None):

        super(DynamicChainComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.rootInputTgt = self.createInput('rootInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.boneOutputs = self.createOutput('boneOutputs', dataType='Xfo[]')

        self.chainEndXfoOutputTgt = self.createOutput('chainEndXfoOutput', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.chainEndPosOutputTgt = self.createOutput('chainEndPosOutput', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


class DynamicChainComponentGuide(DynamicChainComponent):
    """FKChain Component Guide"""

    def __init__(self, name='DynamicChain', parent=None):

        Profiler.getInstance().push("Construct FKCHain Guide Component:" + name)
        super(DynamicChainComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # =========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.numJoints = IntegerAttribute('numJoints', value=4, minValue=1, maxValue=20, parent=guideSettingsAttrGrp)
        self.numJoints.setValueChangeCallback(self.updateNumJointControls)

        self.jointCtrls = []

        numJoints = self.numJoints.getValue()
        jointPositions = self.generateGuidePositions(numJoints)

        for i in xrange(numJoints):
            self.jointCtrls.append(Control('leg' + str(i + 1).zfill(2), parent=self.ctrlCmpGrp, shape="sphere"))

        data = {
           "location": "L",
           "jointPositions": jointPositions,
           "numJoints": self.numJoints.getValue()
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

        data = super(DynamicChainComponentGuide, self).saveData()

        jointPositions = []
        for i in xrange(len(self.jointCtrls)):
            jointPositions.append(self.jointCtrls[i].xfo.tr)

        data['jointPositions'] = jointPositions

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(DynamicChainComponentGuide, self).loadData(data)

        for i in xrange(len(data['jointPositions'])):
            self.jointCtrls[i].xfo.tr = data['jointPositions'][i]

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(DynamicChainComponentGuide, self).getRigBuildData()

        numJoints = self.numJoints.getValue()

        # Calculate FW
        toFirst = self.jointCtrls[0].xfo.tr.subtract(self.jointCtrls[1].xfo.tr).unit()
        toTip = self.jointCtrls[0].xfo.tr.subtract(self.jointCtrls[-1].xfo.tr).unit()
        fw = toTip.cross(toFirst).unit()

        # Calculate Xfos
        boneXfos = []
        boneLengths = []
        for i in xrange(numJoints):
            boneVec = self.jointCtrls[i + 1].xfo.tr.subtract(self.jointCtrls[i].xfo.tr)
            boneLengths.append(boneVec.length())
            bone1Normal = fw.cross(boneVec).unit()
            bone1ZAxis = boneVec.cross(bone1Normal).unit()

            xfo = Xfo()
            xfo.setFromVectors(boneVec.unit(), bone1Normal, bone1ZAxis, self.jointCtrls[i].xfo.tr)

            boneXfos.append(xfo)

        data['boneXfos'] = boneXfos
        data['endXfo'] = self.jointCtrls[-1].xfo
        data['boneLengths'] = boneLengths

        return data


    # ==========
    # Callbacks
    # ==========
    def updateNumJointControls(self, numJoints):
        """Load a saved guide representation from persisted data.

        Arguments:
        numJoints -- object, The number of joints inthe chain.

        Return:
        True if successful.

        """

        if numJoints == 0:
            raise IndexError("'numJoints' must be > 0")

        if numJoints + 1 > len(self.jointCtrls):
            for i in xrange(len(self.jointCtrls), numJoints + 1):
                newCtrl = Control('leg' + str(i + 1).zfill(2), parent=self.ctrlCmpGrp, shape="sphere")
                self.jointCtrls.append(newCtrl)

        elif numJoints + 1 < len(self.jointCtrls):
            numExtraCtrls = len(self.jointCtrls) - (numJoints + 1)
            for i in xrange(numExtraCtrls):
                extraCtrl = self.jointCtrls.pop()
                self.ctrlCmpGrp.removeChild(extraCtrl)

        # Reset the control positions based on new number of joints
        jointPositions = self.generateGuidePositions(numJoints)
        for i in xrange(len(self.jointCtrls)):
            self.jointCtrls[i].xfo.tr = jointPositions[i]

        return True

    def generateGuidePositions(self, numJoints):
        """Generates the positions for the guide controls based on the number
        of joints.

        Args:
            numJoints (int): Number of joints to generate a transform for.

        Returns:
            list: Guide control positions.

        """

        halfPi = math.pi / 2.0
        step = halfPi / numJoints

        xValues = []
        yValues = []
        for i in xrange(numJoints + 1):
            xValues.append(math.cos((i * step) + halfPi) * -10)
            yValues.append(math.sin((i * step) + halfPi) * 10)

        guidePositions = []
        for i in xrange(numJoints + 1):
            guidePositions.append(Vec3(xValues[i], yValues[i], 0.0))

        return guidePositions


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

        return DynamicChainComponentRig


class DynamicChainComponentRig(DynamicChainComponent):
    """FK Chain Leg Rig"""

    def __init__(self, name='FKChain', parent=None):

        Profiler.getInstance().push("Construct FK Chain Rig Component:" + name)
        super(DynamicChainComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # FK
        self.fkCtrlSpaces = []
        self.fkCtrls = []
        self.setNumControls(4)

        # Add Component Params to FK control
        chainSettingsAttrGrp = AttributeGroup("DisplayInfo_ChainSettings", parent=self.fkCtrls[0])
        chainDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=chainSettingsAttrGrp)
        self.simulateInputAttr = BoolAttribute('simulate', value=False, parent=chainSettingsAttrGrp)
        self.resetframeInputAttr = ScalarAttribute('resetframe', value=1, parent=chainSettingsAttrGrp)
        self.frameInputAttr = ScalarAttribute('frame', value=0, parent=chainSettingsAttrGrp)
        self.simBlendStartInputAttr = ScalarAttribute('simBlendStart', value=0.7, minValue=0.0, maxValue=1.0, parent=chainSettingsAttrGrp)
        self.simBlendEndInputAttr = ScalarAttribute('simBlendEnd', value=1.0, minValue=0.0, maxValue=1.0, parent=chainSettingsAttrGrp)
        self.dampeningInputAttr = ScalarAttribute('dampening', value=0.3, minValue=0.0, maxValue=1.0, parent=chainSettingsAttrGrp)
        self.gravityInputAttr = ScalarAttribute('gravity', value=-9.8, parent=chainSettingsAttrGrp)
        self.massStartInputAttr = ScalarAttribute('massStart', value=0.35, minValue=0.0, maxValue=10.0, parent=chainSettingsAttrGrp)
        self.massEndInputAttr = ScalarAttribute('massEnd', value=1.0, minValue=0.0, maxValue=10.0, parent=chainSettingsAttrGrp)

        # Connect IO to controls
        self.drawDebugInputAttr.connect(chainDrawDebugInputAttr)

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
        self.rootInputConstraint = PoseConstraint('_'.join([self.fkCtrlSpaces[0].getName(), 'To', self.rootInputTgt.getName()]))
        self.rootInputConstraint.setMaintainOffset(True)
        self.rootInputConstraint.addConstrainer(self.rootInputTgt)
        self.fkCtrlSpaces[0].addConstraint(self.rootInputConstraint)


        # ===============
        # Add Splice Ops
        # ===============
        # Add Output Splice Op
        self.dynamicChainKLOp = KLOperator('dynamicChainKLOp', 'DynamicChainSolver', 'Kraken')
        self.addOperator(self.dynamicChainKLOp)

        # Add Att Inputs
        self.dynamicChainKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.dynamicChainKLOp.setInput('rigScale', self.rigScaleInputAttr)

        self.dynamicChainKLOp.setInput('simulate', self.simulateInputAttr)
        self.dynamicChainKLOp.setInput('resetframe', self.resetframeInputAttr)
        self.dynamicChainKLOp.setInput('frame', self.frameInputAttr)
        self.dynamicChainKLOp.setInput('simBlendStart', self.simBlendStartInputAttr)
        self.dynamicChainKLOp.setInput('simBlendEnd', self.simBlendEndInputAttr)
        self.dynamicChainKLOp.setInput('dampening', self.dampeningInputAttr)
        self.dynamicChainKLOp.setInput('gravity', self.gravityInputAttr)
        self.dynamicChainKLOp.setInput('massStart', self.massStartInputAttr)
        self.dynamicChainKLOp.setInput('massEnd', self.massEndInputAttr)

        # Add Xfo Inputs
        self.dynamicChainKLOp.setInput('fkPose', self.fkCtrls)

        # Add Xfo Outputs
        self.dynamicChainKLOp.setOutput('animPose', self.boneOutputsTgt)

        # Add Deformer Splice Op
        self.deformersToOutputsKLOp = KLOperator('fkChainDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.deformersToOutputsKLOp)

        # Add Att Inputs
        self.deformersToOutputsKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.deformersToOutputsKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.deformersToOutputsKLOp.setInput('constrainers', self.boneOutputsTgt)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setOutput('constrainees', self.deformerJoints)

        Profiler.getInstance().pop()


    def setNumControls(self, numControls):

        # Add more controls
        if numControls > len(self.fkCtrlSpaces):
            for i in xrange(len(self.fkCtrlSpaces), numControls):
                if i==0:
                    parent = self.ctrlCmpGrp
                else:
                    parent = self.fkCtrls[i - 1]

                boneName = 'bone' + str(i + 1).zfill(2) + 'FK'
                boneFKCtrlSpace = CtrlSpace(boneName, parent=parent)

                boneFKCtrl = Control(boneName, parent=boneFKCtrlSpace, shape="cube")
                boneFKCtrl.alignOnXAxis()
                boneFKCtrl.lockScale(x=True, y=True, z=True)
                boneFKCtrl.lockTranslation(x=True, y=True, z=True)

                self.fkCtrlSpaces.append(boneFKCtrlSpace)
                self.fkCtrls.append(boneFKCtrl)

        # Remove extra ctrls
        elif numControls < len(self.fkCtrlSpaces):
            numExtraCtrls = len(self.fkCtrls) - numControls
            for i in xrange(numExtraCtrls):
                extraCtrlSpace = self.fkCtrlSpaces.pop()
                extraCtrl = self.fkCtrls.pop()
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

        super(DynamicChainComponentRig, self).loadData( data )

        boneXfos = data['boneXfos']
        boneLengths = data['boneLengths']
        numJoints = data['numJoints']

        # Add extra controls and outputs
        self.setNumControls(numJoints)
        self.setNumDeformers(numJoints)

        for i in xrange(numJoints):
            self.fkCtrlSpaces[i].xfo = boneXfos[i]
            self.fkCtrls[i].xfo = boneXfos[i]
            self.fkCtrls[i].scalePoints(Vec3(boneLengths[i], boneLengths[i] * 0.45, boneLengths[i] * 0.45))

        # ==========================
        # Create Output Constraints
        # ==========================
        # This needs to be done here since the 'numJoints' attribute resizes the
        # number of controls and outputs

        self.chainEndXfoOutputConstraint = PoseConstraint('_'.join([self.chainEndXfoOutputTgt.getName(), 'To', self.boneOutputsTgt[-1].getName()]))
        self.chainEndXfoOutputConstraint.setMaintainOffset(True)
        self.chainEndXfoOutputConstraint.addConstrainer(self.boneOutputsTgt[-1])
        self.chainEndXfoOutputTgt.addConstraint(self.chainEndXfoOutputConstraint)

        self.chainEndPosOutputConstraint = PositionConstraint('_'.join([self.chainEndPosOutputTgt.getName(), 'To', self.boneOutputsTgt[-1].getName()]))
        self.chainEndPosOutputConstraint.setMaintainOffset(True)
        self.chainEndPosOutputConstraint.addConstrainer(self.boneOutputsTgt[-1])
        self.chainEndPosOutputTgt.addConstraint(self.chainEndPosOutputConstraint)


        # ============
        # Set IO Xfos
        # ============
        self.rootInputTgt.xfo = boneXfos[0]

        for i in xrange(numJoints):
            self.boneOutputsTgt[i].xfo = boneXfos[i]

        self.chainEndXfoOutputTgt.xfo = data['endXfo']
        self.chainEndPosOutputTgt.xfo = data['endXfo']

        # =============
        # Set IO Attrs
        # =============

        # ====================
        # Evaluate Splice Ops
        # ====================
        # Eval Outputs to Controls Op to evaulate with new outputs and controls
        # self.dynamicChainKLOp.evaluate()

        # evaluate the output splice op to evaluate with new outputs and deformers
        self.deformersToOutputsKLOp.evaluate()

        # evaluate the constraints to ensure the outputs are now in the correct location.
        self.rootInputConstraint.evaluate()
        self.chainEndXfoOutputConstraint.evaluate()


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(DynamicChainComponentGuide)
ks.registerComponent(DynamicChainComponentRig)
