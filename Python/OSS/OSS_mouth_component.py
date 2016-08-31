
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
        self.numSpansAttr = IntegerAttribute('numSpans', value=13, minValue=0, maxValue=20,  parent=self.guideSettingsAttrGrp)

        self.alignXAttr = IntegerAttribute('alignX', value=2, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)
        self.alignYAttr = IntegerAttribute('alignY', value=-1, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)
        self.alignZAttr = IntegerAttribute('alignZ', value=3, minValue=-3, maxValue=3,  parent=self.guideSettingsAttrGrp)

        # midLip
        self.midLipCtrl = Control('midLip', parent=self.lipsCtrl)
        self.midLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_midLipHandleCtrl = Control('L_midLipHandle', parent=self.lipsCtrl)
        self.R_midLipHandleCtrl = Control('R_midLipHandle', parent=self.lipsCtrl)

        self.L_MouthCtrl = Control('L_Mouth', parent=self.lipsCtrl)
        self.R_MouthCtrl = Control('R_Mouth', parent=self.lipsCtrl)

        # upLip
        self.upLipCtrl = Control('upLip', parent=self.lipsCtrl)
        self.upLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_upLipHandleCtrl = Control('L_upLipHandle', parent=self.upLipCtrl)
        self.R_upLipHandleCtrl = Control('R_upLipHandle', parent=self.upLipCtrl)

        self.L_MouthOutCtrl = Control('L_MouthOut', parent=self.lipsCtrl)
        self.R_MouthOutCtrl = Control('R_MouthOut', parent=self.lipsCtrl)

        # loLip
        self.loLipCtrl = Control('loLip', parent=self.lipsCtrl)
        self.loLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_loLipHandleCtrl = Control('L_loLipHandle', parent=self.loLipCtrl)
        self.R_loLipHandleCtrl = Control('R_loLipHandle', parent=self.loLipCtrl)


        # Mark Handles
        for ctrl in [self.L_midLipHandleCtrl,
                     self.R_midLipHandleCtrl,
                     self.L_upLipHandleCtrl,
                     self.R_upLipHandleCtrl,
                     self.L_loLipHandleCtrl,
                     self.R_loLipHandleCtrl]:
            ctrl.setColor("red")


        self.defCtrls = []
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

        # update Inputs
        self.upLipControls.append(self.L_MouthOutCtrl)
        self.upLipControls.append(self.L_upLipHandleCtrl)
        self.upLipControls.append(self.upLipCtrl)
        self.upLipControls.append(self.R_upLipHandleCtrl)
        self.upLipControls.append(self.R_MouthOutCtrl)


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

        # update Inputs
        self.loLipControls.append(self.L_MouthOutCtrl)
        self.loLipControls.append(self.L_loLipHandleCtrl)
        self.loLipControls.append(self.loLipCtrl)
        self.loLipControls.append(self.R_loLipHandleCtrl)
        self.loLipControls.append(self.R_MouthOutCtrl)

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


    def createGuideControls(self, name, ctrlType, controlsList, defNames):
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
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        del self.refInputs[:]

        if ctrlType == "deformers":
            parent = self.jawCtrl
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


        if ctrlType == "lipControls":
            parent = self.midLipCtrl
            defControlNameList =[]

            # Lets build all new handles
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True


            # Setting up names
            lSideControls = ["L_" + x for x in defControlNameList]
            rSideControls = ["R_" + x for x in defControlNameList]

            if lSideControls:
                lSideControls.reverse()

            defControlNameList = lSideControls + ["Mid"] + rSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="circle", scale="0.5")
                newCtrl.rotatePoints(90,0,0)
                newCtrl.setColor("lightsteelblue")
                newCtrl.xfo = parent.xfo
                newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 8)))
                controlsList.append(newCtrl)


        for ctrl in controlsList:
            self.addToSymDict(ctrl)

        return True


    def updateDefNames(self, defNames):
        self.createGuideControls("deformers", self.defCtrls, defNames)

    def updatelipCtrls(self, defNames):
        self.createGuideControls("controls", self.lipCtrls, defNames)


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




    def createGuideControls(self, name, ctrlType, controlsList, defNames):
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

        parent = self.ctrlCmpGrp

        if ctrlType == "deformers":
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
                newCtrl = Locator(defName + "_" + name, parent= self.ctrlCmpGrp)
                newCtrl.setShapeVisibility(False)
                newCtrl.xfo = parent.xfo
                controlsList.append(newCtrl)

                newDef = Joint(defName + "_" + name, parent= self.mouthDef)
                newDef.setComponent(self)
                newDef.constrainTo(newCtrl)


        if ctrlType == "controls":
            defControlNameList =[]

            # Lets build all new handles
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True


            # etting up names
            lSideControls = ["L" + x for x in defControlNameList]
            rSideControls = ["R" + x for x in defControlNameList]

            if lSideControls:
                lSideControls.reverse()

            defControlNameList = lSideControls + ["Mid"] + rSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(name + defName, parent=parent, shape="halfCircle")
                newCtrl.rotatePoints(90,0,0)
                newCtrl.setColor("sienna")
                newCtrl.xfo = parent.xfo
                controlsList.append(newCtrl)
                newCtrl.lockRotation(x=False, y=True, z=True)
                newCtrl.lockScale(x=True, y=True, z=True)
                try:
                    newCtrl.scalePoints(Vec3(.125,.125,.125))
                except:
                    pass


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
                ctrlUberParent = self.insertCtrlSpace(ctrl, name= ctrl.getName() + 'Driven')
                ctrlParent     = self.insertCtrlSpace(ctrl)
                # if i < (half-1):
                #     ctrlParent.constrainTo(self.upLipCtrls[i+1], maintainOffset=True)
                # if (half+1) < i:
                #     ctrlParent.constrainTo(self.upLipCtrls[i-1], maintainOffset=True)
                controlParents.append(ctrlUberParent)
        return controlParents


    def createCurveRig(self, name, rigCtrls = [], rigParams = [], defParams = [], data=None):
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
        defCtrls   = []
        defCtrls   = [lRigCorner] + self.createGuideControls(name, "controls", defCtrls, data["lipCtrlNames"]) + [rRigCorner]
        rigOutputs = self.insertParentSpaces(defCtrls)

        defOutputs = []
        defOutputs  = [lDefCorner] + self.createGuideControls(name, "deformers", defOutputs, data["numSpans"]) + [rDefCorner]

        # - - - - - - - - - - - - - -
        # Rig OP
        # - - - - - - - - - - - - - -
        # create Rest Xfos and Aligns
        rigCtrlsRest = []
        rigCtrlsAligns = []
        for c in rigCtrls:
           rigCtrlsAligns.append(Vec3(1,2,3))

        #need to eliminate this fix-up
        rigCtrlsAligns[3] = Vec3(-1,2,-3)
        rigCtrlsAligns[4] = Vec3(-1,2,3)


        curveRigOp = KLOperator(name+ 'RigOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(curveRigOp)

        curveRigOp.setInput('drawDebug', self.drawDebugInputAttr)
        curveRigOp.setInput('rigScale', 1.0)
        curveRigOp.setInput('degree', 4)
        curveRigOp.setInput('alignX', alignX )
        curveRigOp.setInput('alignY', alignY )
        curveRigOp.setInput('alignZ', alignZ )
        curveRigOp.setInput('keepArcLength', 0.0)
        curveRigOp.setInput('compressionAmt', 0.0)
        curveRigOp.setInput('followCurveTangent', 1)
        curveRigOp.setInput('altTangent', Vec3(-1.0,0.0,0.0))
        curveRigOp.setInput('parent', parent)
        curveRigOp.setInput('useLocalNormal', 1.0)
        curveRigOp.setInput('followCurveNormal', 1.0)

        curveRigOp.setInput('atVec', atXfo)
        curveRigOp.setInput('controlAligns', rigCtrlsAligns)
        curveRigOp.setInput('controls', rigCtrls)
        curveRigOp.setInput('controlsRest', rigCtrls)
        curveRigOp.setInput('params', rigParams)

        curveRigOp.setOutput('outputs', rigOutputs)

        # - - - - - - - - - - - - - -
        # Def OP
        # - - - - - - - - - - - - - -
        # create Rest Xfos and Aligns
        defCtrlsRest = []
        defCtrlsAligns = []
        for c in defCtrls:
           defCtrlsAligns.append(Vec3(1,2,3))
           defCtrlsRest.append(c.xfo)


        # Add lowLip Debug Canvas Op
        curveDefOp = KLOperator(name+ 'DefOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(curveDefOp)

        curveDefOp.setInput('drawDebug', self.drawDebugInputAttr)
        curveDefOp.setInput('rigScale', 1.0)
        curveDefOp.setInput('degree', 3)
        curveDefOp.setInput('alignX', alignX )
        curveDefOp.setInput('alignY', alignY )
        curveDefOp.setInput('alignZ', alignZ )
        curveDefOp.setInput('keepArcLength', 0.0)
        curveDefOp.setInput('compressionAmt', 0.0)
        curveDefOp.setInput('followCurveTangent', 0.25)
        curveDefOp.setInput('altTangent', Vec3(-1.0,0.0,0.0))
        curveDefOp.setInput('parent', parent)
        curveDefOp.setInput('useLocalNormal', 1.0)
        curveDefOp.setInput('followCurveNormal', 1.0)

        curveDefOp.setInput('atVec', atXfo)
        curveDefOp.setInput('controlAligns', defCtrlsAligns)
        curveDefOp.setInput('controls', defCtrls)
        curveDefOp.setInput('controlsRest', defCtrls)
        curveDefOp.setInput('params', defParams)

        curveDefOp.setOutput('outputs', defOutputs)

        return curveRigOp, curveDefOp, defCtrls, defOutputs



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

        self.parentSpaceInputTgt.childJoints = []

        # Mouth
        self.mouthDef = Joint('jaw', parent=self.deformersParent)
        self.mouthDef.setComponent(self)
        self.parentSpaceInputTgt.childJoints.append(self.mouthDef)

        # =========
        # Controls
        # =========
        # Mouth

        self.jawCtrlSpace = CtrlSpace('jaw', parent=self.ctrlCmpGrp)
        self.jawCtrl = Control('jaw', parent=self.jawCtrlSpace, shape="halfCircle", scale=0.5)
        # midMouth
        self.topMouthCtrlSpace = CtrlSpace('topMouth', parent=self.jawCtrlSpace)

        # midMouth
        self.midMouthCtrlSpace = CtrlSpace('midMouth', parent=self.ctrlCmpGrp)
        self.midMouthCtrl = CtrlSpace('midMouth', parent=self.midMouthCtrlSpace)

        # loLip
        self.loLipCtrlSpace = CtrlSpace('loLip', parent=self.jawCtrl)
        self.loLipCtrl = Control('loLip', parent=self.loLipCtrlSpace, shape="halfCircle")
        self.L_loLipHandleCtrl = CtrlSpace('L_loLipHandle', parent=self.loLipCtrl)
        self.R_loLipHandleCtrl = CtrlSpace('R_loLipHandle', parent=self.loLipCtrl)

        # upLip
        self.upLipCtrlSpace = CtrlSpace('upLip', parent=self.jawCtrlSpace)
        self.upLipCtrl = Control('upLip', parent=self.upLipCtrlSpace, shape="halfCircle")
        self.L_upLipHandleCtrl = CtrlSpace('L_upLipHandle', parent=self.upLipCtrl)
        self.R_upLipHandleCtrl = CtrlSpace('R_upLipHandle', parent=self.upLipCtrl)

        self.L_MouthCtrlSpace = CtrlSpace('L_Mouth', parent=self.midMouthCtrl)
        self.L_MouthCtrl = Control('L_Mouth', parent=self.L_MouthCtrlSpace, shape="circle", scale=0.5)
        self.L_MouthCornerCtrlSpace = CtrlSpace('L_Mouth', parent=self.L_MouthCtrl)
        self.L_MouthCornerCtrl = Control('L_MouthCorner', parent=self.L_MouthCornerCtrlSpace, shape="circle", scale=0.125)
        self.L_MouthCtrl.setColor("mediumseagreen")

        self.R_MouthCtrlSpace = CtrlSpace('R_Mouth', parent=self.midMouthCtrl)
        self.R_MouthCtrl = Control('R_Mouth', parent=self.R_MouthCtrlSpace, shape="circle", scale=0.5)
        self.R_MouthCornerCtrlSpace = CtrlSpace('R_Mouth', parent=self.R_MouthCtrl)
        self.R_MouthCornerCtrl = Control('R_MouthCorner', parent=self.R_MouthCornerCtrlSpace, shape="circle", scale=0.125)
        self.R_MouthCtrl.setColor("mediumvioletred")


        # ==============
        # Constrain I/O
        # ==============
        # Input
        self.mouthInputConstraint = self.jawCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # Output
        #self.lipOutputTgtConstraint = self.lipOutputTgt.constrainTo(self.midLipCtrl)
        self.mouthOutputTgtConstraint = self.mouthOutputTgt.constrainTo(self.jawCtrl, maintainOffset=False)
        self.jawEndOutputTgtConstraint = self.jawEndOutputTgt.constrainTo(self.jawCtrl, maintainOffset=False)
        self.mouthOutputTgt.parentJoint =  self.mouthDef



        # global Params
        self.offset    = Vec3(0,0.05,0.45)
        self.rigParams = [0, 0.05,0.25,0.5,0.75,0.95, 1]
        #these should be generated during the guide rig creation (hardcoded for now)
        self.defParams = [1, 0.94, 0.86, 0.79, 0.72, 0.653, 0.583, 0.5, 0.417, 0.347, 0.28, 0.21, 0.14, 0.06, 0]

        # upLip
        self.upLipControls   = [self.L_MouthCtrl, self.L_upLipHandleCtrl, self.upLipCtrl, self.R_upLipHandleCtrl, self.R_MouthCtrl]

        self.upLipRigOp, self.upLipDefOp, self.upLipDefCtrls, self.upLipDefOutputs  = self.createCurveRig(
            name = 'upLip',
            rigCtrls = self.upLipControls, 
            rigParams = self.rigParams, 
            defParams = self.defParams,
            data= data
            )


        # loLip
        self.loLipControls   = [self.L_MouthCtrl, self.L_loLipHandleCtrl, self.loLipCtrl, self.R_loLipHandleCtrl, self.R_MouthCtrl]

        self.loLipRigOp, self.loLipDefOp, self.loLipDefCtrls, self.loLipDefOutputs  = self.createCurveRig(
            name = 'loLip',
            rigCtrls = self.loLipControls, 
            rigParams = self.rigParams, 
            defParams = self.defParams,
            data= data
            )

        self.loLipDefCtrls[0]  = self.L_MouthCornerCtrl
        self.loLipDefCtrls[-1] = self.R_MouthCornerCtrl
        self.loLipDefOp.setInput('controls', self.loLipDefCtrls)
        self.loLipDefOp.setInput('controlsRest', self.loLipDefCtrls)

        self.upLipDefCtrls[0]  = self.L_MouthCornerCtrl
        self.upLipDefCtrls[-1] = self.R_MouthCornerCtrl
        self.upLipDefOp.setInput('controls', self.upLipDefCtrls)
        self.upLipDefOp.setInput('controlsRest', self.upLipDefCtrls)

        #blending mouth corner defs
        self.blendMidMouthRigOp = self.blend_two_xfos(
            self.midMouthCtrlSpace,
            self.topMouthCtrlSpace, self.loLipCtrlSpace,
            blend=0.5,
            name="blendMidMouthRigOp")



        # ===============
        # Add Splice Ops
        # ===============
        # Add Deformer Splice Op
        self.jawCtrlConstraint = self.mouthDef.constrainTo(self.jawCtrl, maintainOffset=False)

        # Left corner
        self.L_MouthCornerLoc = Locator('L_mouthCorner', parent=self.ctrlCmpGrp)
        self.L_MouthCornerLoc.setShapeVisibility(False)

        self.blendLeftCornerOp = self.blend_two_xfos(
            self.L_MouthCornerLoc,
            self.loLipDefOutputs[-1], self.upLipDefOutputs[-1],
            blend=0.5,
            name="blendLeftCornerOp")

        self.L_MouthCornerDef = Joint('L_mouthCorner',  parent=self.mouthDef)
        self.L_MouthCornerDef.setComponent(self)
        self.L_MouthCornerDef.constrainTo(self.L_MouthCornerLoc)


        # Right corner
        self.R_MouthCornerLoc = Locator('R_mouthCorner', parent=self.ctrlCmpGrp)
        self.R_MouthCornerLoc.setShapeVisibility(False)

        self.blendRightCornerOp = self.blend_two_xfos(
            self.R_MouthCornerLoc,
            self.loLipDefOutputs[0], self.upLipDefOutputs[0],
            blend=0.5,
            name="blendRightCornerOp")

        self.R_MouthCornerDef = Joint('R_mouthCorner',  parent=self.mouthDef)
        self.R_MouthCornerDef.setComponent(self)
        self.R_MouthCornerDef.constrainTo(self.R_MouthCornerLoc)


        for ctrl in [self.L_loLipHandleCtrl, self.L_upLipHandleCtrl]:
            ctrl.xfo = data['L_midLipHandleXfo']

        for ctrl in [self.R_loLipHandleCtrl, self.R_upLipHandleCtrl]:
            ctrl.xfo = data['R_midLipHandleXfo']

        for ctrl in [self.midMouthCtrlSpace, self.midMouthCtrl, self.topMouthCtrlSpace]:
            ctrl.xfo = data['midLipXfo']

        for ctrl in [self.jawCtrlSpace, self.jawCtrl, self.jawEndOutputTgt, self.mouthOutputTgt,]:
            ctrl.xfo = data['jawXfo']


        self.jawCtrl.rotatePoints(-90.0, 0.0, 0.0)
        self.jawCtrl.xfo = data['jawXfo']
        self.jawCtrl.translatePoints(data['jawEndXfo'].tr - data['jawXfo'].tr)

        for ctrl in [self.L_MouthCtrlSpace, self.L_MouthCtrl, self.L_MouthCornerCtrlSpace, self.L_MouthCornerCtrl]:
            ctrl.xfo = data['L_MouthXfo']
        for ctrl in [self.R_MouthCtrlSpace, self.R_MouthCtrl, self.R_MouthCornerCtrlSpace, self.R_MouthCornerCtrl]:
            ctrl.xfo = data['R_MouthXfo']

        for ctrl in [self.R_MouthCtrl, self.R_MouthCornerCtrl, self.L_MouthCtrl, self.L_MouthCornerCtrl]:
            ctrl.translatePoints(Vec3(Vec3(.5, .5,  0)))
            ctrl.rotatePoints(90.0, 0.0, 0.0)
            ctrl.lockRotation(x=True, y=True, z=True)
            ctrl.lockScale(x=True, y=True, z=True)

        self.R_MouthCtrlSpace.xfo.sc = Vec3(1.0, 1.0, -1.0)

        # Eval Constraints
        self.mouthOutputTgtConstraint.evaluate()
        self.jawEndOutputTgtConstraint.evaluate()

        # loLip

        for ctrl in [self.loLipCtrl, self.upLipCtrl]:
            ctrl.getParent().xfo = data['midLipXfo']
            ctrl.xfo = data['midLipXfo']
            ctrl.rotatePoints(90.0, 0.0, 0.0)
            ctrl.scalePoints(Vec3(Vec3(.5, .125,.5)))
            ctrl.lockScale(x=False, y=True, z=True)
            ctrl.alignOnZAxis()

        for ctrl in (self.loLipDefCtrls + [self.loLipCtrl]):
            ctrl.setColor("burlywood")
            try:
                ctrl.scalePoints(Vec3(Vec3(1,-1,1)))
            except:
                pass

        self.loLipCtrl.translatePoints(Vec3(Vec3(0, -0.75,  .5)))
        self.upLipCtrl.translatePoints(Vec3(Vec3(0,  0.75,  .5)))


        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.scalePoints(globalScale)




        # update the positions of the lip controls to match their uberparents
        # after we eval the operators and get the uber positions
        self.upLipRigOp.evaluate()
        self.loLipRigOp.evaluate()

        #should do this up front - why does hierarchy not get evaluated?
        for ctrls in [self.upLipDefCtrls, self.loLipDefCtrls]:
            for ctrl in ctrls:
                if ctrl not in [self.L_MouthCtrl, self.R_MouthCtrl, self.R_MouthCornerCtrl, self.L_MouthCornerCtrl]:
                    uberParentXfo = ctrl.getParent().getParent().xfo
                    downAxis = Vec3(-1,-1,-1)*uberParentXfo.ori.getYaxis()
                    ctrl.getParent().xfo = xfo.xfoFromDirAndUpV(Vec3(0,0,0), downAxis, uberParentXfo.ori.getZaxis())
                    ctrl.getParent().xfo.tr = uberParentXfo.tr
                    ctrl.xfo = ctrl.getParent().xfo
                    # need to find a proper way of detecting controls of type curve
                    try:
                        ctrl.translatePoints(Vec3(Vec3(0,0,.5)))
                    except: 
                        pass

        self.upLipRigOp.setInput('followCurveTangent', .25)
        self.loLipRigOp.setInput('followCurveTangent', .25)

        self.upLipControlsRest = []
        self.loLipControlsRest = []

        self.evalOperators()
        for i in range(len(self.loLipDefCtrls)):
            print self.loLipDefCtrls[i].xfo
            self.loLipControlsRest.append(Xfo(self.loLipDefCtrls[i].xfo))
        for i in range(len(self.upLipDefCtrls)):
            print self.upLipDefCtrls[i].xfo
            self.upLipControlsRest.append(self.upLipDefCtrls[i].xfo)

        self.loLipDefOp.setInput('controlsRest', self.loLipControlsRest)
        self.upLipDefOp.setInput('controlsRest', self.upLipControlsRest)
        self.evalOperators()


        #self.lipOutputTgtConstraint.evaluate()
        self.mouthOutputTgtConstraint.evaluate()
        self.jawEndOutputTgtConstraint.evaluate()




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMouthGuide)
ks.registerComponent(OSSMouthRig)
