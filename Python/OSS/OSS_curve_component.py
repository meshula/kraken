
import math, re
from kraken.core.maths import Xfo, Vec3
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import ROT_ORDER_STR_TO_INT_MAP

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
# from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "Curve"

class OSSCurveComponent(OSS_Component):
    """Curve Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSCurveComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========

        self.contstrainFirstControl_cmpIn = None
        # Declare Output Xfos
        self.curveBaseOutputTgt = self.createOutput('curveBase', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.CurveEndOutputTgt = self.createOutput('CurveEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.CurveVertebraeOutput = self.createOutput('CurveVertebrae', dataType='Xfo[]')



class OSSCurveComponentGuide(OSSCurveComponent):
    """Curve Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Curve Guide Component:" + name)
        super(OSSCurveComponentGuide, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        # =========
        # Controls
        # ========
        self.name = name
        self.curveCtrlNames = StringAttribute('curveCtrlNames', value="A B C D", parent=self.guideSettingsAttrGrp)
        self.numDeformersAttr = IntegerAttribute('numDeformers', value=6, minValue=0, maxValue=99, parent=self.guideSettingsAttrGrp)
        self.popFirst = BoolAttribute('popFirst', value=False,  parent=self.guideSettingsAttrGrp)
        self.popFirst = BoolAttribute('popLast', value=False, parent=self.guideSettingsAttrGrp)
        self.exposeControls = BoolAttribute('exposeControls', value=True, parent=self.guideSettingsAttrGrp)
        self.tweakControls = BoolAttribute('tweakControls', value=False, parent=self.guideSettingsAttrGrp)
        self.controlSizeTaper = ScalarAttribute('controlSizeTaper', 0.0, maxValue=1.0, minValue=-1.0, parent=self.guideSettingsAttrGrp)
        self.controlHierarchy = BoolAttribute('controlHierarchy', value=True, parent=self.guideSettingsAttrGrp)
        self.contstrainFirstControlInput = BoolAttribute('contstrainFirstControl', value=False, parent=self.guideSettingsAttrGrp)
        self.removeFirstControlInput = BoolAttribute('removeFirstControl', value=False, parent=self.guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        # Guide Controls

        self.controlInputs = []
        self.curveCtrlNames.setValueChangeCallback(self.updateCurveCtrls)

        self.contstrainFirstControlInput.setValueChangeCallback(self.updateContstrainFirstControl)
        # self.removeFirstControlInput.setValueChangeCallback(self.removeFirstControl)

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

        if ctrlType == "curveControls":
            parent = self.ctrlCmpGrp
            defControlNameList =[]

            # Lets build all new handles
            controls = self.convertToStringList(defNames)
            defControlNameList = controls
            if not defControlNameList:  # Nothing to build
                return True


            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="circle")
                newCtrl.setColor("brown")
                newCtrl.xfo = parent.xfo.multiply(Xfo(tr=Vec3(0, i, 0)))
                newCtrl.scalePoints(self.globalScaleVec)
                controlsList.append(newCtrl)
        return True


    def updateDefNames(self, defNames):
        self.createGuideControls("curveDeformers", self.defCtrls, defNames)


    def updateCurveCtrls(self, defNames):
        self.createGuideControls("curveControls", self.controlInputs, defNames)



    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """

        data = super(OSSCurveComponentGuide, self).saveData()

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


        super(OSSCurveComponentGuide, self).loadData( data )

        self.loadAllObjectData(data, "Control")
        self.loadAllObjectData(data, "Transform")

        return True




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


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig.

        Return:
        The JSON rig data object.

        """

        data = super(OSSCurveComponentGuide, self).getRigBuildData()

        # should include getCurveData
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

        return OSSCurveComponentRig


class OSSCurveComponentRig(OSSCurveComponent):
    """Curve Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Curve Rig Component:" + name)
        super(OSSCurveComponentRig, self).__init__(name, parent)

        # ==========
        # Deformers
        # ==========

        self.name = name
        self.deformerJoints = []

        self.controlInputs = []
        self.controlRestInputs = []

        self.curveOutputs = []
        self.params = []
        self.rigControlAligns = []
        #self.setNumDeformers(1)

        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.CurveVertebraeOutput.setTarget(self.curveOutputs)


        # ===============
        # Add Fabric Ops
        # ===============
        # Add Curve Canvas Op

        self.NURBSCurveKLOp = KLOperator('curve', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.NURBSCurveKLOp)

        self.NURBSCurveKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.NURBSCurveKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.NURBSCurveKLOp.setInput('alignX', 1 )
        self.NURBSCurveKLOp.setInput('alignY', 2 )
        self.NURBSCurveKLOp.setInput('alignZ', 3 )
        self.NURBSCurveKLOp.setInput('degree', 3)
        self.NURBSCurveKLOp.setInput('keepArcLength', 0.0)
        self.NURBSCurveKLOp.setInput('compressionAmt', 0.5)
        self.NURBSCurveKLOp.setInput('followCurveTangent', 1.0)
        self.NURBSCurveKLOp.setInput('useLocalNormal', 1.0)
        self.NURBSCurveKLOp.setInput('followCurveNormal', 1.0)
        self.NURBSCurveKLOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.NURBSCurveKLOp.setInput('parent', self.parentSpaceInputTgt)
        self.NURBSCurveKLOp.setInput('atVec', self.ctrlCmpGrp) # atVec should be optional, but is not currently in the Solver
        self.NURBSCurveKLOp.setInput('controlAligns', self.rigControlAligns)
        self.NURBSCurveKLOp.setInput('controls', self.controlInputs)
        self.NURBSCurveKLOp.setInput('controlsRest', self.controlRestInputs)
        self.NURBSCurveKLOp.setInput('params', self.params )

        self.NURBSCurveKLOp.setOutput('outputs', self.curveOutputs)



        Profiler.getInstance().pop()


    def createControls(self, ctrlType, controlsList, defNames, data):

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        parent = self.ctrlCmpGrp
        self.exposeControls = bool(data['exposeControls'])  #This should be a simple method instead
        self.tweakControls = bool(data['tweakControls'])  #This should be a simple method instead
        self.controlHierarchy = bool(data['controlHierarchy'])  #This should be a simple method instead


        if ctrlType == "curveDeformers":
            defControlNameList = []

            #Build Deformer Names
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True

            for i, defName in enumerate(defControlNameList):
                newCtrl = Locator(self.name + defName + "_" + ctrlType.replace("Def",""), parent= self.ctrlCmpGrp)
                newCtrl.setShapeVisibility(False)
                controlsList.append(newCtrl)

                newDef = Joint(self.name + defName + "_" + ctrlType.replace("Def",""), parent= self.mouthDef)
                newDef.setComponent(self)
                newDef.constrainTo(newCtrl)

        if ctrlType == "curveControls":

            defControlNameList =[]

            # Lets build all new handles
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True

            for i, defName in enumerate(defControlNameList):

                if self.controlHierarchy and len(controlsList):
                    parent = controlsList[-1]

                if self.exposeControls:
                    newCtrl = Control(self.name + defName, parent=parent, shape="squarePointed")
                    newCtrl.setColor("red")
                else:
                    newCtrl = Transform(self.name + defName, parent=parent)

                newCtrl.xfo = data[defName + "Xfo"]
                controlsList.append(newCtrl)

        return controlsList


    def fillValues(self, numDefs, minVal=0.0, maxVal=1.0, popFirst=False, popLast=False):
        params = []
        if numDefs == 1:
            return [0.5]
        for i in range(numDefs):
            ratio = float(i) / float(numDefs-1)
            params.append((1.0-ratio)*minVal + ratio*maxVal)
        if popFirst and (len(params) > 1):
            del params[0]
        if popLast and (len(params) > 1):
            del params[-1]
        return params

    def setNumDeformers(self, numDeformers, data):
        for output in reversed(self.curveOutputs):
            output.getParent().removeChild(output)
        del self.curveOutputs[:] #Clear since this array obj is tied to output already

        for joint in reversed(self.deformerJoints):
            joint.getParent().removeChild(joint)
        del self.deformerJoints[:] #Clear since this array obj is tied to output already

        # Determine params for number of Deformers
        self.popFirst = bool(data['popFirst'])  #This should be a simple method instead
        self.popLast = bool(data['popLast'])  #This should be a simple method instead

        self.params = self.fillValues(numDeformers, minVal=0.0, maxVal=1.0, popFirst=self.popFirst, popLast=self.popLast)


        numDeformers = len(self.params)


        # Add new deformers and outputs
        for i in xrange(len(self.curveOutputs), numDeformers):
            name = 'Curve' + str(i).zfill(2)
            #Need dynamic ports branch to be able to see this updated in Graph
            CurveOutput = self.createOutput(name, dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            self.curveOutputs.append(CurveOutput)

        parent = self.deformersParent
        for i in xrange(len(self.deformerJoints), numDeformers):
            if i != 0:
                parent = self.deformerJoints[-1]
            name = str(i).zfill(2)
            CurveDef = Joint(self.name + name, parent=parent)
            CurveDef.setComponent(self)
            self.deformerJoints.append(CurveDef)
            if i == 0:
                self.parentSpaceInputTgt.childJoints = [CurveDef]

        if hasattr(self, 'NURBSCurveKLOp'):  # Check in case this is ever called from Guide callback
            self.NURBSCurveKLOp.setInput('params',  self.params)

        return True


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSCurveComponentRig, self).loadData( data )

        numDeformers = data['numDeformers']

        self.controlInputs = self.createControls("curveControls", self.controlInputs, data["curveCtrlNames"], data)

        self.globalScaleVec = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers, data)

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.firstCurveCtrl = self.controlInputs[0].getParent()

        for i in xrange(len(self.controlInputs)):
            self.controlRestInputs.append(self.controlInputs[i].xfo)


        if self.controlInputs:
            # build control hierarchy
            numCtrls = len(self.controlInputs)
            taperRatio = float(data['controlSizeTaper'])/(numCtrls-1)
            for i in range(numCtrls):
                ctrl = self.controlInputs[i]
                if ctrl.getTypeName() != "Transform":
                    ctrl.scalePoints(self.globalScaleVec)
                    ctrl.scalePoints(Vec3(1 - i*taperRatio, 1 - i*taperRatio, 1 - i*taperRatio))
                    ctrl.setColor("gold")
                    ctrlParent = ctrl.insertCtrlSpace()
                else:
                    ctrlParent = ctrl
                #this is for a curve only solution
                if not self.controlHierarchy or i ==0:
                    ctrlParent.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
                self.rigControlAligns.append(Vec3(1,2,3))
        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.evalOperators()
        self.NURBSCurveKLOp.evaluate()

        for i in xrange(len(self.curveOutputs)):
            constraint = self.deformerJoints[i].constrainTo(self.curveOutputs[i])
            constraint.evaluate()
        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important



        # evaluate the constraint op so that all the joint transforms are updated.I s
        self.curveBaseOutputConstraint =  self.curveBaseOutputTgt.constrainTo(self.curveOutputs[0])
        self.CurveEndOutputConstraint  =  self.CurveEndOutputTgt.constrainTo(self.curveOutputs[-1])


        if data["contstrainFirstControl"]:
            self.contstrainFirstControl_cmpIn = self.createInput('firstControlXfo', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
            self.controlInputs[0].removeAllConstraints()
            self.controlInputs[0].constrainTo(self.contstrainFirstControl_cmpIn, maintainOffset=True)

        # # ====================
        # # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # # ====================
        # # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.curveBaseOutputConstraint.evaluate()
        self.CurveEndOutputConstraint.evaluate()

        self.curveBaseOutputTgt.parentJoint = self.deformerJoints[0]
        # self.curveEndOutputTgt.parentJoint  = self.deformerJoints[-1]

        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


        # ====================
        # Extra Shape Mods
        # ====================
        # JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        # globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.tagJointsWithPartNames([self.getDecoratedName()])




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSCurveComponentGuide)
ks.registerComponent(OSSCurveComponentRig)
