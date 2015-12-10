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
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.layer import Layer
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


class OSSSpineComponent(BaseExampleComponent):
    """Spine Component"""

    def __init__(self, name="spineBase", parent=None):
        super(OSSSpineComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.spineMainSrtInputTgt = self.createInput('mainSrt', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.spineCogOutputTgt = self.createOutput('cog', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.spineBaseOutputTgt = self.createOutput('spineBase', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.pelvisOutputTgt = self.createOutput('pelvis', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.spineEndOutputTgt = self.createOutput('spineEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.spineVertebraeOutput = self.createOutput('spineVertebrae', dataType='Xfo[]')

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()
        self.lengthInputAttr = self.createInput('length', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs

        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)

class OSSSpineComponentGuide(OSSSpineComponent):
    """Spine Component Guide"""

    def __init__(self, name='spine', parent=None):

        Profiler.getInstance().push("Construct Spine Guide Component:" + name)
        super(OSSSpineComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # ========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.numDeformersAttr = IntegerAttribute('numDeformers', value=1, minValue=0, maxValue=20, parent=guideSettingsAttrGrp)

        # Guide Controls
        self.cog = Control('cogPosition', parent=self.ctrlCmpGrp, shape="sphere")
        self.cog.scalePoints(Vec3(1.2, 1.2, 1.2))
        self.cog.setColor('red')

        self.torsoCtrl = Control('torsoPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.chestCtrl = Control('chestPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.upChestCtrl = Control('upChestPosition', parent=self.ctrlCmpGrp, shape='sphere')
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        self.loadData({
            'name': name,
            'location': 'M',
            'cogPosition': Vec3(0.0, 11.1351, -0.1382),
            'torsoPosition': Vec3(0.0, 11.1351, -0.1382),
            'chestPosition': Vec3(0.0, 11.8013, -0.1995),
            'upChestPosition': Vec3(0.0, 12.4496, -0.3649),
            'numDeformers': 6,
            'globalComponentCtrlSize': 1.0
        })

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
        data['torsoPosition'] = self.torsoCtrl.xfo.tr
        data['chestPosition'] = self.chestCtrl.xfo.tr
        data['upChestPosition'] = self.upChestCtrl.xfo.tr
        data['numDeformers'] = self.numDeformersAttr.getValue()

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSSpineComponentGuide, self).loadData( data )

        self.cog.xfo.tr = data["cogPosition"]
        self.torsoCtrl.xfo.tr = data["torsoPosition"]
        self.chestCtrl.xfo.tr = data["chestPosition"]
        self.upChestCtrl.xfo.tr = data["upChestPosition"]
        self.numDeformersAttr.setValue(data["numDeformers"])

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.torsoCtrl.scalePoints(globalScaleVec)
        self.chestCtrl.scalePoints(globalScaleVec)
        self.upChestCtrl.scalePoints(globalScaleVec)

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSSpineComponentGuide, self).getRigBuildData()

        data['cogPosition'] = self.cog.xfo.tr
        data['torsoPosition'] = self.torsoCtrl.xfo.tr
        data['chestPosition'] = self.chestCtrl.xfo.tr
        data['upChestPosition'] = self.upChestCtrl.xfo.tr
        data['numDeformers'] = self.numDeformersAttr.getValue()

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

    def __init__(self, name="spine", parent=None):

        Profiler.getInstance().push("Construct Spine Rig Component:" + name)
        super(OSSSpineComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # COG
        self.cogCtrlSpace = CtrlSpace('cog', parent=self.ctrlCmpGrp)
        self.cogCtrl = Control('cog', parent=self.cogCtrlSpace, shape="circle")
        self.cogCtrl.scalePoints(Vec3(6.0, 6.0, 6.0))
        self.cogCtrl.setColor("orange")

        # Torso
        self.torsoCtrlSpace = CtrlSpace('torso', parent=self.cogCtrl)
        self.torsoCtrl = Control('torso', parent=self.torsoCtrlSpace, shape="circle")
        self.torsoCtrl.scalePoints(Vec3(4.0, 4.0, 4.0))
        self.torsoCtrl.setColor("blue")

        # Chest
        self.chestCtrlSpace = CtrlSpace('chest', parent=self.torsoCtrl)
        self.chestCtrl = Control('chest', parent=self.chestCtrlSpace, shape="circle")
        self.chestCtrl.scalePoints(Vec3(4.5, 4.5, 4.5))


        # UpChest
        self.upChestCtrlSpace = CtrlSpace('upChest', parent=self.chestCtrl)
        self.upChestCtrl = Control('upChest', parent=self.upChestCtrlSpace, shape="circle")
        self.upChestCtrl.scalePoints(Vec3(6.0, 6.0, 6.0))
        self.upChestCtrl.setColor("blue")

        # Pelvis
        self.pelvisCtrlSpace = CtrlSpace('pelvis', parent=self.cogCtrl)
        self.pelvisCtrl = Control('pelvis', parent=self.pelvisCtrlSpace, shape="cube")
        self.pelvisCtrl.alignOnYAxis(negative=True)
        self.pelvisCtrl.scalePoints(Vec3(2.0, 1.5, 1.5))


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.deformerJoints = []
        self.spineOutputs = []
        self.setNumDeformers(1)

        pelvisDef = Joint('pelvis', parent=self.defCmpGrp)
        pelvisDef.setComponent(self)

        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.spineVertebraeOutput.setTarget(self.spineOutputs)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.spineSrtInputConstraint = PoseConstraint('_'.join([self.cogCtrlSpace.getName(), 'To', self.spineMainSrtInputTgt.getName()]))
        self.spineSrtInputConstraint.addConstrainer(self.spineMainSrtInputTgt)
        self.spineSrtInputConstraint.setMaintainOffset(True)
        self.cogCtrlSpace.addConstraint(self.spineSrtInputConstraint)

        # Constraint outputs
        self.spineCogOutputConstraint = PoseConstraint('_'.join([self.spineCogOutputTgt.getName(), 'To', self.cogCtrl.getName()]))
        self.spineCogOutputConstraint.addConstrainer(self.cogCtrl)
        self.spineCogOutputTgt.addConstraint(self.spineCogOutputConstraint)

        self.spineBaseOutputConstraint = PoseConstraint('_'.join([self.spineBaseOutputTgt.getName(), 'To', 'spineBase']))
        self.spineBaseOutputConstraint.addConstrainer(self.spineOutputs[0])
        self.spineBaseOutputTgt.addConstraint(self.spineBaseOutputConstraint)

        self.pelvisOutputConstraint = PoseConstraint('_'.join([self.pelvisOutputTgt.getName(), 'To', self.pelvisCtrl.getName()]))
        self.pelvisOutputConstraint.addConstrainer(self.pelvisCtrl)
        self.pelvisOutputTgt.addConstraint(self.pelvisOutputConstraint)

        self.spineEndOutputConstraint = PoseConstraint('_'.join([self.spineEndOutputTgt.getName(), 'To', 'spineEnd']))
        self.spineEndOutputConstraint.addConstrainer(self.spineOutputs[0])
        self.spineEndOutputTgt.addConstraint(self.spineEndOutputConstraint)


        # ===============
        # Add Splice Ops
        # ===============
        # Add Spine Splice Op
        self.bezierSpineKLOp = KLOperator('spineKLOp', 'BezierSpineSolver', 'Kraken')
        self.addOperator(self.bezierSpineKLOp)

        # Add Att Inputs
        self.bezierSpineKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.bezierSpineKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.bezierSpineKLOp.setInput('length', self.lengthInputAttr)

        # Add Xfo Inputs
        self.bezierSpineKLOp.setInput('base', self.torsoCtrl)
        self.bezierSpineKLOp.setInput('baseHandle', self.chestCtrl)
        self.bezierSpineKLOp.setInput('tipHandle', self.upChestCtrl)
        # temp now until handles are swapped
        self.bezierSpineKLOp.setInput('tip', self.upChestCtrl)

        # Add Xfo Outputs
        self.bezierSpineKLOp.setOutput('outputs', self.spineOutputs)

        # Add Deformer Splice Op
        self.deformersToOutputsKLOp = KLOperator('spineDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.deformersToOutputsKLOp)

        # Add Att Inputs
        self.deformersToOutputsKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.deformersToOutputsKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setInput('constrainers', self.spineOutputs)

        # Add Xfo Outputs
        self.deformersToOutputsKLOp.setOutput('constrainees', self.deformerJoints)

        # Add Pelvis Splice Op
        self.pelvisDefKLOp = KLOperator('pelvisDeformerKLOp', 'PoseConstraintSolver', 'Kraken')
        self.addOperator(self.pelvisDefKLOp)

        # Add Att Inputs
        self.pelvisDefKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.pelvisDefKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.pelvisDefKLOp.setInput('constrainer', self.pelvisOutputTgt)

        # Add Xfo Outputs
        self.pelvisDefKLOp.setOutput('constrainee', pelvisDef)


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
        torsoPosition = data['torsoPosition']
        chestPosition = data['chestPosition']
        upChestPosition = data['upChestPosition']
        numDeformers = data['numDeformers']

        self.cogCtrlSpace.xfo.tr = cogPosition
        self.cogCtrl.xfo.tr = cogPosition

        self.pelvisCtrlSpace.xfo.tr = cogPosition
        self.pelvisCtrl.xfo.tr = cogPosition

        self.torsoCtrlSpace.xfo.tr = torsoPosition
        self.torsoCtrl.xfo.tr = torsoPosition

        self.chestCtrlSpace.xfo.tr = chestPosition
        self.chestCtrl.xfo.tr = chestPosition

        self.upChestCtrlSpace.xfo.tr = upChestPosition
        self.upChestCtrl.xfo.tr = upChestPosition


        length = torsoPosition.distanceTo(chestPosition) + chestPosition.distanceTo(upChestPosition)
        self.lengthInputAttr.setMax(length * 3.0)
        self.lengthInputAttr.setValue(length)

        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        # Updating constraint to use the updated last output.
        self.spineEndOutputConstraint.setConstrainer(self.spineOutputs[-1], index=0)

        # ============
        # Set IO Xfos
        # ============

        # ====================
        # Evaluate Splice Ops
        # ====================
        # evaluate the spine op so that all the output transforms are updated.
        self.bezierSpineKLOp.evaluate()

        # evaluate the constraint op so that all the joint transforms are updated.
        self.deformersToOutputsKLOp.evaluate()
        self.pelvisDefKLOp.evaluate()

        # evaluate the constraints to ensure the outputs are now in the correct location.
        self.spineCogOutputConstraint.evaluate()
        self.spineBaseOutputConstraint.evaluate()
        self.pelvisOutputConstraint.evaluate()
        self.spineEndOutputConstraint.evaluate()

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.cogCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.pelvisCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.chestCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'],1.0, data['globalComponentCtrlSize']))
        self.upChestCtrl.scalePoints(Vec3( data['globalComponentCtrlSize'], 1.0, data['globalComponentCtrlSize']))


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSSpineComponentGuide)
ks.registerComponent(OSSSpineComponentRig)
