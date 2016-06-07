
import math, re
from kraken.core.maths import Vec3
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.euler import rotationOrderStrToIntMapping

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

        # Declare Output Xfos
        self.firstOutputTgt = self.createOutput('hips', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.pelvisOutputTgt = self.createOutput('pelvis', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.CurveEndOutputTgt = self.createOutput('CurveEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        self.CurveVertebraeOutput = self.createOutput('CurveVertebrae', dataType='Xfo[]')



class OSSCurveComponentGuide(OSSCurveComponent):
    """Curve Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Curve Guide Component:" + name)
        super(OSSCurveComponentGuide, self).__init__(name, parent)

        # =========
        # Controls
        # ========
        self.curveCtrlNames = StringAttribute('curveCtrlNames', value="Pelvis Torso Chest UpChest", parent=self.guideSettingsAttrGrp)
        self.numDeformersAttr = IntegerAttribute('numDeformers', value=6, minValue=0, maxValue=99, parent=self.guideSettingsAttrGrp)
        #self.numDeformersAttr.setValueChangeCallback(self.updateNumDeformers)  # Unnecessary unless changing the guide rig objects depending on num joints
        # Guide Controls

        self.curveCtrls = []
        self.curveDeformers = []
        self.curveCtrlNames.setValueChangeCallback(self.updateCurveCtrls)


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
                newCtrl.setColor("brownMuted")
                newCtrl.xfo = parent.xfo
                # newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 8)))
                # newCtrl.scalePoints(Vec3(.5,.5,.5))
                controlsList.append(newCtrl)
        return True


    def updateDefNames(self, defNames):
        self.createGuideControls("curveDeformers", self.defCtrls, defNames)


    def updateCurveCtrls(self, defNames):
        self.createGuideControls("curveControls", self.curveCtrls, defNames)



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

        globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        globalScaleVec = Vec3(globalScale, globalScale, globalScale)

        return True



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

        self.deformerJoints = []

        self.controlInputs = []
        self.controlRestInputs = []

        self.CurveOutputs = []
        self.params = []
        self.rigControlAligns = []
        #self.setNumDeformers(1)

        self.curveCtrls = []
        self.curveDeformers = []
        # =====================
        # Create Component I/O
        # =====================
        # Setup component Xfo I/O's
        self.CurveVertebraeOutput.setTarget(self.CurveOutputs)


        # ===============
        # Add Fabric Ops
        # ===============
        # Add Curve Canvas Op

        self.NURBSCurveKLOp = KLOperator('NURBSCurveKLOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(self.NURBSCurveKLOp)

        self.NURBSCurveKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.NURBSCurveKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.NURBSCurveKLOp.setInput('alignX', 1 )
        self.NURBSCurveKLOp.setInput('alignY', 2 )
        self.NURBSCurveKLOp.setInput('alignZ', 3 )
        self.NURBSCurveKLOp.setInput('degree', 3)
        self.NURBSCurveKLOp.setInput('keepArcLength', 0.0)
        self.NURBSCurveKLOp.setInput('compressionAmt', 0.4)
        self.NURBSCurveKLOp.setInput('followCurveTangent', 0.0)
        self.NURBSCurveKLOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        self.NURBSCurveKLOp.setInput('parent', self.ctrlCmpGrp)
        self.NURBSCurveKLOp.setInput('atVec', self.ctrlCmpGrp) # atVec should be optional, but is not currently in the Solver
        self.NURBSCurveKLOp.setInput('controlAligns', self.rigControlAligns)
        self.NURBSCurveKLOp.setInput('controls', self.curveCtrls)
        self.NURBSCurveKLOp.setInput('controlsRest', self.controlRestInputs)
        self.NURBSCurveKLOp.setInput('params', self.params )

        self.NURBSCurveKLOp.setOutput('outputs', self.CurveOutputs)



        Profiler.getInstance().pop()


    def createControls(self, ctrlType, controlsList, defNames, data):

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        parent = self.ctrlCmpGrp

        if ctrlType == "curveDeformers":
            defControlNameList = []

            #Build Deformer Names
            defControlNameList = self.convertToStringList(defNames)
            if not defControlNameList:  # Nothing to build
                return True

            for i, defName in enumerate(defControlNameList):
                newCtrl = Locator(defName + "_" + ctrlType.replace("Def",""), parent= self.ctrlCmpGrp)
                newCtrl.setShapeVisibility(False)
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

            for i, defName in enumerate(defControlNameList):
                newCtrl = Control(defName, parent=parent, shape="squarePointed")
                newCtrl.setColor("red")
                newCtrl.xfo = data[defName + "Xfo"]
                controlsList.append(newCtrl)

        return controlsList


    def setNumDeformers(self, numDeformers):

        for output in reversed(self.CurveOutputs):
            output.getParent().removeChild(output)
        del self.CurveOutputs[:] #Clear since this array obj is tied to output already

        for joint in reversed(self.deformerJoints):
            joint.getParent().removeChild(joint)
        del self.deformerJoints[:] #Clear since this array obj is tied to output already

        # Add new deformers and outputs
        for i in xrange(len(self.CurveOutputs), numDeformers):
            name = 'Curve' + str(i).zfill(2)
            #Need dynamic ports branch to be able to see this updated in Graph
            CurveOutput = self.createOutput(name, dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            self.CurveOutputs.append(CurveOutput)

        parent = self.deformersParent
        for i in xrange(len(self.deformerJoints), numDeformers):
            if i != 0:
                parent = self.deformerJoints[-1]
            name = 'Curve' + str(i).zfill(2)
            CurveDef = Joint(name, parent=parent)
            CurveDef.setComponent(self)
            self.deformerJoints.append(CurveDef)
            if name == "pelvis":
                self.parentSpaceInputTgt.childJoints = [CurveDef]


        # Determine params for number of Deformers
        a = 0.0
        b = 1.0
        for i in range(numDeformers):
            print i
            ratio = float(i) / float(numDeformers-1)
            self.params.append((1.0-ratio)*a + ratio*b)
            self.rigControlAligns.append(Vec3(1,2,3))

        print self.params
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

        self.curveDeformers = []
        print data
        self.curveCtrls = self.createControls("curveControls", self.curveCtrls, data["curveCtrlNames"], data)

        # self.curveDeformers = self.createGuideControls("curveDeformers", self.curveDeformers, data["numDeformers"])

        # Update number of deformers and outputs
        self.setNumDeformers(numDeformers)

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.firstCurveCtrl = self.curveCtrls[0].getParent()
        # self.firstCtrlSpaceConstraint  = self.firstCurveCtrl.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        print "curveCtrls: %s "%(len(self.curveCtrls))
        for i in range(len(self.curveCtrls)):
            self.controlRestInputs.append(self.curveCtrls[i].xfo)

        if self.curveCtrls:
            # build control hierarchy
            numCtrls = len(self.curveCtrls)

            for i in range(numCtrls):
                ctrl = self.curveCtrls[i]
                ctrl.setColor("yellowMuted")
                ctrlParent = ctrl.insertCtrlSpace()



        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()
        self.NURBSCurveKLOp.evaluate()

        # evaluate the constraint op so that all the joint transforms are updated.
        for i in xrange(len(self.CurveOutputs)):
            constraint = self.deformerJoints[i].constrainTo(self.CurveOutputs[i])
            constraint.evaluate()
            
        # Constrain Outputs
        # self.CurveEndOutputConstraint = self.CurveEndOutputTgt.constrainTo(self.CurveOutputs[-1])


        # # ====================
        # # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # # ====================
        # # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        # self.firstCtrlSpaceConstraint.evaluate()
        # self.hipsOutputConstraint.evaluate()
        # #self.CurveBaseOutputConstraint.evaluate()
        # #self.pelvisOutputConstraint.evaluate()
        # self.CurveEndOutputConstraint.evaluate()

        # self.firstOutputTgt.parentJoint = self.deformerJoints[0]
        # self.pelvisOutputTgt.parentJoint = self.deformerJoints[0]
        # self.CurveEndOutputTgt.parentJoint = self.deformerJoints[-1]

        # Don't eval *input* constraints because they should all have maintainOffset on and get evaluated at the end during build()


        # ====================
        # Extra Shape Mods
        # ====================
        # JSON data at this point is generated by guide rig and passed to this rig, should include all defaults+loaded info
        # globalScale = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])





from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSCurveComponentGuide)
ks.registerComponent(OSSCurveComponentRig)
