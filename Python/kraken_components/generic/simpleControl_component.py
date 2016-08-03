from kraken.core.maths import Vec3, Vec3, Euler, Quat, Xfo

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


class SimpleControlComponent(BaseExampleComponent):
    """Simple Control Component Base"""

    def __init__(self, name='SimpleControl', parent=None):
        super(SimpleControlComponent, self).__init__(name, parent)


        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.mainInputTgt = self.createInput('mainInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.outputTgt = self.createOutput('output', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.rigScaleOutputAttr = self.createOutput('rigScale', dataType='Float', value=1.0, parent=self.cmpOutputAttrGrp).getTarget()


class SimpleControlComponentGuide(SimpleControlComponent):
    """Simple Control Component Guide"""

    def __init__(self, name='SimpleControl', parent=None):

        Profiler.getInstance().push("Construct Simple Control Guide Component:" + name)
        super(SimpleControlComponentGuide, self).__init__(name, parent)

        # =========
        # Attributes
        # =========
        # Add Component Params to IK control
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        self.ctrlSizeInputAttr = ScalarAttribute('ctrlSize', value=5.0, minValue=1.0, maxValue=50.0, parent=guideSettingsAttrGrp)
        self.ctrlSizeInputAttr.setValueChangeCallback(self.resizeMainCtrl)

        # =========
        # Controls
        # =========

        # Guide Controls
        self.mainCtrl = Control('main', parent=self.ctrlCmpGrp, shape='square')
        self.mainCtrl.rotatePoints(90, 0, 0)

        data = {
            "location": 'M',
            "ctrlSize": self.ctrlSizeInputAttr.getValue(),
            "ctrlXfo": Xfo(tr=Vec3(0.0, 0.0, 0.0))
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
        data = super(SimpleControlComponentGuide, self).saveData()

        data["ctrlSize"] = self.ctrlSizeInputAttr.getValue()
        data["ctrlXfo"] = self.mainCtrl.xfo

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(SimpleControlComponentGuide, self).loadData( data )

        self.ctrlSizeInputAttr.setValue(data["ctrlSize"])
        self.mainCtrl.xfo = data["ctrlXfo"]

        scaleValue = data["ctrlSize"]
        self.mainCtrl.setShape('square')
        self.mainCtrl.rotatePoints(90, 0, 0)
        self.mainCtrl.scalePoints(Vec3(scaleValue, scaleValue, scaleValue))

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(SimpleControlComponentGuide, self).getRigBuildData()

        data["ctrlSize"] = self.ctrlSizeInputAttr.getValue()
        data["ctrlXfo"] = self.mainCtrl.xfo

        return data

    # ==========
    # Callbacks
    # ==========
    def resizeMainCtrl(self, newSize):
        self.mainCtrl.setShape('square')
        self.mainCtrl.rotatePoints(90, 0, 0)
        self.mainCtrl.scalePoints(Vec3(newSize, newSize, newSize))

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

        return SimpleControlComponentRig


class SimpleControlComponentRig(SimpleControlComponent):
    """Simple Control Component Rig"""

    def __init__(self, name='SimpleControl', parent=None):

        Profiler.getInstance().push("Construct Simple Control Rig Component:" + name)
        super(SimpleControlComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Add Controls
        self.mainCtrl = Control('main', shape='square', parent=self.ctrlCmpGrp)
        self.mainCtrlSpace = self.mainCtrl.insertCtrlSpace()
        self.mainCtrl.lockScale(x=True, y=True, z=True)

        # Add Component Params to Main control
        mainSrtSettingsAttrGrp = AttributeGroup('DisplayInfo_MainSrtSettings', parent=self.mainCtrl)
        self.rigScaleAttr = ScalarAttribute('rigScale', value=1.0, parent=mainSrtSettingsAttrGrp, minValue=0.1, maxValue=100.0)

        self.rigScaleOutputAttr.connect(self.rigScaleAttr)

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.addItem('defCmpGrp', self.defCmpGrp)
        self.mainDef = Joint('main', parent=self.defCmpGrp)
        self.mainDef.setComponent(self)

        # ==============
        # Constrain I/O
        # ==============
        # Constrain inputs
        self.mainInputConstraint = PoseConstraint('_'.join([self.mainCtrlSpace.getName(), 'To', self.mainInputTgt.getName()]))
        self.mainInputConstraint.setMaintainOffset(True)
        self.mainInputConstraint.addConstrainer(self.mainInputTgt)
        self.mainCtrlSpace.addConstraint(self.mainInputConstraint)

        # Constrain outputs
        self.mainOutputConstraint = PoseConstraint('_'.join([self.outputTgt.getName(), 'To', self.mainCtrl.getName()]))
        self.mainOutputConstraint.addConstrainer(self.mainCtrl)
        self.outputTgt.addConstraint(self.mainOutputConstraint)

        # Constrain deformers
        self.mainDefConstraint = PoseConstraint('_'.join([self.mainDef.getName(), 'To', self.mainCtrl.getName()]))
        self.mainDefConstraint.addConstrainer(self.mainCtrl)
        self.mainDef.addConstraint(self.mainDefConstraint)

        # ===============
        # Add Canvas Ops
        # ===============

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(SimpleControlComponentRig, self).loadData( data )

        ctrlSize = data.get('ctrlSize', 1.0)
        ctrlXfo = data.get('ctrlXfo', Xfo())

        # ================
        # Resize Controls
        # ================
        self.mainCtrl.setShape('square')
        self.mainCtrl.rotatePoints(90, 0, 0)
        self.mainCtrl.scalePoints(Vec3(ctrlSize, ctrlSize, ctrlSize))

        # =======================
        # Set Control Transforms
        # =======================
        self.mainCtrlSpace.xfo = ctrlXfo
        self.mainCtrl.xfo = ctrlXfo

        # ============
        # Set IO Xfos
        # ============
        self.mainInputTgt.xfo = ctrlXfo
        self.mainDef.xfo = ctrlXfo
        self.outputTgt.xfo = ctrlXfo

        # ====================
        # Evaluate Constraints
        # ====================
        self.mainInputConstraint.evaluate()
        self.mainOutputConstraint.evaluate()
        self.mainDefConstraint.evaluate()

        # ====================
        # Evaluate Canvas Ops
        # ====================


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(SimpleControlComponentGuide)
ks.registerComponent(SimpleControlComponentRig)
