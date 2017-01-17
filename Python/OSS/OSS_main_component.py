from kraken.core.maths import Vec3, Vec3, Euler, Quat, Xfo
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import *

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint


from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.transform import Transform
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control
from kraken.core.objects.control import Curve

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from kraken.core.configs.config import Config

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "main"

class OSSMainComponent(OSS_Component):
    """Main Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None, data=None):
        super(OSSMainComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # The graph throws error when this is not here.
        # Seems like we can't connect inputs to outputs of the same name.
        # Have Eric / Phil take a look at this
        self.removeInputByName("rigScale")

        # Declare Output Xfos
        self.masterOutputTgt = self.createOutput('master', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.offsetOutputTgt = self.createOutput('offset', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.cogOutputTgt = self.createOutput('cog', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.rootOutputTgt = self.createOutput('root', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        # Declare Input Attrs

        # Declare Output Attrs
        self.rigScaleOutputAttr = self.createOutput('rigScale', dataType='Float', value=1.0, parent=self.cmpOutputAttrGrp).getTarget()



class OSSMainComponentGuide(OSSMainComponent):
    """Main Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Main Guide Component:" + name)
        super(OSSMainComponentGuide, self).__init__(name, parent)

        # =========
        # Attributes
        # =========
        self.mocap = False

        # Guide Settings
        #self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
        self.rootMotionBlendDefault = ScalarAttribute('rootMotionBlendDefault', value=1.0, minValue=0.0, maxValue=1.0, parent=self.guideSettingsAttrGrp)
        self.createCogControl = BoolAttribute('createCogControl', value=True, parent=self.guideSettingsAttrGrp)
        self.createOffsetControl = BoolAttribute('createOffsetControl', value=True, parent=self.guideSettingsAttrGrp)
        self.createRootControl = BoolAttribute('createRootControl', value=True, parent=self.guideSettingsAttrGrp)
        self.createCogJoint = BoolAttribute('createCogJoint', value=False, parent=self.guideSettingsAttrGrp)
        self.mainCtrlShape = StringAttribute('mainCtrlShape', value="MASTER_SHAPE", parent=self.guideSettingsAttrGrp)
        # =========
        # Controls
        # =========

        # Guide Controls
        self.mainCtrl = Control('master', shape='circle', parent=self.ctrlCmpGrp)
        if self.mainCtrlShape not in Config.getInstance().getControlShapes().keys():
            self.mainCtrl.setCurveData(MASTER_SHAPE) #Why does this not work for guide controls?
        else:
            self.mainCtrl.setShape(self.mainCtrlShape) #Why does this not work for guide controls?


        self.cogCtrl = Control('cogPosition', parent=self.ctrlCmpGrp, shape="circle")
        self.cogCtrl.scalePoints(Vec3(2, 2, 2))
        self.cogCtrl.setColor('red')

        self.visIconCtrl = Control('visPosition', parent=self.ctrlCmpGrp)

        self.mocapIconCtrl = None

        self.init_data = {
                "mainXfo": Xfo(tr=Vec3(0.0, 0.0, 0.0)),
                "cogPosition": Vec3(0.0, 10.0, 0.0),
                "visIconXfo": Xfo(tr=Vec3(0.0, 0.0, 5.0)),
                "mocapIconXfo": Xfo(tr=Vec3(0.0, 0.0, 5.0)),
               }

        self.loadData(self.init_data)

        Profiler.getInstance().pop()


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """
        data = dict(self.init_data)
        data.update(super(OSSMainComponentGuide, self).saveData())

        data["mainXfo"] = self.mainCtrl.xfo
        data['cogPosition'] = self.cogCtrl.xfo.tr
        data['visIconXfo'] = self.visIconCtrl.xfo

        if self.mocap:
            data['mocapIconXfo'] = self.mocapIconCtrl.xfo

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

        #saveData() will grab the guide settings values (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSMainComponentGuide, self).loadData(data)


        self.mainCtrl.xfo = data["mainXfo"]
        self.mainCtrl.scalePoints(Vec3(10, 1.0, 10))
        self.mainCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))

        self.cogCtrl.xfo.tr = data["cogPosition"]

        self.cogCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))

        self.mocap = bool(data["mocap"])

        if self.mocap:
            if 'mocapIconXfo' in data.keys():
                self.mocapIconCtrl.xfo = data['mocapIconXfo']
                self.mocapIconCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))

        self.visIconCtrl.xfo = data['visIconXfo']
        if "oss_vis" not in Config.getInstance().getControlShapes():
            self.visIconCtrl.setCurveData(VIS_SHAPE)
        self.visIconCtrl.scalePoints(Vec3(8, 1.0, 8))
        self.visIconCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))

        return True



    def updateMocap(self, mocap):
        """ Callback to changing the component setting 'useOtherIKGoalInput'
        Really, we should build this ability into the system, to add/remove input attrs based on guide setting bools.
        That way, we don't have to write these callbacks.
        """
        if mocap:
            if self.mocapIconCtrl is None:
                self.mocapIconCtrl = Control('mocapIcon', parent=self.ctrlCmpGrp)
                self.mocapIconCtrl.setCurveData(MOCAP_SHAPE)
                self.mocapIconCtrl.setColor("mediumpurple")
                self.mocapIconCtrl.scalePoints(Vec3(2.0, 2.0, 2.0))
                self.mocapIconCtrl.xfo.tr = Vec3(0.0, 0.0, 3.0)  #How to load default in this callback without access to data?
                self.mocap = True


        else:
            if self.mocapIconCtrl is not None:
                self.mocapIconCtrl.getParent().removeChild(self.mocapIconCtrl) #There should be a simpler way!
                self.mocapIconCtrl = None
                self.mocap = False




    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """
        data = super(OSSMainComponentGuide, self).getRigBuildData()

        data["mainXfo"] = self.mainCtrl.xfo
        data['cogPosition'] = self.cogCtrl.xfo.tr
        data['visIconXfo'] = self.visIconCtrl.xfo

        if self.mocap:
            data['mocapIconXfo'] = self.mocapIconCtrl.xfo

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


        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSMainComponentRig, self).loadData(data)

        self.mocap = bool(data["mocap"])

        self.mocap = False

        # =========
        # Controls
        # =========
        # Add Controls
        self.mainCtrlShape = str(data['mainCtrlShape'])
        self.mainCtrl = FKControl('master', shape='circle', parent=self.ctrlCmpGrp)

        if self.mainCtrlShape not in Config.getInstance().getControlShapes():
            self.mainCtrl.setCurveData(MASTER_SHAPE) #Why does this not work for guide controls?
        else:
            self.mainCtrl.setShape(self.mainCtrlShape) #Why does this not work for guide controls?

        self.mainCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZXY"])  #Set with component settings later
        self.mainCtrl.setColor("lightsalmon")
        self.mainCtrl.lockScale(x=True, y=True, z=True)
        self.mainCtrlSpace = self.mainCtrl.insertCtrlSpace()

        # COG
        self.createOffsetControl = bool(data['createOffsetControl'])

        if self.createOffsetControl:
            self.offsetCtrl = FKControl('offset', shape='circle', parent=self.mainCtrl)
            self.offsetCtrl.setColor("steelblue")
            if "oss_master" not in Config.getInstance().getControlShapes():
                self.offsetCtrl.setCurveData(MASTER_SHAPE)
            self.offsetCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"] * 0.6, 1.0, data["globalComponentCtrlSize"] * 0.6))  # fix this scale issue
        else:
            self.offsetCtrl = Transform('cog', parent=self.mainCtrl)

        self.offsetCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZXY"])  #Set with component settings later
        self.offsetCtrl.lockScale(x=True, y=True, z=True)
        self.offsetCtrlSpace = self.insertParentSpace(self.offsetCtrl)


        self.createRootControl = bool(data['createRootControl'])
        if self.createRootControl:
            self.rootCtrl = FKControl('root', shape='arrow', parent=self.mainCtrl)
            self.rootCtrl.setColor("gold")
            self.rootCtrl.scalePoints(Vec3(10.0, 10.0, 5.0))
            self.rootCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"] * 0.6, 1.0, data["globalComponentCtrlSize"] * 0.6))  # fix this scale issue
        else:
            self.rootCtrl = Transform('root', parent=self.mainCtrl)


        self.rootCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZXY"])  #Set with component settings later
        self.rootCtrl.lockScale(x=True, y=True, z=True)
        rootMotionBlendAttrGrp = AttributeGroup("______", parent=self.rootCtrl)
        self.rootMotionBlendDefault = data['rootMotionBlendDefault']
        self.rootCtrl.rootMotionBlendAttr  = ScalarAttribute('rootMotionBlend', value=self.rootMotionBlendDefault, minValue=0.0, maxValue=1.0, parent=rootMotionBlendAttrGrp)
        self.rootCtrlSpace = self.insertParentSpace(self.rootCtrl)


        # Just for visibility, so animators can see where joint control is
        self.rootMotionCtrl = Control('root_motion', shape='arrow', parent=self.ctrlCmpGrp)
        self.rootMotionCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["XYZ"])  #Match root joint so Euler values are same for debugging
        self.rootMotionCtrl.setColor("gray")
        self.rootMotionCtrl.lockTranslation(x=True, y=True, z=True)
        self.rootMotionCtrl.lockRotation(x=True, y=True, z=True)
        self.rootMotionCtrl.lockScale(x=True, y=True, z=True)
        self.rootMotionCtrl.scalePoints(Vec3(10.0, 10.0, 5.0))
        self.rootMotionCtrl.scalePoints(Vec3(0.3, 0.3, 0.3))
        self.rootMotionCtrlSpace = self.rootMotionCtrl.insertCtrlSpace()

        # Just for visibility, so animators can see where auto root is
        self.autoRootCtrl = Control('auto_root', shape='arrow', parent=self.mainCtrl)

        self.autoRootCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZXY"])  #MUST be ZXY to match aim in Z axis and Y-up from COG ori constraint
        self.autoRootCtrl.setColor("gray")
        self.autoRootCtrl.lockTranslation(x=True, y=True, z=True)
        self.autoRootCtrl.lockRotation(x=True, y=True, z=True)
        self.autoRootCtrl.lockScale(x=True, y=True, z=True)
        self.autoRootCtrl.scalePoints(Vec3(10.0, 10.0, 5.0))
        self.autoRootCtrl.scalePoints(Vec3(0.95, 0.95, 0.99))
        YFollowBlendAttrGrp = AttributeGroup("______", parent=self.autoRootCtrl)
        self.autoRootCtrl.YFollowBlendAttr  = ScalarAttribute('YFollowBlend', value=0, minValue=0.0, maxValue=1.0, parent=YFollowBlendAttrGrp)
        self.autoRootCtrlSpace = self.autoRootCtrl.insertCtrlSpace()
        # Haven't made this a fabric system yet


        # COG
        self.createCogControl = bool(data['createCogControl'])

        if self.createCogControl:
            self.cogCtrl = FKControl('cog', parent=self.offsetCtrl, shape="circle")
            self.cogCtrl.scalePoints(Vec3(10.0, 10.0, 10.0))
            self.cogCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.cogCtrl.setColor("orange")

        else:
            self.cogCtrl = Transform('cog', parent=self.offsetCtrl)


        self.cogCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["ZXY"])  #Set with component settings later
        self.cogCtrlSpace = self.insertParentSpace(self.cogCtrl)
        self.cog_root_offset = Transform('cog_root_offset', parent=self.cogCtrl)

        # VIS
        self.visIconCtrl = Control('vis', parent=self.ctrlCmpGrp)
        if "oss_vis" not in Config.getInstance().getControlShapes():
            self.visIconCtrl.setCurveData(VIS_SHAPE)
        self.visIconCtrl.scalePoints(Vec3(0.5, 0.5, 0.5))
        self.visIconCtrl.setColor("gold")
        self.visIconCtrl.constrainTo(self.mainCtrl, maintainOffset=True)

        # Add Component Params to IK control
        MainSettingsAttrGrp = AttributeGroup('DisplayInfo_MainSettings', parent=self.mainCtrl)
        self.rigScaleAttr = ScalarAttribute('rigScale', value=1.0, parent=MainSettingsAttrGrp, minValue=0.1, maxValue=100.0)

        self.rigScaleOutputAttr.connect(self.rigScaleAttr)

        # ==========
        # Deformers
        # ==========
        self.deformersLayer = self.getOrCreateLayer('deformers')
        self.deformersParent = self.deformersLayer



        # ==========
        # Deformers
        # ==========


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        # Constraint outputs
        self.masterOutputTgtConstraint = self.masterOutputTgt.constrainTo(self.mainCtrl)
        self.offsetOutputTgtConstraint = self.offsetOutputTgt.constrainTo(self.offsetCtrl)


        # ===============
        # Add Splice Ops
        # ===============
        #Add Rig Scale Splice Op
        self.rigScaleKLOp = KLOperator('scale', 'RigScaleSolver', 'Kraken')
        self.addOperator(self.rigScaleKLOp)

        # Add Att Inputs
        self.rigScaleKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.rigScaleKLOp.setInput('rigScale', self.rigScaleOutputAttr)

        # Add Xfo Inputs

        # Add Xfo Outputs
        self.rigScaleKLOp.setOutput('target', self.mainCtrlSpace)



        # ================
        # Resize Controls
        # ================
        self.mainCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], data["globalComponentCtrlSize"], data["globalComponentCtrlSize"]))
        self.rootMotionCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"] * 0.6, 1.0, data["globalComponentCtrlSize"] * 0.6))  # fix this scale issue
        self.autoRootCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"] * 0.6, 1.0, data["globalComponentCtrlSize"] * 0.6))  # fix this scale issue


        # =======================
        # Set Control Transforms
        # =======================
        self.mainCtrlSpace.xfo = data["mainXfo"]
        self.mainCtrl.xfo = data["mainXfo"]
        self.offsetCtrlSpace.xfo = data["mainXfo"]
        self.offsetCtrl.xfo = data["mainXfo"]
        self.rootCtrl.xfo = data["mainXfo"]

        self.cogCtrlSpace.xfo.tr = data["cogPosition"]
        self.cogCtrl.xfo.tr = data["cogPosition"]

        self.cog_root_offset.xfo.tr = data["cogPosition"]
        self.cog_root_offset.xfo.tr.x = 0  # reset to zero for root motion
        self.cog_root_offset.xfo.tr.z = 0 # reset to zero for root motion



        self.visIconCtrl.xfo = data['visIconXfo']
        self.visIconCtrl.scalePoints(Vec3(8, 1.0, 8))
        self.visIconCtrl.scalePoints(Vec3(data["globalComponentCtrlSize"], 1.0, data["globalComponentCtrlSize"]))


        if self.mocap:


            self.mocapIconCtrl = Control('mocap', parent=self.ctrlCmpGrp)
            if "oss_mocap" not in Config.getInstance().getControlShapes():
                self.mocapIconCtrl.setCurveData(MOCAP_SHAPE)
            self.mocapIconCtrl.xfo = data["mocapIconXfo"]
            self.mocapIconCtrl.setColor("mediumpurple")
            self.mocapIconCtrl.scalePoints(Vec3(2.0, 2.0, 2.0))
            self.mocapIconCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))

            self.mocapIconCtrl.constrainTo(self.offsetCtrl, maintainOffset=True)

            self.mocapIconAttrGrp = AttributeGroup("___Mocap___", parent=self.mocapIconCtrl)

            self.mocapInputAttr = ScalarAttribute('mocap', value=0.0, minValue=0.0, maxValue=1.0, parent=self.mocapIconAttrGrp)

            # COG
            self.cogMocapCtrl = MCControl('cog', parent=self.offsetCtrl, shape="circle")
            self.cogMocapCtrl.setColor("mediumpurple")
            self.cogMocapCtrl.xfo.tr = data["cogPosition"]
            self.cogMocapCtrlSpace = self.cogMocapCtrl.insertCtrlSpace()

            self.cogMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))

            #Maybe we should add an aditional master mc offset?

             # Blend anim and mocap together
            self.mocapHierBlendSolver = KLOperator(self.getName()+'mocap', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.mocapHierBlendSolver)
            self.mocapHierBlendSolver.setInput('blend', self.mocapInputAttr)  # connect this to attr
            # Add Att Inputs
            self.mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.mocapHierBlendSolver.setInput('rigScale', self.rigScaleAttr)
            # Add Xfo Inputs
            self.mocapHierBlendSolver.setInput('hierA',[self.cogCtrl])
            self.mocapHierBlendSolver.setInput('hierB',[self.cogMocapCtrl])
            self.cogCtrl_link = Transform('cogCtrlSpace_link', parent=self.outputHrcGrp)
            self.mocapHierBlendSolver.setOutput('hierOut',[self.cogCtrl_link])

            self.mocapHierBlendSolver.evaluate()

            # Add Xfo Outputs
            self.cogOutputTgtConstraint = self.cogOutputTgt.constrainTo(self.cogCtrl_link)
        else:     # Constraint outputs
            self.cogOutputTgtConstraint = self.cogOutputTgt.constrainTo(self.cogCtrl)


        blendTRSOp = gnOp = self.blend_two_xfos(
            self.rootOutputTgt,
            self.rootCtrl, self.autoRootCtrl,
            blend=self.rootCtrl.rootMotionBlendAttr,
            name= 'RootMotionBlendKLOp')

        self.rootMotionCtrl.constrainTo(self.rootOutputTgt)

        self.rootDef = Joint('root', parent=self.deformersParent)
        self.rootDef.setComponent(self) # Need an elegant automatic way to do this
        self.rootDef.constrainTo(self.rootOutputTgt)
        # COG
        self.createCogJoint = bool(data['createCogJoint'])
        if self.createCogJoint:
            self.cogDef = Joint('cog', parent=self.rootDef)
            self.cogDef.constrainTo(self.cogCtrl, maintainOffset=False)

        #Set all parents to rootDef since that is the only joint option
        self.rootOutputTgt.parentJoint = self.rootDef
        self.masterOutputTgt.parentJoint = self.rootDef
        self.offsetOutputTgt.parentJoint = self.rootDef
        self.cogOutputTgt.parentJoint = self.rootDef

        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()

        self.masterOutputTgtConstraint.evaluate()
        self.offsetOutputTgtConstraint.evaluate()
        self.cogOutputTgtConstraint.evaluate()

        self.tagJointsWithPartNames([self.getDecoratedName()])


