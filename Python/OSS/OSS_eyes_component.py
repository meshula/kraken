import re

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
from kraken.core.objects.locator import Locator

from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "eyes"

class OSSEyesComponent(OSS_Component):
    """Eyes Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSEyesComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Output Xfos
        self.eyesOutputTgt = self.createOutput('eyes', dataType='Xfo', parent=self.outputHrcGrp).getTarget()
        self.eyesEndOutputTgt = self.createOutput('eyesEnd', dataType='Xfo', parent=self.outputHrcGrp).getTarget()

        # Declare Input Attrs

class OSSEyesComponentGuide(OSSEyesComponent):
    """Eyes Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Eyes Guide Component:" + name)
        super(OSSEyesComponentGuide, self).__init__(name, parent)

         # Guide Settings
        self.EyeRadius = ScalarAttribute('EyeRadius', value=2.0, minValue=0.0,   maxValue=50.0, parent=self.guideSettingsAttrGrp)
        self.EyesCtrlNames = StringAttribute('EyesNames', value="L_Eye R_Eye", parent=self.guideSettingsAttrGrp)

        # =========
        # Controls
        # =========
        # Guide Controls

        self.eyesCtrl = Control('eyes', parent=self.ctrlCmpGrp, shape="null")
        self.eyesEndCtrl = Control('eyesEnd', parent=self.ctrlCmpGrp, shape="square")
        self.eyesEndCtrl.rotatePoints(0,90,0)

        self.eyesCtrls = []


        data = {
                "name": name,
                "location": "M",
                "eyesXfo": Xfo(Vec3(0, 15, 0)),
                "eyesEndXfo": Xfo(Vec3(0, 15, 10))
               }

        # find out how to properly access data in updateAnControls
        self.eyesCtrl.xfo = data['eyesXfo']
        self.eyesEndCtrl.xfo = data['eyesEndXfo']
        self.EyesCtrlNames.setValueChangeCallback(self.updateEyesControls)

        self.loadData(data)

        Profiler.getInstance().pop()

    def updateAnControls(self, controlsList, handleNames):
        """Load a saved guide representation from persisted data.

        Arguments:
        numtweakers -- object, The number of palm/toes

        Return:
        True if successful.

        """
        self.controlXforms = []

        globalScale = 1.0

        # Store current values if guide controls already exist
        current = 0
        for i, ctrl in enumerate(controlsList):

            if ctrl.getParent() is self.eyesCtrl:
                self.controlXforms.append([ctrl.xfo])
                current = len(self.controlXforms) -1
            else:
                self.controlXforms[current].append(ctrl.xfo)

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        # Lets build all new handles
        animControlNameList = getAnimControlNameList(handleNames)

        if not animControlNameList:  # Nothing to build
            return True

        segments = ["fK", "ik"]
        offset = 2
        lSideIdx= 0
        rSideIdx= 0
        sideIdx = 0

        for i, handleName in enumerate(animControlNameList):
            parent = self.eyesCtrl
            for j, segment in enumerate(segments):


                sideIdx = 0
                if handleName.startswith("L"):
                    lSideIdx += 1
                    sideIdx = lSideIdx
                elif handleName.startswith("R"):
                    rSideIdx += 1
                    sideIdx = -rSideIdx


                if j == 0:
                    newCtrl = Control(handleName+"_"+segment, parent= self.eyesCtrl, shape="direction")
                    newCtrl.setShape("direction")
                    newCtrl.setColor("yellow")
                    newCtrl.rotatePoints(90,0,0)
                    newCtrl.translatePoints(Vec3(0,0,1))
                    newCtrl.scalePoints(Vec3(1,1,self.EyeRadius.getValue()))
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(sideIdx*offset, 0, 0)))
                    parent = newCtrl

                else:
                    newCtrl = Control(handleName+"_"+segment, parent=parent, shape="square")
                    newCtrl.setShape("square")
                    newCtrl.setColor("red")
                    newCtrl.lockTranslation(x=True, y=True, z=True)
                    newCtrl.lockRotation(x=True, y=True, z=True)
                    newCtrl.lockScale(x=True, y=True, z=True)
                    newCtrl.scalePoints(Vec3(.5,.5,.5))
                    newCtrl.rotatePoints(90,0,0)
                    newCtrl.translatePoints(Vec3(0,0,10))

                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 0)))


                # parent = newCtrl
                controlsList.append(newCtrl)

                if i < len(self.controlXforms):
                    if j < len(self.controlXforms[i]):
                        newCtrl.xfo = self.controlXforms[i][j]

        return True


    def updateEyesControls(self, handleNames):
        self.updateAnControls(self.eyesCtrls, handleNames)


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """

        data = super(OSSEyesComponentGuide, self).saveData()

        data['eyesXfo'] = self.eyesCtrl.xfo
        data['eyesEndXfo'] = self.eyesEndCtrl.xfo


        for ctrlListName in ["eyesCtrls"]:
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
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSEyesComponentGuide, self).loadData( data )

        self.eyesCtrl.xfo = data['eyesXfo']
        self.eyesEndCtrl.xfo = data['eyesEndXfo']


        for ctrlListName in ["eyesCtrls"]:
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
        data = super(OSSEyesComponentGuide, self).getRigBuildData()

        # Values
        eyesPosition = self.eyesCtrl.xfo.tr
        eyesEndPosition = self.eyesEndCtrl.xfo.tr

        eyesXfo = Xfo()

        # eyesXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, eyesPosition)

        eyesLen = eyesPosition.subtract(eyesEndPosition).length()

        # data['eyesXfo'] = eyesXfo
        data['eyesEndXfo'] = self.eyesEndCtrl.xfo
        data['eyesXfo'] = self.eyesCtrl.xfo
        data['eyesLen'] = eyesLen

        for ctrlListName in ["eyesCtrls"]:
            ctrls = getattr(self, ctrlListName)
            xfos = []
            for i in xrange(len(ctrls)):
                xfos.append(ctrls[i].xfo)
            data[ctrlListName+"Xfos"] = xfos

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

        return OSSEyesComponentRig


class OSSEyesComponentRig(OSSEyesComponent):
    """Eyes Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Eyes Rig Component:" + name)
        super(OSSEyesComponentRig, self).__init__(name, parent)

        self.parentSpaceInputTgt.childJoints = []
        # =========
        # Controls
        # =========
        # Eyes
        self.eyesCtrlSpace = CtrlSpace('eyes', parent=self.ctrlCmpGrp)
        # self.eyesCtrl = Control('eyes', parent=self.ctrlCmpGrp, shape="square")
        # self.eyesCtrl.alignOnXAxis()


        self.eyeTrackerSpace = CtrlSpace('eyeTracker', parent=self.ctrlCmpGrp)
        self.eyeTracker = Control('eyeTracker', parent=self.eyeTrackerSpace, shape="circle")
        self.eyeTrackerUpSpace = CtrlSpace('eyeTrackerUp', parent=self.eyesCtrlSpace)
        self.eyeTrackerIKSpace = CtrlSpace('eyeTrackerIK', parent=self.ctrlCmpGrp)
        self.eyeTracker.rotatePoints(90,0,0)
        self.eyeTracker.lockRotation(x=True, y=True, z=True)
        # ==========
        # Deformers
        # ==========

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.eyeCtrlConstraint = self.eyesCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        # self.eyeTrackerIKSpaceConstraint = self.eyeTrackerIKSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        self.eyeTrackerSpaceConstraint = self.eyeTrackerSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)

        # ===============
        # Add Fabric Ops
        # ===============
        # Add Spine Canvas Op
        self.EyeAutoAimKLOp = KLOperator('EyeAutoAimKLOp', 'OSS_AimKLSolver', 'OSS_Kraken')
        self.addOperator(self.EyeAutoAimKLOp)

        # Add Att Inputs
        self.EyeAutoAimKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.EyeAutoAimKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.EyeAutoAimKLOp.setInput('blend',  0)
        self.EyeAutoAimKLOp.setInput('atAxis',  0)
        self.EyeAutoAimKLOp.setInput('upAxis',  5)

        self.EyeAutoAimKLOp.setOutput('result', self.eyeTrackerIKSpace)
        self.EyeAutoAimKLOp.setInput('position', self.eyeTracker)
        self.EyeAutoAimKLOp.setInput('ik', self.eyesCtrlSpace)
        self.EyeAutoAimKLOp.setInput('fk', self.eyeTracker)
        # Add Xfo Inputs
        self.EyeAutoAimKLOp.setInput('up', self.eyeTrackerUpSpace)
        # temp now until handles are swapped

        Profiler.getInstance().pop()



    def createControls(self, handleNames, data):

        animControlNameList = getAnimControlNameList(handleNames)


        segments = ["fk", "ik"]

        globalScale = data['globalComponentCtrlSize']



        for i, handleName in enumerate(animControlNameList):
            parent = self.eyesCtrlSpace
            # newCtrls = []
            # build fk handle
            for j, segment in enumerate(segments):
                #Eventually, we need outputs and ports for this component for each handle segment
                #spineOutput = ComponentOutput(handleName+"_"+segment, parent=self.outputHrcGrp)

                newCtrlSpace = CtrlSpace(handleName+"_"+segment, parent=parent)
                # newCtrl = Control(handleName+"_"+segment, parent=newCtrlSpace, shape="circle")

                if segment == "fk":
                    # fkCtrl = Transform(handleName+"_"+segment, parent=newCtrlSpace)
                    fkCtrl = Control(handleName+"_fk", parent=newCtrlSpace, shape="direction")
                    upCtrlSpace = fkCtrl.insertCtrlSpace()
                    fkCtrl.setShape("direction")
                    fkCtrl.setColor("yellow")
                    fkCtrl.lockTranslation(x=True, y=True, z=True)
                    fkCtrl.rotatePoints(90,0,0)
                    fkCtrl.translatePoints(Vec3(0,0,1))
                    fkCtrl.scalePoints(Vec3(1,1,data['EyeRadius']))
                    # newCtrls.append(fkCtrl)
                    newRef = Joint(handleName+"_ref", parent=self.deformersParent)
                    newRef.setComponent(self)
                    newRefConstraint = newRef.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
                    self.parentSpaceInputTgt.childJoints.append(newRef)

                    newLoc = Locator(handleName+"_fk", parent=self.ctrlCmpGrp)
                    newLoc.setVisibility(False)

                    newDef = Joint(handleName+"_fk", parent=newRef)
                    newDef.setComponent(self)
                    newDefConstraint = newDef.constrainTo(newLoc)

                    nameSettingsAttrGrp = AttributeGroup(handleName+"DisplayInfo_nameSettingsAttrGrp", parent=fkCtrl)
                    upVSpaceBlendInputAttr = ScalarAttribute(handleName+'FKIK', value=0.0, minValue=0.0, maxValue=1.0, parent=nameSettingsAttrGrp)



                if segment == "ik":
                    # break these out more explicitly
                    ikCtrl = Control(handleName+"_"+segment, parent=self.eyeTrackerIKSpace, shape="square")
                    ikCtrlEndSpace = ikCtrl.insertCtrlSpace()
                    ikCtrl.setShape("square")
                    ikCtrl.setColor("red")
                    ikCtrl.lockRotation(x=True, y=True, z=True)
                    ikCtrl.rotatePoints(90,0,0)
                    ikCtrl.scalePoints(Vec3(.5,.5,.5))
                    # newCtrls.append(ikCtrl)

                ctrlListName = "eyesCtrls"

                # solve this properly
                if "eyesCtrlsXfos" in data.keys():
                    index = i*len(segments) + j

                    if (i + j) < len(data["eyesCtrlsXfos"]):
                        newCtrlSpace.xfo = data["eyesCtrlsXfos"][index]
                        if segment == "fk":
                            fkCtrl.xfo = data["eyesCtrlsXfos"][index]
                            newRef.xfo = data["eyesCtrlsXfos"][index]
                            upCtrlSpace.xfo = data["eyesCtrlsXfos"][index].multiply(Xfo(Vec3(0.0, 1, 0)))
                        if segment == "ik":
                            ikCtrl.xfo = data["eyesCtrlsXfos"][index]
                            newXfo = data["eyesCtrlsXfos"][index].multiply(Xfo(Vec3(0.0, 0.0, data['eyesLen'])))
                            ikCtrlEndSpace.xfo = newXfo
                            ikCtrl.xfo = newXfo



            # ===============
            # Add Fabric Ops
            # ===============
            # Add Spine Canvas Op
            self.EyeIkFkBlendKLOp = KLOperator('EyeIkFkBlendKLOp'+"_"+handleName, 'OSS_AimKLSolver', 'OSS_Kraken')
            self.addOperator(self.EyeIkFkBlendKLOp)

            # Add Att Inputs
            self.EyeIkFkBlendKLOp.setInput('blend',  upVSpaceBlendInputAttr)
            self.EyeIkFkBlendKLOp.setInput('position', fkCtrl)
            self.EyeIkFkBlendKLOp.setInput('atAxis',  0)
            self.EyeIkFkBlendKLOp.setInput('upAxis',  2)

            self.EyeIkFkBlendKLOp.setOutput('result', newLoc)
            self.EyeIkFkBlendKLOp.setInput('ik', ikCtrl)
            self.EyeIkFkBlendKLOp.setInput('fk', fkCtrl)
            # Add Xfo Inputs
            self.EyeIkFkBlendKLOp.setInput('up', upCtrlSpace)
            # temp now until handles are swapped


        return True




    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSEyesComponentRig, self).loadData( data )

        parent = self.eyesCtrlSpace
        self.eyesCtrlSpace.xfo = data['eyesXfo']
        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['eyesXfo']
        self.eyesEndOutputTgt.xfo = data['eyesEndXfo']

        self.eyeTrackerUpSpace.xfo = data['eyesXfo'].multiply(Xfo(Vec3(0.0, -1, 0)))
        self.eyeTrackerSpace.xfo = data['eyesEndXfo']
        self.eyeTracker.xfo = data['eyesEndXfo']
        self.eyeTrackerIKSpace.xfo = data['eyesEndXfo']



        self.createControls(data["EyesNames"], data)

        # Eval Operators
        # self.evalOperators()


def getAnimControlNameList(handleNames):
    """ tokenizes string argument, returns a list"""
    animControlNameList = re.split(r'[ ,:;]+', handleNames)

    # These checks should actually prevent the component_inspector from closing maybe?
    for name in animControlNameList:
        if name and not re.match(r'^[\w_]+$', name):
            # Eventaully specific exception just for component class that display component name, etc.
            raise ValueError("handleNames \""+name+"\" contains non-alphanumeric characters in component \""+self.getName()+"\"")

    animControlNameList = [x for x in animControlNameList if x != ""]

    if not animControlNameList:
        return []

    if len(animControlNameList) > len(set(animControlNameList)):
        raise ValueError("Duplicate names in handleNames in component \""+self.getName()+"\"")

    return animControlNameList

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSEyesComponentGuide)
ks.registerComponent(OSSEyesComponentRig)