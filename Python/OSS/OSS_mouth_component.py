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

COMPONENT_NAME = "mouth"

class OSSMouth(BaseExampleComponent):
    """OSS Mouth Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSMouth, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.mouthBaseInputTgt = self.createInput('mouthBase', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.mouthOutputTgt = self.createOutput('mouth', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)

class OSSMouthGuide(OSSMouth):
    """OSS Mouth Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Mouth Guide Component:" + name)
        super(OSSMouthGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        self.mouthCtrl = Control('mouth', parent=self.ctrlCmpGrp, shape="circle")
        self.mouthCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.mouthCtrl.scalePoints(Vec3(3.5, 3.5, 3.5))


        data = {
                "name": name,
                "location": "M",
                "mouthXfo": Xfo(Vec3(0.0, 2, 0)),
                "mouthCtrlCrvData": self.mouthCtrl.getCurveData(),
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

        data = super(OSSMouthGuide, self).saveData()

        data['mouthXfo'] = self.mouthCtrl.xfo
        data['mouthCtrlCrvData'] = self.mouthCtrl.getCurveData()

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

        super(OSSMouthGuide, self).loadData( data )

        self.mouthCtrl.xfo = data['mouthXfo']
        self.mouthCtrl.setCurveData(data['mouthCtrlCrvData'])

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSMouthGuide, self).getRigBuildData()

        data['mouthXfo'] = self.mouthCtrl.xfo
        data['mouthCtrlCrvData'] = self.mouthCtrl.getCurveData()

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

        return OSSMouthRig


class OSSMouthRig(OSSMouth):
    """OSS Mouth Component Rig"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Mouth Rig Component:" + name)
        super(OSSMouthRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Mouth Aim
        self.mouthAimCtrlSpace = CtrlSpace('mouthAim', parent=self.ctrlCmpGrp)
        self.mouthAimCtrl = Control('mouthAim', parent=self.mouthAimCtrlSpace, shape="sphere")
        self.mouthAimCtrl.scalePoints(Vec3(0.35, 0.35, 0.35))
        self.mouthAimCtrl.lockScale(x=True, y=True, z=True)

        self.mouthAimUpV = Locator('mouthAimUpV', parent=self.mouthAimCtrl)
        self.mouthAimUpV.setShapeVisibility(False)

        # Mouth
        self.mouthAim = Locator('mouthAim', parent=self.ctrlCmpGrp)
        self.mouthAim.setShapeVisibility(False)

        self.mouthCtrlSpace = CtrlSpace('mouth', parent=self.ctrlCmpGrp)
        self.mouthCtrl = Control('mouth', parent=self.mouthCtrlSpace, shape="circle")
        self.mouthCtrl.lockTranslation(x=True, y=True, z=True)
        self.mouthCtrl.lockScale(x=True, y=True, z=True)


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)

        mouthDef = Joint('mouth', parent=defCmpGrp)
        mouthDef.setComponent(self)

        # ==============
        # Constrain I/O
        # ==============
        self.mouthToAimConstraint = PoseConstraint('_'.join([self.mouthCtrlSpace.getName(), 'To', self.mouthAim.getName()]))
        self.mouthToAimConstraint.setMaintainOffset(True)
        self.mouthToAimConstraint.addConstrainer(self.mouthAim)
        self.mouthCtrlSpace.addConstraint(self.mouthToAimConstraint)

        # Constraint inputs
        self.mouthAimInputConstraint = PoseConstraint('_'.join([self.mouthAimCtrlSpace.getName(), 'To', self.mouthBaseInputTgt.getName()]))
        self.mouthAimInputConstraint.setMaintainOffset(True)
        self.mouthAimInputConstraint.addConstrainer(self.mouthBaseInputTgt)
        self.mouthAimCtrlSpace.addConstraint(self.mouthAimInputConstraint)

        # # Constraint outputs
        self.mouthOutputConstraint = PoseConstraint('_'.join([self.mouthOutputTgt.getName(), 'To', self.mouthCtrl.getName()]))
        self.mouthOutputConstraint.addConstrainer(self.mouthCtrl)
        self.mouthOutputTgt.addConstraint(self.mouthOutputConstraint)

        # ===============
        # Add Splice Ops
        # ===============

        # Add Aim Splice Op
        # =================
        # self.mouthAimCanvasOp = KLOperator('mouthAimCanvasOp', 'DirectionConstraintSolver', 'Kraken')
        self.mouthAimCanvasOp = CanvasOperator('mouthAimCanvasOp', 'Kraken.Solvers.DirectionConstraintSolver')
        self.addOperator(self.mouthAimCanvasOp)

        # Add Att Inputs
        self.mouthAimCanvasOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.mouthAimCanvasOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.mouthAimCanvasOp.setInput('position', self.mouthBaseInputTgt)
        self.mouthAimCanvasOp.setInput('upVector', self.mouthAimUpV)
        self.mouthAimCanvasOp.setInput('atVector', self.mouthAimCtrl)

        # Add Xfo Outputs
        self.mouthAimCanvasOp.setOutput('constrainee', self.mouthAim)

        # Add Deformer Splice Op
        # ======================
        self.deformersToOutputsKLOp = KLOperator('mouthDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.deformersToOutputsKLOp)

        # Add Att Inputs
        self.deformersToOutputsKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.deformersToOutputsKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setInput('constrainers', [self.mouthOutputTgt])

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setOutput('constrainees', [mouthDef])

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSMouthRig, self).loadData( data )

        mouthXfo = data['mouthXfo']
        mouthCtrlCrvData = data['mouthCtrlCrvData']

        self.mouthAimCtrlSpace.xfo.ori = mouthXfo.ori
        self.mouthAimCtrlSpace.xfo.tr = mouthXfo.tr.add(Vec3(0, 0, 4))
        self.mouthAimCtrl.xfo = self.mouthAimCtrlSpace.xfo

        self.mouthAimUpV.xfo.ori = self.mouthAimCtrl.xfo.ori
        self.mouthAimUpV.xfo.tr = self.mouthAimCtrl.xfo.tr.add(Vec3(0, 3, 0))

        self.mouthAim.xfo = mouthXfo
        self.mouthCtrlSpace.xfo = mouthXfo
        self.mouthCtrl.xfo = mouthXfo
        self.mouthCtrl.setCurveData(mouthCtrlCrvData)

        # ============
        # Set IO Xfos
        # ============
        self.mouthBaseInputTgt.xfo = mouthXfo
        self.mouthOutputTgt.xfo = mouthXfo

        # ====================
        # Evaluate Splice Ops
        # ====================
        # evaluate the constraint op so that all the joint transforms are updated.
        self.mouthAimCanvasOp.evaluate()
        self.deformersToOutputsKLOp.evaluate()

        # evaluate the constraints to ensure the outputs are now in the correct location.
        self.mouthToAimConstraint.evaluate()
        self.mouthAimInputConstraint.evaluate()
        self.mouthOutputConstraint.evaluate()


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMouthGuide)
ks.registerComponent(OSSMouthRig)
