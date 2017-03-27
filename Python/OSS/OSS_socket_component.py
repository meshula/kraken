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
from kraken.core.objects.space import Space
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component


COMPONENT_NAME = "socket"


class OSSSocket(OSS_Component):
    """Socket Component Base"""

    def __init__(self, name='socket', parent=None):
        super(OSSSocket, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.socketOutputTgt = self.createOutput('socket', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs


class OSSSocketGuide(OSSSocket):
    """Socket Component Guide"""

    def __init__(self, name='socket', parent=None):

        Profiler.getInstance().push("Construct Socket Guide Component:" + name)
        super(OSSSocketGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.socketCtrl = Control('socket', parent=self.ctrlCmpGrp, shape="null")
        self.socketCtrl.setColor("pink")

        data = {
                "name": name,
                "location": "M",
                "socketXfo": Xfo(Vec3(0.0, 0.0, 0.0)),
                'socketCtrlCrvData': self.socketCtrl.getCurveData()
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

        data = super(OSSSocketGuide, self).saveData()

        data['socketXfo'] = self.socketCtrl.xfo
        #data['socketCtrlCrvData'] = self.socketCtrl.getCurveData()

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """


        super(OSSSocketGuide, self).loadData( data )

        self.socketCtrl.xfo = data['socketXfo']
        #self.socketCtrl.setCurveData(data['socketCtrlCrvData'])

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.socketCtrl.scalePoints(globalScaleVec)
        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSSocketGuide, self).getRigBuildData()


        data['socketXfo'] = self.socketCtrl.xfo
        data['socketCtrlCrvData'] = self.socketCtrl.getCurveData()

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

        return OSSSocketRig


class OSSSocketRig(OSSSocket):
    """Socket Component"""

    def __init__(self, name='Socket', parent=None):

        Profiler.getInstance().push("Construct Socket Rig Component:" + name)
        super(OSSSocketRig, self).__init__(name, parent)



    def createControls(self, data):

        # =========
        # Controls
        # =========
        # Socket

        self.socketCtrl = Control(self.getName(), parent=self.ctrlCmpGrp, shape="circle")
        self.socketCtrl.xfo = data['socketXfo']
        self.socketCtrl.setColor("pink")
        self.socketCtrl.alignOnYAxis()
        self.socketSpace = self.socketCtrl.insertSpace()

        self.socket_offsetCtrl = Control(self.getName() + '_offset', parent=self.socketCtrl, shape="null")
        self.socket_offsetCtrl.xfo = data['socketXfo']
        #self.socket_offsetCtrl.setCurveData(data['socket_offsetCtrlCrvData'])
        self.socket_offsetCtrl.setColor("pink")

        # ==========
        # Deformers
        # ==========
        self.socketDef = Joint(self.getName(), parent=self.deformersParent)
        self.socketDef.setComponent(self)

        self.parentSpaceInputTgt.childJoints = [self.socketDef]

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.socketInputConstraint = self.socketSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Constraint outputs
        self.socketOutputTgtConstraint = self.socketOutputTgt.constrainTo(self.socket_offsetCtrl)
        self.socketDefConstraint = self.socketDef.constrainTo(self.socket_offsetCtrl)
        self.socketOutputTgtConstraint.evaluate()

        self.socketOutputTgt.parentJoint =  self.socketDef

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSSocketRig, self).loadData( data )

        self.createControls(data)

        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.socket_offsetCtrl.scalePoints(globalScale)
        self.socketCtrl.scalePoints(globalScale)

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSocketGuide)
ks.registerComponent(OSSSocketRig)
