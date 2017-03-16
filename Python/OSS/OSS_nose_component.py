from kraken.core.maths import Vec3, Xfo, Quat
from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV, aimAt
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import *

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.components.component_output import ComponentOutput
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.transform import Transform
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.layer import Layer
from kraken.core.objects.control import Control
from kraken.core.objects.locator import Locator

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component


COMPONENT_NAME = "nose"

class OSSNoseComponent(OSS_Component):
    """Nose Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSNoseComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.worldSRTInputTgt = self.createInput('worldSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.midLipInputTgt = self.createInput('midLip', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.noseTopOutputTgt = self.createOutput('noseTop', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.noseTipOutputTgt = self.createOutput('noseTip', dataType='Xfo', parent=self.outputHrcGrp).getTarget()



class OSSNoseComponentGuide(OSSNoseComponent):
    """Nose Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Nose Guide Component:" + name)
        super(OSSNoseComponentGuide, self).__init__(name, parent)

        self.constrainBaseToControl = BoolAttribute('constrainBaseToControl', value=False, parent=self.guideSettingsAttrGrp)
        self.constrainEndToControl = BoolAttribute('constrainEndToControl', value=False, parent=self.guideSettingsAttrGrp)

        # =========
        # Controls
        # ========
        # Guide Controls
        self.noseUpCtrl  = Control('noseUp', parent=self.ctrlCmpGrp, shape='null')
        self.noseTopCtrl = Control('noseTop', parent=self.ctrlCmpGrp, shape='circle')
        self.noseTopCtrl.scalePoints(Vec3(2, 2, 2))
        self.noseTopCtrl.setColor('red')
        self.noseMidCtrl = Control('noseMid', parent=self.ctrlCmpGrp, shape='circle')
        self.noseTipCtrl = Control('noseTip', parent=self.ctrlCmpGrp, shape='circle')
        self.noseEndCtrl = Control('noseEnd', parent=self.ctrlCmpGrp, shape='null')
        self.midLipCtrl = Control('midLipRef', parent=self.ctrlCmpGrp, shape='circle')

        self.numDeformersAttr = IntegerAttribute('numDeformers', value=4, minValue=0, maxValue=20, parent=self.guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints

        data = {
            'name': name,
            'location': 'M',
            'noseUpXfo': Xfo(Vec3(0.0, 0, -5)),
            'noseTopXfo': Xfo(Vec3(0.0, 5, 0)),
            'noseMidXfo': Xfo(Vec3(0.0, 3, 0)),
            'noseTipXfo': Xfo(Vec3(0.0, 2, 0)),
            'noseEndXfo': Xfo(Vec3(0.0, 1, 0)),
            'midLipXfo': Xfo(Vec3(0.0, 0, 0)),
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

        data = super(OSSNoseComponentGuide, self).saveData()

        # this should live in the GuideClase - also should considere Inherited Types
        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        #Reset all shapes, but really we should just recreate all controls from loadData instead of init
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSNoseComponentGuide, self).loadData( data )

        self.loadAllObjectData(data, "Control")
        self.loadAllObjectData(data, "Transform")

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.noseTopCtrl.scalePoints(globalScaleVec)
        self.noseTipCtrl.scalePoints(globalScaleVec)

        return True




    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSNoseComponentGuide, self).getRigBuildData()


        # should include getCurveData
        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")


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

        return OSSNoseComponentRig


