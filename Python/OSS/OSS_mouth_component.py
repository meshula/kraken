
import math, re

from kraken.core.maths import RotationOrder
from kraken.core.maths import Math_degToRad 
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

from kraken.core.maths import *

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
        self.lipOutputTgt      = self.createOutput('lip', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.mouthOutputTgt    = self.createOutput('mouth', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.lMouthCornerOutputTgt = self.createOutput('L_MouthCorner', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.rMouthCornerOutputTgt = self.createOutput('R_MouthCorner', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.upLipMidOutputTgt = self.createOutput('upLipMid', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.loLipMidOutputTgt = self.createOutput('loLipMid', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.jawEndOutputTgt = self.createOutput('jawEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

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
        # midLip
        self.lipsCtrl = Control('lips', parent=self.ctrlCmpGrp, shape='cube')
        self.lipsCtrl.setColor("green")

        self.lipCtrlNames = StringAttribute('lipCtrlNames', value="1 Sneer", parent=self.guideSettingsAttrGrp)
        self.lipDefParams = StringAttribute('lipDefParams', value="1 0.94 0.86 0.79 0.72 0.653 0.583 0.5 0.417 0.347 0.28 0.21 0.14 0.06 0", parent=self.guideSettingsAttrGrp)
        # self.numSpansAttr = IntegerAttribute('numSpans', value=13, minValue=0, maxValue=20,  parent=self.guideSettingsAttrGrp)

        self.alignXAttr = IntegerAttribute('alignX', value=2, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)
        self.alignYAttr = IntegerAttribute('alignY', value=-1, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)
        self.alignZAttr = IntegerAttribute('alignZ', value=3, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)


        self.mouthCtrl = Control('mouth', parent=self.ctrlCmpGrp)

        # midLip
        self.midLipCtrl = Control('midLip', parent=self.lipsCtrl)
        self.midLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_midLipHandleCtrl = Control('midLipHandle', parent=self.lipsCtrl, metaData={"altLocation":"L"})
        self.R_midLipHandleCtrl = Control('midLipHandle', parent=self.lipsCtrl, metaData={"altLocation":"R"})

        self.L_MouthCtrl = Control('Mouth', parent=self.lipsCtrl, metaData={"altLocation":"L"})
        self.R_MouthCtrl = Control('Mouth', parent=self.lipsCtrl, metaData={"altLocation":"R"})




        # Mark Handles
        for ctrl in [self.L_midLipHandleCtrl,
                     self.R_midLipHandleCtrl]:
            ctrl.setColor("red")


        self.Level1Ctrls = []
        self.lipCtrls = []
        self.symMapping = {}

        # Add Mouth Symmetry Canvas Op
        self.lSideObjs = []
        self.rSideObjs = []
        self.lSideParentObjs = []

        # Add Att Inputs
        self.refInputs = []
        self.midLipControls = []
        self.midLipOutputs = []

        self.jawCtrl = Control('jaw', parent=self.ctrlCmpGrp, shape="sphere")
        self.jawEndCtrl = Control('jawEnd', parent=self.lipsCtrl, shape="halfCircle", scale=0.5)
        self.jawEndCtrl.rotatePoints(-90.0, 0.0, 0.0)
        self.jawCtrl.setColor("green")
        self.jawEndCtrl.setColor("green")

        # setting inital Guide Data
        # note that we're not setting the R Side Objects since all R_ objects are currently reflected from their L_ symmetric Partner
        data = {
                "name": name,
                "location": "M",
                "mouthXfo": Xfo(Vec3(0, 15, 0)),
                "jawXfo": Xfo(Vec3(0, 15, 0)),
                "lipsXfo": Xfo(Vec3(0, 15, 4)),
                "midLipXfo": Xfo(Vec3(0, 15, 4)),
                "L_midLipHandleXfo": Xfo(Vec3(1.75, 15, 4)),
                "R_midLipHandleXfo": Xfo(Vec3(-1.75, 15, 4)),
                "loLipXfo": Xfo(Vec3(0, 13, 4)),
                "L_loLipHandleXfo": Xfo(Vec3(1.75, 13, 4)),
                "R_loLipHandleXfo": Xfo(Vec3(-1.75, 13, 4)),
                "upLipXfo": Xfo(Vec3(0, 17, 4)),
                "L_upLipHandleXfo": Xfo(Vec3(1.75, 17, 4)),
                "R_upLipHandleXfo": Xfo(Vec3(-1.75, 17, 4)),
                "L_MouthXfo": Xfo(Vec3(3, 15, 3)),
                "R_MouthXfo": Xfo(Vec3(-3, 15, 3)),
                "L_MouthOutXfo": Xfo(Vec3(4, 15, 2)),
                "R_MouthOutXfo": Xfo(Vec3(-4, 15, 2)),
                "jawEndXfo": Xfo(Vec3(0, 12, 4)),
                "alignX": 2,
                "alignY": -1,
                "alignZ": 3
               }


        self.paramOut = []
        # Add midLip Debug Canvas Op
        self.midLipGuideOp = CanvasOperator('midLipGuideOp', 'OSS.Solvers.NURBSCurveGuideSolver')
        self.addOperator(self.midLipGuideOp)

        self.midLipGuideOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.midLipGuideOp.setInput('rigScale', 1.0)
        self.midLipGuideOp.setInput('degree', 4)

        self.midLipGuideOp.setInput('controls', self.midLipControls)
        self.midLipGuideOp.setInput('refMats', self.midLipControls)

        self.midLipGuideOp.setOutput('result', self.paramOut )

        # update Inputs
        self.midLipControls.append(self.L_MouthCtrl)
        self.midLipControls.append(self.L_midLipHandleCtrl)
        self.midLipControls.append(self.midLipCtrl)
        self.midLipControls.append(self.R_midLipHandleCtrl)
        self.midLipControls.append(self.R_MouthCtrl)


        # Add upLip Debug Canvas Op
        self.upLipGuideOp = CanvasOperator('upLipGuideOp', 'OSS.Solvers.NURBSCurveGuideSolver')
        self.addOperator(self.upLipGuideOp)

        self.upLipControls = []

        self.upLipGuideOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.upLipGuideOp.setInput('rigScale', 1.0)
        self.upLipGuideOp.setInput('degree', 3)

        self.upLipGuideOp.setInput('controls', self.upLipControls)
        self.upLipGuideOp.setInput('refMats', self.upLipControls)

        self.upLipGuideOp.setOutput('result', self.paramOut)



        # Add lowLip Debug Canvas Op
        self.loLipGuideOp = CanvasOperator('loLipGuideOp', 'OSS.Solvers.NURBSCurveGuideSolver')
        self.addOperator(self.loLipGuideOp)

        self.loLipControls = []

        self.loLipGuideOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.loLipGuideOp.setInput('rigScale', 1.0)
        self.loLipGuideOp.setInput('degree', 3)

        self.loLipGuideOp.setInput('controls', self.loLipControls)
        self.loLipGuideOp.setInput('refMats', self.loLipControls)

        self.loLipGuideOp.setOutput('result', self.paramOut )


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

        self.reflectionOp.setInput('alignX',   -1)
        self.reflectionOp.setInput('inputs',   self.lSideObjs)
        self.reflectionOp.setInput('inputParents', self.lSideParentObjs)
        self.reflectionOp.setOutput('results', self.rSideObjs)

        self.loadData(data)

        Profiler.getInstance().pop()

    def addToSymDict(self, ctrl):
        if not self.symMapping:
            self.symMapping = {}

        name = ctrl.getName()
        side = ctrl.getMetaDataItem("altLocation")

        # lock non sided Controls x translation
        if not side:
            ctrl.lockTranslation(x=True, y=False, z=False)
            return  self.symMapping


        # lock non sided Controls x translation
        if not name in self.symMapping:
             self.symMapping[name] = {}

        if side == "L":
             self.symMapping[name]["lSide"] = ctrl
             self.symMapping[name]["lSideParent"] = ctrl.getParent()
        else:
             self.symMapping[name]["rSide"] = ctrl

        return self.symMapping


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """

        data = super(OSSMouthGuide, self).saveData()

        # this should live in the GuideClass - also should considere Inherited Types
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
        mouthPosition = self.jawCtrl.xfo.tr
        jawEndPosition = self.jawEndCtrl.xfo.tr
        mouthLen = mouthPosition.subtract(jawEndPosition).length()

        # Calculate Mouth Xfo

        # atVector
        # mouthUpV = Vec3(0.0, 1.0, 0.0)

        # rootToEnd = jawEndPosition.subtract(mouthPosition).unit()
        # rootToUpV = mouthUpV.subtract(mouthPosition).unit()
        # bone1ZAxis = rootToUpV.cross(rootToEnd).unit()
        # bone1Normal = bone1ZAxis.cross(rootToEnd).unit()

        jawXfo = self.jawEndCtrl.xfo
        # jawXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, mouthPosition)



        data = super(OSSMouthGuide, self).getRigBuildData()

        # should include getCurveData
        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")
        data['jawXfo'] = self.jawCtrl.xfo
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

        Profiler.getInstance().pop()




    def createGuideControls(self, name, ctrlType, controlsList, names):
        # Delete current controls
        '''
        self.controlXforms = []
        # Store current values if guide controls already exist
        # for i, name in enumerate(["lipDeformers", "lipControls"]):
        current = 0
        for i, ctrl in enumerate(controlsList):
            self.controlXforms.append([ctrl.xfo])
            if ctrl.getParent() is self.jawCtrl:
                self.controlXforms.append([ctrl.xfo])
                current = len(self.controlXforms) -1
            else:
                self.controlXforms[current].append(ctrl.xfo)
        '''

        lSideControls = []
        rSideControls = []

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrlParent = ctrl.getParent()
            if ctrlParent:
                ctrlParent.removeChild(ctrl)
        del controlsList[:]


        if ctrlType == "deformers":
            # length of controls minus ends
            numNames = len(names)-2
            parent = Transform(name + 'Deformers', parent=self.ctrlCmpGrp)
            #Build Deformer Names
            half = int(math.floor(numNames/2))
            for i in range(half):
                lSideControls.append(str(half-i))
                rSideControls.append(str(i+1))

            lSideControls.reverse()
            rSideControls.reverse()


            def creatDefControl(defName, side=None):
                newCtrl = Locator(defName + "_" + name, parent= parent)
                newCtrl.setShapeVisibility(False)
                newCtrl.xfo = parent.xfo
                controlsList.append(newCtrl)

                newDef = Joint(defName + "_" + name, parent= self.mouthDef)
                newDef.constrainTo(newCtrl)

                if side:
                    newCtrl.setMetaDataItem("altLocation", side)
                    newDef.setMetaDataItem("altLocation", side)


            for defCtrlName in rSideControls:
                creatDefControl(defCtrlName, side="R")

            if not numNames % 2 == 0:
                creatDefControl("Mid")

            for defCtrlName in lSideControls:
                creatDefControl(defCtrlName, side="L")


        if ctrlType == "controls":

            parent = Transform(name + 'Controls', parent=self.ctrlCmpGrp)
            # Lets build all new handles
            controlNameList = self.convertToStringList(names)
            if not controlNameList:  # Nothing to build
                return True


            # etting up names
            lSideControls = [x for x in reversed(controlNameList)]
            rSideControls = [x for x in controlNameList]



            def createControl(ctrlName, side=None):
                newCtrl = Control(name + ctrlName, parent=parent, shape="halfCircle")
                newCtrl.rotatePoints(90,0,0)
                newCtrl.setColor("sienna")
                newCtrl.xfo = parent.xfo
                controlsList.append(newCtrl)
                newCtrl.lockRotation(x=False, y=True, z=True)
                newCtrl.lockScale(x=True, y=True, z=True)
                if side:
                    newCtrl.setMetaDataItem("altLocation", side)
                try:
                    newCtrl.scalePoints(Vec3(.125,.125,.125))
                except:
                    pass

            for ctrlName in rSideControls:
                createControl(ctrlName, side="R")

            createControl("Mid")

            for ctrlName in lSideControls:
                createControl(ctrlName, side="L")


        # for ctrl in controlsList:
        #     self.addToSymDict(ctrl)

        return controlsList


    def insertCtrlSpace(self, ctrl, name=None):
        """Adds a CtrlSpace object above this object - inserted here to work on Transforms

        Args:
            name (string): optional name for this CtrlSpace, default is same as
                this object

        Returns:
            object: New CtrlSpace object

        """

        if name is None:
            name = ctrl.getName()

        newCtrlSpace = CtrlSpace(name, parent=ctrl.getParent())
        if ctrl.getParent() is not None:
            ctrl.getParent().removeChild(ctrl)

        if ctrl.getMetaDataItem("altLocation"):
            newCtrlSpace.setMetaDataItem("altLocation", ctrl.getMetaDataItem("altLocation"))

        ctrl.setParent(newCtrlSpace)
        newCtrlSpace.addChild(ctrl)

        newCtrlSpace.xfo = Xfo(ctrl.xfo)

        # To ensure that names of control spaces don't clash with controls and
        # if they do, set's the control space's name back to what it was intended
        if ctrl.getName() == name:
            newCtrlSpace.setName(name)

        return newCtrlSpace

    def insertParentSpaces(self, controls = []):
        numCtrls = len(controls)
        controlParents = []
        if numCtrls:
            # build control hierarchy
            half = int(math.floor(numCtrls/2))

            evenNumCtrls = (numCtrls % 2 == 0)

            for i in range(numCtrls):
                ctrl = controls[i]
                ctrl.setColor("goldenrod")
                ctrlGrandParent = self.insertCtrlSpace(ctrl, name= ctrl.getName() + 'Driven')
                ctrlParent     = self.insertCtrlSpace(ctrl)
                # if i < (half-1):
                #     ctrlParent.constrainTo(self.upLipCtrls[i+1], maintainOffset=True)
                # if (half+1) < i:
                #     ctrlParent.constrainTo(self.upLipCtrls[i-1], maintainOffset=True)
                controlParents.append(ctrlGrandParent)
        return controlParents


    def createCurveRig(self, name, Level0Ctrls = [], rigParams = [], lLevel0Params = [], data=None):
        # Todo should be passed
        alignX = data["alignX"]
        alignY = data["alignY"]
        alignZ = data["alignZ"]
        atXfo = self.jawCtrl
        parent = self.jawCtrlSpace
        # Corner Transforms
        # Corner Transforms
        lRigCorner = Transform('L_' + name + 'RigCorner', parent=self.ctrlCmpGrp)
        rRigCorner = Transform('R_' + name + 'RigCorner', parent=self.ctrlCmpGrp)
        lDefCorner = Transform('L_' + name + 'DefCorner', parent=self.ctrlCmpGrp)
        rDefCorner = Transform('R_' + name + 'DefCorner', parent=self.ctrlCmpGrp)

        # Add Controls and parent spaces
        Level1Ctrls   = []
        Level1Ctrls   = [lRigCorner] + self.createGuideControls(name, "controls", Level1Ctrls, data["lipCtrlNames"]) + [rRigCorner]
        rigOutputs = self.insertParentSpaces(Level1Ctrls)

        Level1Outputs = []
        Level1Outputs  = [lDefCorner] + self.createGuideControls(name, "deformers", Level1Outputs, lLevel0Params) + [rDefCorner]

        # - - - - - - - - - - - - - -
        # Rig OP
        # - - - - - - - - - - - - - -
        # create Rest Xfos and Aligns
        Level0CtrlsRest = []
        Level0CtrlsAligns = []
        for c in Level0Ctrls:
           Level0CtrlsAligns.append(Vec3(1,2,3))

        #need to eliminate this fix-up

        Level0CtrlsAligns[-1] = Vec3(-1,2,3)

        altTangent = Vec3(-1.0,0.0,0.0)

        curveLevel0Op = KLOperator(name+ 'Level0Op', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(curveLevel0Op)

        if name == 'upLip':
            curveLevel0Op.setInput('alignX', alignX )
            curveLevel0Op.setInput('alignY', alignY )
            curveLevel0Op.setInput('alignZ', alignZ )
        else:
            curveLevel0Op.setInput('alignX', alignX )
            curveLevel0Op.setInput('alignY', alignY )
            curveLevel0Op.setInput('alignZ', alignZ )

        curveLevel0Op.setInput('altTangent', altTangent)
        curveLevel0Op.setInput('drawDebug', self.drawDebugInputAttr)
        curveLevel0Op.setInput('rigScale', 1.0)
        curveLevel0Op.setInput('degree', 4)
        curveLevel0Op.setInput('keepArcLength', 0.0)
        curveLevel0Op.setInput('compressionAmt', 0.0)
        curveLevel0Op.setInput('followCurveTangent', 1)
        curveLevel0Op.setInput('parent', parent)
        curveLevel0Op.setInput('useLocalNormal', 1.0)
        curveLevel0Op.setInput('followCurveNormal', 1.0)

        curveLevel0Op.setInput('atVec', atXfo)
        curveLevel0Op.setInput('controlAligns', Level0CtrlsAligns)
        curveLevel0Op.setInput('controls', Level0Ctrls)
        curveLevel0Op.setInput('controlsRest', Level0Ctrls)
        curveLevel0Op.setInput('params', rigParams)

        curveLevel0Op.setOutput('outputs', rigOutputs)

        # - - - - - - - - - - - - - -
        # Def OP
        # - - - - - - - - - - - - - -
        # create Rest Xfos and Aligns
        Level1CtrlsRest = []
        Level1CtrlsAligns = []

        Level1CtrlsRot = []
        for c in Level1Ctrls:
            Level1CtrlsRot.append(Transform(c.getName()+ 'Rot', parent=c))


        for c in Level1CtrlsRot:
            Level1CtrlsAligns.append(Vec3(1,2,3))
            Level1CtrlsRest.append(c.xfo)

        Level1CtrlsAligns[-1] = Vec3(-1,2,-3)

        # Add lowLip Debug Canvas Op
        curveLevel1Op = KLOperator(name+ 'Level1Op', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(curveLevel1Op)

        curveLevel1Op.setInput('drawDebug', self.drawDebugInputAttr)
        curveLevel1Op.setInput('rigScale', 1.0)
        curveLevel1Op.setInput('degree', 3)
        if name == 'upLip':
            curveLevel1Op.setInput('alignX', alignX )
            curveLevel1Op.setInput('alignY', alignY )
            curveLevel1Op.setInput('alignZ', alignZ )
        else:
            curveLevel1Op.setInput('alignX', alignX )
            curveLevel1Op.setInput('alignY', alignY )
            curveLevel1Op.setInput('alignZ', alignZ )

        curveLevel1Op.setInput('altTangent', altTangent)

        curveLevel1Op.setInput('keepArcLength', 0.0)
        curveLevel1Op.setInput('compressionAmt', 0.0)
        curveLevel1Op.setInput('followCurveTangent', 0.25)
        curveLevel1Op.setInput('parent', parent)
        curveLevel1Op.setInput('useLocalNormal', 1.0)
        curveLevel1Op.setInput('followCurveNormal', 1.0)

        curveLevel1Op.setInput('atVec', atXfo)
        curveLevel1Op.setInput('controlAligns', Level1CtrlsAligns)
        curveLevel1Op.setInput('controls', Level1CtrlsRot)
        curveLevel1Op.setInput('controlsRest', Level1Ctrls)
        curveLevel1Op.setInput('params', lLevel0Params)

        curveLevel1Op.setOutput('outputs', Level1Outputs)

        return curveLevel0Op, Level0Ctrls, curveLevel1Op, Level1Ctrls, Level1Outputs



    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """
        super(OSSMouthRig, self).loadData( data )

        # ==========
        # Deformers
        # ==========


        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.parentSpaceInputTgt.childJoints = []

        # Mouth
        self.mouthDef = Joint('mouth', parent=self.deformersParent)

        self.jawDef = Joint('jaw', parent=self.mouthDef)
        self.parentSpaceInputTgt.childJoints.append(self.mouthDef)

        self.lMouthDef = Joint('mouth', parent=self.mouthDef, metaData={"altLocation":"L"})
        self.rMouthDef = Joint('mouth', parent=self.mouthDef, metaData={"altLocation":"R"})

        # =========
        # Controls
        # =========
        # Jaw
        self.lipsRefSpace = CtrlSpace('lipsRef', parent=self.ctrlCmpGrp)

        self.jawCtrlSpace = CtrlSpace('jaw', parent=self.ctrlCmpGrp)
        self.jawCtrl = Control('jaw', parent=self.jawCtrlSpace, shape="halfCircle", scale=0.5)

        # midMouth
        self.midMouthCtrlSpace = CtrlSpace('midMouth', parent=self.ctrlCmpGrp)
        self.midMouthRefSpace = CtrlSpace('midMouthRef', parent=self.ctrlCmpGrp)

        # Mouth
        self.mouthCtrlSpace = CtrlSpace('mouth', parent=self.ctrlCmpGrp)
        self.mouthCtrl = Control('mouth', parent=self.mouthCtrlSpace, shape="halfCircle", scale=0.5)

        # loLip
        self.loLipCtrlSpace = CtrlSpace('loLip', parent=self.ctrlCmpGrp)
        self.loLipRefSpace = CtrlSpace('loLipRef', parent=self.jawCtrl)
        self.loLipCtrl = Control('loLip', parent=self.loLipCtrlSpace, shape="halfCircle")

        self.loLipCtrlAttrGrp = AttributeGroup("loLipSettings", parent=self.loLipCtrl)
        self.loLipCtrlRotation = ScalarAttribute('Curl', value=0.0,  parent=self.loLipCtrlAttrGrp)

        self.L_loLipHandleCtrl = CtrlSpace('loLipHandle', parent=self.loLipCtrl, metaData={"altLocation":"L"})
        self.R_loLipHandleCtrl = CtrlSpace('loLipHandle', parent=self.loLipCtrl, metaData={"altLocation":"R"})

        # upLip
        self.upLipCtrlSpace = CtrlSpace('upLip', parent=self.ctrlCmpGrp)
        self.upLipCtrl = Control('upLip', parent=self.upLipCtrlSpace, shape="halfCircle")

        self.upLipCtrlAttrGrp = AttributeGroup("upLipSettings", parent=self.upLipCtrl)
        self.upLipCtrlRotation = ScalarAttribute('Curl', value=0.0,  parent=self.upLipCtrlAttrGrp)

        self.L_upLipHandleCtrl = CtrlSpace('upLipHandle', parent=self.upLipCtrl, metaData={"altLocation":"L"})
        self.R_upLipHandleCtrl = CtrlSpace('upLipHandle', parent=self.upLipCtrl, metaData={"altLocation":"R"})

        self.L_MouthRefSpace = CtrlSpace('MouthRef', parent=self.midMouthCtrlSpace, metaData={"altLocation":"L"})
        self.L_MouthCtrlSpace = CtrlSpace('Mouth', parent=self.midMouthCtrlSpace, metaData={"altLocation":"L"})
        self.L_MouthCtrl = Control('Mouth', parent=self.L_MouthCtrlSpace, shape="circle", scale=0.5, metaData={"altLocation":"L"})
        self.L_MouthCornerCtrlSpace = CtrlSpace('Mouth', parent=self.L_MouthCtrl, metaData={"altLocation":"L"})
        self.L_MouthCornerCtrl = Control('MouthCorner', parent=self.L_MouthCornerCtrlSpace, shape="circle", scale=0.125, metaData={"altLocation":"L"})
        self.L_MouthCtrl.setColor("mediumseagreen")

        self.R_MouthRefSpace = CtrlSpace('MouthRef', parent=self.midMouthCtrlSpace, metaData={"altLocation":"R"})
        self.R_MouthCtrlSpace = CtrlSpace('Mouth', parent=self.midMouthCtrlSpace, metaData={"altLocation":"R"})
        self.R_MouthCtrl = Control('Mouth', parent=self.R_MouthCtrlSpace, shape="circle", scale=0.5, metaData={"altLocation":"R"})
        self.R_MouthCornerCtrlSpace = CtrlSpace('Mouth', parent=self.R_MouthCtrl, metaData={"altLocation":"R"})
        self.R_MouthCornerCtrl = Control('MouthCorner', parent=self.R_MouthCornerCtrlSpace, shape="circle", scale=0.125, metaData={"altLocation":"R"})
        self.R_MouthCtrl.setColor("mediumvioletred")


        # ==============
        # Constrain I/O
        # ==============
        # Input
        self.mouthInputConstraint = self.mouthCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.mouthInputConstraint = self.lipsRefSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.mouthInputConstraint = self.jawCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Output
        #self.lipOutputTgtConstraint = self.lipOutputTgt.constrainTo(self.midLipCtrl)
        self.lMouthCornerOutputTgtConstraint = self.lMouthCornerOutputTgt.constrainTo(self.L_MouthCornerCtrl, maintainOffset=False)
        self.rMouthCornerOutputTgtConstraint = self.rMouthCornerOutputTgt.constrainTo(self.R_MouthCornerCtrl, maintainOffset=False)

        self.mouthOutputTgtConstraint = self.mouthOutputTgt.constrainTo(self.jawCtrl, maintainOffset=False)
        self.jawEndOutputTgtConstraint = self.jawEndOutputTgt.constrainTo(self.jawCtrl, maintainOffset=False)
        self.mouthOutputTgt.parentJoint =  self.mouthDef



        # global Params
        self.offset    = Vec3(0,0.05,0.45)
        self.rigParams = [0, 0.05,0.25,0.5,0.75,0.95, 1]
        #these should be generated during the guide rig creation (hardcoded for now)

        self.lLevel0Params = self.convertToScalarList(data["lipDefParams"])
        # upLip
        self.upLipControls   = [self.L_MouthCtrl, self.L_upLipHandleCtrl, self.upLipCtrl, self.R_upLipHandleCtrl, self.R_MouthCtrl]

        self.upLipLevel0Op, self.upLipDefLevel0Ctrls, self.upLipLevel1Op, self.upLipLevel1Ctrls, self.upLipLevel1Outputs  = self.createCurveRig(
            name = 'upLip',
            Level0Ctrls = self.upLipControls,
            rigParams = self.rigParams,
            lLevel0Params = self.lLevel0Params,
            data= data
            )


        # loLip
        self.loLipControls   = [self.L_MouthCtrl, self.L_loLipHandleCtrl, self.loLipCtrl, self.R_loLipHandleCtrl, self.R_MouthCtrl]

        self.loLipLevel0Op, self.loLipDefLevel0Ctrls, self.loLipLevel1Op, self.loLipLevel1Ctrls, self.loLipLevel1Outputs  = self.createCurveRig(
            name = 'loLip',
            Level0Ctrls = self.loLipControls,
            rigParams = self.rigParams,
            lLevel0Params = self.lLevel0Params,
            data= data
            )


        #Mouth Offset
        self.offsetOp([self.loLipRefSpace, self.lipsRefSpace,  self.midMouthRefSpace],
                      [self.loLipCtrlSpace, self.upLipCtrlSpace, self.midMouthCtrlSpace],
                       self.mouthCtrl.getParent(), self.mouthCtrl, name="offsetOp")


        for Level1Op, ctrls in [(self.loLipLevel1Op, self.loLipLevel1Ctrls), (self.upLipLevel1Op, self.upLipLevel1Ctrls)]:
            ctrls2 = [ctrl.getChildren()[0] for ctrl in ctrls]
            ctrls2[0]  = self.L_MouthCornerCtrl
            ctrls2[-1] = self.R_MouthCornerCtrl
            Level1Op.setInput('controls', ctrls2)
            Level1Op.setInput('controlsRest', ctrls2)


        #blending mouth corner defs
        self.blendMidMouthLevel0Op = self.blend_two_xfos(
            self.midMouthRefSpace,
            self.jawCtrl, self.jawCtrlSpace,
            blend=0.5,
            name="blendMidMouthLevel0Op")



        # ===============
        # Add Splice Ops
        # ===============
        # Add Deformer Splice Op
        self.jawCtrlConstraint = self.jawDef.constrainTo(self.jawCtrl, maintainOffset=False)

        # Left corner
        self.L_MouthCornerLoc = Locator('mouthCorner', parent=self.ctrlCmpGrp, metaData={"altLocation":"L"})
        self.L_MouthCornerLoc.setShapeVisibility(False)

        self.blendLeftCornerOp = KLOperator('blendLeftCornerOp', 'OSS_WeightedAverageMat44KLSolver', 'OSS_Kraken')
        self.addOperator(self.blendLeftCornerOp)

        self.LMouthAlignSpaces = [self.loLipLevel1Outputs[-2], self.upLipLevel1Outputs[-2]]
        self.LMouthAlignWeights = [0.5,0.5]

        # Add Att Inputs
        self.blendLeftCornerOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.blendLeftCornerOp.setInput('rigScale', self.rigScaleInputAttr)
        self.blendLeftCornerOp.setInput('mats', self.LMouthAlignSpaces)
        self.blendLeftCornerOp.setInput('matWeights', self.LMouthAlignWeights)
        self.blendLeftCornerOp.setInput('translationAmt',  0)
        self.blendLeftCornerOp.setInput('scaleAmt',  0)
        self.blendLeftCornerOp.setInput('rotationAmt',  1)
        self.blendLeftCornerOp.setOutput('result', self.L_MouthCornerLoc)


        # Right corner
        self.R_MouthCornerLoc = Locator('mouthCorner', parent=self.ctrlCmpGrp, metaData={"altLocation":"R"})
        self.R_MouthCornerLoc.setShapeVisibility(False)

        self.blendRightCornerOp = KLOperator('blendRightCornerOp', 'OSS_WeightedAverageMat44KLSolver', 'OSS_Kraken')
        self.addOperator(self.blendRightCornerOp)

        self.RMouthAlignSpaces = [self.loLipLevel1Outputs[1], self.upLipLevel1Outputs[1]]
        self.RMouthAlignWeights = [0.5,0.5]

        # Add Att Inputs
        self.blendRightCornerOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.blendRightCornerOp.setInput('rigScale', self.rigScaleInputAttr)
        self.blendRightCornerOp.setInput('mats', self.RMouthAlignSpaces)
        self.blendRightCornerOp.setInput('matWeights', self.RMouthAlignWeights)
        self.blendRightCornerOp.setInput('translationAmt',  0)
        self.blendRightCornerOp.setInput('scaleAmt',  0)
        self.blendRightCornerOp.setInput('rotationAmt',  1)
        self.blendRightCornerOp.setOutput('result', self.R_MouthCornerLoc)

        # Add Att Inputs
        self.L_MouthCornerDef = Joint('mouthCorner',  parent=self.mouthDef, metaData={"altLocation":"L"})
        self.L_MouthCornerDef.constrainTo(self.L_MouthCornerLoc)

        self.R_MouthCornerDef = Joint('mouthCorner',  parent=self.mouthDef, metaData={"altLocation":"R"})
        self.R_MouthCornerDef.constrainTo(self.R_MouthCornerLoc)

        self.lMouthDefPosConstraint = self.lMouthDef.constrainTo(self.L_MouthCornerLoc, constraintType="Position")
        self.rMouthDefConstraint = self.rMouthDef.constrainTo(self.R_MouthCornerLoc, constraintType="Position")

        # global ControlScaling before moving them into position
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.scalePoints(globalScale)

        # move controls into position
        for ctrl in [self.L_loLipHandleCtrl, self.L_upLipHandleCtrl]:
            ctrl.xfo = data['L_midLipHandleXfo']

        for ctrl in [self.R_loLipHandleCtrl, self.R_upLipHandleCtrl]:
            ctrl.xfo = data['R_midLipHandleXfo']

        for ctrl in [self.midMouthCtrlSpace, self.lipsRefSpace, self.midMouthRefSpace, self.loLipRefSpace]:
            ctrl.xfo = data['midLipXfo']

        for ctrl in [self.jawCtrlSpace, self.jawCtrl, self.jawEndOutputTgt, self.mouthOutputTgt, self.mouthCtrlSpace, self.mouthCtrl, self.mouthDef]:
            ctrl.xfo = data['jawXfo']


        for ctrl in [self.mouthCtrlSpace, self.mouthCtrl]:
            ctrl.xfo = data['mouthXfo']


        for ctrl in [self.L_MouthCtrlSpace, self.L_MouthCtrl, self.L_MouthCornerCtrlSpace, self.L_MouthCornerCtrl, self.L_MouthRefSpace]:
            ctrl.xfo = data['L_MouthXfo']

        for ctrl in [self.R_MouthCtrlSpace, self.R_MouthCtrl, self.R_MouthCornerCtrlSpace, self.R_MouthCornerCtrl, self.R_MouthRefSpace]:
            ctrl.xfo = data['R_MouthXfo']

        for ctrl in [self.R_MouthCtrl, self.R_MouthCornerCtrl]:
            ctrl.translatePoints(Vec3(Vec3(-.5, -.5,  0)))
            ctrl.rotatePoints(90.0, 0.0, 0.0)
            ctrl.lockRotation(x=True, y=True, z=True)
            ctrl.lockScale(x=True, y=True, z=True)


        for ctrl in [self.L_MouthCtrl, self.L_MouthCornerCtrl]:
            ctrl.translatePoints(Vec3(Vec3(.5, .5,  0)))
            ctrl.rotatePoints(90.0, 0.0, 0.0)
            ctrl.lockRotation(x=True, y=True, z=True)
            ctrl.lockScale(x=True, y=True, z=True)

        self.R_MouthCtrlSpace.xfo = self.R_MouthCtrlSpace.xfo.multiply(Xfo(sc=Vec3(-1,1,1)))

        #align work
        # self.R_MouthCtrlSpace.xfo.sc = Vec3(1.0, 1.0, -1.0)

        # Eval Constraints
        self.mouthOutputTgtConstraint.evaluate()
        self.jawEndOutputTgtConstraint.evaluate()

        # loLip

        for ctrl in [self.loLipCtrl, self.upLipCtrl]:
            ctrl.getParent().xfo = data['midLipXfo']
            ctrl.xfo = data['midLipXfo']
            ctrl.rotatePoints(90.0, 0.0, 0.0)
            ctrl.scalePoints(Vec3(Vec3(.5, .125,.5)))
            ctrl.lockRotation(x=False, y=True, z=True)
            ctrl.lockScale(x=False, y=True, z=True)
            ctrl.alignOnZAxis()

        for ctrl in (self.loLipLevel1Ctrls + [self.loLipCtrl]):
            ctrl.setColor("burlywood")
            try:
                ctrl.scalePoints(Vec3(Vec3(1,-1,1)))
            except:
                pass


        self.loLipCtrl.translatePoints(Vec3(Vec3(0, -0.75,  .5)))
        self.upLipCtrl.translatePoints(Vec3(Vec3(0,  0.75,  .5)))




        self.jawCtrl.rotatePoints(-90.0, 0.0, 0.0)
        self.jawCtrl.xfo = data['jawXfo']
        self.jawCtrl.translatePoints((data['jawEndXfo'].tr - data['jawXfo'].tr))


        # update the positions of the lip controls to match their grandparents
        # after we eval the operators and get the grand positions
        self.upLipLevel0Op.setInput('followCurveTangent', .25)
        self.loLipLevel0Op.setInput('followCurveTangent', .25)
        self.upLipLevel0Op.evaluate()
        self.loLipLevel0Op.evaluate()



        uplipCtrlOffset = Vec3(0,0,.5)
        lolipCtrlOffset = Vec3(0,0,-.5)
        uplipOffset = Vec3(0,0.75,0)
        lolipOffset = Vec3(0,-0.75,0)
        
        #should do this up front - why does hierarchy not get evaluated?
        rot = Xfo() 
        rot.ori.setFromEulerAngles(Vec3(Math_degToRad(0.0), Math_degToRad(180.0), Math_degToRad(0.0)))

        lips = [self.upLipLevel1Ctrls, self.loLipLevel1Ctrls]
        for l in xrange(len(lips)):
            for ctrl in lips[l]:
                if ctrl not in [self.L_MouthCtrl, self.R_MouthCtrl, self.R_MouthCornerCtrl, self.L_MouthCornerCtrl]:
                    grandParentXfo = ctrl.getParent().getParent().xfo
                    downAxis = Vec3(-1,-1,-1)*grandParentXfo.ori.getYaxis()
                    ctrl.getParent().xfo = xfo.xfoFromDirAndUpV(Vec3(0,0,0), downAxis, grandParentXfo.ori.getZaxis())
                    ctrl.getParent().xfo.tr = grandParentXfo.tr
                    ctrl.xfo = ctrl.getParent().xfo
                    ctrl.getChildren()[0].xfo = ctrl.getParent().xfo
                    # need to find a proper way of detecting controls of type curve
                    try:
                        if l:
                            ctrl.getParent().xfo.tr -= uplipOffset
                            ctrl.xfo.tr -= Vec3(uplipOffset)
                            ctrl.translatePoints(uplipCtrlOffset)
                            ctrl.translatePoints(uplipOffset)
                        else:

                            ctrl.getParent().xfo.tr -= lolipOffset
                            ctrl.xfo.tr -= Vec3(lolipOffset)
                            ctrl.translatePoints(lolipCtrlOffset)
                            ctrl.translatePoints(lolipOffset)
                            ctrl.xfo.ori = ctrl.xfo.ori * rot.ori
                    except:
                        pass

        self.upLipControlsRest = []
        self.loLipControlsRest = []

        self.evalOperators()

        for i in range(len(self.loLipLevel1Ctrls)):
            self.loLipControlsRest.append(Xfo(self.loLipLevel1Ctrls[i].xfo))

        for i in range(len(self.upLipLevel1Ctrls)):
            self.upLipControlsRest.append(Xfo(self.upLipLevel1Ctrls[i].xfo))

        self.loLipLevel1Op.setInput('controlsRest', self.loLipControlsRest)
        self.upLipLevel1Op.setInput('controlsRest', self.upLipControlsRest)


        controlLen = len(self.upLipLevel1Outputs)
        half = int(math.floor(controlLen/2))
        self.upLipMidOutputTgtConstraint  = self.upLipMidOutputTgt.constrainTo(self.upLipLevel1Outputs[half], maintainOffset=False)
        self.lopLipMidOutputTgtConstraint = self.loLipMidOutputTgt.constrainTo(self.loLipLevel1Outputs[half], maintainOffset=False)

        self.evalOperators()
        #self.lipOutputTgtConstraint.evaluate()
        self.mouthOutputTgtConstraint.evaluate()
        self.jawEndOutputTgtConstraint.evaluate()




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMouthGuide)
ks.registerComponent(OSSMouthRig)
