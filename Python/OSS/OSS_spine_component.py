from kraken.core.maths import Vec3

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

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *

COMPONENT_NAME = "spine"

class OSSSpineComponent(BaseExampleComponent):
    """Spine Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSSpineComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.spineCogOutputTgt = self.createOutput('cog', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.spineBaseOutputTgt = self.createOutput('spineBase', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.pelvisOutputTgt = self.createOutput('pelvis', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.spineEndOutputTgt = self.createOutput('spineEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.spineVertebraeOutput = self.createOutput('spineVertebrae', dataType='Xfo[]')

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs

        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSSpineComponentGuide(OSSSpineComponent):
    """Spine Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Spine Guide Component:" + name)
        super(OSSSpineComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # ========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)


        # Guide Controls
        self.cog = Control('cogPosition', parent=self.ctrlCmpGrp, shape="circle")
        self.cog.scalePoints(Vec3(2, 2, 2))
        self.cog.setColor('red')

        self.pelvisCtrl = Control('pelvisPosition', parent=self.ctrlCmpGrp, shape='null')
        self.torsoCtrl = Control('torsoPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.chestCtrl = Control('chestPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.upChestCtrl = Control('upChestPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.neckCtrl = Control('neckPosition', parent=self.ctrlCmpGrp, shape='null')
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        self.numDeformersAttr = IntegerAttribute('numDeformers', value=6, minValue=0, maxValue=20, parent=guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
        self.mocapInputAttr = None

        data = {
            'name': name,
            'location': 'M',
            'pelvisPosition': Vec3(0.0, 9, 0),
            'cogPosition': Vec3(0.0, 10, 0),
            'torsoPosition': Vec3(0.0, 10, 0),
            'chestPosition': Vec3(0.0, 12, 0),
            'upChestPosition': Vec3(0.0, 14, 0),
            'neckPosition': Vec3(0.0, 15, 0),
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

        data = super(OSSSpineComponentGuide, self).saveData()

        data['cogPosition'] = self.cog.xfo.tr
        data['pelvisPosition'] = self.pelvisCtrl.xfo.tr
        data['torsoPosition'] = self.torsoCtrl.xfo.tr
        data['chestPosition'] = self.chestCtrl.xfo.tr
        data['upChestPosition'] = self.upChestCtrl.xfo.tr
        data['neckPosition'] = self.neckCtrl.xfo.tr

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

        super(OSSSpineComponentGuide, self).loadData( data )

        self.cog.xfo.tr = data["cogPosition"]
        self.pelvisCtrl.xfo.tr = data["pelvisPosition"]
        self.torsoCtrl.xfo.tr = data["torsoPosition"]
        self.chestCtrl.xfo.tr = data["chestPosition"]
        self.upChestCtrl.xfo.tr = data["upChestPosition"]
        self.neckCtrl.xfo.tr = data["neckPosition"]

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.pelvisCtrl.scalePoints(globalScaleVec)
        self.torsoCtrl.scalePoints(globalScaleVec)
        self.chestCtrl.scalePoints(globalScaleVec)
        self.upChestCtrl.scalePoints(globalScaleVec)
        self.neckCtrl.scalePoints(globalScaleVec)

        return True


    def updateMocap(self, mocap):
        """ Callback to changing the component setting 'useOtherIKGoalInput'
        Really, we should build this ability into the system, to add/remove input attrs based on guide setting bools.
        That way, we don't have to write these callbacks.
        """
        if mocap:
            if self.mocapInputAttr is None:
                self.mocapInputAttr = self.createInput('mocap', dataType='Float', parent=self.cmpInputAttrGrp)

        else:
            if self.mocapInputAttr is not None:
                self.deleteInput('mocap', parent=self.cmpInputAttrGrp)
                self.mocapInputAttr = None


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSSpineComponentGuide, self).getRigBuildData()

        data['cogPosition'] = self.cog.xfo.tr
        data['hipsPosition'] = self.cog.xfo.tr
        data['pelvisPosition'] = self.pelvisCtrl.xfo.tr
        data['torsoPosition'] = self.torsoCtrl.xfo.tr
        data['chestPosition'] = self.chestCtrl.xfo.tr
        data['upChestPosition'] = self.upChestCtrl.xfo.tr
        data['neckPosition'] = self.neckCtrl.xfo.tr

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

        return OSSSpineComponentRig


class OSSSpineComponentRig(OSSSpineComponent):
    """Spine Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Spine Rig Component:" + name)
        super(OSSSpineComponentRig, self).__init__(name, parent)

        self.mocap = False
        # =========
        # Controls
        # =========

        # COG
        self.cogCtrl = FKControl('cog', parent=self.ctrlCmpGrp, shape="circle")
        self.cogCtrl.scalePoints(Vec3(6.0, 6.0, 6.0))
        self.cogCtrl.setColor("orange")
        self.cogCtrlSpace = self.cogCtrl.insertCtrlSpace()

        # hips
        self.hipsCtrl = FKControl('hips', parent=self.cogCtrl, shape="cube")
        height = 2.0
        self.hipsCtrl.scalePoints(Vec3(4.5, height, 2.5))
        self.hipsCtrl.translatePoints(Vec3(0, -height/2, 0))
        self.hipsCtrlSpace = self.hipsCtrl.insertCtrlSpace()

        # Pelvis
        self.pelvisCtrlSpace = CtrlSpace('pelvis', parent=self.hipsCtrl)
        # self.pelvisCtrl = Control('pelvis', parent=self.pelvisCtrlSpace, shape="cube")
        # self.pelvisCtrl.setColor("green")
        # self.pelvisCtrl.scalePoints(Vec3(1, 1, 1))

        # Torso
        self.torsoCtrl = FKControl('torso', parent=self.cogCtrl, shape="square")
        self.torsoCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.torsoCtrlSpace = self.torsoCtrl.insertCtrlSpace()


        # Chest
        self.chestCtrl = FKControl('chest', parent=self.torsoCtrl, shape="square")
        self.chestCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.chestCtrlSpace = self.chestCtrl.insertCtrlSpace()

        # UpChest
        self.upChestCtrl = FKControl('upChest', parent=self.chestCtrl, shape="square")
        self.upChestCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
        self.upChestCtrlSpace = self.upChestCtrl.insertCtrlSpace()

        # Neck
        self.neckCtrlSpace = CtrlSpace('neck', parent=self.upChestCtrl)

        # ==========
        # Deformers
        # ==========


        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.deformerJoints = []
        self.spineOutputs = []
        self.setNumDeformers(1)

        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.spineVertebraeOutput.setTarget(self.spineOutputs)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.cogCtrlSpaceConstraint = self.cogCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # ===============
        # Add Fabric Ops
        # ===============
        # Add Spine Canvas Op
        self.ZSplineSpineCanvasOp = CanvasOperator('ZSplineSpineCanvasOp', 'OSS.Solvers.ZSplineSpineSolver')

        self.addOperator(self.ZSplineSpineCanvasOp)

        # Add Att Inputs
        self.ZSplineSpineCanvasOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.ZSplineSpineCanvasOp.setInput('rigScale', self.rigScaleInputAttr)
        self.ZSplineSpineCanvasOp.setInput('numDeformers',  1)
        # Add Xfo Inputs
        self.ZSplineSpineCanvasOp.setInput('pelvis', self.pelvisCtrlSpace)
        self.ZSplineSpineCanvasOp.setInput('torso', self.torsoCtrl)
        self.ZSplineSpineCanvasOp.setInput('chest', self.chestCtrl)
        self.ZSplineSpineCanvasOp.setInput('upChest', self.upChestCtrl)
        self.ZSplineSpineCanvasOp.setInput('neck', self.neckCtrlSpace)
        # temp now until handles are swapped


        # Add Xfo Outputs
        self.ZSplineSpineCanvasOp.setOutput('outputs', self.spineOutputs)

        # Add Deformer Splice Op
        self.outputsToDeformersOKLOp = KLOperator('spineDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersOKLOp)

        # Add Att Inputs
        self.outputsToDeformersOKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersOKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Outputs
        self.outputsToDeformersOKLOp.setInput('constrainers', self.spineOutputs)

        # Add Xfo Outputs
        self.outputsToDeformersOKLOp.setOutput('constrainees', self.deformerJoints)



        Profiler.getInstance().pop()


    def setNumDeformers(self, numDeformers):

        # Add new deformers and outputs
        for i in xrange(len(self.spineOutputs), numDeformers):
            name = 'spine' + str(i + 1).zfill(2)
            spineOutput = ComponentOutput(name, parent=self.outputHrcGrp)
            self.spineOutputs.append(spineOutput)

        for i in xrange(len(self.deformerJoints), numDeformers):
            name = 'spine' + str(i + 1).zfill(2)
            spineDef = Joint(name, parent=self.defCmpGrp)
            spineDef.setComponent(self)
            self.deformerJoints.append(spineDef)

        if hasattr(self, 'ZSplineSpineCanvasOp'):  # Check in case this is ever called from Guide callback
            self.ZSplineSpineCanvasOp.setInput('numDeformers',  numDeformers)

        return True


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSSpineComponentRig, self).loadData( data )

        cogPosition = data['cogPosition']
        hipsPosition = data['hipsPosition']
        pelvisPosition = data['pelvisPosition']
        torsoPosition = data['torsoPosition']
        chestPosition = data['chestPosition']
        upChestPosition = data['upChestPosition']
        neckPosition = data['neckPosition']
        numDeformers = data['numDeformers']

        self.mocap = bool(data["mocap"])

        self.cogCtrlSpace.xfo.tr = cogPosition
        self.cogCtrl.xfo.tr = cogPosition

        self.hipsCtrlSpace.xfo.tr = hipsPosition
        self.hipsCtrl.xfo.tr = hipsPosition

        self.pelvisCtrlSpace.xfo.tr = pelvisPosition
        # self.pelvisCtrl.xfo.tr = pelvisPosition

        self.torsoCtrlSpace.xfo.tr = torsoPosition
        self.torsoCtrl.xfo.tr = torsoPosition

        self.chestCtrlSpace.xfo.tr = chestPosition
        self.chestCtrl.xfo.tr = chestPosition

        self.upChestCtrlSpace.xfo.tr = upChestPosition
        self.upChestCtrl.xfo.tr = upChestPosition

        self.neckCtrlSpace.xfo.tr = neckPosition
        # self.neckCtrl.xfo.tr = neckPosition

        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        # Constrain Outputs
        self.spineBaseOutputConstraint = self.spineBaseOutputTgt.constrainTo(self.spineOutputs[0])
        self.spineEndOutputConstraint = self.spineEndOutputTgt.constrainTo(self.spineOutputs[-1])

        if self.mocap:

            self.mocapInputAttr = self.createInput('mocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            # COG
            self.cogMocapCtrl = MCControl('cog', parent=self.ctrlCmpGrp, shape="circle")
            self.cogMocapCtrl.scalePoints(Vec3(5.0, 5.0, 5.0))
            self.cogMocapCtrl.setColor("purpleLight")
            self.cogMocapCtrl.xfo.tr = cogPosition
            self.cogMocapCtrlSpace = self.cogMocapCtrl.insertCtrlSpace()

            self.cogMocapCtrlSpaceConstraint = self.cogMocapCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

            # hips
            self.pelvisMocapCtrl = MCControl('pelvis', parent=self.cogMocapCtrl, shape="circle")
            height = 2.0
            self.pelvisMocapCtrl.scalePoints(Vec3(4.5, height, 2.5))
            self.pelvisMocapCtrl.setColor("purpleLight")
            self.pelvisMocapCtrl.xfo.tr = pelvisPosition
            self.pelvisMocapCtrlSpace = self.pelvisMocapCtrl.insertCtrlSpace()

            # Torso
            self.torsoMocapCtrl = MCControl('torso', parent=self.cogMocapCtrl, shape="circle")
            self.torsoMocapCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
            self.torsoMocapCtrl.setColor("purpleLight")
            self.torsoMocapCtrl.xfo.tr = torsoPosition
            self.torsoMocapCtrlSpace = self.torsoMocapCtrl.insertCtrlSpace()

            # Chest
            self.chestMocapCtrl = MCControl('chest', parent=self.torsoMocapCtrl, shape="circle")
            self.chestMocapCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
            self.chestMocapCtrl.setColor("purpleLight")
            self.chestMocapCtrl.xfo.tr = chestPosition
            self.chestMocapCtrlSpace = self.chestMocapCtrl.insertCtrlSpace()

            # UpChest
            self.upChestMocapCtrl = MCControl('upChest', parent=self.chestMocapCtrl, shape="circle")
            self.upChestMocapCtrl.scalePoints(Vec3(5.0, 3.0, 3.0))
            self.upChestMocapCtrl.setColor("purpleLight")
            self.upChestMocapCtrl.xfo.tr = upChestPosition
            self.upChestMocapCtrlSpace = self.upChestMocapCtrl.insertCtrlSpace()

            # Neck
            self.neckMocapCtrlSpace = CtrlSpace('neckPosition', parent=self.upChestMocapCtrl)
            self.neckMocapCtrlSpace.xfo.tr = neckPosition

            # Blend anim and mocap together
            self.mocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'mocap_HierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.mocapHierBlendSolver)
            self.mocapHierBlendSolver.setInput('blend', self.mocapInputAttr)  # connect this to attr
            # Add Att Inputs
            self.mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            self.mocapHierBlendSolver.setInput('hierA',
                [
                self.cogCtrl,
                self.pelvisCtrlSpace,
                self.torsoCtrl,
                self.chestCtrl,
                self.upChestCtrl,
                self.neckCtrlSpace
                ],
            )

            self.mocapHierBlendSolver.setInput('hierB',
                [
                self.cogMocapCtrl,
                self.pelvisMocapCtrlSpace,
                self.torsoMocapCtrl,
                self.chestMocapCtrl,
                self.upChestMocapCtrl,
                self.neckMocapCtrlSpace
                ]
            )
            #Create some nodes just for the ouput of the blend.
            #Wish we could just make direct connections....

            self.cogCtrlSpace_link = CtrlSpace('cogCtrlSpace_link', parent=self.outputHrcGrp)
            self.pelvisCtrlSpace_link = CtrlSpace('pelvisCtrlSpace_link', parent=self.outputHrcGrp)
            self.torsoCtrl_link = CtrlSpace('torsoCtrl_link', parent=self.outputHrcGrp)
            self.chestCtrl_link = CtrlSpace('chestCtrl_link', parent=self.outputHrcGrp)
            self.upChestCtrl_link = CtrlSpace('upChestCtrl_link', parent=self.outputHrcGrp)
            self.neckCtrlSpace_link = CtrlSpace('neckCtrlSpace_link', parent=self.outputHrcGrp)

            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.cogCtrlSpace_link,
                self.pelvisCtrlSpace_link,
                self.torsoCtrl_link,
                self.chestCtrl_link,
                self.upChestCtrl_link,
                self.neckCtrlSpace_link
                ]
            )
            self.mocapHierBlendSolver.setInput("parentIndexes", [-1, 0, 0, 2, 3, 4])
            self.mocapHierBlendSolver.evaluate()

            # Add Xfo Outputs
            self.ZSplineSpineCanvasOp.setInput('pelvis', self.pelvisCtrlSpace_link)
            self.ZSplineSpineCanvasOp.setInput('torso', self.torsoCtrl_link)
            self.ZSplineSpineCanvasOp.setInput('chest', self.chestCtrl_link)
            self.ZSplineSpineCanvasOp.setInput('upChest', self.upChestCtrl_link)
            self.ZSplineSpineCanvasOp.setInput('neck', self.neckCtrlSpace_link)

            self.spineCogOutputConstraint = self.spineCogOutputTgt.constrainTo(self.cogCtrlSpace_link)
            self.pelvisOutputConstraint = self.pelvisOutputTgt.constrainTo(self.pelvisCtrlSpace_link)
        else:     # Constraint outputs
            self.spineCogOutputConstraint = self.spineCogOutputTgt.constrainTo(self.cogCtrl)
            self.pelvisOutputConstraint = self.pelvisOutputTgt.constrainTo(self.pelvisCtrlSpace)


        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()

        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.spineCogOutputConstraint.evaluate()
        self.spineBaseOutputConstraint.evaluate()
        self.pelvisOutputConstraint.evaluate()
        self.spineEndOutputConstraint.evaluate()
        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


        # ====================
        # Extra Shape Mods
        # ====================
        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.cogCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.hipsCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.torsoCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.chestCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.upChestCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], 1.0, data['globalComponentCtrlSize']))

        if self.mocap:
            self.cogMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.pelvisMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.torsoMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.chestMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
            self.upChestMocapCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], 1.0, data['globalComponentCtrlSize']))


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSpineComponentGuide)
ks.registerComponent(OSSSpineComponentRig)
