from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV, aimAt
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import *

from kraken.core.objects.components.base_example_component import BaseExampleComponent

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.string_attribute import StringAttribute

from kraken.core.objects.constraints.pose_constraint import PoseConstraint

from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.hierarchy_group import HierarchyGroup
from kraken.core.objects.transform import Transform
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component


COMPONENT_NAME = "shoulder"

class OSSShoulderComponent(OSS_Component):
    """Shoulder Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None, data=None):
        super(OSSShoulderComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.shldrOutputTgt = self.createOutput('shldr', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.shldrEndOutputTgt = self.createOutput('shldrEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs

class OSSShoulderComponentGuide(OSSShoulderComponent):
    """Shoulder Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Shoulder Guide Component:" + name)
        super(OSSShoulderComponentGuide, self).__init__(name, parent)


         # Guide Settings
        #self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
        self.mocapInputAttr = None


        # =========
        # Controls
        # =========
        # Guide Controls

        self.shldrCtrl = FKControl('shldr', parent=self.ctrlCmpGrp, shape="sphere")
        self.shldrUpVCtrl = Control('shldrUpV', parent=self.ctrlCmpGrp, shape="triangle")
        self.shldrUpVCtrl.setColor('red')
        self.shldrEndCtrl = Control('shldrEnd', parent=self.ctrlCmpGrp, shape="sphere")

        data = {
                "name": name,
                "location": "L",
                "shldrXfo": Xfo(Vec3(0.1322, 15.403, -0.5723)),
                "shldrUpVXfo": Xfo(Vec3(0.0, 1.0, 0.0)),
                "shldrEndXfo": Xfo(Vec3(2.27, 15.295, -0.753))
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

        data = super(OSSShoulderComponentGuide, self).saveData()

        data['shldrXfo'] = self.shldrCtrl.xfo
        data['shldrUpVXfo'] = self.shldrUpVCtrl.xfo
        data['shldrEndXfo'] = self.shldrEndCtrl.xfo

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

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSShoulderComponentGuide, self).loadData( data )

        self.shldrCtrl.xfo = data['shldrXfo']
        self.shldrUpVCtrl.xfo = data['shldrUpVXfo']
        self.shldrEndCtrl.xfo = data['shldrEndXfo']

        return True


    def updateMocap(self, mocap):
        """ Callback to changing the component setting 'useOtherIKGoalInput'
        Really, we should build this ability into the system, to add/remove input attrs based on guide setting bools.
        That way, we don't have to write these callbacks.
        """
        if mocap:
            if self.mocapInputAttr is None:
                self.mocapInputAttr = self.createInput('mocap', dataType='Float', parent=self.cmpInputAttrGrp)
                self.mocap = True

        else:
            if self.mocapInputAttr is not None:
                self.deleteInput('mocap', parent=self.cmpInputAttrGrp)
                self.mocapInputAttr = None
                self.mocap = False


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSShoulderComponentGuide, self).getRigBuildData()

        self.boneAxisStr = "POSX"
        if self.getLocation() == 'R':
            self.boneAxisStr = "NEGX"
        self.boneAxis = AXIS_NAME_TO_TUPLE_MAP[self.boneAxisStr]

        self.upAxisStr = "NEGY"
        if self.getLocation() == 'R':
            self.upAxisStr = "POSY"
        self.upAxis = AXIS_NAME_TO_TUPLE_MAP[self.upAxisStr]


        # Values
        shldrPosition = self.shldrCtrl.xfo.tr

        shldrUpV = self.shldrUpVCtrl.xfo.tr
        shldrEndPosition = self.shldrEndCtrl.xfo.tr


        shldrXfo = Xfo(self.shldrCtrl.xfo)
        aimAt(shldrXfo, aimPos=self.shldrEndCtrl.xfo.tr, upVector=shldrUpV, aimAxis=self.boneAxis, upAxis=self.upAxis)

        shldrEndXfo = Xfo(self.shldrEndCtrl.xfo)
        shldrEndXfo.ori = shldrEndXfo.ori = shldrXfo.ori

        shldrLen = shldrXfo.tr.subtract(shldrEndXfo.tr).length()

        data['shldrXfo'] = shldrXfo
        data['shldrLen'] = shldrLen
        data['shldrEndXfo'] = shldrEndXfo


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

        return OSSShoulderComponentRig


