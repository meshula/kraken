from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo

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

COMPONENT_NAME = "shoulder"

class OSSShoulderComponent(BaseExampleComponent):
    """Shoulder Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None, data=None):
        super(OSSShoulderComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.shldrOutputTgt = self.createOutput('shldr', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.shldrEndOutputTgt = self.createOutput('shldrEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()
        self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=self.getLocation() is 'R', parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSShoulderComponentGuide(OSSShoulderComponent):
    """Shoulder Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Shoulder Guide Component:" + name)
        super(OSSShoulderComponentGuide, self).__init__(name, parent)


         # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.mocapAttr.setValueChangeCallback(self.updateMocap, updateNodeGraph=True, )
        self.mocapInputAttr = None

        # =========
        # Controls
        # =========
        # Guide Controls

        self.shldrCtrl = Control('shldr', parent=self.ctrlCmpGrp, shape="sphere")
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
        for ctrl in self.getAllHierarchyNodes(classType=Control):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSShoulderComponentGuide, self).loadData( data )

        self.shldrCtrl.xfo = data['shldrXfo']
        self.shldrUpVCtrl.xfo = self.shldrCtrl.xfo.multiply(data['shldrUpVXfo'])
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

        else:
            if self.mocapInputAttr is not None:
                self.deleteInput('mocap', parent=self.cmpInputAttrGrp)
                self.mocapInputAttr = None


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSShoulderComponentGuide, self).getRigBuildData()

        # Values
        shldrPosition = self.shldrCtrl.xfo.tr

        shldrUpV = self.shldrUpVCtrl.xfo.tr
        shldrEndPosition = self.shldrEndCtrl.xfo.tr


        # Calculate Shoulder Xfo
        rootToEnd = shldrEndPosition.subtract(shldrPosition).unit()
        rootToUpV = shldrUpV.subtract(shldrPosition).unit()
        bone1ZAxis = rootToUpV.cross(rootToEnd).unit()
        bone1Normal = bone1ZAxis.cross(rootToEnd).unit()

        shldrXfo = Xfo()
        shldrXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, shldrPosition)

        shldrEndXfo = Xfo(shldrXfo)
        shldrEndXfo.tr = shldrEndPosition

        shldrLen = shldrPosition.subtract(shldrEndPosition).length()

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
        self.shldrCtrlSpace = CtrlSpace('shldr', parent=self.ctrlCmpGrp)
        self.shldrCtrl = Control('shldr', parent=self.shldrCtrlSpace, shape="square")
        self.shldrCtrl.alignOnXAxis()

        self.shldrEndCtrlSpace = CtrlSpace('shldrEnd', parent=self.shldrCtrl)

        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.ctrlCmpGrp.setComponent(self)

        self.shldrDef = Joint('shldr', parent=defCmpGrp)
        self.shldrDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs

        self.shldrCtrlConstraint = self.shldrCtrl.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

        # ===============
        # Add Splice Ops
        # ===============
        # Add Deformer Splice Op
        spliceOp = KLOperator('shldrDeformerKLOp', 'PoseConstraintSolver', 'Kraken')
        self.addOperator(spliceOp)

        # Add Att Inputs
        spliceOp.setInput('drawDebug', self.drawDebugInputAttr)
        spliceOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        spliceOp.setInput('constrainer', self.shldrOutputTgt)

        # Add Xfo Outputs
        spliceOp.setOutput('constrainee', self.shldrDef)

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """


        super(OSSShoulderComponentRig, self).loadData( data )


        self.mocap = bool(data["mocap"])

        self.shldrCtrlSpace.xfo = data['shldrXfo']
        self.shldrCtrl.xfo = data['shldrXfo']
        xoffset = 2
        self.shldrCtrl.scalePoints(Vec3(data['shldrLen'], 4, 4))

        self.shldrCtrl.translatePoints(Vec3(xoffset, -5.0, 0.0))

        self.shldrEndCtrlSpace.xfo = data['shldrEndXfo']

        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['shldrXfo']
        self.shldrEndOutputTgt.xfo = data['shldrXfo']
        self.shldrOutputTgt.xfo = data['shldrXfo']


        if self.mocap:
            self.mocapInputAttr = self.createInput('mocap', dataType='Float', value=0.0, minValue=0.0, maxValue=1.0, parent=self.cmpInputAttrGrp).getTarget()

            self.shldrMocapCtrl = Control('shldr_mocap', parent=self.ctrlCmpGrp, shape="circle")
            self.shldrMocapCtrl.scalePoints(Vec3(5.0, 5.0, 5.0))
            self.shldrMocapCtrl.setColor("purpleLight")
            self.shldrMocapCtrl.xfo = data['shldrXfo']
            self.shldrMocapCtrlSpace = self.shldrMocapCtrl.insertCtrlSpace()

            self.shldrMocapCtrlSpaceConstraint = self.shldrMocapCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)

            self.shdlrEndMocapSpaceCtrl = CtrlSpace('shdlrEnd_mocap', parent=self.shldrMocapCtrl)
            self.shdlrEndMocapSpaceCtrl.xfo = data['shldrEndXfo']

            self.mocapHierBlendSolver = KLOperator(self.getLocation()+self.getName()+'mocap_HierBlendSolver', 'OSS_HierBlendSolver', 'OSS_Kraken')
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

            self.shldrMocapCtrl_link = CtrlSpace('shldrMocapCtrl_link', parent=self.outputHrcGrp)
            self.shdlrEndMocapSpaceCtrl_link = CtrlSpace('shdlrEndMocapSpaceCtrl_link', parent=self.outputHrcGrp)

            self.mocapHierBlendSolver.setOutput('hierOut',
                [
                self.shldrMocapCtrl_link,
                self.shdlrEndMocapSpaceCtrl_link,
                ]
            )
            self.shldrOutputTgtConstraint = self.shldrOutputTgt.constrainTo(self.shldrMocapCtrl_link)
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



from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSShoulderComponentGuide)
ks.registerComponent(OSSShoulderComponentRig)