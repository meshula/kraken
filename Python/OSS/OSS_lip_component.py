
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
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
COMPONENT_NAME = "lip"


class OSSLip(BaseExampleComponent):
    """Lip Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSLip, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.lipOutputTgt = self.createOutput('lip', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.mouthOutputTgt = self.createOutput('mouth', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.mouthEndOutputTgt = self.createOutput('mouthEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs


        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)

class OSSLipGuide(OSSLip):
    """Lip Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Lip Guide Component:" + name)
        super(OSSLipGuide, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Guide Controls
        self.guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=self.guideSettingsAttrGrp)
        self.lipCtrlNames = StringAttribute('lipCtrlNames', value="UD Sneer Pinch", parent=self.guideSettingsAttrGrp)
        self.numSpansAttr = IntegerAttribute('numSpans', value=13, minValue=0, maxValue=20,  parent=self.guideSettingsAttrGrp)

        # midLip
        self.midLipCtrl = Control('midLip', parent=self.ctrlCmpGrp)
        self.midLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_midLipHandleCtrl = Control('L_midLipHandle', parent=self.midLipCtrl)
        self.R_midLipHandleCtrl = Control('R_midLipHandle', parent=self.midLipCtrl)
        self.midDummy = Control('midDummy', parent=self.ctrlCmpGrp)

        self.lMouthCtrl = Control('L_Mouth', parent=self.ctrlCmpGrp)
        self.rMouthCtrl = Control('R_Mouth', parent=self.ctrlCmpGrp)

        # upLip
        self.upLipCtrl = Control('upLip', parent=self.ctrlCmpGrp)
        self.upLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_upLipHandleCtrl = Control('L_upLipHandle', parent=self.upLipCtrl)
        self.R_upLipHandleCtrl = Control('R_upLipHandle', parent=self.upLipCtrl)
        self.upDummy = Control('upDummy', parent=self.ctrlCmpGrp)

        self.lMouthOutCtrl = Control('L_MouthOut', parent=self.ctrlCmpGrp)
        self.rMouthOutCtrl = Control('R_MouthOut', parent=self.ctrlCmpGrp)

        # loLip
        self.loLipCtrl = Control('loLip', parent=self.ctrlCmpGrp)
        self.loLipCtrl.lockTranslation(x=True, y=False, z=False)
        self.L_loLipHandleCtrl = Control('L_loLipHandle', parent=self.loLipCtrl)
        self.R_loLipHandleCtrl = Control('R_loLipHandle', parent=self.loLipCtrl)
        self.loDummy = Control('loDummy', parent=self.ctrlCmpGrp)


        self.lipCtrlNames.setValueChangeCallback(self.updatelipCtrls)
        self.numSpansAttr.setValueChangeCallback(self.updateDefNames)

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

        # Add Lip Symmetry Canvas Op
        self.lSideObjs = []
        self.rSideObjs = []
        self.lSideParentObjs = []

        # Add Att Inputs
        self.refInputs = []
        self.midLipControls = []
        self.midLipOutputs = []

        self.mouthCtrl = Control('mouth', parent=self.ctrlCmpGrp, shape="sphere")
        self.mouthEndCtrl = Control('mouthEnd', parent=self.ctrlCmpGrp, shape="sphere")
        self.mouthCtrl.setColor("green")
        self.mouthEndCtrl.setColor("green")

        data = {
                "name": name,
                "location": "M",
                "midLipXfo": Xfo(Vec3(0, 15, 4)),
                "L_midLipHandleXfo": Xfo(Vec3(2, 15, 4)),
                "R_midLipHandleXfo": Xfo(Vec3(-2, 15, 4)),
                "loLipXfo": Xfo(Vec3(0, 13, 4)),
                "L_loLipHandleXfo": Xfo(Vec3(2, 13, 4)),
                "R_loLipHandleXfo": Xfo(Vec3(-2, 13, 4)),
                "upLipXfo": Xfo(Vec3(0, 17, 4)),
                "L_upLipHandleXfo": Xfo(Vec3(2, 17, 4)),
                "R_upLipHandleXfo": Xfo(Vec3(-2, 17, 4)),
                'lipCtrlCrvData': self.midLipCtrl.getCurveData(),
                "mouthXfo": Xfo(Vec3(0, 15, 0)),
                "lMouthXfo": Xfo(Vec3(3, 15, 3)),
                "rMouthXfo": Xfo(Vec3(-3, 15, 3)),
                "lMouthOutXfo": Xfo(Vec3(4, 15, 2)),
                "rMouthOutXfo": Xfo(Vec3(-4, 15, 2)),
                "mouthEndXfo": Xfo(Vec3(0, 14, 4))
               }



        # Add midLip Debug Canvas Op
        self.midLipDebugOp = CanvasOperator('midLipDebugOp', 'OSS.Solvers.NURBSDebug')
        self.addOperator(self.midLipDebugOp)

        self.midLipDebugOp.setInput('drawDebug', 1)
        self.midLipDebugOp.setInput('rigScale', 1.0)
        self.midLipDebugOp.setInput('degree', 4)
        self.midLipDebugOp.setInput('keepArcLength', 1.0)

        self.midLipDebugOp.setInput('upVec', Xfo(Vec3(0.0,15.0,3.0)))
        self.midLipDebugOp.setInput('controls', self.midLipControls)
        self.midLipDebugOp.setInput('refMats', self.refInputs)

        self.midLipDebugOp.setOutput('outputs', self.midLipOutputs)
        self.midLipDebugOp.setOutput('dummyResult', self.midDummy.xfo.tr)

        # update Inputs
        self.midLipControls.append(self.lMouthCtrl)
        self.midLipControls.append(self.L_midLipHandleCtrl)
        self.midLipControls.append(self.midLipCtrl)
        self.midLipControls.append(self.R_midLipHandleCtrl)
        self.midLipControls.append(self.rMouthCtrl)

        self.midLipOutputs.append(self.midDummy)


        # Add upLip Debug Canvas Op
        self.upLipDebugOp = CanvasOperator('upLipDebugOp', 'OSS.Solvers.NURBSDebug')
        self.addOperator(self.upLipDebugOp)

        self.upLipControls = []
        self.upLipOutputs = []

        self.upLipDebugOp.setInput('drawDebug', 1)
        self.upLipDebugOp.setInput('rigScale', 1.0)
        self.upLipDebugOp.setInput('degree', 3)
        self.upLipDebugOp.setInput('keepArcLength', 1.0)

        self.upLipDebugOp.setInput('upVec', Xfo(Vec3(0.0,15.0,3.0)))
        self.upLipDebugOp.setInput('controls', self.upLipControls)
        self.upLipDebugOp.setInput('refMats', self.refInputs)

        self.upLipDebugOp.setOutput('outputs', self.upLipOutputs)
        self.upLipDebugOp.setOutput('dummyResult', self.upDummy.xfo.tr)

        # update Inputs
        self.upLipControls.append(self.lMouthOutCtrl)
        self.upLipControls.append(self.L_upLipHandleCtrl)
        self.upLipControls.append(self.upLipCtrl)
        self.upLipControls.append(self.R_upLipHandleCtrl)
        self.upLipControls.append(self.rMouthOutCtrl)

        self.upLipOutputs.append(self.upDummy)



        # Add lowLip Debug Canvas Op
        self.loLipDebugOp = CanvasOperator('loLipDebugOp', 'OSS.Solvers.NURBSDebug')
        self.addOperator(self.loLipDebugOp)

        self.loLipControls = []
        self.loLipOutputs = []

        self.loLipDebugOp.setInput('drawDebug', 1)
        self.loLipDebugOp.setInput('rigScale', 1.0)
        self.loLipDebugOp.setInput('degree', 3)
        self.loLipDebugOp.setInput('keepArcLength', 1.0)

        self.loLipDebugOp.setInput('upVec', Xfo(Vec3(0.0,15.0,3.0)))
        self.loLipDebugOp.setInput('controls', self.loLipControls)
        self.loLipDebugOp.setInput('refMats', self.refInputs)

        self.loLipDebugOp.setOutput('outputs', self.loLipOutputs)
        self.loLipDebugOp.setOutput('dummyResult', self.loDummy.xfo.tr)

        # update Inputs
        self.loLipControls.append(self.lMouthOutCtrl)
        self.loLipControls.append(self.L_loLipHandleCtrl)
        self.loLipControls.append(self.loLipCtrl)
        self.loLipControls.append(self.R_loLipHandleCtrl)
        self.loLipControls.append(self.rMouthOutCtrl)

        self.loLipOutputs.append(self.loDummy)


        # Add reflection Canvas Op, should feed inputs from self.symMapping
        self.reflectionOp = CanvasOperator('reflectionOp', 'OSS.Solvers.reflectMat44Solver')
        self.addOperator(self.reflectionOp)

        self.reflectionOp.setInput('inputs',   self.lSideObjs)
        self.reflectionOp.setInput('inputParents',  self.lSideParentObjs)
        self.reflectionOp.setOutput('results', self.rSideObjs)

        for ctrl in [self.L_loLipHandleCtrl,
                     self.L_upLipHandleCtrl,
                     self.L_midLipHandleCtrl,
                     self.lMouthCtrl,
                     self.lMouthOutCtrl,
                     self.R_midLipHandleCtrl,
                     self.rMouthCtrl,
                     self.R_loLipHandleCtrl,
                     self.R_upLipHandleCtrl,
                     self.rMouthOutCtrl]:
            self.addToSymDict(ctrl)

        for k,value in self.symMapping.iteritems():
            self.lSideObjs.append(value["lSide"])
            self.lSideParentObjs.append(value["lSideParent"])
            self.rSideObjs.append(value["rSide"])

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


    def updateDefControls(self, ctrlType, controlsList, defNames):
        # Delete current controls
        self.controlXforms = []
        # Store current values if guide controls already exist
        # for i, name in enumerate(["lipDeformers", "lipControls"]):
        current = 0
        for i, ctrl in enumerate(controlsList):
            self.controlXforms.append([ctrl.xfo])
            '''
            if ctrl.getParent() is self.mouthCtrl:
                self.controlXforms.append([ctrl.xfo])
                current = len(self.controlXforms) -1
            else:
                self.controlXforms[current].append(ctrl.xfo)
            '''

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]


        del self.refInputs[:]

        if ctrlType == "lipDeformers":
            parent = self.mouthCtrl
            defControlNameList = []

            #Build Deformer Names
            half = int(math.floor(defNames/2))
            rSideControls = []
            lSideControls =[]
            n=0
            for i in range(half):
                lSideControls.append('L_' + str(half-n))
                rSideControls.append('R_' + str(n+1))
                n += 1

            if not defNames % 2 == 0:
                defControlNameList = rSideControls + ['Mid'] + lSideControls
            else:
                defControlNameList = rSideControls + lSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="sphere")
                newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 5)))
                newCtrl.scalePoints(Vec3(.25,.25,.25))
                controlsList.append(newCtrl)

                j=0
                if i < len(self.controlXforms):
                    if j < len(self.controlXforms[i]):
                        newCtrl.xfo = self.controlXforms[i][j]


        if ctrlType == "lipControls":
            parent = self.midLipCtrl
            defControlNameList =[]

            # Lets build all new handles
            defControlNameList = convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True


            # etting up names
            lSideControls = ["L_" + x for x in defControlNameList]
            rSideControls = ["R_" + x for x in defControlNameList]

            defControlNameList = rSideControls +  ["Mid"] + lSideControls

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="circle")
                newCtrl.rotatePoints(90,0,0)
                newCtrl.setColor("blue")
                newCtrl.xfo = parent.xfo
                newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 8)))
                newCtrl.scalePoints(Vec3(.5,.5,.5))
                controlsList.append(newCtrl)


                j=0
                if i < len(self.controlXforms):
                    if j < len(self.controlXforms[i]):
                        newCtrl.xfo = self.controlXforms[i][j]


        for ctrl in controlsList:
            self.addToSymDict(ctrl)

        return True


    def updateDefNames(self, defNames):
        print "Callback running"
        self.updateDefControls("lipDeformers", self.defCtrls, defNames)
        print "in upDefNames; %s"%self.symMapping

    def updatelipCtrls(self, defNames):
        self.updateDefControls("lipControls", self.lipCtrls, defNames)


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """
        data = super(OSSLipGuide, self).saveData()

        data['midLipXfo'] = self.midLipCtrl.xfo
        data['L_midLipHandleXfo'] = self.L_midLipHandleCtrl.xfo
        data['R_midLipHandleXfo'] = self.R_midLipHandleCtrl.xfo

        data['upLipXfo'] = self.upLipCtrl.xfo
        data['L_upLipHandleXfo'] = self.L_upLipHandleCtrl.xfo
        data['R_upLipHandleXfo'] = self.R_upLipHandleCtrl.xfo

        data['loLipXfo'] = self.loLipCtrl.xfo
        data['L_loLipHandleXfo'] = self.L_loLipHandleCtrl.xfo
        data['R_loLipHandleXfo'] = self.R_loLipHandleCtrl.xfo

        data['mouthXfo'] = self.mouthCtrl.xfo

        data['lMouthXfo'] = self.lMouthCtrl.xfo
        data['rMouthXfo'] = self.rMouthCtrl.xfo
        data['mouthEndXfo'] = self.mouthEndCtrl.xfo

        data['lMouthOutXfo'] = self.lMouthOutCtrl.xfo
        data['rMouthOutXfo'] = self.rMouthOutCtrl.xfo

        for ctrlListName in ["defCtrls", "lipCtrls"]:
            ctrls = getattr(self, ctrlListName)
            xfos = []
            for i in xrange(len(ctrls)):
                xfos.append(ctrls[i].xfo)
            data[ctrlListName+"Xfos"] = xfos

        return data


    def loadData(self, data):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        #Reset all shapes, but really we should just recreate all controls from loadData instead of init
        # for ctrl in self.getAllHierarchyNodes(classType=Control):
        #     ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data


        super(OSSLipGuide, self).loadData( data )

        self.loLipCtrl.xfo = data['loLipXfo']
        self.L_loLipHandleCtrl.xfo = data['L_loLipHandleXfo']
        self.R_loLipHandleCtrl.xfo = data['R_loLipHandleXfo']

        self.upLipCtrl.xfo = data['upLipXfo']
        self.L_upLipHandleCtrl.xfo = data['L_upLipHandleXfo']
        self.R_upLipHandleCtrl.xfo = data['R_upLipHandleXfo']

        self.midLipCtrl.xfo = data['midLipXfo']
        self.L_midLipHandleCtrl.xfo = data['L_midLipHandleXfo']
        self.R_midLipHandleCtrl.xfo = data['R_midLipHandleXfo']

        self.lMouthCtrl.xfo = data['lMouthXfo']
        self.rMouthCtrl.xfo = data['rMouthXfo']
        self.lMouthOutCtrl.xfo = data['lMouthOutXfo']
        self.rMouthOutCtrl.xfo = data['rMouthOutXfo']

        self.mouthCtrl.xfo = data['mouthXfo']
        self.mouthEndCtrl.xfo = data['mouthEndXfo']

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec =Vec3(globalScale, globalScale, globalScale)

        self.midLipCtrl.scalePoints(globalScaleVec)

        for ctrlListName in ["defCtrls", "lipCtrls"]:
            ctrls = getattr(self, ctrlListName)
            if ctrlListName+"Xfos" in data.keys():
                for i in xrange(len(data[ctrlListName+"Xfos"])):
                    if i < len(ctrls):
                        ctrls[i].xfo = data[ctrlListName+"Xfos"][i]

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

        # UpVector
        mouthUpV= Xfo(Vec3(0.0, 1.0, 0.0)).tr

        rootToEnd = mouthEndPosition.subtract(mouthPosition).unit()

        rootToUpV = mouthUpV.subtract(mouthPosition).unit()
        bone1ZAxis = rootToUpV.cross(rootToEnd).unit()
        bone1Normal = bone1ZAxis.cross(rootToEnd).unit()

        mouthXfo = Xfo()
        mouthXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, mouthPosition)

        mouthLen = mouthPosition.subtract(mouthEndPosition).length()


        data = super(OSSLipGuide, self).getRigBuildData()




        data['mouthXfo'] = mouthXfo
        data['mouthLen'] = mouthLen
        data['lipCtrlCrvData'] = self.midLipCtrl.getCurveData()
        data['lipXfo'] = self.midLipCtrl.xfo
        data['midLipXfo'] = self.midLipCtrl.xfo
        data['lMouthXfo'] = self.lMouthCtrl.xfo
        data['rMouthXfo'] = self.rMouthCtrl.xfo
        data['lipCtrlCrvData'] = self.midLipCtrl.getCurveData()
        data['mouthEndXfo'] = self.mouthEndCtrl.xfo

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

        return OSSLipRig


class OSSLipRig(OSSLip):
    """Lip Component"""

    def __init__(self, name='Lip', parent=None):

        Profiler.getInstance().push("Construct Lip Rig Component:" + name)
        super(OSSLipRig, self).__init__(name, parent)

        # =========
        # Controls
        # =========
        # Mouth
        self.mouthCtrlSpace = CtrlSpace('mouth', parent=self.ctrlCmpGrp)
        self.mouthCtrl = Control('mouth', parent=self.mouthCtrlSpace, shape="square")
        self.mouthCtrl.alignOnXAxis()
        # Lip
        self.loLipCtrlSpace = CtrlSpace('midLip', parent=self.mouthCtrlSpace)
        self.loLipCtrl = Control('midLip', parent=self.loLipCtrlSpace, shape="square")
        self.loLipCtrl.alignOnXAxis()

        self.midLipCtrlSpace = CtrlSpace('loLip', parent=self.mouthCtrlSpace)
        self.midLipCtrl = Control('loLip', parent=self.midLipCtrlSpace, shape="square")
        self.midLipCtrl.alignOnXAxis()

        self.lMouthCtrlSpace = CtrlSpace('L_Mouth', parent=self.mouthCtrlSpace)
        self.lMouthCtrl = Control('L_Mouth', parent=self.lMouthCtrlSpace, shape="cube")

        self.rMouthCtrlSpace = CtrlSpace('R_Mouth', parent=self.mouthCtrlSpace)
        self.rMouthCtrl = Control('R_Mouth', parent=self.rMouthCtrlSpace, shape="cube")

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.ctrlCmpGrp.setComponent(self)

        # Mouth
        self.mouthDef = Joint('mouth', parent=self.defCmpGrp)
        self.mouthDef.setComponent(self)
        # Lip
        self.lipDef = Joint(self.getName(), parent=self.defCmpGrp)
        self.lipDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Mouth
        self.mouthInputConstraint = self.mouthCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.mouthConstraint = self.mouthOutputTgt.constrainTo(self.mouthCtrl, maintainOffset=False)
        self.mouthEndConstraint = self.mouthEndOutputTgt.constrainTo(self.mouthCtrl, maintainOffset=False)

        # Lip
        # lipInputConstraint = PoseConstraint('_'.join([self.midLipCtrl.getName(), 'To', self.parentSpaceInputTgt.getName()]))
        # lipInputConstraint.setMaintainOffset(True)
        # lipInputConstraint.addConstrainer(self.parentSpaceInputTgt)
        # self.midLipCtrlSpace.addConstraint(lipInputConstraint)

        # Constraint outputs
        lipConstraint = PoseConstraint('_'.join([self.lipOutputTgt.getName(), 'To', self.midLipCtrl.getName()]))
        lipConstraint.addConstrainer(self.midLipCtrl)
        self.lipOutputTgt.addConstraint(lipConstraint)


        # ===============
        # Add Splice Ops
        # ===============
        # Add Deformer Splice Op
        spliceOp = KLOperator('lipDeformerKLOp', 'PoseConstraintSolver', 'Kraken')
        self.addOperator(spliceOp)

        # Add Att Inputs
        spliceOp.setInput('drawDebug', self.drawDebugInputAttr)
        spliceOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        spliceOp.setInput('constrainer', self.lipOutputTgt)

        # Add Xfo Outputs
        spliceOp.setOutput('constrainee', self.lipDef)

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSLipRig, self).loadData( data )


        self.mouthCtrlSpace.xfo = data['mouthXfo']
        self.mouthCtrl.xfo = data['mouthXfo']
        self.mouthCtrl.rotatePoints(0.0, 0.0, 90.0)
        self.mouthCtrl.translatePoints(Vec3(Vec3(data['mouthLen'], -0.5 , 0.0)))



        self.lMouthCtrlSpace.xfo = data['lMouthXfo']
        self.lMouthCtrl.xfo = data['lMouthXfo']

        self.rMouthCtrlSpace.xfo = data['rMouthXfo']
        self.rMouthCtrl.xfo = data['rMouthXfo']
        # ============
        # Set IO Xfos
        # ============
        self.mouthEndOutputTgt.xfo = data['mouthXfo']
        self.mouthOutputTgt.xfo = data['mouthXfo']

        # Eval Constraints
        self.mouthConstraint.evaluate()
        self.mouthEndConstraint.evaluate()


        self.midLipCtrlSpace.xfo = data['lipXfo']
        self.midLipCtrl.xfo = data['lipXfo']
        self.midLipCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.midLipCtrl.scalePoints(Vec3(Vec3(1, .25,1)))
        self.midLipCtrl.translatePoints(Vec3(Vec3(-0.5 ,1, 0)))

        self.loLipCtrlSpace.xfo = data['lipXfo']
        self.loLipCtrl.xfo = data['lipXfo']
        self.loLipCtrl.rotatePoints(90.0, 0.0, 0.0)
        self.loLipCtrl.scalePoints(Vec3(Vec3(1, .25,1)))
        self.loLipCtrl.translatePoints(Vec3(Vec3(-0.5 ,-1,  0)))

        globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])
        self.midLipCtrl.scalePoints(globalScale)
        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['lipXfo']
        self.lipOutputTgt.xfo = data['lipXfo']


def convertToStringList(inputString):
    """ tokenizes string argument, returns a list"""
    stringList = re.split(r'[ ,:;]+', inputString)

    # These checks should actually prevent the component_inspector from closing maybe?
    for name in stringList:
        if name and not re.match(r'^[\w_]+$', name):
            # Eventaully specific exception just for component class that display component name, etc.
            raise ValueError("inputString \""+name+"\" contains non-alphanumeric characters in component \""+self.getName()+"\"")

    stringList = [x for x in stringList if x != ""]

    if not stringList:
        return []

    if len(stringList) > len(set(stringList)):
        raise ValueError("Duplicate names in inputString in component \""+self.getName()+"\"")

    return stringList

def convertToScalarList(inputString):
    """ tokenizes string argument, returns a list"""
    stringList = re.split(r'[ ,:;]+', inputString)
    scalarList = []
    # These checks should actually prevent the component_inspector from closing maybe?
    for name in stringList:
        if name:
            try:
                scalarList.append(float(name))
            except ValueError:
                raise ValueError("inputString \""+name+"\" cannot be converted to float: \""+self.getName()+"\"")


    # scalarList = [x for x in scalarList if x != ""]

    if not scalarList:
        return []

    if len(scalarList) > len(set(scalarList)):
        raise ValueError("Duplicate names in inputString in component \""+self.getName()+"\"")

    return scalarList


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSLipGuide)
ks.registerComponent(OSSLipRig)
