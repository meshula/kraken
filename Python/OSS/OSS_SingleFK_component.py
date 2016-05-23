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

COMPONENT_NAME = "SingleFK"


class OSSSingleFK(OSS_Component):
    """SingleFK Component Base"""

    def __init__(self, name='SingleFK', parent=None):
        super(OSSSingleFK, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.SingleFKStartOutputTgt = self.createOutput('start', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.SingleFKEndOutputTgt = self.createOutput('end', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs


class OSSSingleFKGuide(OSSSingleFK):
    """SingleFK Component Guide"""

    def __init__(self, name='SingleFK', parent=None):

        Profiler.getInstance().push("Construct SingleFK Guide Component:" + name)
        super(OSSSingleFKGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.SingleFKCtrl = Control(self.getName() , parent=self.ctrlCmpGrp, shape="null")
        self.SingleFKEndCtrl = Control(self.getName() + 'End', shape="cube", parent=self.SingleFKCtrl)

        data = {
                "name": name,
                "location": "M",
                self.getName() + "SingleFKCtrlXfo": Xfo(Vec3(0.0, 0.0, 0.0)),
                self.getName() + "EndCtrlXfo": Xfo(Vec3(0.0, 1.0, 0.0)),
                self.getName() + 'CrvData': self.SingleFKCtrl.getCurveData()
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

        data = super(OSSSingleFKGuide, self).saveData()

        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")
        #data['SingleFKCtrlCrvData'] = self.SingleFKCtrl.getCurveData()
        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data


        super(OSSSingleFKGuide, self).loadData( data )


        self.loadAllObjectData(data, "Control")
        self.loadAllObjectData(data, "Transform")


        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.SingleFKCtrl.scalePoints(globalScaleVec)
        for d in data:
            print d
        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSSingleFKGuide, self).getRigBuildData()


        # should include getCurveData
        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")
        print data

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

        return OSSSingleFKRig


class OSSSingleFKRig(OSSSingleFK):
    """SingleFK Component"""

    def __init__(self, name='SingleFK', parent=None):

        Profiler.getInstance().push("Construct SingleFK Rig Component:" + name)
        super(OSSSingleFKRig, self).__init__(name, parent)



    def createControls(self, data):

        # =========
        # Controls
        # =========
        # SingleFK

        self.SingleFK_offsetCtrl = Control(self.getName() + '_offset', parent=self.ctrlCmpGrp, shape="cube")
        self.SingleFK_offsetCtrl.xfo = data[self.getName() + 'Xfo']
        self.SingleFK_offsetCtrl.alignOnXAxis()
        self.SingleFK_offsetCtrlSpace = self.SingleFK_offsetCtrl.insertCtrlSpace()

        self.SingleFKCtrl = Control(self.getName(), parent=self.SingleFK_offsetCtrl, shape="null")
        self.SingleFKCtrl.xfo = data[self.getName() + 'Xfo']
        self.SingleFKEndOutputTgt.xfo = data[self.getName() + 'EndXfo']
        #self.SingleFKCtrl.setCurveData(data['SingleFKCtrlCrvData'])

        # ==========
        # Deformers
        # ==========
        self.SingleFKDef = Joint(self.getName(), parent=self.deformersParent)
        self.SingleFKDef.setComponent(self)

        self.parentSpaceInputTgt.childJoints = [self.SingleFKDef]

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.SingleFKInputConstraint = self.SingleFK_offsetCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Constraint outputs
        self.SingleFKStartOutputTgtConstraint = self.SingleFKStartOutputTgt.constrainTo(self.SingleFKCtrl)
        self.SingleFKEndOutputTgtConstraint = self.SingleFKEndOutputTgt.constrainTo(self.SingleFKCtrl, maintainOffset=True)
        self.SingleFKDefConstraint = self.SingleFKDef.constrainTo(self.SingleFKCtrl)
        self.SingleFKStartOutputTgtConstraint.evaluate()
        self.SingleFKEndOutputTgtConstraint.evaluate()

        self.SingleFKStartOutputTgt.parentJoint =  self.SingleFKDef
        self.SingleFKEndOutputTgt.parentJoint =  self.SingleFKDef

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSSingleFKRig, self).loadData( data )

        self.createControls(data)


        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.SingleFKCtrl.scalePoints(globalScale)
        self.SingleFK_offsetCtrl.scalePoints(globalScale)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSingleFKGuide)
ks.registerComponent(OSSSingleFKRig)