VIS_SHAPE = [
 {'closed': False,
  'degree': 3,
  'points': [[0.5, 0.0, -0.5],
             [0.333, 0.0, -0.213],
             [0.165, 0.0, 0.075],
             [-0.0, 0.0, 0.364]]},
 {'closed': False,
  'degree': 3,
  'points': [[-0.5, 0.0, -0.5],
             [-0.328, 0.0, -0.212],
             [-0.16, 0.0, 0.076],
             [-0.0, 0.0, 0.364]]}]


MOCAP_SHAPE = [{'closed': False,
  'degree': 3,
  'points': [[0.5, 0.0, -0.5],
             [0.5, 0.0, -0.167],
             [0.5, 0.0, 0.167],
             [0.5, 0.0, 0.5]]},
 {'closed': False,
  'degree': 3,
  'points': [[-0.5, 0.0, 0.5],
             [-0.5, 0.0, 0.167],
             [-0.5, 0.0, -0.167],
             [-0.5, 0.0, -0.5]]},
 {'closed': False,
  'degree': 3,
  'points': [[0.5, 0.0, -0.5],
             [0.333, 0.0, -0.213],
             [0.165, 0.0, 0.075],
             [-0.0, 0.0, 0.364]]},
 {'closed': False,
  'degree': 3,
  'points': [[-0.5, 0.0, -0.5],
             [-0.328, 0.0, -0.212],
             [-0.16, 0.0, 0.076],
             [-0.0, 0.0, 0.364]]}]



