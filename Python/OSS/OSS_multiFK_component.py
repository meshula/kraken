
import math, re
from kraken.core.maths import Xfo, Vec3
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import *

from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV, aimAt

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
from kraken.core.objects.space import Space
from kraken.core.objects.layer import Layer
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
# from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "multiFK"

class OSSmultiFKComponent(OSS_Component):
    """multiFK Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSmultiFKComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========

        self.ikgoal_cmpIn = None
        self.contstrainFirstControl_cmpIn = None
        self.contstrainLastControl_cmpIn = None
        # Declare Output Xfos
        self.baseOutputTgt = self.createOutput('base', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.endOutputTgt = self.createOutput('end', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.multiFKVertebraeOutput = self.createOutput('multiFKVertebrae', dataType='Xfo[]')

        self.tipBoneLenInputAttr = self.createInput('tipBoneLen', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Xfos
        self.nboneOutputs = self.createOutput('nboneOutputs', dataType='Xfo[]')


class OSSmultiFKComponentGuide(OSSmultiFKComponent):
    """multiFK Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct multiFK Guide Component:" + name)
        super(OSSmultiFKComponentGuide, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        # =========
        # Controls
        # ========
        self.name = name
        self.addPartialJoints = BoolAttribute('addPartialJoints', value=False, parent=self.guideSettingsAttrGrp)
        self.multiFKCtrlNames = StringAttribute('multiFKCtrlNames', value="A B C D", parent=self.guideSettingsAttrGrp)
        self.numDeformersAttr = IntegerAttribute('numDeformers', value=6, minValue=0, maxValue=99, parent=self.guideSettingsAttrGrp)
        self.popFirstControl = BoolAttribute('popFirstControl', value=False, parent=self.guideSettingsAttrGrp)
        self.popLastControl = BoolAttribute('popLastControl', value=False, parent=self.guideSettingsAttrGrp)
        self.popFirstJoint = BoolAttribute('popFirstJoint', value=False,  parent=self.guideSettingsAttrGrp)
        self.popLastJoint = BoolAttribute('popLastJoint', value=False, parent=self.guideSettingsAttrGrp)
        self.exposeControls = BoolAttribute('exposeControls', value=True, parent=self.guideSettingsAttrGrp)
        self.isCurveChain = BoolAttribute('isCurveChain', value=True, parent=self.guideSettingsAttrGrp)
        self.isIK = BoolAttribute('IK', value=True, parent=self.guideSettingsAttrGrp)
        self.rootIKIndexAttr = IntegerAttribute('rootIKIndex', value=0, minValue=0, maxValue=10, parent=self.guideSettingsAttrGrp)
        self.tweakControls = BoolAttribute('tweakControls', value=False, parent=self.guideSettingsAttrGrp)
        self.useOtherIKGoalInput = BoolAttribute('useOtherIKGoal', value=False, parent=self.guideSettingsAttrGrp)
        self.controlSizeTaper = ScalarAttribute('controlSizeTaper', 0.0, maxValue=1.0, minValue=-1.0, parent=self.guideSettingsAttrGrp)
        self.controlHierarchy = BoolAttribute('controlHierarchy', value=True, parent=self.guideSettingsAttrGrp)
        self.contstrainFirstControlInput = BoolAttribute('contstrainFirstControl', value=False, parent=self.guideSettingsAttrGrp)
        self.contstrainLastControlInput = BoolAttribute('contstrainLastControl', value=False, parent=self.guideSettingsAttrGrp)

        self.constrainFirstDefToControl = BoolAttribute('constrainFirstDefToControl', value=True, parent=self.guideSettingsAttrGrp)
        self.constrainLastDefToControl = BoolAttribute('constrainLastDefToControl', value=True, parent=self.guideSettingsAttrGrp)

        self.useOtherIKGoalInput.setValueChangeCallback(self.updateUseOtherIKGoal)

        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        # Guide Controls

        self.controls = []
        self.multiFKCtrlNames.setValueChangeCallback(self.updatemultiFKCtrls)

        self.contstrainFirstControlInput.setValueChangeCallback(self.updateContstrainFirstControl)
        self.contstrainLastControlInput.setValueChangeCallback(self.updateContstrainLastControl)
        # self.useOtherIKGoalInput.setValueChangeCallback(self.updateUseOtherIKGoal)

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        self.globalScaleVec = Vec3(globalScale, globalScale, globalScale)

        data = {
                "name": name,
                "location": "M"
               }

        self.loadData(data)

        Profiler.getInstance().pop()



    def createGuideControls(self, ctrlType, controlsList, defNames):

        controls = []
        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        if ctrlType == "multiFKControls":
            parent = self.ctrlCmpGrp
            defControlNameList =[]

            # Lets build all new handles
            controls = self.convertToStringList(defNames, prefix = self.name, joinStr = '', camelCase = True)
            defControlNameList = controls
            if not defControlNameList:  # Nothing to build
                return True


            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="circle")
                newCtrl.setColor("brown")
                newCtrl.xfo = parent.xfo.multiply(Xfo(tr=Vec3(0, i , 0)))
                newCtrl.scalePoints(self.globalScaleVec)
                controlsList.append(newCtrl)
        return True


    def updatemultiFKCtrls(self, defNames):
        self.createGuideControls("multiFKControls", self.controls, defNames)


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """

        data = super(OSSmultiFKComponentGuide, self).saveData()

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
        # get global Scale and create Vec3 for uniform control scaling

        #Reset all shapes, but really we should just recreate all controls from loadData instead of init
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        #saveData() will grab the guide settings values (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data


        if "useOtherIKGoalInput" in data.keys():
            self.updateUseOtherIKGoal(bool(data["useOtherIKGoalInput"]))

        super(OSSmultiFKComponentGuide, self).loadData( data )

        self.loadAllObjectData(data, "Control")
        self.loadAllObjectData(data, "Transform")

        return True



    def updateUseOtherIKGoal(self, useOtherIKGoal):
        """ Callback to changing the component setting 'useOtherIKGoalInput' """

        if useOtherIKGoal:
            if self.ikgoal_cmpIn is None:
                self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
                self.ikBlendAttr = self.createInput(self.name  + 'ikBlend', dataType='Float', parent=self.cmpInputAttrGrp)
                self.softIKAttr = self.createInput('softIK', dataType='Float', parent=self.cmpInputAttrGrp)
                self.squashhAttr = self.createInput('squash', dataType='Float', parent=self.cmpInputAttrGrp)
                self.stretchAttr = self.createInput('stretch', dataType='Float', parent=self.cmpInputAttrGrp)
        else:
            if self.ikgoal_cmpIn is not None:
                # self.deleteInput('ikGoalInput', parent=self.inputHrcGrp)
                # self.deleteInput('ikBlend', parent=self.cmpInputAttrGrp)
                # self.deleteInput('softIK', parent=self.cmpInputAttrGrp)
                # self.deleteInput('stretch', parent=self.cmpInputAttrGrp)
                self.ikgoal_cmpIn = None



    def updateContstrainFirstControl(self, contstrainFirstControl):
        """ Callback to changing the component setting 'useOtherIKGoalInput' """

        if contstrainFirstControl:
            if self.contstrainFirstControl_cmpIn is None:
                self.contstrainFirstControl_cmpIn = self.createInput('firstControlXfo', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        else:
            if self.contstrainFirstControl_cmpIn is not None:
                # self.deleteInput('firstControlXfo', parent=self.inputHrcGrp)
                # self.deleteInput('ikBlend', parent=self.cmpInputAttrGrp)
                # self.ikgoal_cmpIn = None
                self.contstrainFirstControl_cmpIn = None



    def updateContstrainLastControl(self, contstrainLastControl):
        """ Callback to changing the component setting 'useOtherIKGoalInput' """

        if contstrainLastControl:
            if self.contstrainLastControl_cmpIn is None:
                self.contstrainLastControl_cmpIn = self.createInput('lastControlXfo', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        else:
            if self.contstrainLastControl_cmpIn is not None:
                # self.deleteInput('firstControlXfo', parent=self.inputHrcGrp)
                # self.deleteInput('ikBlend', parent=self.cmpInputAttrGrp)
                # self.ikgoal_cmpIn = None
                self.contstrainLastControl_cmpIn = None


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """
        data = super(OSSmultiFKComponentGuide, self).getRigBuildData()
        # ===============
        # Calculate Xfos
        # ===============

        # should include getmultiFKData
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

        return OSSmultiFKComponentRig


