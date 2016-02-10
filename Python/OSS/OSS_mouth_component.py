import re

from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.euler import rotationOrderStrToIntMapping

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
from kraken.core.objects.operators.canvas_operator import CanvasOperator

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from OSS.OSS_control import *

COMPONENT_NAME = "mouth"

class OSSMouthComponent(BaseExampleComponent):
    """Mouth Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSMouthComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
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

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Mouth Guide Component:" + name)
        super(OSSMouthComponentGuide, self).__init__(name, parent)


         # Guide Settings
        guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
        self.mocapAttr = BoolAttribute('mocap', value=False, parent=guideSettingsAttrGrp)
        self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.5, minValue=0.0,   maxValue=50.0, parent=guideSettingsAttrGrp)

        self.an1DCtrlNames = StringAttribute('an1DNames', value="L_BrowInn L_BrowMid L_BrowOut R_BrowInn R_BrowMid R_BrowOut L_loLidInn L_loLidMid L_loLidOut R_loLidInn R_loLidMid R_loLidOut L_upLidInn L_upLidMid L_upLidOut R_upLidInn R_upLidMid R_upLidOut", parent=guideSettingsAttrGrp)
        self.an2DCtrlNames = StringAttribute('an2DNames', value="L_Mouth R_Mouth", parent=guideSettingsAttrGrp)
        self.an3DCtrlNames = StringAttribute('an3DNames', value="", parent=guideSettingsAttrGrp)


        self.an1DCtrlNames.setValueChangeCallback(self.updateAn1DControls)
        self.an2DCtrlNames.setValueChangeCallback(self.updateAn2DControls)
        self.an3DCtrlNames.setValueChangeCallback(self.updateAn3DControls)



        # =========
        # Controls
        # =========
        # Guide Controls

        self.mouthCtrl = Control('mouth', parent=self.ctrlCmpGrp, shape="sphere")
        self.mouthEndCtrl = Control('mouthEnd', parent=self.ctrlCmpGrp, shape="sphere")


        self.an1DCtrls = []
        self.an2DCtrls = []
        self.an3DCtrls = []


        data = {
                "name": name,
                "location": "M",
                "mouthXfo": Xfo(Vec3(0, 15, 0)),
                "mouthEndXfo": Xfo(Vec3(0, 14, 2))
               }

        self.loadData(data)

        Profiler.getInstance().pop()

    def updateAnControls(self, anCtrlType, controlsList, handleNames):
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

            if ctrl.getParent() is self.mouthCtrl:
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

        segments = ["base", "tweak"]

        offset = 0.0
        for i, handleName in enumerate(animControlNameList):
            parent = self.mouthCtrl
            for j, segment in enumerate(segments):


                newCtrl = Control(handleName+"_"+segment, parent=parent, shape="circle")

                if anCtrlType==1: # Slider
                    if j == 0:
                        newCtrl.setShape("square")
                        newCtrl.setColor("red")
                        newCtrl.scalePoints(Vec3(0.125,2,2))
                    else:
                        newCtrl.setShape("square")
                        newCtrl.scalePoints(Vec3(.5,.25,.25))
                        newCtrl.lockTranslation(x=True, y=False, z=True)

                elif anCtrlType==2: # Field
                    if j == 0:
                        newCtrl.setShape("square")
                        newCtrl.setColor("green")
                        newCtrl.scalePoints(Vec3(2,2,2))
                    else:
                        newCtrl.setShape("circle")
                        newCtrl.scalePoints(Vec3(.5,.5,.5))
                        newCtrl.lockTranslation(x=False, y=False, z=True)

                elif anCtrlType==3: # Volume
                    if j == 0:
                        newCtrl.setShape("cube")
                        newCtrl.setColor("blue")
                        newCtrl.scalePoints(Vec3(2,2,2))
                    else:
                        newCtrl.setShape("sphere")
                        newCtrl.scalePoints(Vec3(.5,.5,.5))

                newCtrl.rotatePoints(90,0,00)


                #newCtrl.scalePoints(Vec3(0.25, 0.25, 0.25))
                if j == 0:
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(-offset, 0.0, 0)))
                    offset += 5.0
                else:
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0.0, 0.0, 0)))

                controlsList.append(newCtrl)
                parent = newCtrl

                if i < len(self.controlXforms):
                    if j < len(self.controlXforms[i]):
                        newCtrl.xfo = self.controlXforms[i][j]


        return True


    def updateAn1DControls(self, handleNames):
        self.updateAnControls(1, self.an1DCtrls, handleNames)

    def updateAn2DControls(self, handleNames):
        self.updateAnControls(2, self.an2DCtrls, handleNames)

    def updateAn3DControls(self, handleNames):
        self.updateAnControls(3, self.an3DCtrls, handleNames)


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
        data['mouthEndXfo'] = self.mouthEndCtrl.xfo

        for ctrlListName in ["an1DCtrls", "an2DCtrls", "an3DCtrls"]:
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
        for ctrl in self.getAllHierarchyNodes(classType=Control):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSMouthComponentGuide, self).loadData( data )

        self.mouthCtrl.xfo = data['mouthXfo']
        self.mouthEndCtrl.xfo = data['mouthEndXfo']

        for ctrlListName in ["an1DCtrls", "an2DCtrls", "an3DCtrls"]:
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
        data = super(OSSMouthComponentGuide, self).getRigBuildData()

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

        data['mouthXfo'] = mouthXfo
        data['mouthLen'] = mouthLen

        for ctrlListName in ["an1DCtrls", "an2DCtrls", "an3DCtrls"]:
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

        return OSSMouthComponentRig


class OSSMouthComponentRig(OSSMouthComponent):
    """Mouth Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

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
        self.defCmpGrp = ComponentGroup(self.getName(), self, parent=deformersLayer)
        self.ctrlCmpGrp.setComponent(self)

        self.mouthDef = Joint('mouth', parent=self.defCmpGrp)
        self.mouthDef.setComponent(self)


        # ==============
        # Constrain I/O
        # ==============
        self.mouthInputConstraint = self.mouthCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        self.mouthConstraint = self.mouthOutputTgt.constrainTo(self.mouthCtrl, maintainOffset=False)
        self.mouthEndConstraint = self.mouthEndOutputTgt.constrainTo(self.mouthCtrl, maintainOffset=False)


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



    def createControls(self, anCtrlType, handleNames, data):

        animControlNameList = getAnimControlNameList(handleNames)


        segments = ["base", "tweak"]

        globalScale = data['globalComponentCtrlSize']


        for i, handleName in enumerate(animControlNameList):
            parent = self.mouthCtrlSpace
            newCtrls = []
            newDefs = []
            for j, segment in enumerate(segments):
                #Eventually, we need outputs and ports for this component for each handle segment
                #spineOutput = ComponentOutput(handleName+"_"+segment, parent=self.outputHrcGrp)


                newCtrlSpace = CtrlSpace(handleName+"_"+segment, parent=parent)
                # newCtrl = Control(handleName+"_"+segment, parent=newCtrlSpace, shape="circle")

                if j == 0:
                    newCtrl = Transform(handleName+"_"+segment, parent=newCtrlSpace)
                    '''
                    if anCtrlType ==1: # Slider
                            newCtrl.setShape("square")
                            newCtrl.setColor("red")
                            newCtrl.scalePoints(Vec3(0.125,2,2))
                            # newCtrl.lockTranslation(x=True, y=True, z=True)
                            newCtrl.lockScale(x=True, y=True, z=True)
                            newCtrl.lockRotation(x=True, y=True, z=True)
                    elif anCtrlType==2: # Field
                            newCtrl.setShape("square")
                            newCtrl.setColor("green")
                            newCtrl.scalePoints(Vec3(2,2,2))
                            # newCtrl.lockTranslation(x=True, y=True, z=True)
                            newCtrl.lockScale(x=True, y=True, z=True)
                            newCtrl.lockRotation(x=True, y=True, z=True)
                    elif anCtrlType==3: # Volume
                            newCtrl.setShape("cube")
                            newCtrl.setColor("blue")
                            newCtrl.scalePoints(Vec3(2,2,2))
                            # newCtrl.lockTranslation(x=True, y=True, z=True)
                            newCtrl.lockScale(x=True, y=True, z=True)
                            newCtrl.lockRotation(x=True, y=True, z=True)
                    newCtrl.rotatePoints(90,0,0)
                    '''
                else:
                    newCtrl = Control(handleName+"_"+segment, parent=newCtrlSpace, shape="circle")
                    if anCtrlType ==1: # Slider
                        newCtrl.setShape("square")
                        newCtrl.scalePoints(Vec3(.5,.25,.25))
                        newCtrl.lockTranslation(x=True, y=False, z=True)

                    elif anCtrlType==2: # Field
                        newCtrl.setShape("circle")
                        newCtrl.scalePoints(Vec3(.5,.5,.5))
                        newCtrl.lockTranslation(x=False, y=False, z=True)

                    elif anCtrlType==3: # Volume
                        newCtrl.setShape("sphere")
                        newCtrl.scalePoints(Vec3(.5,.5,.5))
                    newCtrl.rotatePoints(90,0,0)




                # newCtrl.lockTranslation(x=True, y=True, z=True)
                newCtrl.lockScale(x=True, y=True, z=True)
                newCtrl.lockRotation(x=True, y=True, z=True)

                newCtrls.append(newCtrl)

                newDef = Joint(handleName+"_"+segment, parent=self.defCmpGrp)
                newDefs.append(newDef)

                #self.handleConstraints.append(newDef.constrainTo(newCtrl, maintainOffset=False))
                #controlsList.append(newCtrl)
                parent = newCtrl
                ctrlListName = "an"+str(anCtrlType)+"DCtrls"

                if (ctrlListName+"Xfos") in data.keys():

                    index = i*len(segments) + j

                    if (i*anCtrlType + j) < len(data[ctrlListName+"Xfos"]):
                        newCtrlSpace.xfo = data[ctrlListName+"Xfos"][index]
                        newCtrl.xfo = data[ctrlListName+"Xfos"][index]


            # Add Deformer Joint Constrain
            self.outputsToDeformersKLOp     = KLOperator(self.getLocation()+self.getName()+handleName+'DeformerJointsKLOp', 'MultiPoseConstraintSolver', 'Kraken')
            self.RemapScalarValueSolverKLOp = KLOperator(self.getLocation()+self.getName()+handleName+'RemapScalarValueSolverKLOp', 'OSS_RemapScalarValueSolver', 'OSS_Kraken')

            self.addOperator(self.outputsToDeformersKLOp)
            self.addOperator(self.RemapScalarValueSolverKLOp)

            # Add Att Inputs
            self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
            self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)


            self.RemapScalarValueSolverKLOp.setInput('drawDebug', self.drawDebugInputAttr)
            self.RemapScalarValueSolverKLOp.setInput('rigScale', self.rigScaleInputAttr)


            # Add Xfo Inputs
            self.outputsToDeformersKLOp.setInput('constrainers', newCtrls)
            # Add Xfo Outputs

            self.outputsToDeformersKLOp.setOutput('constrainees', newDefs)

            self.outputsToDeformersKLOp.setOutput('constrainees', newDefs)

            self.RemapScalarValueSolverKLOp.setInput('rigScale', self.rigScaleInputAttr)

        return True




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
        self.mouthCtrl.rotatePoints(0.0, 0.0, 90.0)
        self.mouthCtrl.translatePoints(Vec3(Vec3(data['mouthLen'], -0.5 , 0.0)))
        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['mouthXfo']
        self.mouthEndOutputTgt.xfo = data['mouthXfo']
        self.mouthOutputTgt.xfo = data['mouthXfo']

        # Eval Constraints
        self.mouthConstraint.evaluate()
        self.mouthEndConstraint.evaluate()


        self.createControls(3, data["an3DNames"], data)
        self.createControls(2, data["an2DNames"], data)
        self.createControls(1, data["an1DNames"], data)
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
ks.registerComponent(OSSMouthComponentGuide)
ks.registerComponent(OSSMouthComponentRig)