MASTER_SHAPE =     [
      {
      "points":  [
                   [3.3166, 0.0000, 11.2661],
                   [3.3166, 0.0000, 12.1030],
                   [5.5276, 0.0000, 12.1030],
                   [0.0000, 0.0000, 16.2875],
                   [-5.5276, 0.0000, 12.1030],
                   [-3.3166, 0.0000, 12.1030],
                   [-3.3166, 0.0000, 11.2661],
                 ],
      "degree":  1,
      "closed": False,
      },
      {
      "points":  [
                   [3.3166, 0.0000, 11.2661],
                   [3.3166, 0.0000, 11.2661],
                   [4.5318, 0.0000, 10.9408],
                   [6.5792, 0.0000, 9.8464],
                   [8.3737, 0.0000, 8.3737],
                   [9.8464, 0.0000, 6.5792],
                   [10.9408, 0.0000, 4.5318],
                   [11.6147, 0.0000, 2.3103],
                   [11.8422, 0.0000, 0.0000],
                   [11.6147, 0.0000, -2.3103],
                   [10.9408, 0.0000, -4.5318],
                   [9.8464, 0.0000, -6.5792],
                   [8.3737, 0.0000, -8.3737],
                   [6.5792, 0.0000, -9.8464],
                   [4.5318, 0.0000, -10.9408],
                   [0.0000, 0.0000, -12.0087],
                   [-4.5318, 0.0000, -10.9408],
                   [-6.5792, 0.0000, -9.8464],
                   [-8.3737, 0.0000, -8.3737],
                   [-9.8464, 0.0000, -6.5792],
                   [-10.9408, 0.0000, -4.5318],
                   [-11.6147, 0.0000, -2.3103],
                   [-11.8422, 0.0000, 0.0000],
                   [-11.6147, 0.0000, 2.3103],
                   [-10.9408, 0.0000, 4.5318],
                   [-9.8464, 0.0000, 6.5792],
                   [-8.3737, 0.0000, 8.3737],
                   [-6.5792, 0.0000, 9.8464],
                   [-4.5318, 0.0000, 10.9408],
                   [-3.3166, 0.0000, 11.2661],
                   [-3.3166, 0.0000, 11.2661],
                 ],
      "degree":  3,
      "closed": False,
      },
     ]

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMainComponentGuide)
ks.registerComponent(OSSMainComponentRig)