class OSSmultiFKComponentRig(OSSmultiFKComponent):
    """multiFK Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct multiFK Rig Component:" + name)
        super(OSSmultiFKComponentRig, self).__init__(name, parent)

        # ==========
        # Deformers
        # ==========
        self.name = name
        self.defCurveJoints = []
        self.parentSpaceInputTgt.childJoints = []
        self.controls = []

        self.curveBoneOutputs = []
        self.params = []
        #self.setNumDeformers(1)

        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.multiFKVertebraeOutput.setTarget(self.curveBoneOutputs)

        # ===============
        # Add Fabric Ops
        # ===============
        # Add multiFK Canvas Op
        Profiler.getInstance().pop()



    def createCurveOp(self):

        self.rigControlAligns = []
        self.controlRestInputs = []

        for i in xrange(len(self.controls)):
            self.rigControlAligns.append(Vec3(1,2,3))
            self.controlRestInputs.append(self.controls[i].xfo)

        self.NURBSmultiFKKLOp = KLOperator(self.component_name, 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.NURBSmultiFKKLOp)

        self.NURBSmultiFKKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.NURBSmultiFKKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.NURBSmultiFKKLOp.setInput('alignX', 1 )
        self.NURBSmultiFKKLOp.setInput('alignY', 2 )
        self.NURBSmultiFKKLOp.setInput('alignZ', 3 )
        self.NURBSmultiFKKLOp.setInput('degree', 3)
        self.NURBSmultiFKKLOp.setInput('keepArcLength', 0.0)
        self.NURBSmultiFKKLOp.setInput('compressionAmt', 0.5)
        self.NURBSmultiFKKLOp.setInput('followCurveTangent', 1.0)
        self.NURBSmultiFKKLOp.setInput('useLocalNormal', 1.0)
        self.NURBSmultiFKKLOp.setInput('followCurveNormal', 1.0)
        self.NURBSmultiFKKLOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.NURBSmultiFKKLOp.setInput('parent', self.parentSpaceInputTgt)
        self.NURBSmultiFKKLOp.setInput('atVec', self.ctrlCmpGrp) # atVec should be optional, but is not currently in the Solver
        self.NURBSmultiFKKLOp.setInput('controlAligns', self.rigControlAligns)
        self.NURBSmultiFKKLOp.setInput('controls', self.controls)
        self.NURBSmultiFKKLOp.setInput('controlsRest', self.controlRestInputs)
        self.NURBSmultiFKKLOp.setInput('params', self.params )

        self.NURBSmultiFKKLOp.setOutput('outputs', self.curveBoneOutputs)


    def createAlignOp(self, control, alignSpaces, alignWeightNames, alignWeightValues):

        controlSpace       = control.getParent()
        controlSpaceParent = controlSpace.getParent()
        restXfo            = controlSpace.xfo

        alignWeights = []

        alignAttrGrp  = AttributeGroup("Align_Settings", parent=control)

        for i in xrange(len(alignSpaces)):
            alignWeights.append(ScalarAttribute(alignWeightNames[i], value=alignWeightValues[i], minValue=0.0, maxValue=1.0, parent=alignAttrGrp))

        # Add Spine Canvas Op
        alignOp = KLOperator(self.component_name +'_Align', 'OSS_WeightedAverageMat44KLSolver', 'OSS_Kraken')
        self.addOperator(alignOp)

        # Add Att Inputs
        alignOp.setInput('drawDebug', self.drawDebugInputAttr)
        alignOp.setInput('rigScale', self.rigScaleInputAttr)

        alignOp.setInput('mats', alignSpaces)
        alignOp.setInput('matWeights',alignWeights)
        alignOp.setInput('translationAmt',  1)
        alignOp.setInput('scaleAmt',  1)
        alignOp.setInput('rotationAmt',  1)
        alignOp.setInput('parent', controlSpaceParent.getParent())
        alignOp.setInput('restMatParent', controlSpaceParent.xfo)
        alignOp.setInput('restMat', controlSpace.xfo)
        if not i == 0:
            alignOp.setOutput('result', controlSpace)

        return alignOp  


    def createControls(self, ctrlType, controlsList, defNames, data):

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]
        self.defNBoneJoints = []

        parent = self.ctrlCmpGrp
        self.exposeControls = bool(data['exposeControls'])  #This should be a simple method instead
        self.tweakControls = bool(data['tweakControls'])  #This should be a simple method instead
        self.controlHierarchy = bool(data['controlHierarchy'])  #This should be a simple method instead



        if ctrlType == "multiFKControls":
            defControlNameList =[]
            # Lets build all new handles
            defControlNameList = self.convertToStringList(defNames, prefix = self.name, joinStr = '', camelCase = True)
            if not defControlNameList:  # Nothing to build
                return True

            numCtrls = len(defControlNameList)
            taperRatio = float(data['controlSizeTaper'])/(numCtrls-1)
            for i, defName in enumerate(defControlNameList):
                if not bool(data['isCurveChain']):
                    if i == 0:
                        newNBoneDefParent = self.deformersParent
                    else:
                        newNBoneDefParent = self.defNBoneJoints[-1]

                    if (i==0 and bool(data["popFirstJoint"])) or ((i==numCtrls-1) and bool(data["popLastJoint"])):
                        newNBoneDef = Transform(defName, parent=parent)
                    else:
                        newNBoneDef = Joint(defName, parent= newNBoneDefParent)
                        newNBoneDef.setComponent(self)
                        # newNBoneDef.constrainTo(newCtrl)
                    # newNBoneDef = Joint(defName, parent=newNBoneDefParent)
                    # newNBoneDef.setComponent(self)
                    newNBoneDef.xfo = data[defName + "Xfo"]
                    self.defNBoneJoints.append(newNBoneDef)

                if self.controlHierarchy and len(controlsList):
                    parent = controlsList[-1]

                if self.exposeControls:
                    if not bool(data['isCurveChain']) and (i == numCtrls-1) and not bool(data["popLastControl"]) and bool(data["IK"]) :
                        newCtrl = IKControl(defName, parent=self.ctrlCmpGrp, shape="squarePointed")
                        newCtrl.setColor("green")
                        newCtrl.setShape("jack")
                    else:
                        if (i==0 and bool(data["popFirstControl"])) or ((i==numCtrls-1) and bool(data["popLastControl"])):
                            newCtrl = Transform(defName, parent=parent)
                        else:
                            newCtrl = FKControl(defName, parent=parent, shape="squarePointed")

                    try:
                        newCtrl.setColor("gold")
                        newCtrl.scalePoints(self.globalScaleVec)
                        newCtrl.scalePoints(Vec3(1 - i*taperRatio, 1 - i*taperRatio, 1 - i*taperRatio))
                    except Exception, e:
                        print e

                else:
                    newCtrl = Transform(defName, parent=parent)

                newCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["YXZ"])  #Set with component settings later
                newCtrl.xfo = data[defName + "Xfo"]
                newCtrlParent = newCtrl.insertSpace()


                # align
                if not bool(data['isCurveChain']) and (i == numCtrls-1) and bool(data["IK"]):
                    newCtrlAttrGrp  = AttributeGroup("DisplayInfo_Settings", parent=newCtrl)
                    self.ikBlendAttr = ScalarAttribute(self.name + 'ikBlend', value=0.0, minValue=0.0, maxValue=1.0, parent=newCtrlAttrGrp)
                    newCtrl.setParent(self.ctrlCmpGrp)
                
                controlsList.append(newCtrl)    


        # if self.addPartialJoints:
        #               twistXfo = self.createOutput(digiSegDefs[j].getName()+"_partial", dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        #               twistXfo.xfo = digiSegDefs[j].xfo
        #               twistXfo.constrainTo(digiSegDefs[j].getParent(), maintainOffset=True)
        #               self.createPartialJoint(digiSegDefs[j], baseTranslate=twistXfo, baseRotate=twistXfo, parent=digiSegDefs[j].getParent())



        controlXfos = [ctrl.xfo for ctrl in controlsList]
        upVXfo = self.calculateUpVXfo(controlXfos, controlsList[-1].xfo)

        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "POSZ"
        if self.getLocation() == 'R':
            self.upAxisStr = "NEGZ"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]


        for i in xrange(len(controlsList)):
        # align last control
            if i < len(controlsList)-1:
        #         xfo = Xfo()
        #         xfo = self.alignXfo(controlsList, i)
        #         controlsList[i].getParent().xfo = xfo
        #         controlsList[i].xfo = xfo
                aimAt(controlsList[i].xfo, aimPos=controlsList[i+1].xfo.tr, upPos=upVXfo.tr, aimAxis=self.boneAxis, upAxis=tuple([x for x in self.upAxis]))
            else: 
                # take previous' Control Rotation
                controlsList[i].xfo.ori = controlsList[i-1].xfo.ori

            controlsList[i].getParent().xfo = controlsList[i].xfo

            try:
                controlsList[i].rotatePoints(0,-90, -90)
                if self.getLocation() == 'R':
                    controlsList[i].rotatePoints(0, 180, 0)
            except Exception, e:
                print e
                

        return controlsList





    def setNumDeformers(self, numDeformers, data):
        for output in reversed(self.curveBoneOutputs):
            output.getParent().removeChild(output)
        del self.curveBoneOutputs[:] #Clear since this array obj is tied to output already

        for joint in reversed(self.defCurveJoints):
            joint.getParent().removeChild(joint)
        del self.defCurveJoints[:] #Clear since this array obj is tied to output already

        # Determine params for number of Deformers
        self.params = self.fillValues(numDeformers, minVal=0.0, maxVal=1.0, popFirst=bool(data['popFirstJoint']), popLast=bool(data['popLastJoint']))


        numDeformers = len(self.params)


        # Add new deformers and outputs
        for i in xrange(len(self.curveBoneOutputs), numDeformers):
            name = self.component_name + str(i).zfill(2)
            #Need dynamic ports branch to be able to see this updated in Graph
            multiFKOutput = self.createOutput(name, dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            self.curveBoneOutputs.append(multiFKOutput)

        parent = self.deformersParent
        for i in xrange(len(self.defCurveJoints), numDeformers):
            if i != 0:
                parent = self.defCurveJoints[-1]
            name = str(i).zfill(2)
            multiFKDef = Joint(self.name + name, parent=parent)
            multiFKDef.setComponent(self)
            self.defCurveJoints.append(multiFKDef)


        if hasattr(self, 'NURBSmultiFKKLOp'):  # Check in case this is ever called from Guide callback
            self.NURBSmultiFKKLOp.setInput('params',  self.params)

        return True


    def calculateUpVXfo(self, boneXfos, endXfo):
        """Calculates the transform for the UpV control.

        Args:
            boneXfos (list): Bone transforms.
            endXfo (Xfo): Transform for the end of the chain.

        Returns:
            Xfo: Up Vector transform.

        """

        # Calculate FW
        toFirst = boneXfos[1].tr.subtract(boneXfos[0].tr).unit()
        toTip = endXfo.tr.subtract(boneXfos[0].tr).unit()
        fw = toTip.cross(toFirst).unit()


        chainNormal = fw.cross(toTip).unit()
        chainZAxis = toTip.cross(chainNormal).unit()

        chainXfo = Xfo()
        chainXfo.setFromVectors(toTip.unit(), chainNormal, chainZAxis, boneXfos[0].tr)

        rootToTip = endXfo.tr.subtract(boneXfos[0].tr).length()

        upVXfo = Xfo()

        upVXfo.tr = chainXfo.transformVector(Vec3(rootToTip / 2.0, rootToTip / 1.5, 0.0))
        # upVXfo.tr = Vec3(0, 0,10)
        return upVXfo


    def alignXfo(self, controls, i):

        # Calculate Xfo
        dirVec = self.controls[i + 1].xfo.tr - self.controls[i].xfo.tr
        normal = self.controls[i].xfo.ori.getZaxis().cross(dirVec).unit()
        zAxis = dirVec.cross(normal).unit()
        xfo = Xfo()
        xfo.setFromVectors(dirVec.unit(), normal, zAxis, self.controls[i].xfo.tr)
        return xfo

    def createIKAttrs(self, data):
        defName = self.convertToStringList(data["multiFKCtrlNames"], prefix = self.name, joinStr = '', camelCase = True)[-1]
        self.useOtherIKGoal = bool(data['useOtherIKGoal'])
        self.limbIKSpace = Space(defName, parent=self.ctrlCmpGrp)
        self.limbIKSpace.xfo = data[defName + 'Xfo']
        # hand
        if self.useOtherIKGoal: #Do not use this as a control, hide it
            self.limbIKCtrl = self.controls[-1] #Transform(self.ikHandleName, parent=self.limbIKSpace)
        else:
            self.limbIKCtrl = self.controls[-1] #IKControl(self.ikHandleName, parent=self.limbIKSpace, shape="jack")
        self.limbIKCtrl.xfo = data[defName + 'Xfo']


        # Add Component Params to IK control
        limbSettingsAttrGrp = AttributeGroup("DisplayInfo_LimbSettings", parent=self.limbIKCtrl)
        if self.useOtherIKGoal:
            self.ikgoal_cmpIn = self.createInput('ikGoalInput', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
            self.limbIKCtrl.constrainTo(self.ikgoal_cmpIn, maintainOffset=True)
            self.ikBlendAttr = self.createInput('ikBlend', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            self.softIKAttr = self.createInput('softIK', dataType='Float', value=0.0, minValue=0.0, parent=self.cmpInputAttrGrp).getTarget()
            self.squashAttr = self.createInput('squash', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
            self.stretchAttr = self.createInput('stretch', dataType='Float', value=1.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()
        else:
            self.ikgoal_cmpIn = None
            self.ikBlendAttr = ScalarAttribute('ikBlend', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
            self.softIKAttr = ScalarAttribute('softIK', value=0.0, minValue=0.0, parent=limbSettingsAttrGrp)
            self.squashAttr = ScalarAttribute('squash', value=0.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)
            self.stretchAttr = ScalarAttribute('stretch', value=1.0, minValue=0.0, maxValue=1.0, parent=limbSettingsAttrGrp)

    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSmultiFKComponentRig, self).loadData( data )

        self.component_name = data["name"]
        numDeformers = data['numDeformers']

        self.globalScaleVec = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.controls = self.createControls("multiFKControls", self.controls, data["multiFKCtrlNames"], data)

        # - - - - - - - 
        # get FK Bones

        # Align Controls and parents
        numControls = len(self.controls)-1

        if bool(data['isCurveChain']):
            # Update number of deformers and outputs
            self.setNumDeformers(numDeformers, data)

            self.createCurveOp()


        if not bool(data['isCurveChain']):
            boneXfos = []
            boneLengths = []
            # number of controsl and Joints are the same for now
            self.numJoints = numControls
            self.nboneOutputsTgt= []

            self.IkEndOutputTgt = Transform(self.component_name+ 'IKEnd', parent=self.ctrlCmpGrp)


            for i in xrange(self.numJoints):
                boneVec = self.controls[i + 1].xfo.tr.subtract(self.controls[i].xfo.tr)
                boneLengths.append(boneVec.length())
                xfo = self.controls[i].xfo
                boneXfos.append(xfo)
                self.defNBoneJoints[i].xfo = xfo

                name = 'bone' + str(i + 1).zfill(2)
                self.defNBoneJoints[i].setComponent(self)
                legOutput = ComponentOutput(name, parent=self.outputHrcGrp)
                self.nboneOutputsTgt.append(legOutput)
                if not bool(data["IK"]):
                    self.defNBoneJoints[i].constrainTo(self.controls[i])
                    


            data['boneXfos'] = boneXfos

            data['endXfo'] = self.controls[-1].xfo
            data['boneLengths'] = boneLengths

            if bool(data["IK"]):
                # # - - - - - - - 
                # self.chainBase = Space('chainBase', parent=self.ctrlCmpGrp)
                # self.chainBase.xfo = 
                
                # Create Upvector
                self.upVSpace = Space(self.component_name + 'UpV', parent=self.ctrlCmpGrp)
                self.upVCtrl = Control(self.component_name + 'UpV', parent=self.upVSpace, shape="triangle")
                self.upVCtrl.alignOnXAxis()

                endXfo = self.controls[-1].xfo
                upVXfo = self.calculateUpVXfo(boneXfos, endXfo)
                self.upVSpace.xfo = upVXfo
                self.upVCtrl.xfo = upVXfo


                self.legIKCtrl = self.controls[-1]
                self.fkCtrls = self.controls[0:-1]
                # self.defNBoneJoints = self.defNBoneJoints[0:-1]

                # ===============
                # Add Canvas Ops
                # ===============
                # self.boneOutputsTgt = []
                self.nboneOutputs.setTarget(self.nboneOutputsTgt)

                # Add Canvas Op
                self.nBoneSolverKLOp = KLOperator(self.component_name, 'OSS_NBoneIKSolver', 'OSS_Kraken')
                self.addOperator(self.nBoneSolverKLOp)

                # # Add Att Inputs
                self.nBoneSolverKLOp.setInput('drawDebug', self.drawDebugInputAttr)
                self.nBoneSolverKLOp.setInput('rigScale', self.rigScaleInputAttr)
                self.nBoneSolverKLOp.setInput('useInitPose', 1)
                self.nBoneSolverKLOp.setInput('ikblend', self.ikBlendAttr)
                self.nBoneSolverKLOp.setInput('rootIndex',  data["rootIKIndex"])
                self.nBoneSolverKLOp.setInput('tipBoneLen', self.tipBoneLenInputAttr)

                # Add Xfo Inputs
                self.nBoneSolverKLOp.setInput('chainBase', self.controls[0])
                self.nBoneSolverKLOp.setInput('ikgoal', self.legIKCtrl)
                self.nBoneSolverKLOp.setInput('upVector', self.upVCtrl)
                self.nBoneSolverKLOp.setInput('upAxis', Vec3(self.upAxis[0], self.upAxis[1], self.upAxis[2]))

                self.nBoneSolverKLOp.setInput('fkcontrols', self.fkCtrls)

                # Add Xfo Outputs
                # self.nBoneSolverKLOp.setOutput('pose', self.nboneOutputsTgt)
                self.nBoneSolverKLOp.setOutput('pose', self.nboneOutputsTgt)

                self.nBoneSolverKLOp.setOutput('legEnd', self.IkEndOutputTgt)

            # =============
            # Set IO Attrs
            # =============
            tipBoneLen = boneLengths[-1]
            # self.tipBoneLenInputAttr.setMax(tipBoneLen * 2.0)

            # Setting the tip Length reverses the boneVec direction in the nBone sovler (we should provide sign in solver itself)
            if self.getLocation() == 'R':
                self.tipBoneLenInputAttr.setValue(-boneLengths[-1])
            else:
                self.tipBoneLenInputAttr.setValue(boneLengths[-1])


            # Constrain I/O
            # ==============
            # Constraint inputs


        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important

        # for i in xrange(len(self.controls)):
        #     self.alignSpacesKLOp = self.createAlignOp(self.controls[i], alignSpaces = [self.controls[i].getParent().getParent(), self.ctrlCmpGrp], alignWeightNames = ["alignToParent","alignToWorld"], alignWeightValues = [1,0])
        #     self.alignSpacesKLOp.evaluate()

        self.evalOperators()


        if bool(data['isCurveChain']):
            self.baseOutputTgt.constrainTo(self.curveBoneOutputs[0])
            self.endOutputTgt.constrainTo(self.curveBoneOutputs[-1])

            for i in xrange(len(self.curveBoneOutputs)):
                self.defBones = self.defCurveJoints
                self.defBones[i].xfo =  self.curveBoneOutputs[i].xfo
                if (i==0 and bool(data["constrainFirstDefToControl"])):
                    constraint = self.defBones[0].constrainTo(self.controls[0], maintainOffset=True)
                elif (i==len(self.curveBoneOutputs)-1 and bool(data["constrainLastDefToControl"])):
                    constraint = self.defBones[-1].constrainTo(self.controls[-1], maintainOffset=True)
                else:
                    constraint = self.defBones[i].constrainTo(self.curveBoneOutputs[i])
                constraint.evaluate()

        if not bool(data['isCurveChain']) and bool(data['IK']):
            self.baseOutputTgt.constrainTo( self.nboneOutputsTgt[0])
            self.endOutputTgt.constrainTo( self.nboneOutputsTgt[-1])
            for i in xrange(len(self.nboneOutputsTgt)):
                constraint = self.defNBoneJoints[i].constrainTo(self.nboneOutputsTgt[i])
                constraint.evaluate()
                self.defBones = self.defNBoneJoints
            # for i in xrange(len(boneLengths)):
            #     self.boneOutputsTgt[i].xfo = boneXfos[i]

            self.createIKAttrs(data)

        if not bool(data['IK']):
            self.defBones = self.defNBoneJoints

        # if not self.controlHierarchy or i ==0:
        self.controls[0].getParent().constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        self.parentSpaceInputTgt.childJoints = [self.defBones[0]]

        if data["contstrainFirstControl"]:
            self.contstrainFirstControl_cmpIn = self.createInput('firstControlXfo', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
            self.controls[0].removeAllConstraints()
            self.controls[0].constrainTo(self.contstrainFirstControl_cmpIn, maintainOffset=True)

        if data["contstrainLastControl"]:
            self.contstrainLastControl_cmpIn = self.createInput('lastControlXfo', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
            self.controls[-1].removeAllConstraints()
            self.controls[-1].constrainTo(self.contstrainLastControl_cmpIn, maintainOffset=True)


        # # ====================
        # # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # # ====================
        # # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.evalOperators()
    

        self.baseOutputTgt.parentJoint = self.defBones[0]
        self.endOutputTgt.parentJoint  = self.defBones[-1]

        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()

        # ====================
        # Extra Shape Mods
        # ====================
        # JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        # globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSmultiFKComponentGuide)
ks.registerComponent(OSSmultiFKComponentRig)