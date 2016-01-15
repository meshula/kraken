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
from kraken.core.objects.locator import Locator
from kraken.core.objects.joint import Joint
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy



class OSSMouthComponent(BaseExampleComponent):
    """Mouth Component Base"""

    def __init__(self, name='MouthBase', parent=None, data=None):
        super(OSSMouthComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

        # Declare Output Xfos
        self.mouthOutputTgt = self.createOutput('mouth', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.mouthEndOutputTgt = self.createOutput('mouthEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()
        self.rightSideInputAttr = self.createInput('rightSide', dataType='Boolean', value=self.getLocation() is 'R', parent=self.cmpInputAttrGrp).getTarget()

        # Declare Output Attrs
        # Use this color for OSS components (should maybe get this color from a central source eventually)
        self.setComponentColor(155, 155, 200, 255)


class OSSMouthComponentGuide(OSSMouthComponent):
    """Mouth Component Guide"""

    def __init__(self, name='Mouth', parent=None):

        Profiler.getInstance().push("Construct Mouth Guide Component:" + name)
        super(OSSMouthComponentGuide, self).__init__(name, parent)


         # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)


        # =========
        # Controls
        # =========
        # Guide Controls

        self.mouthCtrl = Control('mouth', parent=self.ctrlCmpGrp, shape="sphere")
        self.mouthUpVCtrl = Control('mouthUpV', parent=self.ctrlCmpGrp, shape="triangle") 
        self.mouthUpVCtrl.setColor('red')
        self.mouthEndCtrl = Control('mouthEnd', parent=self.ctrlCmpGrp, shape="sphere")

        data = {
                "name": name,
                "location": "L",
                "mouthXfo": Xfo(Vec3(0, 15, 0)),
                "mouthUpVXfo": Xfo(Vec3(0.0, 1.0, 0.0)),
                "mouthEndXfo": Xfo(Vec3(0, 14, 2))
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

        data = super(OSSMouthComponentGuide, self).saveData()

        data['mouthXfo'] = self.mouthCtrl.xfo
        data['mouthUpVXfo'] = self.mouthUpVCtrl.xfo
        data['mouthEndXfo'] = self.mouthEndCtrl.xfo

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

        super(OSSMouthComponentGuide, self).loadData( data )

        self.mouthCtrl.xfo = data['mouthXfo']
        self.mouthUpVCtrl.xfo = self.mouthCtrl.xfo.multiply(data['mouthUpVXfo'])
        self.mouthEndCtrl.xfo = data['mouthEndXfo']

        return True


    def getRigBuildData(self):
        """Returns the Guide data used by the Rig Component to define the layout of the final rig..

        Return:
        The JSON rig data object.

        """

        data = super(OSSMouthComponentGuide, self).getRigBuildData()


        # Values
        mouthPosition = self.mouthCtrl.xfo.tr
        mouthUpV = self.mouthUpVCtrl.xfo.tr
        mouthEndPosition = self.mouthEndCtrl.xfo.tr

        # Calculate Mouth Xfo
        rootToEnd = mouthEndPosition.subtract(mouthPosition).unit()
        rootToUpV = mouthUpV.subtract(mouthPosition).unit()
        bone1ZAxis = rootToUpV.cross(rootToEnd).unit()
        bone1Normal = bone1ZAxis.cross(rootToEnd).unit()

        mouthXfo = Xfo()
        mouthXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, mouthPosition)

        mouthLen = mouthPosition.subtract(mouthEndPosition).length()

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

        return OSSMouthComponentRig


class OSSMouthComponentRig(OSSMouthComponent):
    """Mouth Component"""

    def __init__(self, name='Mouth', parent=None):

        Profiler.getInstance().push("Construct Mouth Rig Component:" + name)
        super(OSSMouthComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Mouth
        self.mouthCtrlSpace = CtrlSpace('mouth', parent=self.ctrlCmpGrp)
        self.mouthCtrl = Control('mouth', parent=self.mouthCtrlSpace, shape="square")
        self.mouthCtrl.alignOnXAxis()


        # ==========
        # Deformers
        # ==========
        deformersLayer = self.getOrCreateLayer('deformers')
        defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.ctrlCmpGrp.setComponent(self)

        self.mouthDef = Joint('mouth', parent=defCmpGrp)
        self.mouthDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        mouthInputConstraint = PoseConstraint('_'.join([self.mouthCtrl.getName(), 'To', self.parentSpaceInputTgt.getName()]))
        mouthInputConstraint.setMaintainOffset(True)
        mouthInputConstraint.addConstrainer(self.parentSpaceInputTgt)
        self.mouthCtrlSpace.addConstraint(mouthInputConstraint)

        # Constraint outputs
        mouthConstraint = PoseConstraint('_'.join([self.mouthOutputTgt.getName(), 'To', self.mouthCtrl.getName()]))
        mouthConstraint.addConstrainer(self.mouthCtrl)
        self.mouthOutputTgt.addConstraint(mouthConstraint)

        mouthEndConstraint = PoseConstraint('_'.join([self.mouthEndOutputTgt.getName(), 'To', self.mouthCtrl.getName()]))
        mouthEndConstraint.addConstrainer(self.mouthCtrl)
        self.mouthEndOutputTgt.addConstraint(mouthEndConstraint)


        # ===============
        # Add Splice Ops
        # ===============
        # Add Deformer Splice Op
        spliceOp = KLOperator('mouthDeformerKLOp', 'PoseConstraintSolver', 'Kraken')
        self.addOperator(spliceOp)

        # Add Att Inputs
        spliceOp.setInput('drawDebug', self.drawDebugInputAttr)
        spliceOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        spliceOp.setInput('constrainer', self.mouthOutputTgt)

        # Add Xfo Outputs
        spliceOp.setOutput('constrainee', self.mouthDef)

        Profiler.getInstance().pop()


    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSMouthComponentRig, self).loadData( data )

        self.mouthCtrlSpace.xfo = data['mouthXfo']
        self.mouthCtrl.xfo = data['mouthXfo']


        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['mouthXfo']
        self.mouthEndOutputTgt.xfo = data['mouthXfo']
        self.mouthOutputTgt.xfo = data['mouthXfo']


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSMouthComponentGuide)
ks.registerComponent(OSSMouthComponentRig)