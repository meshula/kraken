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
        self.SingleFKEndOutputTgt.xfo = data[self.getName() + 'Xfo']
        self.SingleFKParentSpace = CtrlSpace(self.getName() + 'ParentSpace', parent=self.ctrlCmpGrp)
        self.SingleFKCtrlSpace = CtrlSpace(self.getName() + 'CtrlSpace', parent=self.SingleFKParentSpace)
        self.SingleFKCtrl = Control(self.getName(), parent=self.SingleFKCtrlSpace, shape="cube")
        #self.SingleFKCtrl.setCurveData(data['SingleFKCtrlCrvData'])


        self.SingleFKParentSpace.xfo = data[self.getName() + 'Xfo']
        self.SingleFKCtrlSpace.xfo = data[self.getName() + 'Xfo']
        self.SingleFKCtrl.xfo = data[self.getName() + 'Xfo']
        # ==========
        # Deformers
        # ==========
        self.SingleFKDef = Joint(self.getName(), parent=self.deformersParent)
        self.SingleFKDef.setComponent(self)
        self.selfAttachWidget = self.insertAttachSpace(self.SingleFKDef)

        self.parentSpaceInputTgt.childJoints = [self.SingleFKDef]

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.SingleFKSpaceConstraint = self.SingleFKParentSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.SingleFKEndOutputTgt.parentJoint =  self.SingleFKDef

        # WorldSpace Blend Aim
        SingleFKSettingsAttrGrp = AttributeGroup("DisplayInfo_Settings", parent=self.SingleFKCtrl)
        self.parentSpaceAttr = ScalarAttribute('alignToParent', value=1.0, minValue=0.0, maxValue=1.0, parent=SingleFKSettingsAttrGrp)
        self.worldSpaceAttr = ScalarAttribute('alignToWorld', value=0.0, minValue=0.0, maxValue=1.0, parent=SingleFKSettingsAttrGrp)

        self.ctrlShapeToggle = BoolAttribute('SingleFKCtrl', value=False, parent=SingleFKSettingsAttrGrp)
        self.selfAttachWidget.getVisibilityAttr().connect(self.ctrlShapeToggle)

        # Add Spine Canvas Op
        self.alignSpacesKLOp = KLOperator('headAlign', 'OSS_WeightedAverageMat44KLSolver', 'OSS_Kraken')
        self.addOperator(self.alignSpacesKLOp)

        self.alignSpaces = []
        self.alignWeights = []
        # Add Att Inputs
        self.alignSpacesKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.alignSpacesKLOp.setInput('rigScale', self.rigScaleInputAttr)

        self.alignSpacesKLOp.setInput('mats', self.alignSpaces)
        self.alignSpacesKLOp.setInput('matWeights', self.alignWeights)
        self.alignSpacesKLOp.setInput('translationAmt',  0)
        self.alignSpacesKLOp.setInput('scaleAmt',  0)
        self.alignSpacesKLOp.setInput('rotationAmt',  1)
        self.alignSpacesKLOp.setInput('parent',  self.SingleFKParentSpace)
        self.alignSpacesKLOp.setOutput('result', self.SingleFKCtrlSpace)



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

        # Add items into Blend
        self.alignSpaces.append(self.SingleFKParentSpace)
        self.alignSpaces.append(self.ctrlCmpGrp)

        self.alignWeights.append(self.parentSpaceAttr)
        self.alignWeights.append(self.worldSpaceAttr)

        # Constraint outputs
        self.SingleFKEndOutputTgtConstraint = self.SingleFKEndOutputTgt.constrainTo(self.SingleFKCtrl, maintainOffset=True)
        self.SingleFKDefConstraint = self.SingleFKDef.constrainTo(self.SingleFKCtrl)
        self.SingleFKEndOutputTgtConstraint.evaluate()

        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.SingleFKCtrl.scalePoints(globalScale)

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSingleFKGuide)
ks.registerComponent(OSSSingleFKRig)
