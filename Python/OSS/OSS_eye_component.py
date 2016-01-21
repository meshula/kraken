from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

COMPONENT_NAME = "eyes"

class OSSEye(BaseExampleComponent):
    """OSS Eye Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None, data=None):
        super(OSSEye, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.eyeBaseInputTgt = self.createInput('eyeBase', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.eyeOutputTgt = self.createOutput('eye', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.eyeAimOutputTgt = self.createOutput('eyeAim', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSEyeGuide(OSSEye):
    """OSS Eye Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None, data=None):

        Profiler.getInstance().push("Construct Eye Guide Component:" + name)
        super(OSSEyeGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        self.eyeCtrl = Control('eye', parent=self.ctrlCmpGrp, shape="sphere")


        if data is None:
            data = {
                    "name": name,
                    "location": "M",
                    "eyeXfo": Xfo(Vec3(0.75, 20, 1)),
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

        data = super(OSSEyeGuide, self).saveData()

        data['eyeXfo'] = self.eyeCtrl.xfo

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

        super(OSSEyeGuide, self).loadData( data )

        self.eyeCtrl.xfo = data['eyeXfo']

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSEyeGuide, self).getRigBuildData()

        data['eyeXfo'] = self.eyeCtrl.xfo

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

        return OSSEyeRig


class OSSEyeRig(OSSEye):
    """OSS Eye Component Rig"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Eye Rig Component:" + name)
        super(OSSEyeRig, self).__init__(name, parent)


    def createControls(self, data):

        location = data['location']

        # =========
        # Controls
        # =========
        # Eye Aim
        self.eyeAimCtrlSpace = CtrlSpace('eyeAim', parent=self.ctrlCmpGrp)
        self.eyeAimCtrl = Control('eyeAim', parent=self.eyeAimCtrlSpace, shape=location.upper())
        self.eyeAimCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.eyeAimCtrl.lockScale(x=True, y=True, z=True)

        self.eyeAimUpV = Locator('eyeAimUpV', parent=self.ctrlCmpGrp)
        self.eyeAimUpV.setShapeVisibility(False)

        # Eye
        self.eyeAim = Locator('eyeAim', parent=self.ctrlCmpGrp)
        self.eyeAim.setShapeVisibility(False)

        self.eyeCtrlSpace = CtrlSpace('eye', parent=self.ctrlCmpGrp)
        self.eyeCtrl = Control('eye', parent=self.eyeCtrlSpace, shape="null")
        self.eyeCtrl.lockTranslation(x=True, y=True, z=True)
        self.eyeCtrl.lockScale(x=True, y=True, z=True)


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)

        eyeDef = Joint('eye', parent=defCmpGrp)
        eyeDef.setComponent(self)

        # ==============
        # Constrain I/O
        # ==============
        self.eyeToAimConstraint = PoseConstraint('_'.join([self.eyeCtrlSpace.getName(), 'To', self.eyeAim.getName()]))
        self.eyeToAimConstraint.setMaintainOffset(True)
        self.eyeToAimConstraint.addConstrainer(self.eyeAim)
        self.eyeCtrlSpace.addConstraint(self.eyeToAimConstraint)

        # Constraint inputs
        self.eyeAimInputConstraint = PoseConstraint('_'.join([self.eyeAimCtrlSpace.getName(), 'To', self.eyeBaseInputTgt.getName()]))
        self.eyeAimInputConstraint.setMaintainOffset(True)
        self.eyeAimInputConstraint.addConstrainer(self.eyeBaseInputTgt)
        self.eyeAimCtrlSpace.addConstraint(self.eyeAimInputConstraint)

        # # Constraint outputs
        self.eyeOutputConstraint = PoseConstraint('_'.join([self.eyeOutputTgt.getName(), 'To', self.eyeCtrl.getName()]))
        self.eyeOutputConstraint.addConstrainer(self.eyeCtrl)
        self.eyeOutputTgt.addConstraint(self.eyeOutputConstraint)


        # ===============q
        # Add Splice Ops
        # ===============

        # Add Aim Splice Op
        # =================
        # self.eyeAimCanvasOp = KLOperator('eyeAimCanvasOp', 'DirectionConstraintSolver', 'Kraken')
        self.eyeAimCanvasOp = CanvasOperator('eyeAimCanvasOp', 'Kraken.Solvers.DirectionConstraintSolver')
        self.addOperator(self.eyeAimCanvasOp)

        # Add Att Inputs
        self.eyeAimCanvasOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.eyeAimCanvasOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.eyeAimCanvasOp.setInput('position', self.eyeBaseInputTgt)
        self.eyeAimCanvasOp.setInput('upVector', self.eyeAimUpV)
        self.eyeAimCanvasOp.setInput('atVector', self.eyeAimCtrl)

        # Add Xfo Outputs
        self.eyeAimCanvasOp.setOutput('constrainee', self.eyeAim)

        # Add Deformer Splice Op
        # ======================
        self.deformersToOutputsKLOp = KLOperator('eyeDeformerKLOp', 'OSS_BlendPoseConstraintSolver', 'Kraken')
        self.addOperator(self.deformersToOutputsKLOp)

        # Add Att Inputs
        self.deformersToOutputsKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.deformersToOutputsKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setInput('constrainers', [self.eyeOutputTgt])

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setOutput('constrainees', [eyeDef])

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSEyeRig, self).loadData( data )

        self.createControls(data)

        eyeXfo = data['eyeXfo']

        self.eyeAimCtrlSpace.xfo.ori = eyeXfo.ori
        self.eyeAimCtrlSpace.xfo.tr = eyeXfo.tr.add(Vec3(0, 0, 10))
        self.eyeAimCtrl.xfo = self.eyeAimCtrlSpace.xfo

        self.eyeAimUpV.xfo.ori = eyeXfo.ori
        self.eyeAimUpV.xfo.tr = eyeXfo.tr.add(Vec3(0, 1, 0))

        self.eyeAim.xfo = eyeXfo
        self.eyeCtrlSpace.xfo = eyeXfo
        self.eyeCtrl.xfo = eyeXfo

        # ============
        # Set IO Xfos
        # ============
        self.eyeBaseInputTgt.xfo = eyeXfo
        self.eyeOutputTgt.xfo = eyeXfo
        self.eyeAimOutputTgt.xfo = eyeXfo

        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()

        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.eyeToAimConstraint.evaluate()
        self.eyeAimInputConstraint.evaluate()
        self.eyeOutputConstraint.evaluate()
        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSEyeGuide)
ks.registerComponent(OSSEyeRig)
