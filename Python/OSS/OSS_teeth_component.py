from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo

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

COMPONENT_NAME = "teeth"


class OSSTeeth(OSS_Component):
    """Teeth Component Base"""

    def __init__(self, name='teeth', parent=None):
        super(OSSTeeth, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.teethOutputTgt = self.createOutput('teeth', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs



class OSSTeethGuide(OSSTeeth):
    """Teeth Component Guide"""

    def __init__(self, name='teeth', parent=None):

        Profiler.getInstance().push("Construct Teeth Guide Component:" + name)
        super(OSSTeethGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.teethCtrl = Control('teeth', parent=self.ctrlCmpGrp, shape="null")
        self.teethCtrl.setColor("pink")

        data = {
                "name": name,
                "location": "M",
                "teethXfo": Xfo(Vec3(0.0, 0.0, 0.0)),
                'teethCtrlCrvData': self.teethCtrl.getCurveData()
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

        data = super(OSSTeethGuide, self).saveData()

        data['teethXfo'] = self.teethCtrl.xfo
        #data['teethCtrlCrvData'] = self.teethCtrl.getCurveData()

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """


        super(OSSTeethGuide, self).loadData( data )

        self.teethCtrl.xfo = data['teethXfo']
        #self.teethCtrl.setCurveData(data['teethCtrlCrvData'])

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.teethCtrl.scalePoints(globalScaleVec)
        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSTeethGuide, self).getRigBuildData()


        data['teethXfo'] = self.teethCtrl.xfo
        data['teethCtrlCrvData'] = self.teethCtrl.getCurveData()

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

        return OSSTeethRig


class OSSTeethRig(OSSTeeth):
    """Teeth Component"""

    def __init__(self, name='Teeth', parent=None):

        Profiler.getInstance().push("Construct Teeth Rig Component:" + name)
        super(OSSTeethRig, self).__init__(name, parent)



    def createControls(self, data):

        # =========
        # Controls
        # =========
        # Teeth

        self.teethCtrl = Control(self.getName(), parent=self.ctrlCmpGrp, shape="circle")
        self.teethCtrlSpace = self.teethCtrl.insertCtrlSpace()
        self.teethCtrlSpace.xfo = data['teethXfo']
        self.teethCtrl.xfo = data['teethXfo']
        #self.teethCtrl.setCurveData(data['teethCtrlCrvData'])
        self.teethCtrl.setColor("turquoise")

        self.teethCtrl.scalePoints(Vec3(Vec3(2.5,2.5,2.5)))
        self.teethCtrl.rotatePoints(90.0, 0.0, 0.0)

        # ==========
        # Deformers
        # ==========

        self.teethDef = Joint(self.getName(), parent=self.deformersLayer)
        self.teethDef.setComponent(self)

        self.parentSpaceInputTgt.childJoints = [self.teethDef]

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.teethInputConstraint = self.teethCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Constraint outputs
        self.teethOutputTgtConstraint = self.teethOutputTgt.constrainTo(self.teethCtrl)
        self.teethDefConstraint = self.teethDef.constrainTo(self.teethCtrl)

        self.teethOutputTgtConstraint.evaluate()

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSTeethRig, self).loadData( data )

        self.createControls(data)

        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.teethCtrl.scalePoints(globalScale)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSTeethGuide)
ks.registerComponent(OSSTeethRig)
