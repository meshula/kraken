from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo, axisStrToTupleMapping
from kraken.core.maths.xfo import xfoFromDirAndUpV
import kraken.core.maths.euler as euler

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute

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

import traceback

class OSSLegComponent(BaseExampleComponent):
    """Leg Component"""

    def __init__(self, name='legBase', parent=None):

        super(OSSLegComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.legPelvisInputTgt = self.createInput('pelvisInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.uplegOutputTgt = self.createOutput('upleg', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.lolegOutputTgt = self.createOutput('loleg', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.legEndXfoOutputTgt = self.createOutput('legEndXfo', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.footOutputTgt = self.createOutput('foot', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.toeOutputTgt = self.createOutput('toe', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.ikgoalOutputTgt = self.createOutput('ikgoal', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.footRockerFootOutputTgt = self.createOutput('footRockerFoot', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.footRockerToeOutputTgt = self.createOutput('footRockerToe', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', value=1.0, dataType='Float', parent=self.cmpInputAttrGrp).getTarget()
        self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        self.drawDebugOutputAttr = self.createOutput('drawDebug', dataType='Boolean', value=False, parent=self.cmpOutputAttrGrp).getTarget()

        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSLegComponentGuide(OSSLegComponent):
    """Leg Component Guide"""

    def __init__(self, name='leg', parent=None, data=None):

        Profiler.getInstance().push("Construct Leg Guide Component:" + name)
        super(OSSLegComponentGuide, self).__init__(name, parent)


        # =========
        # Controls
        # ========

        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)

        # Guide Controls
        self.uplegCtrl = Control('upleg', parent=self.ctrlCmpGrp, shape="sphere")
        self.kneeCtrl = Control('knee', parent=self.ctrlCmpGrp, shape="sphere")
        self.ankleCtrl = Control('ankle', parent=self.ctrlCmpGrp, shape="sphere")
        self.toeCtrl = Control('toe', parent=self.ctrlCmpGrp, shape="sphere")
        self.toeTipCtrl = Control('toeTip', parent=self.ctrlCmpGrp, shape="sphere")
        self.heelPivotCtrl = Control('heelPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.toeTipPivotCtrl = Control('toeTipPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.innerPivotCtrl = Control('innerPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.outerPivotCtrl = Control('outerPivot', parent=self.ctrlCmpGrp, shape="sphere")
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        print "\nOSSLegComponentGuide()  __init__ \ndata:"
        print data

        if data is None:
            data = {
                    "name": name,
                    "location": "L",
                    "uplegXfo": Xfo(Vec3(0.9811, 9.769, -0.4572)),
                    "kneeXfo": Xfo(Vec3(1.4488, 5.4418, -0.5348)),
                    "ankleXfo": Xfo(Vec3(1.841, 1.1516, -1.237)),
                    "toeXfo": Xfo(Vec3(1.85, 0.4, 0.25)),
                    "toeTipXfo": Xfo(Vec3(1.85, 0.4, 1.5)),
                    "heelPivotXfo": Xfo(Vec3(1.85, 0.0, -0.15)),
                    "toeTipPivotXfo": Xfo(Vec3(1.85, 0.0, -0.15)),
                    "innerPivotXfo": Xfo(Vec3(1., 0.0, 0.0)),
                    "outerPivotXfo": Xfo(Vec3(2.15, 0.0, 0.0)),
                    "globalComponentCtrlSize": 1.0
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

        data = super(OSSLegComponentGuide, self).saveData()

        data['uplegXfo'] = self.uplegCtrl.xfo
        data['kneeXfo'] = self.kneeCtrl.xfo
        data['ankleXfo'] = self.ankleCtrl.xfo
        data['toeXfo'] = self.toeCtrl.xfo
        data['toeTipXfo'] = self.toeTipCtrl.xfo
        data['heelPivotXfo'] = self.heelPivotCtrl.xfo
        data['toeTipPivotXfo'] = self.toeTipPivotCtrl.xfo
        data['innerPivotXfo'] = self.innerPivotCtrl.xfo
        data['outerPivotXfo'] = self.outerPivotCtrl.xfo

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """
        #print "\nOSSLegComponentGuide"
        #traceback.print_stack()
        #print "**loadData: ",
        #print data
        super(OSSLegComponentGuide, self).loadData( data )

        #print "**loadData2: ",
        #print data
        #print "-----------"

        if "uplegXfo" in data.keys():
            self.uplegCtrl.xfo = data['uplegXfo']
        if "kneeXfo" in data.keys():
            self.kneeCtrl.xfo = data['kneeXfo']
        if "ankleXfo" in data.keys():
            self.ankleCtrl.xfo = data['ankleXfo']
        if "toeXfo" in data.keys():
            self.toeCtrl.xfo = data['toeXfo']
        if "toeTipXfo" in data.keys():
            self.toeTipCtrl.xfo = data['toeTipXfo']
        if "heelPivotXfo" in data.keys():
            self.heelPivotCtrl.xfo = data['heelPivotXfo']
        if "toeTipPivotXfo" in data.keys():
            self.toeTipPivotCtrl.xfo = data['toeTipPivotXfo']
        if "innerPivotXfo" in data.keys():
            self.innerPivotCtrl.xfo = data['innerPivotXfo']
        if "outerPivotXfo" in data.keys():
            self.outerPivotCtrl.xfo = data['outerPivotXfo']


        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.uplegCtrl.scalePoints(globalScaleVec)
        self.kneeCtrl.scalePoints(globalScaleVec)
        self.ankleCtrl.scalePoints(globalScaleVec)
        self.toeCtrl.scalePoints(globalScaleVec)
        self.toeTipCtrl.scalePoints(globalScaleVec)
        self.heelPivotCtrl.scalePoints(globalScaleVec)
        self.toeTipPivotCtrl.scalePoints(globalScaleVec)
        self.innerPivotCtrl.scalePoints(globalScaleVec)
        self.outerPivotCtrl.scalePoints(globalScaleVec)

        return True



    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSLegComponentGuide, self).getRigBuildData()

        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping[boneAxisStr]

        upAxisStr = "POSY"
        if self.getLocation() == 'R':
            upAxisStr = "NEGY"
        upAxis = axisStrToTupleMapping[upAxisStr]


        # Values
        uplegPosition = self.uplegCtrl.xfo.tr
        kneePosition = self.kneeCtrl.xfo.tr
        anklePosition = self.ankleCtrl.xfo.tr
        toePosition = self.toeCtrl.xfo.tr
        toeTipPosition = self.toeTipCtrl.xfo.tr
        heelPivotPosition = self.heelPivotCtrl.xfo.tr
        toeTipPivotPosition = self.toeTipPivotCtrl.xfo.tr
        innerPivotPosition = self.innerPivotCtrl.xfo.tr
        outerPivotPosition = self.outerPivotCtrl.xfo.tr


        # Calculate Upleg Xfo
        uplegXfo = Xfo(self.uplegCtrl.xfo)
        # upAxis neg Y assumes the knee is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #uplegXfo.aimAt(self.kneeCtrl.xfo.tr, upPos=self.ankleCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis.negate())
        uplegXfo.aimAt(aimPos=self.kneeCtrl.xfo.tr, upPos=self.ankleCtrl.xfo.tr, aimAxis=boneAxis, upAxis=tuple([-x for x in upAxis]))


        # Calculate Knee Xfo
        kneeXfo = Xfo(self.kneeCtrl.xfo)
        # upAxis neg Y assumes the knee is bent forward.  To avoid this stuff, build a guide system with an actual upVector
        # to get rid of any ambiguity
        #kneeXfo.aimAt(self.toeCtrl.xfo.tr, upPos=self.uplegCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis.negate())
        kneeXfo.aimAt(aimPos=self.ankleCtrl.xfo.tr, upPos=self.uplegCtrl.xfo.tr, aimAxis=boneAxis, upAxis=tuple([-x for x in upAxis]))

        # Get lengths
        uplegLen = uplegPosition.subtract(kneePosition).length()
        lolegLen = kneePosition.subtract(anklePosition).length()
        footLen = anklePosition.subtract(toePosition).length()
        toeLen = toePosition.subtract(toeTipPosition).length()

        handleXfo = Xfo()
        handleXfo.tr = anklePosition

        ankleXfo = Xfo()
        ankleXfo.tr = anklePosition
        # ankleXfo.ori = kneeXfo.ori

        ankleXfo = Xfo()
        ankleXfo.tr = anklePosition
        # ankleXfo.ori = kneeXfo.ori


        heelPivotXfo = Xfo()
        heelPivotXfo.tr = heelPivotPosition

        toeTipPivotXfo = Xfo()
        toeTipPivotXfo.tr = toeTipPivotPosition

        innerPivotXfo = Xfo()
        innerPivotXfo.tr = innerPivotPosition

        outerPivotXfo = Xfo()
        outerPivotXfo.tr = outerPivotPosition

        footPosition = anklePosition
        # Calculate Foot Xfo
        footToToe = toePosition.subtract(footPosition).unit()

        footToKnee = kneePosition.subtract(footPosition).unit()

        bone2Normal = footToKnee.cross(footToToe).unit()

        bone2ZAxis = footToToe.cross(bone2Normal).unit()

        toeXfo = Xfo(self.toeCtrl.xfo)
        toeXfo.aimAt(aimPos=self.toeTipCtrl.xfo.tr, upPos=self.kneeCtrl.xfo.tr, aimAxis=boneAxis, upAxis=upAxis)

        footXfo = Xfo(ankleXfo)
        footXfo.aimAt(aimPos=toeXfo.tr, upPos=kneeXfo.tr, aimAxis=boneAxis, upAxis=upAxis)

        upVXfo = Xfo()
        offset = [x * uplegLen * 2 for x in upAxis]

        upVXfo.tr = kneeXfo.transformVector(Vec3(offset[0], offset[1], offset[2]))



        data['uplegXfo'] = uplegXfo
        data['kneeXfo'] = kneeXfo
        data['handleXfo'] = handleXfo
        data['ankleXfo'] = ankleXfo
        data['footXfo'] = footXfo
        data['toeXfo'] = toeXfo
        data['upVXfo'] = upVXfo
        data['uplegLen'] = uplegLen
        data['lolegLen'] = lolegLen
        data['footLen'] = footLen
        data['toeLen'] = toeLen
        data['heelPivotXfo'] = heelPivotXfo
        data['toeTipPivotXfo'] = toeTipPivotXfo
        data['innerPivotXfo'] = innerPivotXfo
        data['outerPivotXfo'] = outerPivotXfo

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

        return OSSLegComponentRig


class OSSLegComponentRig(OSSLegComponent):
    """Leg Component"""

    def __init__(self, name='leg', parent=None):

        Profiler.getInstance().push("Construct Leg Rig Component:" + name)
        super(OSSLegComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # upleg
        self.uplegFKCtrlSpace = CtrlSpace('uplegFK', parent=self.ctrlCmpGrp)
        self.uplegFKCtrl = Control('uplegFK', parent=self.uplegFKCtrlSpace, shape="cube")
        #self.setCurveData
        self.uplegFKCtrl.alignOnXAxis()

        # loleg
        self.lolegFKCtrlSpace = CtrlSpace('lolegFK', parent=self.uplegFKCtrl)
        self.lolegFKCtrl = Control('lolegFK', parent=self.lolegFKCtrlSpace, shape="cube")
        self.lolegFKCtrl.alignOnXAxis()

        # Ankle
        self.legIKCtrlSpace = CtrlSpace('IK', parent=self.ctrlCmpGrp)
        self.legIKCtrl = Control('IK', parent=self.legIKCtrlSpace, shape="cross")
        self.legIKTarget = CtrlSpace('IK', parent=self.legIKCtrl)

        # FK Foot
        self.footCtrlSpace = CtrlSpace('foot', parent=self.ctrlCmpGrp)
        self.footCtrl = Control('foot', parent=self.footCtrlSpace, shape="cube")
        self.footCtrl.alignOnXAxis()

        # FK Toe
        self.toeCtrlSpace = CtrlSpace('toe', parent=self.footCtrl)
        self.toeCtrl = Control('toe', parent=self.toeCtrlSpace, shape="cube")
        self.toeCtrl.alignOnXAxis()

        # Mocap Foot
        self.footMocap = Control('footMocap', parent=self.footCtrlSpace, shape="cube")
        self.footMocap.alignOnXAxis()

        # Mocap Toe
        self.toeMocapSpace = CtrlSpace('toeMocap', parent=self.footMocap)
        self.toeMocap = Control('toeMocap', parent=self.toeMocapSpace, shape="cube")
        self.toeMocap.alignOnXAxis()



        # Rig Ref objects
        self.footRefSrt = Locator('footRef', parent=self.ctrlCmpGrp)

        # Add Component Params to IK control
        footSettingsAttrGrp = AttributeGroup("DisplayInfo_FootSettings", parent=self.footCtrl)
        footLinkToWorldInputAttr = ScalarAttribute('linkToWorld', 1.0, maxValue=1.0, parent=footSettingsAttrGrp)

        # Add Component Params to IK control
        legSettingsAttrGrp = AttributeGroup("DisplayInfo_LegSettings", parent=self.legIKCtrl)
        legDrawDebugInputAttr = BoolAttribute('drawDebug', value=False, parent=legSettingsAttrGrp)
        self.legBone0LenInputAttr = ScalarAttribute('bone0Len', value=1.0, parent=legSettingsAttrGrp)
        self.legBone1LenInputAttr = ScalarAttribute('bone1Len', value=1.0, parent=legSettingsAttrGrp)
        legIKBlendInputAttr = ScalarAttribute('ikBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        mocapBlendInputAttr = ScalarAttribute('mocapBlend', value=1.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        parentIndexInputAttr = ScalarAttribute('parentIndex', value=1.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        footIKInputAttr = ScalarAttribute('footIK', value=1.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        #legSoftIKInputAttr = BoolAttribute('softIK', value=True, parent=legSettingsAttrGrp)
        legSoftDistInputAttr = ScalarAttribute('softDist', value=0.0, minValue=0.0, parent=legSettingsAttrGrp)
        legStretchBlendInputAttr = ScalarAttribute('stretch', value=0.0, minValue=0.0, maxValue=1.0, parent=legSettingsAttrGrp)
        footRockerInputAttr = ScalarAttribute('footRocker', value=0.0, minValue=-180.0, maxValue=180.0, parent=legSettingsAttrGrp)
        ballBreakInputAttr = ScalarAttribute('ballBreak', value=45.0, minValue=0, maxValue=90.0, parent=legSettingsAttrGrp)
        footTiltInputAttr = ScalarAttribute('footTilt', value=0.0, minValue=-180, maxValue=180.0, parent=legSettingsAttrGrp)

        self.drawDebugInputAttr.connect(legDrawDebugInputAttr)

        # UpV
        self.legUpVCtrlSpace = CtrlSpace('UpV', parent=self.ctrlCmpGrp)
        self.legUpVCtrl = Control('UpV', parent=self.legUpVCtrlSpace, shape="triangle")
        self.legUpVCtrl.alignOnZAxis()



        # =========
        # Locators for foot pivot
        # =========
        self.toeJointLocator = Locator('toeJoint', parent=self.legIKCtrl)
        #self.toeJointLocator.setVisibility(False) # does not seem to work, but setShapeVisibility does
        self.toeJointLocator.setShapeVisibility(False)
        self.footJointLocator = Locator('footJoint', parent=self.legIKCtrl)
        self.footJointLocator.setShapeVisibility(False)
        self.heelPivotLocator = Locator('heelPivot', parent=self.legIKCtrl)
        self.heelPivotLocator.setShapeVisibility(False)
        self.toePivotLocator = Locator('toePivot', parent=self.legIKCtrl)
        self.toePivotLocator.setShapeVisibility(False)
        self.toeTipPivotLocator = Locator('toeTipPivot', parent=self.legIKCtrl)
        self.toeTipPivotLocator.setShapeVisibility(False)
        self.innerPivotLocator = Locator('innerPivot', parent=self.legIKCtrl)
        self.innerPivotLocator.setShapeVisibility(False)
        self.outerPivotLocator = Locator('outerPivot', parent=self.legIKCtrl)
        self.outerPivotLocator.setShapeVisibility(False)

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)

        uplegDef = Joint('upleg', parent=self.defCmpGrp)
        uplegDef.setComponent(self)

        lolegDef = Joint('loleg', parent=self.defCmpGrp)
        lolegDef.setComponent(self)

        ankleDef = Joint('ankle', parent=self.defCmpGrp)
        ankleDef.setComponent(self)

        self.footDef = Joint('foot', parent=self.defCmpGrp)
        self.footDef.setComponent(self)

        self.toeDef = Joint('toe', parent=self.defCmpGrp)
        self.toeDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.legIKCtrlSpaceInputConstraint = PoseConstraint('_'.join([self.legIKCtrlSpace.getName(), 'To', self.globalSRTInputTgt.getName()]))
        self.legIKCtrlSpaceInputConstraint.setMaintainOffset(True)
        self.legIKCtrlSpaceInputConstraint.addConstrainer(self.globalSRTInputTgt)
        self.legIKCtrlSpace.addConstraint(self.legIKCtrlSpaceInputConstraint)

        self.legUpVCtrlSpaceInputConstraint = PoseConstraint('_'.join([self.legUpVCtrlSpace.getName(), 'To', self.globalSRTInputTgt.getName()]))
        self.legUpVCtrlSpaceInputConstraint.setMaintainOffset(True)
        self.legUpVCtrlSpaceInputConstraint.addConstrainer(self.globalSRTInputTgt)
        self.legUpVCtrlSpace.addConstraint(self.legUpVCtrlSpaceInputConstraint)

        self.legRootInputConstraint = PoseConstraint('_'.join([self.uplegFKCtrlSpace.getName(), 'To', self.legPelvisInputTgt.getName()]))
        self.legRootInputConstraint.setMaintainOffset(True)
        self.legRootInputConstraint.addConstrainer(self.legPelvisInputTgt)
        self.uplegFKCtrlSpace.addConstraint(self.legRootInputConstraint)


        self.footCtrlSpaceConstraint = PoseConstraint('_'.join([self.footCtrlSpace.getName(), 'To', self.legEndXfoOutputTgt.getName()]))
        self.footCtrlSpaceConstraint.setMaintainOffset(True)
        self.footCtrlSpaceConstraint.addConstrainer(self.legEndXfoOutputTgt)
        self.footCtrlSpace.addConstraint(self.footCtrlSpaceConstraint)


        # ===============
        # Add KL Ops
        # ===============

        # Add FootRocker KL Op
        self.footRockerKLOp = KLOperator('footRockerKLOp', 'OSS_FootRockerSystem', 'OSS_Kraken')
        self.addOperator(self.footRockerKLOp)

        # Add Att Inputs
        # If the following line is not present, the build fails "Exception: Operator 'footRockerKLOp' of type 'FootRockerSystem' arg 'drawDebug' not connected."
        self.footRockerKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.footRockerKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.footRockerKLOp.setInput('rightSide', self.rightSideInputAttr)
        self.footRockerKLOp.setInput('footRocker', footRockerInputAttr)
        self.footRockerKLOp.setInput('ballBreak', ballBreakInputAttr)
        self.footRockerKLOp.setInput('footTilt', footTiltInputAttr)

        # Add Xfo Inputs
        self.footRockerKLOp.setInput('ikCtrl', self.legIKTarget)
        self.footRockerKLOp.setInput('heelPivot', self.heelPivotLocator)
        self.footRockerKLOp.setInput('ballPivot', self.toePivotLocator)
        self.footRockerKLOp.setInput('toePivot', self.toeTipPivotLocator)
        self.footRockerKLOp.setInput('footJointLoc', self.footJointLocator)
        self.footRockerKLOp.setInput('toeJointLoc', self.toeJointLocator)
        self.footRockerKLOp.setInput('innerPivotLoc', self.innerPivotLocator)
        self.footRockerKLOp.setInput('outerPivotLoc', self.outerPivotLocator)

        # Add Xfo Outputs
        self.footRockerKLOp.setOutput('ikHandle', self.ikgoalOutputTgt)
        self.footRockerKLOp.setOutput('footJoint', self.footRockerFootOutputTgt)
        self.footRockerKLOp.setOutput('toeJoint', self.footRockerToeOutputTgt)



        # Add Leg KL Op
        self.legIKKLOp = KLOperator('legKLOp', 'OSS_TwoBoneIKSolver', 'OSS_Kraken')
        self.addOperator(self.legIKKLOp)

        # Add Att Inputs
        self.legIKKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.legIKKLOp.setInput('rigScale', self.rigScaleInputAttr)

        self.legIKKLOp.setInput('bone0Len', self.legBone0LenInputAttr)
        self.legIKKLOp.setInput('bone1Len', self.legBone1LenInputAttr)
        self.legIKKLOp.setInput('ikBlend', legIKBlendInputAttr)
        #self.legIKKLOp.setInput('mocapBlend', mocapBlendInputAttr)
        #self.legIKKLOp.setInput('footIK', footIKInputAttr)
        #self.legIKKLOp.setInput('softIK', legSoftIKInputAttr)
        self.legIKKLOp.setInput('softDist', legSoftDistInputAttr)
        self.legIKKLOp.setInput('stretch', legStretchBlendInputAttr)
        self.legIKKLOp.setInput('rightSide', self.rightSideInputAttr)

        # Add Xfo Inputs
        self.legIKKLOp.setInput('root', self.legPelvisInputTgt)
        self.legIKKLOp.setInput('bone0FK', self.uplegFKCtrl)
        self.legIKKLOp.setInput('bone1FK', self.lolegFKCtrl)
        self.legIKKLOp.setInput('ikHandle', self.ikgoalOutputTgt)
        self.legIKKLOp.setInput('upV', self.legUpVCtrl)

        # Add Xfo Outputs
        self.legIKKLOp.setOutput('bone0Out', self.uplegOutputTgt)
        self.legIKKLOp.setOutput('bone1Out', self.lolegOutputTgt)
        self.legIKKLOp.setOutput('bone2Out', self.legEndXfoOutputTgt)


        # Add Leg Deformer KL Op
        self.outputsToDeformersKLOp = KLOperator('legDeformerKLOp', 'MultiPoseConstraintSolver', 'Kraken')
        self.addOperator(self.outputsToDeformersKLOp)

        # Add Att Inputs
        self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.outputsToDeformersKLOp.setInput('constrainers', [self.uplegOutputTgt, self.lolegOutputTgt, self.legEndXfoOutputTgt])

        # Add Xfo Outputs
        self.outputsToDeformersKLOp.setOutput('constrainees', [uplegDef, lolegDef, ankleDef])




        # Add Foot Deformer KL Op
        self.IKFootBlendKLOp = KLOperator('IKFootBlendKLOp', 'OSS_IKFootBlendSolver', 'OSS_Kraken')
        self.addOperator(self.IKFootBlendKLOp)

        # Add Att Inputs
        self.IKFootBlendKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.IKFootBlendKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.IKFootBlendKLOp.setInput('blend', footIKInputAttr)

        # Add Xfo Inputs)
        self.IKFootBlendKLOp.setInput('ikFoot', self.footRockerFootOutputTgt)
        self.IKFootBlendKLOp.setInput('fkFoot', self.footCtrl)
        self.IKFootBlendKLOp.setInput('ikToe', self.footRockerToeOutputTgt)
        self.IKFootBlendKLOp.setInput('fkToe', self.toeCtrl)
        # Add Xfo Outputs
        self.IKFootBlendKLOp.setOutput('foot', self.footOutputTgt)
        self.IKFootBlendKLOp.setOutput('toe', self.toeOutputTgt)


        # Add HierBlend Solver
        self.hierBlendSolver = KLOperator('legHierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
        self.addOperator(self.hierBlendSolver)
        self.hierBlendSolver.setInput('blend', mocapBlendInputAttr)
        #self.hierBlendSolver.resizeInput('parentIndexes', 2)
        self.hierBlendSolver.setInput('parentIndexes', [2, 3])
        #self.hierBlendSolver.setInput('parentIndexes', [IntegerAttribute("blah", value=2), IntegerAttribute("blah2" ,value=3)])


        # Add Att Inputs
        self.hierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        self.hierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        self.hierBlendSolver.setInput('hierA', [self.footOutputTgt, self.toeOutputTgt])
        self.hierBlendSolver.setInput('hierB', [self.footMocap, self.toeMocap])

        # Add Xfo Outputs
        self.hierBlendSolver.setOutput('hierOut', [self.footDef, self.toeDef])



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

        super(OSSLegComponentRig, self).loadData( data )


        # TODO: make this a property of the component
        boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            boneAxisStr = "NEGX"
        boneAxis = axisStrToTupleMapping["NEGX"]


        #Upleg
        self.uplegFKCtrlSpace.xfo = data['uplegXfo']
        self.uplegFKCtrl.xfo = data['uplegXfo']
        self.uplegFKCtrl.scalePointsOnAxis(data['uplegLen'], boneAxisStr)

        self.uplegOutputTgt.xfo = data['uplegXfo']
        self.lolegOutputTgt.xfo = data['kneeXfo']

        # Loleg
        self.lolegFKCtrlSpace.xfo = data['kneeXfo']
        self.lolegFKCtrl.xfo = data['kneeXfo']
        self.lolegFKCtrl.scalePointsOnAxis(data['lolegLen'], boneAxisStr)

        self.footCtrlSpace.xfo = data['footXfo']
        self.footCtrl.xfo = data['footXfo']
        self.footCtrl.scalePointsOnAxis(data['footLen'], boneAxisStr)

        self.toeCtrlSpace.xfo = data['toeXfo']
        self.toeCtrl.xfo = data['toeXfo']
        self.toeCtrl.scalePointsOnAxis(data['toeLen'], boneAxisStr)

        self.footMocap.xfo = data['footXfo']
        self.footMocap.scalePointsOnAxis(data['footLen'], boneAxisStr)

        self.toeMocapSpace.xfo = data['toeXfo']
        self.toeMocap.xfo = data['toeXfo']
        self.toeMocap.scalePointsOnAxis(data['toeLen'], boneAxisStr)


        #Until later when we have better guide rigs setups, assume world Y up and Z forward to toe
        self.legIKCtrlSpace.xfo.tr = data['heelPivotXfo'].tr
        self.legIKCtrlSpace.xfo.aimAt(aimVector=Vec3(0, 1, 0), upPos=self.toeCtrl.xfo.tr, aimAxis=(0, 1, 0), upAxis=(0, 0, 1))
        self.legIKCtrl.xfo = self.legIKCtrlSpace.xfo
        self.legIKTarget.xfo = self.legIKCtrlSpace.xfo
        self.legIKTarget.xfo.tr = data['ankleXfo'].tr


        if self.getLocation() == "R":
            pass
            #self.legIKCtrl.rotatePoints(0, 90, 0)
            #self.legIKCtrl.translatePoints(Vec3(-1.0, 0.0, 0.0))
        else:
            pass
            #self.legIKCtrl.rotatePoints(0, -90, 0)
            #self.legIKCtrl.translatePoints(Vec3(1.0, 0.0, 0.0))

        self.legUpVCtrlSpace.xfo = data['upVXfo']
        self.legUpVCtrl.xfo = data['upVXfo']

        self.rightSideInputAttr.setValue(self.getLocation() == 'R')
        self.legBone0LenInputAttr.setMin(0.0)
        self.legBone0LenInputAttr.setMax(data['uplegLen'] * 3.0)
        self.legBone0LenInputAttr.setValue(data['uplegLen'])
        self.legBone1LenInputAttr.setMin(0.0)
        self.legBone1LenInputAttr.setMax(data['lolegLen'] * 3.0)
        self.legBone1LenInputAttr.setValue(data['lolegLen'])

        self.legPelvisInputTgt.xfo = data['uplegXfo']
        self.toeJointLocator.xfo = data["toeXfo"]
        self.footJointLocator.xfo = data["footXfo"]

        self.heelPivotLocator.xfo = data["heelPivotXfo"]
        self.heelPivotLocator.xfo.ori = self.legIKCtrl.xfo.ori
        self.toeTipPivotLocator.xfo = data["toeTipPivotXfo"]
        self.toeTipPivotLocator.xfo.ori = self.legIKCtrl.xfo.ori
        self.innerPivotLocator.xfo = data["innerPivotXfo"]
        self.innerPivotLocator.xfo.ori = self.legIKCtrl.xfo.ori
        self.outerPivotLocator.xfo = data["outerPivotXfo"]
        self.outerPivotLocator.xfo.ori = self.legIKCtrl.xfo.ori
        self.toePivotLocator.xfo = data["toeXfo"]
        self.toePivotLocator.xfo.ori = self.legIKCtrl.xfo.ori

        # Eval Constraints
        self.legIKCtrlSpaceInputConstraint.evaluate()
        self.legUpVCtrlSpaceInputConstraint.evaluate()
        self.legRootInputConstraint.evaluate()

        # Eval Operators
        self.footRockerKLOp.evaluate()
        self.legIKKLOp.evaluate()
        self.outputsToDeformersKLOp.evaluate()
        self.IKFootBlendKLOp.evaluate()
        self.hierBlendSolver.evaluate()

        #JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.uplegFKCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.lolegFKCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.footCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.toeCtrl.scalePoints(Vec3(1.0, data['globalComponentCtrlSize'], data['globalComponentCtrlSize']))
        self.legIKCtrl.scalePoints(globalScale)
        self.legUpVCtrl.scalePoints(globalScale)

        footPlane = Control("TMP", shape="square")
        footPlane.alignOnZAxis()
        footPlane.scalePoints(Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], 1.0))
        footPlane.scalePointsOnAxis(self.legIKCtrl.xfo.tr.subtract(self.toeTipPivotLocator.xfo.tr).length(), "POSZ")
        self.legIKCtrl.appendCurveData(footPlane.getCurveData())



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSLegComponentGuide)
ks.registerComponent(OSSLegComponentRig)
