from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.quat import Quat
from kraken.core.maths import Math_degToRad

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.transform import Transform
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from kraken.log import getLogger

logger = getLogger('kraken')


class HeadComponent(BaseExampleComponent):
    """Head Component Base"""

    def __init__(self, name='headBase', parent=None, *args, **kwargs):
        super(HeadComponent, self).__init__(name, parent, *args, **kwargs)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.neckRefInputTgt = self.createInput('neckRef', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.worldRefInputTgt = self.createInput('worldRef', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.headOutputTgt = self.createOutput('head', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.jawOutputTgt = self.createOutput('jaw', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.eyeLOutputTgt = self.createOutput('eyeL', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.eyeROutputTgt = self.createOutput('eyeR', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


class HeadComponentGuide(HeadComponent):
    """Head Component Guide"""

    def __init__(self, name='head', parent=None, *args, **kwargs):

        Profiler.getInstance().push("Construct Head Guide Component:" + name)
        super(HeadComponentGuide, self).__init__(name, parent, *args, **kwargs)


        # =========
        # Controls
        # =========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)


        sphereCtrl = Control('sphere', shape='sphere')
        sphereCtrl.scalePoints(Vec3(0.375, 0.375, 0.375))

        self.headCtrl = Control('head', parent=self.ctrlCmpGrp, shape='square')
        self.headCtrl.rotatePoints(90, 0, 0)
        self.headCtrl.translatePoints(Vec3(0.0, 0.5, 0.0))
        self.headCtrl.scalePoints(Vec3(1.8, 2.0, 2.0))

        self.eyeLeftCtrl = Control('eyeLeft', parent=self.headCtrl, shape='arrow_thin')
        self.eyeLeftCtrl.translatePoints(Vec3(0, 0, 0.5))
        self.eyeLeftCtrl.rotatePoints(0, 90, 0)
        self.eyeLeftCtrl.appendCurveData(sphereCtrl.getCurveData())

        self.eyeRightCtrl = Control('eyeRight', parent=self.headCtrl, shape='arrow_thin')
        self.eyeRightCtrl.translatePoints(Vec3(0, 0, 0.5))
        self.eyeRightCtrl.rotatePoints(0, 90, 0)
        self.eyeRightCtrl.appendCurveData(sphereCtrl.getCurveData())

        self.jawCtrl = Control('jaw', parent=self.headCtrl, shape='square')
        self.jawCtrl.rotatePoints(90, 0, 0)
        self.jawCtrl.rotatePoints(0, 90, 0)
        self.jawCtrl.translatePoints(Vec3(0.0, -0.5, 0.5))
        self.jawCtrl.scalePoints(Vec3(1.0, 0.8, 1.5))
        self.jawCtrl.setColor('orange')

        eyeXAlignOri = Quat()
        eyeXAlignOri.setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(-90))

        self.default_data = {
            "name": name,
            "location": "M",
            "headXfo": Xfo(Vec3(0.0, 17.5, -0.5)),
            "headCrvData": self.headCtrl.getCurveData(),
            "eyeLeftXfo": Xfo(tr=Vec3(0.375, 18.5, 0.5), ori=eyeXAlignOri),
            "eyeLeftCrvData": self.eyeLeftCtrl.getCurveData(),
            "eyeRightXfo": Xfo(tr=Vec3(-0.375, 18.5, 0.5), ori=eyeXAlignOri),
            "eyeRightCrvData": self.eyeRightCtrl.getCurveData(),
            "jawXfo": Xfo(Vec3(0.0, 17.875, -0.275)),
            "jawCrvData": self.jawCtrl.getCurveData()
        }

        self.loadData(self.default_data)

        Profiler.getInstance().pop()


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """

        data = super(HeadComponentGuide, self).saveData()

        data['headXfo'] = self.headCtrl.xfo
        data['headCrvData'] = self.headCtrl.getCurveData()
        data['eyeLeftXfo'] = self.eyeLeftCtrl.xfo
        data['eyeLeftCrvData'] = self.eyeLeftCtrl.getCurveData()
        data['eyeRightXfo'] = self.eyeRightCtrl.xfo
        data['eyeRightCrvData'] = self.eyeRightCtrl.getCurveData()
        data['jawXfo'] = self.jawCtrl.xfo
        data['jawCrvData'] = self.jawCtrl.getCurveData()

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(HeadComponentGuide, self).loadData(data)

        self.headCtrl.xfo = data.get('headXfo', self.default_data['headXfo'])
        self.headCtrl.setCurveData(data.get('headCrvData', self.default_data['headCrvData']))
        self.eyeLeftCtrl.xfo = data.get('eyeLeftXfo', self.default_data['eyeLeftXfo'])
        self.eyeLeftCtrl.setCurveData(data.get('eyeLeftCrvData', self.default_data['eyeLeftCrvData']))
        self.eyeRightCtrl.xfo = data.get('eyeRightXfo', self.default_data['eyeRightXfo'])
        self.eyeRightCtrl.setCurveData(data.get('eyeRightCrvData', self.default_data['eyeRightCrvData']))
        self.jawCtrl.xfo = data.get('jawXfo', self.default_data['jawXfo'])
        self.jawCtrl.setCurveData(data.get('jawCrvData', self.default_data['jawCrvData']))

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(HeadComponentGuide, self).getRigBuildData()

        data['headXfo'] = self.headCtrl.xfo
        data['headCrvData'] = self.headCtrl.getCurveData()

        data['eyeLeftXfo'] = self.eyeLeftCtrl.xfo
        data['eyeLeftCrvData'] = self.eyeLeftCtrl.getCurveData()

        data['eyeRightXfo'] = self.eyeRightCtrl.xfo
        data['eyeRightCrvData'] = self.eyeRightCtrl.getCurveData()

        data['jawXfo'] = self.jawCtrl.xfo
        data['jawCrvData'] = self.jawCtrl.getCurveData()


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

        return HeadComponentRig


class HeadComponentRig(HeadComponent):
    """Head Component Rig"""

    def __init__(self, name='head', parent=None):

        Profiler.getInstance().push("Construct Head Rig Component:" + name)
        super(HeadComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Head
        self.headCtrl = Control('head', parent=self.ctrlCmpGrp, shape='circle')
        self.headCtrl.lockScale(x=True, y=True, z=True)
        self.headCtrl.lockTranslation(x=True, y=True, z=True)
        self.headCtrlSpace = self.headCtrl.insertCtrlSpace()
        self.headCtrl.rotatePoints(0, 0, 90)
        self.headCtrl.scalePoints(Vec3(3, 3, 3))
        self.headCtrl.translatePoints(Vec3(0, 1, 0.25))

        # Eye Left
        self.eyeLeftCtrl = Control('eyeLeft', parent=self.ctrlCmpGrp, shape='sphere')
        self.eyeLeftCtrl.lockScale(x=True, y=True, z=True)
        self.eyeLeftCtrl.lockTranslation(x=True, y=True, z=True)
        self.eyeLeftCtrlSpace = self.eyeLeftCtrl.insertCtrlSpace()
        self.eyeLeftCtrl.rotatePoints(0, 90, 0)
        self.eyeLeftCtrl.scalePoints(Vec3(0.5, 0.5, 0.5))
        self.eyeLeftCtrl.setColor('mediumblue')

        # Eye Right
        self.eyeRightCtrl = Control('eyeRight', parent=self.ctrlCmpGrp, shape='sphere')
        self.eyeRightCtrl.lockScale(x=True, y=True, z=True)
        self.eyeRightCtrl.lockTranslation(x=True, y=True, z=True)
        self.eyeRightCtrlSpace = self.eyeRightCtrl.insertCtrlSpace()
        self.eyeRightCtrl.rotatePoints(0, 90, 0)
        self.eyeRightCtrl.scalePoints(Vec3(0.5, 0.5, 0.5))
        self.eyeRightCtrl.setColor('mediumblue')

        # LookAt Control
        self.lookAtCtrl = Control('lookAt', parent=self.ctrlCmpGrp, shape='square')
        self.lookAtCtrl.lockScale(x=True, y=True, z=True)
        self.lookAtCtrl.rotatePoints(90, 0, 0)
        self.lookAtCtrlSpace = self.lookAtCtrl.insertCtrlSpace()

        self.eyeLeftBase = Transform('eyeLeftBase', parent=self.headCtrl)
        self.eyeRightBase = Transform('eyeRightBase', parent=self.headCtrl)
        self.eyeLeftUpV = Transform('eyeLeftUpV', parent=self.headCtrl)
        self.eyeRightUpV = Transform('eyeRightUpV', parent=self.headCtrl)
        self.eyeLeftAtV = Transform('eyeLeftAtV', parent=self.lookAtCtrl)
        self.eyeRightAtV = Transform('eyeRightAtV', parent=self.lookAtCtrl)

        # Jaw
        self.jawCtrl = Control('jaw', parent=self.headCtrl, shape='cube')
        self.jawCtrlSpace = self.jawCtrl.insertCtrlSpace()
        self.jawCtrl.lockScale(x=True, y=True, z=True)
        self.jawCtrl.lockTranslation(x=True, y=True, z=True)
        self.jawCtrl.alignOnYAxis(negative=True)
        self.jawCtrl.alignOnZAxis()
        self.jawCtrl.scalePoints(Vec3(1.45, 0.65, 1.25))
        self.jawCtrl.translatePoints(Vec3(0, -0.25, 0))
        self.jawCtrl.setColor('orange')


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.addItem('defCmpGrp', self.defCmpGrp)

        headDef = Joint('head', parent=self.defCmpGrp)
        headDef.setComponent(self)

        jawDef = Joint('jaw', parent=self.defCmpGrp)
        jawDef.setComponent(self)

        eyeLeftDef = Joint('eyeLeft', parent=self.defCmpGrp)
        eyeLeftDef.setComponent(self)

        eyeRightDef = Joint('eyeRight', parent=self.defCmpGrp)
        eyeRightDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.headInputConstraint = PoseConstraint('_'.join([self.headCtrlSpace.getName(), 'To', self.neckRefInputTgt.getName()]))
        self.headInputConstraint.setMaintainOffset(True)
        self.headInputConstraint.addConstrainer(self.neckRefInputTgt)
        self.headCtrlSpace.addConstraint(self.headInputConstraint)

        # Constraint outputs
        self.headOutputConstraint = PoseConstraint('_'.join([self.headOutputTgt.getName(), 'To', self.headCtrl.getName()]))
        self.headOutputConstraint.addConstrainer(self.headCtrl)
        self.headOutputTgt.addConstraint(self.headOutputConstraint)

        self.jawOutputConstraint = PoseConstraint('_'.join([self.jawOutputTgt.getName(), 'To', self.jawCtrl.getName()]))
        self.jawOutputConstraint.addConstrainer(self.jawCtrl)
        self.jawOutputTgt.addConstraint(self.jawOutputConstraint)

        self.eyeLOutputConstraint = PoseConstraint('_'.join([self.eyeLOutputTgt.getName(), 'To', self.eyeLeftCtrl.getName()]))
        self.eyeLOutputConstraint.addConstrainer(self.eyeLeftCtrl)
        self.eyeLOutputTgt.addConstraint(self.eyeLOutputConstraint)

        self.eyeROutputConstraint = PoseConstraint('_'.join([self.eyeROutputTgt.getName(), 'To', self.eyeRightCtrl.getName()]))
        self.eyeROutputConstraint.addConstrainer(self.eyeRightCtrl)
        self.eyeROutputTgt.addConstraint(self.eyeROutputConstraint)

        # Add Eye Left Direction KL Op
        self.eyeLeftDirKLOp = KLOperator('eyeLeftDir', 'DirectionConstraintSolver', 'Kraken')
        self.addOperator(self.eyeLeftDirKLOp)

        # Add Att Inputs
        self.eyeLeftDirKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.eyeLeftDirKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.eyeLeftDirKLOp.setInput('position', self.eyeLeftBase)
        self.eyeLeftDirKLOp.setInput('upVector', self.eyeLeftUpV)
        self.eyeLeftDirKLOp.setInput('atVector', self.eyeLeftAtV)

        # Add Xfo Outputs
        self.eyeLeftDirKLOp.setOutput('constrainee', self.eyeLeftCtrlSpace)

        # Add Eye Right Direction KL Op
        self.eyeRightDirKLOp = KLOperator('eyeRightDir', 'DirectionConstraintSolver', 'Kraken')
        self.addOperator(self.eyeRightDirKLOp)

        # Add Att Inputs
        self.eyeRightDirKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.eyeRightDirKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.eyeRightDirKLOp.setInput('position', self.eyeRightBase)
        self.eyeRightDirKLOp.setInput('upVector', self.eyeRightUpV)
        self.eyeRightDirKLOp.setInput('atVector', self.eyeRightAtV)

        # Add Xfo Outputs
        self.eyeRightDirKLOp.setOutput('constrainee', self.eyeRightCtrlSpace)


        # Add Deformer Joints KL Op
        self.outputsToDeformersKLOp = KLOperator('defConstraint', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)

        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.headOutputTgt, self.jawOutputTgt, self.eyeROutputTgt, self.eyeLOutputTgt])

        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [headDef, jawDef, eyeRightDef, eyeLeftDef])

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(HeadComponentRig, self).loadData(data)

        headXfo = data.get('headXfo')
        headCrvData = data.get('headCrvData')
        eyeLeftXfo = data.get('eyeLeftXfo')
        eyeLeftCrvData = data.get('eyeLeftCrvData')
        eyeRightXfo = data.get('eyeRightXfo')
        eyeRightCrvData = data.get('eyeRightCrvData')
        jawXfo = data.get('jawXfo')
        jawCrvData = data.get('jawCrvData')

        self.headCtrlSpace.xfo = headXfo
        self.headCtrl.xfo = headXfo
        self.headCtrl.setCurveData(headCrvData)

        # self.eyeLeftCtrlSpace.xfo = eyeLeftXfo
        # self.eyeLeftCtrl.xfo = eyeLeftXfo
        self.eyeLeftCtrl.setCurveData(eyeLeftCrvData)

        # self.eyeRightCtrlSpace.xfo = eyeRightXfo
        # self.eyeRightCtrl.xfo = eyeRightXfo
        self.eyeRightCtrl.setCurveData(eyeRightCrvData)

        # LookAt
        eyeLeftRelXfo = headXfo.inverse() * eyeLeftXfo
        eyeRightRelXfo = headXfo.inverse() * eyeRightXfo
        eyeMidRelPos = eyeLeftRelXfo.tr.linearInterpolate(eyeRightRelXfo.tr, 0.5)
        eyeMidRelPos = eyeMidRelPos + Vec3(0.0, 0.0, 8.0)
        eyeLen = eyeLeftRelXfo.tr.distanceTo(eyeRightRelXfo.tr)

        self.eyeLeftBase.xfo = eyeLeftXfo
        self.eyeRightBase.xfo = eyeRightXfo

        self.eyeLeftUpV.xfo = eyeLeftXfo * Xfo(Vec3(0, 1, 0))
        self.eyeRightUpV.xfo = eyeRightXfo * Xfo(Vec3(0, 1, 0))

        self.eyeLeftAtV.xfo.tr = eyeLeftXfo.transformVector(Vec3(8.0, 0.0, 0.0))
        self.eyeRightAtV.xfo.tr = eyeRightXfo.transformVector(Vec3(8.0, 0.0, 0.0))

        lookAtXfo = headXfo.clone()
        lookAtXfo.tr = headXfo.transformVector(eyeMidRelPos)

        self.lookAtCtrl.scalePoints(Vec3(eyeLen * 1.6, eyeLen * 0.65, 1.0))
        self.lookAtCtrl.xfo = lookAtXfo
        self.lookAtCtrlSpace.xfo = lookAtXfo

        self.jawCtrlSpace.xfo = jawXfo
        self.jawCtrl.xfo = jawXfo
        self.jawCtrl.setCurveData(jawCrvData)

        # ============
        # Set IO Xfos
        # ============
        self.neckRefInputTgt.xfo = headXfo
        self.worldRefInputTgt.xfo = headXfo
        self.headOutputTgt.xfo = headXfo
        self.jawOutputTgt.xfo = jawXfo
        self.eyeLOutputTgt.xfo = eyeLeftXfo
        self.eyeROutputTgt.xfo = eyeRightXfo

        # Eval Constraints
        self.headInputConstraint.evaluate()
        self.headOutputConstraint.evaluate()
        self.jawOutputConstraint.evaluate()
        self.eyeLOutputConstraint.evaluate()
        self.eyeROutputConstraint.evaluate()

        # Eval Operators
        self.eyeLeftDirKLOp.evaluate()
        self.eyeRightDirKLOp.evaluate()
        self.outputsToDeformersKLOp.evaluate()

        # Have to set the eye control xfos to match the evaluated xfos from
        self.eyeLeftCtrl.xfo = self.eyeLeftCtrlSpace.xfo
        self.eyeRightCtrl.xfo = self.eyeRightCtrlSpace.xfo


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(HeadComponentGuide)
ks.registerComponent(HeadComponentRig)