class OSSNoseComponentRig(OSSNoseComponent):
    """Nose Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Nose Rig Component:" + name)
        super(OSSNoseComponentRig, self).__init__(name, parent)

        # =========
        # Controls
        # =========
        # NoseAimUp
        self.noseAlignSpaces = Transform('noseAlignSpaces', parent=self.ctrlCmpGrp)

        self.noseUpCtrl = Transform('noseUpCtrl', parent=self.noseAlignSpaces)

        # NoseTop
        self.noseTopCtrl = FKControl('noseTop', parent=self.ctrlCmpGrp, shape="circle", scale=1.5)
        self.noseTopCtrlSpace = self.noseTopCtrl.insertCtrlSpace()
        self.noseTopBlendSpace = Transform('noseTopBlend', parent=self.ctrlCmpGrp)
        self.noseTopFKSpace = Transform('noseTopFKSpace', parent=self.noseAlignSpaces)
        self.noseTopAlignSpace = Transform('noseTopAlign', parent=self.ctrlCmpGrp)
        # self.noseMidCtrlAlignSpace = Transform('noseMidCtrlAlignSpace', parent=self.noseTopAlignSpace)
        self.noseTopAlignSpaceRest = Transform('noseTopAlignRest', parent=self.noseAlignSpaces)

        self.noseTopDef = Joint('noseTop', parent=self.deformersParent)
        self.noseTopDef.setComponent(self)
        self.parentSpaceInputTgt.childJoints = [self.noseTopDef]

        # NoseMid
        self.noseMidCtrl = FKControl('noseMid', parent=self.noseTopCtrl, shape="circle", scale=1.5)
        self.noseMidCtrlSpaceRest = Transform('noseMidCtrlSpaceRest', parent=self.noseAlignSpaces)
        self.noseMidCtrlSpace  = self.noseMidCtrl.insertCtrlSpace()
        self.noseMidDef = Joint('noseMid', parent=self.noseTopDef)

        # NoseTip
        self.noseTipCtrl = FKControl('noseTip', parent=self.noseMidCtrl, shape="circle", scale=2)
        # self.noseTipCtrlAlignSpace = Transform('noseTipCtrlAlignSpace', parent=self.noseMidCtrlAlignSpace)
        self.noseTipCtrlSpaceRest = Transform('noseTipCtrlSpaceRest', parent=self.ctrlCmpGrp)
        self.noseTipCtrlSpace  = self.noseTipCtrl.insertCtrlSpace()
        self.noseTipDef = Joint('noseTip', parent=self.noseMidDef)

        # NoseAimObjects
        self.noseTipSpace = CtrlSpace('noseTip', parent=self.globalSRTInputTgt)

        self.midLipSpace = Transform('midLipSpace', parent=self.noseAlignSpaces)

        # Attributes
        noseSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.noseTipCtrl)
        self.alignToLip     = ScalarAttribute('alignToLip', value=.2, minValue=0.0, maxValue=1.0, parent=noseSettingsAttrGrp)
        self.midBlend       = ScalarAttribute('midBlend', value=.25, minValue=0.0, maxValue=1.0, parent=noseSettingsAttrGrp)
        self.tipBlend = ScalarAttribute('tipBlend', value=1, minValue=0.0, maxValue=1.0, parent=noseSettingsAttrGrp)

        Profiler.getInstance().pop()




    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSNoseComponentRig, self).loadData( data )
        noseTopXfo = data['noseTopXfo']
        noseMidXfo = data['noseMidXfo']
        noseTipXfo = data['noseTipXfo']
        noseEndXfo = data['noseEndXfo']
        noseUpXfo = data['noseUpXfo']
        numDeformers = data['numDeformers']


        self.noseUpCtrl.xfo = noseUpXfo
        self.noseTopCtrlSpace.xfo = noseTopXfo
        self.noseTopBlendSpace.xfo = noseTopXfo
        self.noseTopAlignSpace.xfo = noseTopXfo
        self.noseTopFKSpace.xfo = noseTopXfo
        self.noseTopAlignSpaceRest.xfo = noseTopXfo
        self.noseTopCtrl.xfo = noseTopXfo

        self.noseMidCtrl.xfo = noseMidXfo
        self.noseMidCtrlSpace.xfo = noseMidXfo
        self.noseMidCtrlSpaceRest.xfo = noseMidXfo
        # self.noseMidCtrlAlignSpace.xfo = noseMidXfo

        self.noseTipCtrlSpace.xfo = noseTipXfo
        self.noseTipCtrl.xfo = noseTipXfo
        self.noseTipCtrlSpaceRest.xfo = noseTipXfo
        # self.noseTipCtrlAlignSpace.xfo = noseTipXfo

        self.midLipSpace.xfo = self.midLipInputTgt.xfo
        self.midLipSpace.xfo = data['midLipRefXfo']
        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.midLipSpace.constrainTo(self.midLipInputTgt, maintainOffset=True).evaluate()

        # we should just set the orientation of the reference frame after evaluating the AimOperator - but for whatever reason we're not getting the proper midLipSpace in time
        noseTopOri = Quat()
        dirVec = (data['midLipRefXfo'].tr - noseTopXfo.tr).unit()
        upVec =  (noseUpXfo.tr - noseTopXfo.tr).unit()
        noseTopOri.setFromDirectionAndUpvector(dirVec,upVec)

        # ===============
        # Add Fabric Ops
        # ===============
        # Add Spine Canvas Op
        self.noseTopAimKLOP = KLOperator('noseTop', 'OSS_AimKLSolver', 'OSS_Kraken')
        self.addOperator(self.noseTopAimKLOP)
        # Add Att Inputs
        self.noseTopAimKLOP.setInput('drawDebug', self.drawDebugInputAttr)
        self.noseTopAimKLOP.setInput('rigScale', self.rigScaleInputAttr)
        self.noseTopAimKLOP.setInput('blend',  1)
        self.noseTopAimKLOP.setInput('rest', self.noseTopAlignSpaceRest)
        self.noseTopAimKLOP.setInput('ik', self.midLipSpace)
        # Add Xfo Inputs
        self.noseTopAimKLOP.setInput('up', self.noseUpCtrl)
        self.noseTopAimKLOP.setOutput('result', self.noseTopAlignSpace)


        # Add Spine Canvas Op
        # Add Att Inputs
        self.alignNoseToLipOp = self.blend_two_xfos(
            self.noseTopBlendSpace,
            self.noseTopFKSpace, self.noseTopAlignSpace,
            blendTranslate=0,
            blendRotate=self.alignToLip,
            blendScale=0,
            name= 'alignNoseToLipOp')

        # self.midBlendOp = self.blend_two_xfos(
        #     self.noseMidCtrlSpace,
        #     self.noseMidCtrlSpaceRest, self.noseMidCtrlAlignSpace,
        #     parentSpace = self.noseTopCtrl,
        #     blendTranslate=self.midBlend,
        #     blendRotate=self.midBlend,
        #     blendScale=self.midBlend,
        #     name= 'midBlendOp')

        # self.tipBlendOp = self.blend_two_xfos(
        #     self.noseTipCtrlSpace,
        #     self.noseTipCtrlSpaceRest, self.noseTipCtrlAlignSpace,
        #     parentSpace = self.ctrlCmpGrp,
        #     blendTranslate=self.tipBlend,
        #     blendRotate=self.tipBlend,
        #     blendScale=self.tipBlend,
        #     name= 'tipBlendOp')


        self.noseAlignSpaces.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        self.noseTopAimKLOP.evaluate()
        self.noseTopFKSpace.xfo.ori = noseTopOri
        self.noseTopCtrlSpace.constrainTo(self.noseTopBlendSpace, maintainOffset=True)

        self.noseTopDef.constrainTo(self.noseTopCtrl)
        self.noseMidDef.constrainTo(self.noseMidCtrl)
        self.noseTipDef.constrainTo(self.noseTipCtrl)



        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.noseTopCtrl.scalePoints(globalScale)
        self.noseTipCtrl.scalePoints(globalScale)

        self.evalOperators()
        self.noseTopOutputTgt.constrainTo(self.noseTipCtrl)
        self.noseTipOutputTgt.constrainTo(self.noseTipCtrl)

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSNoseComponentGuide)
ks.registerComponent(OSSNoseComponentRig)
