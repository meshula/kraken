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

COMPONENT_NAME = "socket"


class OSSSocket(BaseExampleComponent):
    """Socket Component Base"""

    def __init__(self, name='socket', parent=None):
        super(OSSSocket, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()


        # Declare Output Xfos
        self.socketOutputTgt = self.createOutput('socket', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)

class OSSSocketGuide(OSSSocket):
    """Socket Component Guide"""

    def __init__(self, name='socket', parent=None):

        Profiler.getInstance().push("Construct Socket Guide Component:" + name)
        super(OSSSocketGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=self.guideSettingsAttrGrp)

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

        self.socket_offsetCtrl = Control(self.getName() + '_offset', parent=self.ctrlCmpGrp, shape="circle")
        self.socket_offsetCtrl.xfo = data['socketXfo']
        self.socket_offsetCtrl.setColor("pink")
        self.socket_offsetCtrl.alignOnYAxis()
        self.socket_offsetCtrlSpace = self.socket_offsetCtrl.insertCtrlSpace()

        self.socketCtrl = Control(self.getName(), parent=self.socket_offsetCtrl, shape="null")
        self.socketCtrl.xfo = data['socketXfo']
        #self.socketCtrl.setCurveData(data['socketCtrlCrvData'])
        self.socketCtrl.setColor("pink")

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.ctrlCmpGrp.setComponent(self)

        self.socketDef = Joint(self.getName(), parent=defCmpGrp)
        self.socketDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.socketInputConstraint = self.socket_offsetCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Constraint outputs
        self.socketOutputTgtConstraint = self.socketOutputTgt.constrainTo(self.socketCtrl)
        self.socketDefConstraint = self.socketDef.constrainTo(self.socketCtrl)

        self.socketOutputTgtConstraint.evaluate()

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
        self.socketCtrl.scalePoints(globalScale)
        self.socket_offsetCtrl.scalePoints(globalScale)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSocketGuide)
ks.registerComponent(OSSSocketRig)