class OSSShoulderComponentRig(OSSShoulderComponent):
    """Shoulder Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Shoulder Rig Component:" + name)
        super(OSSShoulderComponentRig, self).__init__(name, parent)

        self.mocap = False

        # =========
        # Controls
        # =========
        # Shoulder
        self.shldrCtrl = FKControl('shldr', parent=self.ctrlCmpGrp, shape="square")
        self.shldrCtrl.ro = RotationOrder(ROT_ORDER_STR_TO_INT_MAP["YXZ"])  #Set with component settings later
        self.shldrCtrlSpace = self.shldrCtrl.insertCtrlSpace()


        self.shldrEndCtrlSpace = CtrlSpace('shldrEnd', parent=self.shldrCtrl)

        # ==========
        # Deformers
        # ==========

        self.ctrlCmpGrp.setComponent(self)

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        self.shldrSpaceCtrlConstraint = self.shldrCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)



        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """


        super(OSSShoulderComponentRig, self).loadData(data)


        self.mocap = bool(data["mocap"])

        self.shldrDef = Joint('shldr', parent=self.deformersParent)
        self.shldrDef.setComponent(self)

        self.parentSpaceInputTgt.childJoints = [self.shldrDef]

        self.shldrOutputTgt.parentJoint = self.shldrDef
        self.shldrEndOutputTgt.parentJoint = self.shldrDef # only one joint option

        self.globalScale = data['globalComponentCtrlSize']
        self.globalScaleVec = Vec3(data['globalComponentCtrlSize'], data['globalComponentCtrlSize'], data['globalComponentCtrlSize'])

        self.shldrCtrlSpace.xfo = data['shldrXfo']
        self.shldrCtrl.xfo = data['shldrXfo']
        xoffset = 2*self.globalScale
        yoffset = -5.0*self.globalScale
        shldrWidth = 4.0*self.globalScale
        if self.getLocation() == 'R':
            xoffset *= -1
            yoffset *= -1

        self.shldrCtrl.alignOnXAxis(self.getLocation() == 'R')
        self.shldrCtrl.scalePoints(Vec3(data['shldrLen'], shldrWidth, shldrWidth))
        self.shldrCtrl.translatePoints(Vec3(xoffset, yoffset, 0.0))
        self.shldrEndCtrlSpace.xfo = data['shldrEndXfo']

        # ============
        # Set IO Xfos
        # ============
        self.shldrEndOutputTgt.xfo = data['shldrXfo']
        self.shldrOutputTgt.xfo = data['shldrXfo']


        if self.mocap:
            self.mocapInputAttr = self.createInput('mocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()

            self.shldrMocapCtrl = MCControl('shldr', parent=self.ctrlCmpGrp, shape="circle")
            self.shldrMocapCtrl.scalePoints(Vec3(5.0, 5.0, 5.0))
            self.shldrMocapCtrl.rotatePoints(0.0, 0.0, 90.0)
            self.shldrMocapCtrl.setColor("mediumpurple")
            self.shldrMocapCtrl.xfo = data['shldrXfo']
            self.shldrMocapCtrlSpace = self.shldrMocapCtrl.insertCtrlSpace()

            self.shldrMocapCtrlSpaceConstraint = self.shldrMocapCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

            self.shdlrEndMocapSpaceCtrl = CtrlSpace('shdlrEnd', parent=self.shldrMocapCtrl)
            self.shdlrEndMocapSpaceCtrl.xfo = data['shldrEndXfo']

            self.mocapHierBlendSolver = KLOperator(self.getName()+'mocap', 'OSS_HierBlendSolver', 'OSS_Kraken')
            self.addOperator(self.mocapHierBlendSolver)
            self.mocapHierBlendSolver.setInput('blend', self.mocapInputAttr)  # connect this to attr
            # Add Att Inputs
            self.mocapHierBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
            self.mocapHierBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
            # Add Xfo Inputs
            self.mocapHierBlendSolver.setInput('hierA',
                [
                self.shldrCtrl,
                self.shldrEndCtrlSpace
                ],
            )

            self.mocapHierBlendSolver.setInput('hierB',
                [
                self.shldrMocapCtrl,
                self.shdlrEndMocapSpaceCtrl,
                ]
            )
            #Create some nodes just for the oupt of the blend.
            #Wish we could just make direct connections....

            self.shldrMocap_link = Transform('shldrMocap_link', parent=self.outputHrcGrp)
            self.shdlrEndMocapSpaceCtrl_link = Transform('shdlrEndMocapSpaceCtrl_link', parent=self.outputHrcGrp)

            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.shldrMocap_link,
                self.shdlrEndMocapSpaceCtrl_link,
                ]
            )
            self.shldrOutputTgtConstraint = self.shldrOutputTgt.constrainTo(self.shldrMocap_link)
            self.shldrEndOutputTgtConstraint = self.shldrEndOutputTgt.constrainTo(self.shdlrEndMocapSpaceCtrl_link)
        else:
            self.shldrOutputTgtConstraint = self.shldrOutputTgt.constrainTo(self.shldrCtrl)
            self.shldrEndOutputTgtConstraint = self.shldrEndOutputTgt.constrainTo(self.shldrEndCtrlSpace)

        # ====================
        # Evaluate Fabric Ops
        # ====================
        # Eval Operators # Order is important
        self.evalOperators()


        # ====================
        # Evaluate Output Constraints (needed for building input/output connection constraints in next pass)
        # ====================
        # Evaluate the *output* constraints to ensure the outputs are now in the correct location.
        self.shldrOutputTgtConstraint.evaluate()
        self.shldrEndOutputTgtConstraint.evaluate()

        self.shldrDef.constrainTo(self.shldrOutputTgt).evaluate()

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSShoulderComponentGuide)
ks.registerComponent(OSSShoulderComponentRig)