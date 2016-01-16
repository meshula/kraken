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

COMPONENT_NAME = "main"

class OSSMainComponent(BaseExampleComponent):
    """Main Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None, data=None):
        super(OSSMainComponent, self).__init__(name, parent)


        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.globalOutputTgt = self.createOutput('global', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.offsetOutputTgt = self.createOutput('offset', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.rigScaleOutputAttr = self.createOutput('rigScale', dataType='Float', value=1.0, parent=self.cmpOutputAttrGrp).getTarget()

        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSMainComponentGuide(OSSMainComponent):
    """Main Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Main Guide Component:" + name)
        super(OSSMainComponentGuide, self).__init__(name, parent)

        # =========
        # Attributes
        # =========

        # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        # =========
        # Controls
        # =========

        # Guide Controls
        self.mainCtrl = Control('main', parent=self.ctrlCmpGrp, shape="circle")


        data = {
                "location": 'M',
                "mainXfo": Xfo(tr=Vec3(0.0, 0.0, 0.0))
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
        data = super(OSSMainComponentGuide, self).saveData()

        data["mainXfo"] = self.mainCtrl.xfo

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

        super(OSSMainComponentGuide, self).loadData( data )

        self.mainCtrl.xfo = data["mainXfo"]

        self.mainCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSMainComponentGuide, self).getRigBuildData()

        data["mainXfo"] = self.mainCtrl.xfo

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

        return OSSMainComponentRig

class OSSMainComponentRig(OSSMainComponent):
    """Main Component Rig"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Main Rig Component:" + name)
        super(OSSMainComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Add Controls
        self.mainCtrlSpace = CtrlSpace('global', parent=self.ctrlCmpGrp)
        self.mainCtrl = Control('global', shape='main', parent=self.mainCtrlSpace)
        self.mainCtrl.setColor("turqoise")
        self.mainCtrl.lockScale(x=True, y=True, z=True)

        self.offsetCtrlSpace = CtrlSpace('Offset', parent=self.mainCtrl)
        self.offsetCtrl = Control('Offset', shape='main', parent=self.offsetCtrlSpace)
        self.offsetCtrl.setColor("turqoiseDark")
        self.offsetCtrl.lockScale(x=True, y=True, z=True)

        # Add Component Params to IK control
        MainSettingsAttrGrp = AttributeGroup('DisplayInfo_MainSettings', parent=self.mainCtrl)
        self.rigScaleAttr = ScalarAttribute('rigScale', value=1.0, parent=MainSettingsAttrGrp, minValue=0.1, maxValue=100.0)

        self.rigScaleOutputAttr.connect(self.rigScaleAttr)

        # ==========
        # Deformers
        # ==========


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # Constraint outputs
        globalConstraint = PoseConstraint('_'.join([self.globalOutputTgt.getName(), 'To', self.mainCtrl.getName()]))
        globalConstraint.addConstrainer(self.mainCtrl)
        self.globalOutputTgt.addConstraint(globalConstraint)

        offsetConstraint = PoseConstraint('_'.join([self.offsetOutputTgt.getName(), 'To', self.mainCtrl.getName()]))
        offsetConstraint.addConstrainer(self.offsetCtrl)
        self.offsetOutputTgt.addConstraint(offsetConstraint)


        # ===============
        # Add Splice Ops
        # ===============
        #Add Rig Scale Splice Op
        self.rigScaleKLOp = KLOperator('rigScaleKLOp', 'RigScaleSolver', 'Kraken')
        self.addOperator(self.rigScaleKLOp)

        # Add Att Inputs
        self.rigScaleKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.rigScaleKLOp.setInput('rigScale', self.rigScaleOutputAttr)

        # Add Xfo Inputs

        # Add Xfo Outputs
        self.rigScaleKLOp.setOutput('target', self.mainCtrlSpace)


        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSMainComponentRig, self).loadData( data )

        # ================
        # Resize Controls
        # ================
        self.mainCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))
        self.offsetCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"] * 0.6, 1.0, data["globalComponentCtrlSize"] * 0.6))  # fix this scale issue

        # =======================
        # Set Control Transforms
        # =======================
        self.mainCtrlSpace.xfo = data["mainXfo"]
        self.mainCtrl.xfo = data["mainXfo"]
        self.offsetCtrlSpace.xfo = data["mainXfo"]
        self.offsetCtrl.xfo = data["mainXfo"]

        # ============
        # Set IO Xfos
        # ============
        self.globalOutputTgt = data["mainXfo"]
        self.offsetOutputTgt = data["mainXfo"]


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMainComponentGuide)
ks.registerComponent(OSSMainComponentRig)
