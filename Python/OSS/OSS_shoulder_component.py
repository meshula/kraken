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



class OSSShoulderComponent(BaseExampleComponent):
    """Shoulder Component Base"""

    def __init__(self, name='shoulderBase', parent=None, data=None):
        super(OSSShoulderComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.spineEndInputTgt = self.createInput('spineEnd', dataType='Xfo', parent=self.inputHrcGrp).getTarget()

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

    def __init__(self, name='shoulder', parent=None):

        Profiler.getInstance().push("Construct Shoulder Guide Component:" + name)
        super(OSSShoulderComponentGuide, self).__init__(name, parent)


         # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)


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

        shldrLen = shldrPosition.subtract(shldrEndPosition).length()

        data['shldrXfo'] = shldrXfo
        data['shldrLen'] = shldrLen

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

    def __init__(self, name='Shoulder', parent=None):

        Profiler.getInstance().push("Construct Shoulder Rig Component:" + name)
        super(OSSShoulderComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Shoulder
        self.shldrCtrlSpace = CtrlSpace('shldr', parent=self.ctrlCmpGrp)
        self.shldrCtrl = Control('shldr', parent=self.shldrCtrlSpace, shape="cube")
        self.shldrCtrl.alignOnXAxis()


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
        shldrInputConstraint = PoseConstraint('_'.join([self.shldrCtrl.getName(), 'To', self.spineEndInputTgt.getName()]))
        shldrInputConstraint.setMaintainOffset(True)
        shldrInputConstraint.addConstrainer(self.spineEndInputTgt)
        self.shldrCtrlSpace.addConstraint(shldrInputConstraint)

        # Constraint outputs
        shldrConstraint = PoseConstraint('_'.join([self.shldrOutputTgt.getName(), 'To', self.shldrCtrl.getName()]))
        shldrConstraint.addConstrainer(self.shldrCtrl)
        self.shldrOutputTgt.addConstraint(shldrConstraint)

        shldrEndConstraint = PoseConstraint('_'.join([self.shldrEndOutputTgt.getName(), 'To', self.shldrCtrl.getName()]))
        shldrEndConstraint.addConstrainer(self.shldrCtrl)
        self.shldrEndOutputTgt.addConstraint(shldrEndConstraint)


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

        self.shldrCtrlSpace.xfo = data['shldrXfo']
        self.shldrCtrl.xfo = data['shldrXfo']
        self.shldrCtrl.scalePoints(Vec3(data['shldrLen'], 0.75, 0.75))

        if data['location'] == "R":
            self.shldrCtrl.translatePoints(Vec3(0.0, 0.0, -1.0))
        else:
            self.shldrCtrl.translatePoints(Vec3(0.0, 0.0, 1.0))

        # ============
        # Set IO Xfos
        # ============
        self.spineEndInputTgt.xfo = data['shldrXfo']
        self.shldrEndOutputTgt.xfo = data['shldrXfo']
        self.shldrOutputTgt.xfo = data['shldrXfo']


from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSShoulderComponentGuide)
ks.registerComponent(OSSShoulderComponentRig)