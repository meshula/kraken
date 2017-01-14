from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.constants import *

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
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

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "tongue"


class OSSTongue(OSS_Component):
    """Tongue Component Base"""

    def __init__(self, name='tongue', parent=None):
        super(OSSTongue, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.tongueOutputTgt = self.createOutput('tongue', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs


class OSSTongueGuide(OSSTongue):
    """Tongue Component Guide"""

    def __init__(self, name='tongue', parent=None):

        Profiler.getInstance().push("Construct Tongue Guide Component:" + name)
        super(OSSTongueGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.tongueCtrl = Control('tongue', parent=self.ctrlCmpGrp, shape="null")
        self.tongueCtrl.setColor("red")

        data = {
                "name": name,
                "location": "M",
                "tongueXfo": Xfo(Vec3(0.0, 0.0, 0.0)),
                'tongueCtrlCrvData': self.tongueCtrl.getCurveData()
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

        data = super(OSSTongueGuide, self).saveData()

        data['tongueXfo'] = self.tongueCtrl.xfo
        #data['tongueCtrlCrvData'] = self.tongueCtrl.getCurveData()

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """


        super(OSSTongueGuide, self).loadData( data )

        self.tongueCtrl.xfo = data['tongueXfo']
        #self.tongueCtrl.setCurveData(data['tongueCtrlCrvData'])

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.tongueCtrl.scalePoints(globalScaleVec)
        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSTongueGuide, self).getRigBuildData()


        data['tongueXfo'] = self.tongueCtrl.xfo
        data['tongueCtrlCrvData'] = self.tongueCtrl.getCurveData()

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

        return OSSTongueRig


class OSSTongueRig(OSSTongue):
    """Tongue Component"""

    def __init__(self, name='Tongue', parent=None):

        Profiler.getInstance().push("Construct Tongue Rig Component:" + name)
        super(OSSTongueRig, self).__init__(name, parent)

        self.parentSpaceInputTgt.childJoints = []

    def createControls(self, data):

        # =========
        # Controls
        # =========
        # Tongue

        self.tongueCtrl = Control(self.getName(), parent=self.ctrlCmpGrp, shape="circle")
        self.tongueCtrlSpace = self.tongueCtrl.insertCtrlSpace()
        self.tongueCtrlSpace.xfo = data['tongueXfo']
        self.tongueCtrl.xfo = data['tongueXfo']
        #self.tongueCtrl.setCurveData(data['tongueCtrlCrvData'])
        self.tongueCtrl.setColor("pink")

        self.tongueCtrl.scalePoints(Vec3(Vec3(2.5,2.5,2.5)))
        self.tongueCtrl.rotatePoints(90.0, 0.0, 0.0)

        # ==========
        # Deformers
        # ==========
        self.tongueDef = Joint(self.getName(), parent=self.deformersParent)
        self.tongueDef.setComponent(self)
        self.parentSpaceInputTgt.childJoints.append(self.tongueDef)
        self.tongueOutputTgt.parentJoint =  self.tongueDef


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.tongueInputConstraint = self.tongueCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Constraint outputs
        self.tongueOutputTgtConstraint = self.tongueOutputTgt.constrainTo(self.tongueCtrl)
        self.tongueDefConstraint = self.tongueDef.constrainTo(self.tongueCtrl)

        self.tongueOutputTgtConstraint.evaluate()

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSTongueRig, self).loadData( data )

        self.createControls(data)

        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.tongueCtrl.scalePoints(globalScale)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSTongueGuide)
ks.registerComponent(OSSTongueRig)
