
import math, re

from kraken.core.maths import Vec3, AXIS_NAME_TO_TUPLE_MAP, AXIS_NAME_TO_INT_MAP
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.euler import rotationOrderStrToIntMapping

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
from kraken.core.objects.locator import Locator
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "mouth"


class OSSMouth(OSS_Component):
    """Mouth Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSMouth, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.curveOutputTgt = self.createOutput('curve', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.mouthOutputTgt = self.createOutput('mouth', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.mouthEndOutputTgt = self.createOutput('mouthEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs


class OSSMouthGuide(OSSMouth):
    """Mouth Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Mouth Guide Component:" + name)
        super(OSSMouthGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.curveCtrlNames = StringAttribute('curveCtrlNames', value="1 Sneer", parent=self.guideSettingsAttrGrp)
        self.numSpansAttr = IntegerAttribute('numSpans', value=13, minValue=0, maxValue=20,  parent=self.guideSettingsAttrGrp)

        self.alignXAttr = IntegerAttribute('alignX', value=2, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)
        self.alignYAttr = IntegerAttribute('alignY', value=-1, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)
        self.alignZAttr = IntegerAttribute('alignZ', value=3, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)

        # midCurve
        self.midCurveCtrl = Control('midCurve', parent=self.ctrlCmpGrp)
        self.midCurveCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_midCurveHandleCtrl = Control('L_midCurveHandle', parent=self.midCurveCtrl)
        self.R_midCurveHandleCtrl = Control('R_midCurveHandle', parent=self.midCurveCtrl)
        self.midDummy = Control('midDummy', parent=self.ctrlCmpGrp)

        self.lMouthCtrl = Control('L_Mouth', parent=self.ctrlCmpGrp)
        self.rMouthCtrl = Control('R_Mouth', parent=self.ctrlCmpGrp)

        # upCurve
        self.upCurveCtrl = Control('upCurve', parent=self.ctrlCmpGrp)
        self.upCurveCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_upCurveHandleCtrl = Control('L_upCurveHandle', parent=self.upCurveCtrl)
        self.R_upCurveHandleCtrl = Control('R_upCurveHandle', parent=self.upCurveCtrl)
        self.upDummy = Control('upDummy', parent=self.ctrlCmpGrp)

        self.lMouthOutCtrl = Control('L_MouthOut', parent=self.ctrlCmpGrp)
        self.rMouthOutCtrl = Control('R_MouthOut', parent=self.ctrlCmpGrp)

        # loCurve
        self.loCurveCtrl = Control('loCurve', parent=self.ctrlCmpGrp)
        self.loCurveCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_loCurveHandleCtrl = Control('L_loCurveHandle', parent=self.loCurveCtrl)
        self.R_loCurveHandleCtrl = Control('R_loCurveHandle', parent=self.loCurveCtrl)
        self.loDummy = Control('loDummy', parent=self.ctrlCmpGrp)



        for ctrl in [self.L_midCurveHandleCtrl,
                     self.R_midCurveHandleCtrl,
                     self.L_upCurveHandleCtrl,
                     self.R_upCurveHandleCtrl,
                     self.L_loCurveHandleCtrl,
                     self.R_loCurveHandleCtrl]:
            ctrl.setColor("red")


        self.defCtrls = []
        self.curveCtrls = []
        self.symMapping = {}

        # Add Mouth Symmetry Canvas Op
        self.lSideObjs = []
        self.rSideObjs = []
        self.lSideParentObjs = []

        # Add Att Inputs
        self.refInputs = []
        self.midCurveControls = []
        self.midCurveOutputs = []

        self.mouthCtrl = Control('mouth', parent=self.ctrlCmpGrp, shape="sphere")
        self.mouthEndCtrl = Control('mouthEnd', parent=self.ctrlCmpGrp, shape="sphere")
        self.mouthCtrl.setColor("green")
        self.mouthEndCtrl.setColor("green")

        # setting inital Guide Data
        # note that we're not setting the R Side Objects since all R_ objects are currently reflected from their L_ symmetric Partner
        data = {
                "name": name,
                "location": "M",
                "mouthXfo": Xfo(Vec3(0, 15, 0)),
                "midCurveXfo": Xfo(Vec3(0, 15, 4)),
                "L_midCurveHandleXfo": Xfo(Vec3(1.75, 15, 4)),
                "R_midCurveHandleXfo": Xfo(Vec3(-1.75, 15, 4)),
                "loCurveXfo": Xfo(Vec3(0, 13, 4)),
                "L_loCurveHandleXfo": Xfo(Vec3(1.75, 13, 4)),
                "R_loCurveHandleXfo": Xfo(Vec3(-1.75, 13, 4)),
                "upCurveXfo": Xfo(Vec3(0, 17, 4)),
                "L_upCurveHandleXfo": Xfo(Vec3(1.75, 17, 4)),
                "R_upCurveHandleXfo": Xfo(Vec3(-1.75, 17, 4)),
                "L_MouthXfo": Xfo(Vec3(3, 15, 3)),
                "R_MouthXfo": Xfo(Vec3(-3, 15, 3)),
                "L_MouthOutXfo": Xfo(Vec3(4, 15, 2)),
                "R_MouthOutXfo": Xfo(Vec3(-4, 15, 2)),
                "mouthEndXfo": Xfo(Vec3(0, 15, 4)),
                "alignX": 2,
                "alignY": -1,
                "alignZ": 3
               }


        self.paramOut = []
        # Add midCurve Debug Canvas Op
        self.midCurveGuideOp = CanvasOperator('midCurveGuideOp', 'OSS.Solvers.NURBSCurveGuideSolver')
        self.addOperator(self.midCurveGuideOp)

        self.midCurveGuideOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.midCurveGuideOp.setInput('rigScale', 1.0)
        self.midCurveGuideOp.setInput('degree', 4)

        self.midCurveGuideOp.setInput('controls', self.midCurveControls)
        self.midCurveGuideOp.setInput('refMats', self.midCurveControls)

        self.midCurveGuideOp.setOutput('result', self.paramOut )

        # update Inputs
        self.midCurveControls.append(self.lMouthCtrl)
        self.midCurveControls.append(self.L_midCurveHandleCtrl)
        self.midCurveControls.append(self.midCurveCtrl)
        self.midCurveControls.append(self.R_midCurveHandleCtrl)
        self.midCurveControls.append(self.rMouthCtrl)

        self.midCurveOutputs.append(self.midDummy)


        # Add upCurve Debug Canvas Op
        self.upCurveGuideOp = CanvasOperator('upCurveGuideOp', 'OSS.Solvers.NURBSCurveGuideSolver')
        self.addOperator(self.upCurveGuideOp)

        self.upCurveControls = []
        self.upCurveOutputs = []

        self.upCurveGuideOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.upCurveGuideOp.setInput('rigScale', 1.0)
        self.upCurveGuideOp.setInput('degree', 3)

        self.upCurveGuideOp.setInput('controls', self.upCurveControls)
        self.upCurveGuideOp.setInput('refMats', self.upCurveControls)

        self.upCurveGuideOp.setOutput('result', self.paramOut)

        # update Inputs
        self.upCurveControls.append(self.lMouthOutCtrl)
        self.upCurveControls.append(self.L_upCurveHandleCtrl)
        self.upCurveControls.append(self.upCurveCtrl)
        self.upCurveControls.append(self.R_upCurveHandleCtrl)
        self.upCurveControls.append(self.rMouthOutCtrl)


        # Add lowCurve Debug Canvas Op
        self.loCurveGuideOp = CanvasOperator('loCurveGuideOp', 'OSS.Solvers.NURBSCurveGuideSolver')
        self.addOperator(self.loCurveGuideOp)

        self.loCurveControls = []
        self.loCurveOutputs = []

        self.loCurveGuideOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.loCurveGuideOp.setInput('rigScale', 1.0)
        self.loCurveGuideOp.setInput('degree', 3)

        self.loCurveGuideOp.setInput('controls', self.loCurveControls)
        self.loCurveGuideOp.setInput('refMats', self.loCurveControls)

        self.loCurveGuideOp.setOutput('result', self.paramOut )

        # update Inputs
        self.loCurveControls.append(self.lMouthOutCtrl)
        self.loCurveControls.append(self.L_loCurveHandleCtrl)
        self.loCurveControls.append(self.loCurveCtrl)
        self.loCurveControls.append(self.R_loCurveHandleCtrl)
        self.loCurveControls.append(self.rMouthOutCtrl)

        self.allObject3Ds = self.getHierarchyNodes(classType="Control")

        for ctrl in self.allObject3Ds:
            self.addToSymDict(ctrl)

        for k,value in self.symMapping.iteritems():
            self.lSideObjs.append(value["lSide"])
            self.lSideParentObjs.append(value["lSideParent"])
            self.rSideObjs.append(value["rSide"])


        # Add reflection Canvas Op, should feed inputs from self.symMapping
        self.reflectionOp = CanvasOperator('reflectionOp', 'OSS.Solvers.reflectMat44Solver')
        self.addOperator(self.reflectionOp)

        self.reflectionOp.setInput('inputs',   self.lSideObjs)
        self.reflectionOp.setInput('inputParents',  self.lSideParentObjs)
        self.reflectionOp.setOutput('results', self.rSideObjs)

        self.loadData(data)

        Profiler.getInstance().pop()

    def addToSymDict(self, ctrl):
        if not self.symMapping:
            self.symMapping = {}
        name = ctrl.getName()
        if not (name.startswith("L_") or name.startswith("R_")):
            ctrl.lockTranslation(x=True, y=False, z=False)
            return  self.symMapping

        if name.startswith("R_"):
            idxName = name.replace("R_","L_")
        else:
            idxName = name

        if not idxName in  self.symMapping:
             self.symMapping[idxName] = {}

        if name.startswith("L_"):
             self.symMapping[idxName]["lSide"] = ctrl
             self.symMapping[idxName]["lSideParent"] = ctrl.getParent()
        else:
             self.symMapping[idxName]["rSide"] = ctrl

        return self.symMapping


    def createGuideControls(self, ctrlType, controlsList, defNames):
        # Delete current controls
        '''
        self.controlXforms = []
        # Store current values if guide controls already exist
        # for i, name in enumerate(["curveDeformers", "curveControls"]):
        current = 0
        for i, ctrl in enumerate(controlsList):
            self.controlXforms.append([ctrl.xfo])
            if ctrl.getParent() is self.mouthCtrl:
                self.controlXforms.append([ctrl.xfo])
                current = len(self.controlXforms) -1
            else:
                self.controlXforms[current].append(ctrl.xfo)
        '''
        lSideControls = []
        rSideControls = []
        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        del self.refInputs[:]

        if ctrlType == "curveDeformers":
            parent = self.mouthCtrl
            defControlNameList = []

            #Build Deformer Names
            half = int(math.floor(defNames/2))

            n=0
            for i in range(half):
                lSideControls.append('L_' + str(half-n))
                rSideControls.append('R_' + str(n+1))
                n += 1


            if lSideControls:
                lSideControls.reverse()

                defControlNameList = lSideControls + ["Mid"] + rSideControls

            if not defNames % 2 == 0:
                defControlNameList = lSideControls + ["Mid"] + rSideControls
            else:
                defControlNameList = lSideControls + rSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="sphere")
                newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 5)))
                newCtrl.scalePoints(Vec3(.125,.125,.125))
                controlsList.append(newCtrl)


        if ctrlType == "curveControls":
            parent = self.midCurveCtrl
            defControlNameList =[]

            # Lets build all new handles
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True


            # etting up names
            lSideControls = ["L_" + x for x in defControlNameList]
            rSideControls = ["R_" + x for x in defControlNameList]

            if lSideControls:
                lSideControls.reverse()

            defControlNameList = lSideControls + ["Mid"] + rSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="circle")
                newCtrl.rotatePoints(90,0,0)
                newCtrl.setColor("brownMuted")
                newCtrl.xfo = parent.xfo
                newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 8)))
                newCtrl.scalePoints(Vec3(.5,.5,.5))
                controlsList.append(newCtrl)


        for ctrl in controlsList:
            self.addToSymDict(ctrl)

        return True


    def updateDefNames(self, defNames):
        self.createGuideControls("curveDeformers", self.defCtrls, defNames)

    def updatecurveCtrls(self, defNames):
        self.createGuideControls("curveControls", self.curveCtrls, defNames)


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """


        data = super(OSSMouthGuide, self).saveData()

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

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data


        super(OSSMouthGuide, self).loadData( data )


        self.loadAllObjectData(data, "Control")
        self.loadAllObjectData(data, "Transform")


        return True



    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        # Values
        mouthPosition = self.mouthCtrl.xfo.tr
        mouthEndPosition = self.mouthEndCtrl.xfo.tr

        # Calculate Mouth Xfo

        # atVector
        mouthUpV = Xfo(Vec3(0.0, 1.0, 0.0)).tr

        rootToEnd = mouthEndPosition.subtract(mouthPosition).unit()
        rootToUpV = mouthUpV.subtract(mouthPosition).unit()
        bone1ZAxis = rootToUpV.cross(rootToEnd).unit()
        bone1Normal = bone1ZAxis.cross(rootToEnd).unit()

        mouthXfo = Xfo()
        mouthXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, mouthPosition)

        mouthLen = mouthPosition.subtract(mouthEndPosition).length()


        data = super(OSSMouthGuide, self).getRigBuildData()

        # should include getCurveData
        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")
        data['mouthXfo'] = mouthXfo
        data['mouthLen'] = mouthLen
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

        return OSSMouthRig


class OSSMouthRig(OSSMouth):
    """Mouth Component"""

    def __init__(self, name='Mouth', parent=None):

        Profiler.getInstance().push("Construct Mouth Rig Component:" + name)
        super(OSSMouthRig, self).__init__(name, parent)

        # ==========
        # Deformers
        # ==========

        self.parentSpaceInputTgt.childJoints = []

        # Mouth
        self.mouthDef = Joint('mouth', parent=self.deformersParent)
        self.mouthDef.setComponent(self)
        self.parentSpaceInputTgt.childJoints.append(self.mouthDef)

        # =========
        # Controls
        # =========
        # Mouth

        self.mouthCtrlSpace = CtrlSpace('mouth', parent=self.ctrlCmpGrp)
        self.mouthCtrl = Control('mouth', parent=self.mouthCtrlSpace, shape="halfCircle")

        # midMouth
        self.topMouthCtrlSpace = CtrlSpace('topMouth', parent=self.mouthCtrlSpace)

        # midMouth
        self.midMouthCtrlSpace = CtrlSpace('midMouth', parent=self.ctrlCmpGrp)
        self.midMouthCtrl = CtrlSpace('midMouth', parent=self.midMouthCtrlSpace)

        # self.allMouthCtrl = Control('allMouth', parent=self.midMouthCtrlSpace, shape="square")
        # loCurve
        self.loCurveCtrlSpace = CtrlSpace('loCurve', parent=self.mouthCtrl)
        self.loCurveCtrl = Control('loCurve', parent=self.loCurveCtrlSpace, shape="halfCircle")
        self.L_loCurveHandleCtrl = CtrlSpace('L_loCurveHandle', parent=self.loCurveCtrl)
        self.R_loCurveHandleCtrl = CtrlSpace('R_loCurveHandle', parent=self.loCurveCtrl)
        self.loDummy = CtrlSpace('loDummy', parent=self.ctrlCmpGrp)

        # upCurve
        self.upCurveCtrlSpace = CtrlSpace('upCurve', parent=self.mouthCtrlSpace)
        self.upCurveCtrl = Control('upCurve', parent=self.upCurveCtrlSpace, shape="halfCircle")
        self.L_upCurveHandleCtrl = CtrlSpace('L_upCurveHandle', parent=self.upCurveCtrl)
        self.R_upCurveHandleCtrl = CtrlSpace('R_upCurveHandle', parent=self.upCurveCtrl)
        self.upDummy = CtrlSpace('upDummy', parent=self.ctrlCmpGrp)


        self.lMouthCtrlSpace = CtrlSpace('L_Mouth', parent=self.midMouthCtrl)
        self.lMouthCtrl = Control('L_Mouth_tweak', parent=self.lMouthCtrlSpace, shape="circle")
        self.lMouthCtrl.alignOnXAxis()
        self.rMouthCtrlSpace = CtrlSpace('R_Mouth', parent=self.midMouthCtrl)
        self.rMouthCtrl = Control('R_Mouth_tweak', parent=self.rMouthCtrlSpace, shape="circle")
        self.rMouthCtrl.alignOnXAxis()


        # ==============
        # Constrain I/O
        # ==============
        # Mouth
        self.mouthInputConstraint = self.mouthCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.mouthConstraint = self.mouthOutputTgt.constrainTo(self.mouthCtrl, maintainOffset=False)
        self.mouthEndConstraint = self.mouthEndOutputTgt.constrainTo(self.mouthCtrl, maintainOffset=False)

        self.mouthOutputTgt.parentJoint =  self.mouthDef

        # Curve
        # curveInputConstraint = PoseConstraint('_'.join([self.midCurveCtrl.getName(), 'To', self.parentSpaceInputTgt.getName()]))
        # curveInputConstraint.setMaintainOffset(True)
        # curveInputConstraint.addConstrainer(self.parentSpaceInputTgt)
        # self.midCurveCtrlSpace.addConstraint(curveInputConstraint)

        # Constraint outputs
        # curveConstraint = PoseConstraint('_'.join([self.curveOutputTgt.getName(), 'To', self.midCurveCtrl.getName()]))
        # curveConstraint.addConstrainer(self.midCurveCtrl)
        # self.curveOutputTgt.addConstraint(curveConstraint)
        Profiler.getInstance().pop()




    def createGuideControls(self, ctrlType, controlsList, defNames):
        # Delete current controls
        '''
        self.controlXforms = []
        # Store current values if guide controls already exist
        # for i, name in enumerate(["curveDeformers", "curveControls"]):
        current = 0
        for i, ctrl in enumerate(controlsList):
            self.controlXforms.append([ctrl.xfo])
            if ctrl.getParent() is self.mouthCtrl:
                self.controlXforms.append([ctrl.xfo])
                current = len(self.controlXforms) -1
            else:
                self.controlXforms[current].append(ctrl.xfo)
        '''

        lSideControls = []
        rSideControls = []
        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        parent = self.ctrlCmpGrp

        if ctrlType == "upCurveDef" or ctrlType == "loCurveDef":
            defControlNameList = []

            #Build Deformer Names
            half = int(math.floor(defNames/2))

            n=0
            for i in range(half):
                lSideControls.append('L_' + str(half-n))
                rSideControls.append('R_' + str(n+1))
                n += 1

            lSideControls.reverse()
            rSideControls.reverse()

            if not defNames % 2 == 0:
                defControlNameList = rSideControls + ["Mid"] + lSideControls
            else:
                defControlNameList = rSideControls + lSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Locator(defName + "_" + ctrlType.replace("Def",""), parent= self.ctrlCmpGrp)
                newCtrl.setShapeVisibility(False)
                newCtrl.xfo = parent.xfo
                controlsList.append(newCtrl)

                newDef = Joint(defName + "_" + ctrlType.replace("Def",""), parent= self.mouthDef)
                newDef.setComponent(self)
                newDef.constrainTo(newCtrl)


        if ctrlType == "curveControls":
            defControlNameList =[]

            # Lets build all new handles
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True


            # etting up names
            lSideControls = ["L_" + x for x in defControlNameList]
            rSideControls = ["R_" + x for x in defControlNameList]

            if lSideControls:
                lSideControls.reverse()

            defControlNameList = lSideControls + ["Mid"] + rSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="halfCircle")
                newCtrl.rotatePoints(90,0,0)
                newCtrl.setColor("brownMuted")
                newCtrl.xfo = parent.xfo
                newCtrl.scalePoints(Vec3(.125,.125,.125))
                controlsList.append(newCtrl)
                newCtrl.lockRotation(x=False, y=True, z=True)
                newCtrl.lockScale(x=True, y=True, z=True)



        # for ctrl in controlsList:
        #     self.addToSymDict(ctrl)

        return controlsList



    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSMouthRig, self).loadData( data )


        # ===============
        # Add Fabric Ops
        # ===============
        # Add NURBSCurveXfoSolver Canvas Op
        # Add lowCurve Guide Canvas Op
        self.alignX = data["alignX"]
        self.alignY = data["alignY"]
        self.alignZ = data["alignZ"]

        self.upCurveRigOp = KLOperator('upCurveRigOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')

        self.addOperator(self.upCurveRigOp)
        # self.params = [0.025,0.125,0.3,0.5,0.7,0.875,0.975]
        self.params = [0.05,0.25,0.5,0.75,0.95]

        self.upCurveControls = []
        self.upCurveOutputs = []
        self.rigControlAligns = []
        self.upCurveControls.append(self.lMouthCtrl)
        self.upCurveControls.append(self.L_upCurveHandleCtrl)
        self.upCurveControls.append(self.upCurveCtrl)
        self.upCurveControls.append(self.R_upCurveHandleCtrl)
        self.upCurveControls.append(self.rMouthCtrl)

        '''

        for i in range(len(self.upCurveControls)):
            ctrl = self.upCurveControls[i]
            newSpace = CtrlSpace(ctrl._name + 'out', parent=ctrl)
            self.upCurveControls[i] = newSpace


        for i in range(len(self.loCurveControls)):
            ctrl = self.upCurveControls[i]
            newSpace = CtrlSpace(ctrl._name + 'out', parent=ctrl)
            self.loCurveControls[i] = newSpace
        '''


        self.upCurveRigOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.upCurveRigOp.setInput('rigScale', 1.0)
        self.upCurveRigOp.setInput('alignX', self.alignX )
        self.upCurveRigOp.setInput('alignY', self.alignY )
        self.upCurveRigOp.setInput('alignZ', self.alignZ )
        self.upCurveRigOp.setInput('degree', 4)
        self.upCurveRigOp.setInput('keepArcLength', 0.0)
        self.upCurveRigOp.setInput('compressionAmt', 0.0)
        self.upCurveRigOp.setInput('followCurveTangent', 0.0)
        self.upCurveRigOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.upCurveRigOp.setInput('parent', self.mouthCtrlSpace)

        self.upCurveRigOp.setInput('atVec', self.mouthCtrl)
        self.upCurveRigOp.setInput('controlAligns', self.rigControlAligns)
        self.upCurveRigOp.setInput('controls', self.upCurveControls)
        self.upCurveRigOp.setInput('controlsRest', self.upCurveControls)
        self.upCurveRigOp.setInput('params',self.params )

        self.upCurveRigOp.setOutput('outputs', self.upCurveOutputs)


        # ===============
        # Add Fabric Ops
        # ===============
        # Add Spine Canvas Op
        # Add lowCurve Guide Canvas Op
        self.loCurveRigOp = KLOperator('loCurveRigOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.loCurveRigOp)

        self.loCurveControls = []
        self.loCurveOutputs = []
        self.loCurveControls.append(self.lMouthCtrl)
        self.loCurveControls.append(self.L_loCurveHandleCtrl)
        self.loCurveControls.append(self.loCurveCtrl)
        self.loCurveControls.append(self.R_loCurveHandleCtrl)
        self.loCurveControls.append(self.rMouthCtrl)

        self.loCurveRigOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.loCurveRigOp.setInput('rigScale', 1.0)
        self.loCurveRigOp.setInput('alignX', self.alignX )
        self.loCurveRigOp.setInput('alignY', self.alignY )
        self.loCurveRigOp.setInput('alignZ', self.alignZ )
        self.loCurveRigOp.setInput('degree', 4)
        self.loCurveRigOp.setInput('keepArcLength', 0.0)
        self.loCurveRigOp.setInput('compressionAmt', 0.0)
        self.loCurveRigOp.setInput('followCurveTangent', 0.0)
        self.loCurveRigOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.loCurveRigOp.setInput('parent', self.mouthCtrlSpace)

        self.loCurveRigOp.setInput('atVec', self.mouthCtrl)
        self.loCurveRigOp.setInput('controlAligns', self.rigControlAligns)
        self.loCurveRigOp.setInput('controls', self.loCurveControls)
        self.loCurveRigOp.setInput('controlsRest', self.loCurveControls)
        self.loCurveRigOp.setInput('params', self.params )

        self.loCurveRigOp.setOutput('outputs', self.loCurveOutputs)

        for i in range(len(self.loCurveControls)):
            self.rigControlAligns.append(Vec3(1,2,3))

        self.rigControlAligns[3] = Vec3(-1,2,-3)
        self.rigControlAligns[4] = Vec3(1,-2,-3)

        # Add lowCurve Guide Canvas Op
        self.blendMidMouthRigOp = CanvasOperator('blendMidMouthRigOp', 'OSS.Solvers.blendMat44Solver')
        self.addOperator(self.blendMidMouthRigOp)

        # self.blendMidMouthRigOp.setInput('drawDebug', self.drawDebugInputAttr)
        # self.blendMidMouthRigOp.setInput('rigScale', 1.0)
        self.blendMidMouthRigOp.setInput('rotationAmt', .5)
        self.blendMidMouthRigOp.setInput('translationAmt', .5)
        self.blendMidMouthRigOp.setInput('scaleAmt', .5)

        self.blendMidMouthRigOp.setInput('parentSpace', self.ctrlCmpGrp)
        self.blendMidMouthRigOp.setInput('A', self.topMouthCtrlSpace)
        self.blendMidMouthRigOp.setInput('B', self.loCurveCtrlSpace)

        self.blendMidMouthRigOp.setOutput('result', self.midMouthCtrlSpace)


        # ===============
        # Add Splice Ops
        # ===============
        # Add Deformer Splice Op

        self.rigCtrls = []
        self.rigDefs = []
        self.rigCtrls.append(self.mouthCtrl)
        self.rigDefs.append(self.mouthDef)

        self.eyeCtrlConstraint = self.mouthDef.constrainTo(self.mouthCtrl, maintainOffset=False)


        # self.outputsToDeformersOKLOp = KLOperator('MultiPoseConstraintOp', 'MultiPoseConstraintSolver', 'Kraken')
        # self.addOperator(self.outputsToDeformersOKLOp)
        # self.outputsToDeformersOKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        # self.outputsToDeformersOKLOp.setInput('rigScale', self.rigScaleInputAttr)
        # self.outputsToDeformersOKLOp.setInput('constrainers', self.rigCtrls)
        # self.outputsToDeformersOKLOp.setOutput('constrainees', self.rigDefs)



        self.upCurveDefs = []
        self.upCurveCtrls = []
        self.upCurveCtrls = self.createGuideControls("curveControls", self.upCurveCtrls, data["curveCtrlNames"])

        self.upCurveDefs = self.createGuideControls("upCurveDef", self.upCurveDefs, data["numSpans"])

        self.lLoCurveCorner = Transform('L_loCurveCorner', parent=self.ctrlCmpGrp)
        self.rLoCurveCorner = Transform('R_loCurveCorner', parent=self.ctrlCmpGrp)
        self.lUpCurveCorner = Transform('L_upCurveCorner', parent=self.ctrlCmpGrp)
        self.rUpCurveCorner = Transform('R_upCurveCorner', parent=self.ctrlCmpGrp)

        curveCtrlY = .05;
        curveCtrlZ = .45;
        if self.upCurveCtrls:
            # build control hierarchy
            numCtrls = len(self.upCurveCtrls)
            half = int(math.floor(numCtrls/2))

            evenNumCtrls = (numCtrls % 2 == 0)

            for i in range(numCtrls):
                ctrl = self.upCurveCtrls[i]
                ctrl.translatePoints(Vec3(Vec3(0, curveCtrlY, curveCtrlZ)))
                ctrl.setColor("yellowMuted")
                ctrlUberParent = ctrl.insertCtrlSpace()
                ctrlParent = ctrl.insertCtrlSpace()

                # if i < (half-1):
                #     ctrlParent.constrainTo(self.upCurveCtrls[i+1], maintainOffset=True)
                # if (half+1) < i:
                #     ctrlParent.constrainTo(self.upCurveCtrls[i-1], maintainOffset=True)
                self.upCurveOutputs.append(ctrlUberParent)

        self.upCurveCtrls = [self.lMouthCtrl] + self.upCurveCtrls + [self.rMouthCtrl]

        self.upCurveRigOp.setOutput('outputs', self.upCurveOutputs)

        # Add lowCurve Debug Canvas Op
        self.upCurveDefOp = KLOperator('upCurveDefOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.upCurveDefOp)

        self.upCurveControls = []
        self.upCurveOutputs = []
        self.defControlAligns = []
        # numDefs plus two for the corners, this should be determined per closest point on curve
        self.paramsOut = [1, .96, .9, .81, .74, .66, .58, 0.5, 0.42, 0.34, 0.26, 0.19, 0.1, 0.04, 0]

        self.upCurveDefs =  [self.rUpCurveCorner] + self.upCurveDefs + [self.lUpCurveCorner]

        self.upCurveDefOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.upCurveDefOp.setInput('rigScale', 1.0)
        self.upCurveDefOp.setInput('degree', 3)
        self.upCurveDefOp.setInput('alignX', self.alignX )
        self.upCurveDefOp.setInput('alignY', self.alignY )
        self.upCurveDefOp.setInput('alignZ', self.alignZ )
        self.upCurveDefOp.setInput('keepArcLength', 0.0)
        self.upCurveDefOp.setInput('compressionAmt', 0.0)
        self.upCurveDefOp.setInput('followCurveTangent', 0.5)
        self.upCurveDefOp.setInput('altTangent', Vec3(0.0,0.0,1.0))
        self.upCurveDefOp.setInput('parent', self.mouthCtrlSpace)

        self.upCurveDefOp.setInput('atVec', self.mouthCtrl)
        self.upCurveDefOp.setInput('controlAligns', self.defControlAligns)
        self.upCurveDefOp.setInput('controls', self.upCurveCtrls)
        self.upCurveDefOp.setInput('controlsRest', self.upCurveCtrls)
        self.upCurveDefOp.setInput('params', self.paramsOut)

        self.upCurveDefOp.setOutput('outputs', self.upCurveDefs)

        self.loCurveDefs = []
        self.loCurveCtrls = []
        self.loCurveCtrls = self.createGuideControls("curveControls", self.loCurveCtrls, data["curveCtrlNames"])
        self.loCurveDefs  = self.createGuideControls("loCurveDef", self.loCurveDefs, data["numSpans"])

        if self.loCurveCtrls:
            # build control hierarchy
            numCtrls = len(self.loCurveCtrls)
            half = int(math.floor(numCtrls/2))
            evenNumCtrls = (numCtrls % 2 == 0)

            for i in range(numCtrls):
                ctrl = self.loCurveCtrls[i]
                ctrl.translatePoints(Vec3(Vec3(0, curveCtrlY, curveCtrlZ)))
                ctrl.scalePoints(Vec3(Vec3(1, -1, 1)))
                ctrlUberParent = ctrl.insertCtrlSpace()
                ctrlParent = ctrl.insertCtrlSpace()
                # if i < (half-1):
                #     ctrlParent.constrainTo(self.loCurveCtrls[i+1], maintainOffset=True)
                # if (half+1) < i:
                #     ctrlParent.constrainTo(self.loCurveCtrls[i-1], maintainOffset=True)
                self.loCurveOutputs.append(ctrlUberParent)

        self.loCurveCtrls = [self.lMouthCtrl] + self.loCurveCtrls + [self.rMouthCtrl]


        self.loCurveRigOp.setOutput('outputs', self.loCurveOutputs)
        # Add lowCurve Debug Canvas Op
        self.loCurveDefOp = KLOperator('loCurveDefOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.loCurveDefOp)

        self.c = []
        self.loCurveOutputs = []
        self.loCurveDefs =  [self.rLoCurveCorner] + self.loCurveDefs + [self.lLoCurveCorner]

        self.loCurveDefOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.loCurveDefOp.setInput('rigScale', 1.0)
        self.loCurveDefOp.setInput('degree', 3)
        self.loCurveDefOp.setInput('alignX', self.alignX )
        self.loCurveDefOp.setInput('alignY', self.alignY )
        self.loCurveDefOp.setInput('alignZ', self.alignZ )
        self.loCurveDefOp.setInput('keepArcLength', 0.0)
        self.loCurveDefOp.setInput('compressionAmt', 0.0)
        self.loCurveDefOp.setInput('followCurveTangent', 0.5)
        self.loCurveDefOp.setInput('altTangent', Vec3(0.0,0.0,1.0))
        self.loCurveDefOp.setInput('parent', self.mouthCtrlSpace)

        self.loCurveDefOp.setInput('atVec', self.mouthCtrl)
        self.loCurveDefOp.setInput('controlAligns', self.defControlAligns)
        self.loCurveDefOp.setInput('controls', self.loCurveCtrls)
        self.loCurveDefOp.setInput('controlsRest', self.loCurveCtrls)
        self.loCurveDefOp.setInput('params', self.paramsOut )

        self.loCurveDefOp.setOutput('outputs', self.loCurveDefs)


        for i in range(len(self.loCurveCtrls)):
            self.defControlAligns.append(Vec3(1,2,3));



        # Add lowCurve Guide Canvas Op
        self.lMouthCornerLoc = Locator('L_mouthCorner', parent=self.ctrlCmpGrp)
        self.lMouthCornerLoc.setShapeVisibility(False)

        self.blendLeftCornerOp = CanvasOperator('blendLeftCornerOp', 'OSS.Solvers.blendMat44Solver')
        self.addOperator(self.blendLeftCornerOp)

        # self.blendLeftCornerOp.setInput('drawDebug', self.drawDebugInputAttr)
        # self.blendLeftCornerOp.setInput('rigScale', 1.0)
        self.blendLeftCornerOp.setInput('rotationAmt', .5)
        self.blendLeftCornerOp.setInput('translationAmt', .5)
        self.blendLeftCornerOp.setInput('scaleAmt', .5)

        self.blendLeftCornerOp.setInput('parentSpace', self.ctrlCmpGrp)
        self.blendLeftCornerOp.setInput('A', self.lUpCurveCorner)
        self.blendLeftCornerOp.setInput('B', self.lLoCurveCorner)

        self.blendLeftCornerOp.setOutput('result', self.lMouthCornerLoc)

        self.lMouthCornerDef = Joint('L_mouthCorner',  parent=self.mouthDef)
        self.lMouthCornerDef.setComponent(self)
        self.lMouthCornerDef.constrainTo(self.lMouthCornerLoc)



        # Add lowCurve Guide Canvas Op
        self.rMouthCornerLoc = Locator('R_mouthCorner', parent=self.ctrlCmpGrp)
        self.rMouthCornerLoc.setShapeVisibility(False)
        self.blendRightCornerOp = CanvasOperator('blendRightCornerOp', 'OSS.Solvers.blendMat44Solver')
        self.addOperator(self.blendRightCornerOp)

        # self.blendRightCornerOp.setInput('drawDebug', self.drawDebugInputAttr)
        # self.blendRightCornerOp.setInput('rigScale', 1.0)
        self.blendRightCornerOp.setInput('rotationAmt', .5)
        self.blendRightCornerOp.setInput('translationAmt', .5)
        self.blendRightCornerOp.setInput('scaleAmt', .5)

        self.blendRightCornerOp.setInput('parentSpace', self.ctrlCmpGrp)
        self.blendRightCornerOp.setInput('A', self.rUpCurveCorner)
        self.blendRightCornerOp.setInput('B', self.rLoCurveCorner)

        self.blendRightCornerOp.setOutput('result', self.rMouthCornerLoc)

        self.rMouthCornerDef = Joint('R_mouthCorner',  parent=self.mouthDef)
        self.rMouthCornerDef.setComponent(self)
        self.rMouthCornerDef.constrainTo(self.rMouthCornerLoc)





        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.topMouthCtrlSpace.xfo = data['midCurveXfo']
        self.mouthCtrlSpace.xfo = data['mouthXfo']
        self.mouthCtrl.xfo = data['mouthXfo']
        self.mouthCtrl.rotatePoints(-90.0, 0.0, 90.0)
        self.mouthCtrl.scalePoints(Vec3(Vec3( .5, .5,  .5)))

        self.lMouthCtrlSpace.xfo = data['L_MouthXfo']
        self.lMouthCtrl.xfo = data['L_MouthXfo']
        self.lMouthCtrl.scalePoints(Vec3(Vec3( .5, .5,  .5)))
        self.lMouthCtrl.translatePoints(Vec3(Vec3(.0, .5,  0)))
        self.lMouthCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.lMouthCtrl.lockRotation(x=True, y=True, z=True)
        self.lMouthCtrl.lockScale(x=True, y=True, z=True)

        self.rMouthCtrlSpace.xfo = data['R_MouthXfo']
        self.rMouthCtrlSpace.xfo.sc = Vec3(1.0, 1.0, -1.0)
        self.rMouthCtrl.xfo = data['R_MouthXfo']
        self.rMouthCtrl.scalePoints(Vec3(Vec3(.5, .5,  .5)))
        self.rMouthCtrl.translatePoints(Vec3(Vec3(.0, .5,  0)))
        self.rMouthCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.rMouthCtrl.lockRotation(x=True, y=True, z=True)
        self.rMouthCtrl.lockScale(x=True, y=True, z=True)

        self.mouthEndOutputTgt.xfo = data['mouthXfo']
        self.mouthOutputTgt.xfo = data['mouthXfo']

        self.evalOperators()

        # Eval Constraints
        self.mouthConstraint.evaluate()
        self.mouthEndConstraint.evaluate()

        # loCurve
        self.loCurveCtrlSpace.xfo = data['midCurveXfo']
        self.loCurveCtrl.xfo = data['midCurveXfo']
        self.loCurveCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.loCurveCtrl.scalePoints(Vec3(Vec3(.5, -.125,.5)))
        self.loCurveCtrl.setColor("brownMuted")
        self.loCurveCtrl.lockScale(x=False, y=True, z=True)

        self.L_loCurveHandleCtrl.xfo = data['L_midCurveHandleXfo']
        self.R_loCurveHandleCtrl.xfo = data['R_midCurveHandleXfo']

        self.midMouthCtrlSpace.xfo = data['midCurveXfo']
        self.midMouthCtrl.xfo = data['midCurveXfo']

        # upCurve
        self.upCurveCtrlSpace.xfo = data['midCurveXfo']
        self.upCurveCtrl.xfo = data['midCurveXfo']
        self.upCurveCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.upCurveCtrl.scalePoints(Vec3(Vec3(.5, .125,.5)))
        self.upCurveCtrl.setColor("yellowMuted")
        self.upCurveCtrl.lockScale(x=False, y=True, z=True)

        self.L_upCurveHandleCtrl.xfo = data['L_midCurveHandleXfo']
        self.R_upCurveHandleCtrl.xfo = data['R_midCurveHandleXfo']

        self.loCurveCtrl.translatePoints(Vec3(Vec3(0, -.75,  .5)))
        self.loCurveCtrl.alignOnZAxis()
        self.upCurveCtrl.translatePoints(Vec3(Vec3(0, 0.75,  .5)))
        self.upCurveCtrl.alignOnZAxis()

        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.scalePoints(globalScale)


        self.mouthCtrl.translatePoints(Vec3(Vec3(data['mouthLen'], -3 , 0.0)))

        # update the positions of the curve controls to match their uberparents
        # after we eval the operators and get the uber positions
        self.upCurveRigOp.evaluate()
        for ctrl in self.upCurveCtrls:
            if ctrl is not self.lMouthCtrl and ctrl is not self.rMouthCtrl:
                uber = ctrl.getParent().getParent()
                ctrl.getParent().xfo = Xfo(uber.xfo)
                ctrl.xfo = Xfo(uber.xfo)
        self.loCurveRigOp.evaluate()
        for ctrl in self.loCurveCtrls:
            if ctrl is not self.lMouthCtrl and ctrl is not self.rMouthCtrl:
                uber = ctrl.getParent().getParent()
                ctrl.getParent().xfo = Xfo(uber.xfo)
                ctrl.xfo = Xfo(uber.xfo)


        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['midCurveXfo']
        self.curveOutputTgt.xfo = data['midCurveXfo']



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMouthGuide)
ks.registerComponent(OSSMouthRig)
