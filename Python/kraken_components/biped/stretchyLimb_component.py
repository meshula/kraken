from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.xfo import xfoFromDirAndUpV

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler


class StretchyLimbComponent(BaseExampleComponent):
    """StretchyLimb Component"""

    def __init__(self, name='limbBase', parent=None, *args, **kwargs):

        super(StretchyLimbComponent, self).__init__(name, parent, *args, **kwargs)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.limbParentInputTgt = self.createInput('limbParent', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.limbUpperOutputTgt = self.createOutput('limbUpperXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.limbLowerOutputTgt = self.createOutput('limbLowerXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.limbEndOutputTgt = self.createOutput('limbEndXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', value=1.0, dataType='Float', parent=self.cmpInputAttrGrp).getTarget()
        # self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()


class StretchyLimbComponentGuide(StretchyLimbComponent):
    """StretchyLimb Component Guide"""

    def __init__(self, name='limb', parent=None, *args, **kwargs):

        Profiler.getInstance().push("Construct StretchyLimb Guide Component:" + name)
        super(StretchyLimbComponentGuide, self).__init__(name, parent, *args, **kwargs)


        # =========
        # Controls
        # ========
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        # Guide Controls
        self.upperCtl = Control('upper', parent=self.ctrlCmpGrp, shape="sphere")
        self.lowerCtl = Control('lower', parent=self.ctrlCmpGrp, shape="sphere")
        self.endCtl = Control('end', parent=self.ctrlCmpGrp, shape="sphere")

        self.default_data = {
                "name": name,
                "location": "L",
                "upperXfo": Xfo(Vec3(0.9811, 9.769, -0.4572)),
                "lowerXfo": Xfo(Vec3(1.4488, 5.4418, -0.5348)),
                "endXfo": Xfo(Vec3(1.841, 1.1516, -1.237))
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

        data = super(StretchyLimbComponentGuide, self).saveData()

        data['upperXfo'] = self.upperCtl.xfo
        data['lowerXfo'] = self.lowerCtl.xfo
        data['endXfo'] = self.endCtl.xfo

        return data

    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(StretchyLimbComponentGuide, self).loadData(data)

        self.upperCtl.xfo = data.get('upperXfo', self.default_data['upperXfo'])
        self.lowerCtl.xfo = data.get('lowerXfo', self.default_data['lowerXfo'])
        self.endCtl.xfo = data.get('endXfo', self.default_data['endXfo'])

        return True

    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(StretchyLimbComponentGuide, self).getRigBuildData()

        # Values
        startPos = self.upperCtl.xfo.tr
        midPos = self.lowerCtl.xfo.tr
        endPos = self.endCtl.xfo.tr

        # Calculate Upper Xfo
        startToEnd = endPos.subtract(startPos).unit()
        startToMid = midPos.subtract(startPos).unit()

        bone1Normal = startToEnd.cross(startToMid).unit()
        bone1ZAxis = startToMid.cross(bone1Normal).unit()

        upperXfo = Xfo()
        upperXfo.setFromVectors(startToMid, bone1Normal, bone1ZAxis, startPos)

        # Calculate Lower Xfo
        midToEnd = endPos.subtract(midPos).unit()
        midToStart = startPos.subtract(midPos).unit()
        bone2Normal = midToStart.cross(midToEnd).unit()
        bone2ZAxis = midToEnd.cross(bone2Normal).unit()

        lowerXfo = Xfo()
        lowerXfo.setFromVectors(midToEnd, bone2Normal, bone2ZAxis, midPos)

        upperLen = startPos.subtract(midPos).length()
        lowerLen = endPos.subtract(midPos).length()

        handleXfo = Xfo()
        handleXfo.tr = endPos

        endXfo = Xfo()
        endXfo.tr = endPos
        # endXfo.ori = lowerXfo.ori

        upVXfo = xfoFromDirAndUpV(startPos, endPos, midPos)
        upVXfo.tr = midPos
        upVXfo.tr = upVXfo.transformVector(Vec3(0, 0, 5))

        data['upperXfo'] = upperXfo
        data['lowerXfo'] = lowerXfo
        data['endXfo'] = endXfo
        data['handleXfo'] = handleXfo
        data['upVXfo'] = upVXfo
        data['upperLen'] = upperLen
        data['lowerLen'] = lowerLen

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

        return StretchyLimbComponentRig


class StretchyLimbComponentRig(StretchyLimbComponent):
    """StretchyLimb Component"""

    def __init__(self, name='limb', parent=None):

        Profiler.getInstance().push("Construct StretchyLimb Rig Component:" + name)
        super(StretchyLimbComponentRig, self).__init__(name, parent)

        # =========
        # Controls
        # =========
        # Upper (FK)
        self.upperFKCtrlSpace = CtrlSpace('upperFK', parent=self.ctrlCmpGrp)
        self.upperFKCtrl = Control('upperFK', parent=self.upperFKCtrlSpace, shape="cube")
        self.upperFKCtrl.alignOnXAxis()

        # Lower (FK)
        self.lowerFKCtrlSpace = CtrlSpace('lowerFK', parent=self.upperFKCtrl)
        self.lowerFKCtrl = Control('lowerFK', parent=self.lowerFKCtrlSpace, shape="cube")
        self.lowerFKCtrl.alignOnXAxis()

        # End (IK)
        self.limbIKCtrlSpace = CtrlSpace('IK', parent=self.ctrlCmpGrp)
        self.limbIKCtrl = Control('IK', parent=self.limbIKCtrlSpace, shape="pin")

        # Add Component Params to IK control
        # TODO: Move these separate control
        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_StretchyLimbSettings", parent=self.limbIKCtrl)
        limbDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=limbSettingsAttrGrp)
        self.limbBone0LenInputAttr = ScalarAttribute('bone0Len', value=1.0, parent=limbSettingsAttrGrp)
        self.limbBone1LenInputAttr = ScalarAttribute('bone1Len', value=1.0, parent=limbSettingsAttrGrp)
        limbIKBlendInputAttr = ScalarAttribute('ikblend', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        limbSoftIKInputAttr = BoolAttribute('softIK', value=True, parent=limbSettingsAttrGrp)
        limbSoftRatioInputAttr = ScalarAttribute('softRatio', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        limbStretchInputAttr = BoolAttribute('stretch', value=True, parent=limbSettingsAttrGrp)
        limbStretchBlendInputAttr = ScalarAttribute('stretchBlend', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        limbSlideInputAttr = ScalarAttribute('slide', value=0.0, minValue=-1.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        limbPinInputAttr = ScalarAttribute('pin', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
        self.rightSideInputAttr = BoolAttribute('rightSide', value=False, parent=limbSettingsAttrGrp)

        self.drawDebugInputAttr.connect(limbDrawDebugInputAttr)

        # UpV (IK Pole Vector)
        self.limbUpVCtrlSpace = CtrlSpace('UpV', parent=self.ctrlCmpGrp)
        self.limbUpVCtrl = Control('UpV', parent=self.limbUpVCtrlSpace, shape="triangle")
        self.limbUpVCtrl.alignOnZAxis()

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.addItem('defCmpGrp', self.defCmpGrp)

        upperDef = Joint('upper', parent=self.defCmpGrp)
        upperDef.setComponent(self)

        lowerDef = Joint('lower', parent=self.defCmpGrp)
        lowerDef.setComponent(self)

        endDef = Joint('end', parent=self.defCmpGrp)
        endDef.setComponent(self)

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.limbIKCtrlSpaceInputConstraint = PoseConstraint('_'.join([self.limbIKCtrlSpace.getName(), 'To', self.globalSRTInputTgt.getName()]))
        self.limbIKCtrlSpaceInputConstraint.setMaintainOffset(True)
        self.limbIKCtrlSpaceInputConstraint.addConstrainer(self.globalSRTInputTgt)
        self.limbIKCtrlSpace.addConstraint(self.limbIKCtrlSpaceInputConstraint)

        self.limbUpVCtrlSpaceInputConstraint = PoseConstraint('_'.join([self.limbUpVCtrlSpace.getName(), 'To', self.globalSRTInputTgt.getName()]))
        self.limbUpVCtrlSpaceInputConstraint.setMaintainOffset(True)
        self.limbUpVCtrlSpaceInputConstraint.addConstrainer(self.globalSRTInputTgt)
        self.limbUpVCtrlSpace.addConstraint(self.limbUpVCtrlSpaceInputConstraint)

        self.limbRootInputConstraint = PoseConstraint('_'.join([self.limbIKCtrl.getName(), 'To', self.limbParentInputTgt.getName()]))
        self.limbRootInputConstraint.setMaintainOffset(True)
        self.limbRootInputConstraint.addConstrainer(self.limbParentInputTgt)
        self.upperFKCtrlSpace.addConstraint(self.limbRootInputConstraint)

        # ===============
        # Add Splice Ops
        # ===============
        # Add StretchyLimb Splice Op
        self.limbIKKLOp = KLOperator('limb', 'TwoBoneStretchyIKSolver', 'Kraken')
        self.addOperator(self.limbIKKLOp)

        # Add Att Inputs
        self.limbIKKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.limbIKKLOp.setInput('rigScale', self.rigScaleInputAttr)

        self.limbIKKLOp.setInput('bone0Len', self.limbBone0LenInputAttr)
        self.limbIKKLOp.setInput('bone1Len', self.limbBone1LenInputAttr)
        self.limbIKKLOp.setInput('ikblend', limbIKBlendInputAttr)
        self.limbIKKLOp.setInput('softIK', limbSoftIKInputAttr)
        self.limbIKKLOp.setInput('softRatio', limbSoftRatioInputAttr)
        self.limbIKKLOp.setInput('stretch', limbStretchInputAttr)
        self.limbIKKLOp.setInput('stretchBlend', limbStretchBlendInputAttr)
        self.limbIKKLOp.setInput('slide', limbSlideInputAttr)
        self.limbIKKLOp.setInput('pin', limbPinInputAttr)
        self.limbIKKLOp.setInput('rightSide', self.rightSideInputAttr)

        # Add Xfo Inputs
        self.limbIKKLOp.setInput('root', self.limbParentInputTgt)
        self.limbIKKLOp.setInput('bone0FK', self.upperFKCtrl)
        self.limbIKKLOp.setInput('bone1FK', self.lowerFKCtrl)
        self.limbIKKLOp.setInput('ikHandle', self.limbIKCtrl)
        self.limbIKKLOp.setInput('upV', self.limbUpVCtrl)

        # Add Xfo Outputs
        self.limbIKKLOp.setOutput('bone0Out', self.limbUpperOutputTgt)
        self.limbIKKLOp.setOutput('bone1Out', self.limbLowerOutputTgt)
        self.limbIKKLOp.setOutput('bone2Out', self.limbEndOutputTgt)

        # =====================
        # Connect the deformers
        # =====================

        # Add StretchyLimb Deformer Splice Op
        self.outputsToDeformersKLOp = KLOperator('defConstraint', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)

        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.limbUpperOutputTgt, self.limbLowerOutputTgt, self.limbEndOutputTgt])

        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [upperDef, lowerDef, endDef])

        Profiler.getInstance().pop()

    # =============
    # Data Methods
    # =============
    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(StretchyLimbComponentRig, self).loadData(data)

        upperXfo = data.get('upperXfo')
        upperLen = data.get('upperLen')
        lowerXfo = data.get('lowerXfo')
        lowerLen = data.get('lowerLen')
        endXfo = data.get('endXfo')
        upVXfo = data.get('upVXfo')

        self.upperFKCtrlSpace.xfo = upperXfo
        self.upperFKCtrl.xfo = upperXfo
        self.upperFKCtrl.scalePoints(Vec3(upperLen, 1.75, 1.75))

        self.limbUpperOutputTgt.xfo = upperXfo
        self.limbLowerOutputTgt.xfo = lowerXfo

        self.lowerFKCtrlSpace.xfo = lowerXfo
        self.lowerFKCtrl.xfo = lowerXfo
        self.lowerFKCtrl.scalePoints(Vec3(lowerLen, 1.5, 1.5))

        self.limbIKCtrlSpace.xfo.tr = endXfo.tr
        self.limbIKCtrl.xfo.tr = endXfo.tr

        if self.getLocation() == "R":
            self.limbIKCtrl.rotatePoints(0, 90, 0)
            self.limbIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            self.limbIKCtrl.rotatePoints(0, -90, 0)
            self.limbIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))

        self.limbUpVCtrlSpace.xfo = upVXfo
        self.limbUpVCtrl.xfo = upVXfo

        self.limbBone0LenInputAttr.setMin(0.0)
        self.limbBone0LenInputAttr.setMax(upperLen * 3.0)
        self.limbBone0LenInputAttr.setValue(upperLen)
        self.limbBone1LenInputAttr.setMin(0.0)
        self.limbBone1LenInputAttr.setMax(lowerLen * 3.0)
        self.limbBone1LenInputAttr.setValue(lowerLen)

        self.limbParentInputTgt.xfo = upperXfo

        # Set Attrs
        self.rightSideInputAttr.setValue(self.getLocation() is 'R')

        # Eval Constraints
        self.limbIKCtrlSpaceInputConstraint.evaluate()
        self.limbUpVCtrlSpaceInputConstraint.evaluate()
        self.limbRootInputConstraint.evaluate()

        # Eval Operators
        self.limbIKKLOp.evaluate()
        self.outputsToDeformersKLOp.evaluate()


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(StretchyLimbComponentGuide)
ks.registerComponent(StretchyLimbComponentRig)
