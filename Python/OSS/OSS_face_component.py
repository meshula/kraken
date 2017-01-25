import re
import json

from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.maths.constants import ROT_ORDER_STR_TO_INT_MAP

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
from OSS.OSS_component import OSS_Component

COMPONENT_NAME = "face"

class OSSFaceComponent(OSS_Component):
    """Face Component Base"""

    def __init__(self, name=COMPONENT_NAME, parent=None):
        super(OSSFaceComponent, self).__init__(name, parent)

        # ===========
        # Declare IO
        # ===========
        # Declare Inputs Xfos

        # Declare Input Attrs



class OSSFaceComponentGuide(OSSFaceComponent):
    """Face Component Guide"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Face Guide Component:" + name)
        super(OSSFaceComponentGuide, self).__init__(name, parent)


         # Guide Settings
        self.an1DCtrlNames = StringAttribute('an1DNames', value="BrowInn BrowMid BrowOut loLidInn loLidMid loLidOut upLidInn upLidMid upLidOut", parent=self.guideSettingsAttrGrp)
        self.shapesToControlsJSON = StringAttribute('shapesToControlsJSON', value="", parent=self.guideSettingsAttrGrp)
        self.an2DCtrlNames = StringAttribute('an2DNames', value="", parent=self.guideSettingsAttrGrp)
        self.an3DCtrlNames = StringAttribute('an3DNames', value="", parent=self.guideSettingsAttrGrp)
        self.LeftRightPairsAttr = BoolAttribute('LeftRightPairs', value=True, parent=self.guideSettingsAttrGrp)
        self.LeftRightPairsAttr.setValueChangeCallback(self.updateLeftRightPairs)

        self.MirrorLeftToRightAttr = BoolAttribute('MirrorLeftToRightAttr', value=True, parent=self.guideSettingsAttrGrp)
        self.MirrorLeftToRightAttr.setValueChangeCallback(self.updateLeftRightPairs)

        self.an1DCtrlNames.setValueChangeCallback(self.updateAn1DControls)
        self.an2DCtrlNames.setValueChangeCallback(self.updateAn2DControls)
        self.an3DCtrlNames.setValueChangeCallback(self.updateAn3DControls)


        # =========
        # Controls
        # =========
        # Guide Controls

        self.faceCtrl = Control('face', parent=self.ctrlCmpGrp, shape="sphere")
        self.faceEndCtrl = Control('faceEnd', parent=self.ctrlCmpGrp, shape="sphere")


        self.an1DCtrls = []
        self.an2DCtrls = []
        self.an3DCtrls = []


        data = {
                "name": name,
                "location": "M",
                "faceXfo": Xfo(Vec3(0, 15, 0)),
                "faceEndXfo": Xfo(Vec3(0, 14, 2))
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
        lmcontrolXforms = []
        rcontrolXforms = []

        mirrorL2R = self.MirrorLeftToRightAttr.getValue()

        globalScale = 1.0

        # Store current values if guide controls already exist
        current = 0
        for ctrl in controlsList:
            if ctrl.getMetaDataItem("altLocation") == "R":
                rcontrolXforms.append(ctrl.xfo)
            else:
                lmcontrolXforms.append(ctrl.xfo)

        # Delete current controls
        for ctrl in reversed(controlsList):
            ctrl.getParent().removeChild(ctrl)
        del controlsList[:]

        # Lets build all new handles
        animControlNameList = getAnimControlNameList(handleNames)

        if self.LeftRightPairsAttr.getValue():
            sides = ["L", "R"]
        else:
            sides = [self.getLocation()]

        if not animControlNameList:  # Nothing to build
            return True

        segments = ["base", "tweak"]

        for side in sides:

            controlXforms = lmcontrolXforms
            mult = 1.0
            if side == "R":
                if not mirrorL2R:
                    controlXforms = rcontrolXforms
                mult = -1.0

            offset = 0.0

            for i, handleName in enumerate(animControlNameList):
                parent = self.faceCtrl
                for j, segment in enumerate(segments):

                    newCtrl = Control(handleName+"_"+segment, parent=parent, shape="circle")
                    if side != self.getLocation():
                        newCtrl.setMetaDataItem("altLocation", side)

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
                    if segment == "base":
                        offset += 5.0 * mult
                        newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(offset, 0.0, 0)))
                        newCtrl.xfo

                    else:
                        newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0.0, 0.0, 0)))

                    controlsList.append(newCtrl)
                    parent = newCtrl

                    if side == "R" and not mirrorL2R:
                        indexOffset == len(animControlNameList)
                    else:
                        indexOffset = 0

                    # If we have stored xforms, put them back

                    index = indexOffset + (i * len(segments) + j)
                    if index < len(controlXforms):
                        xfo = Xfo(controlXforms[index])
                        if side == "R" and mirrorL2R:
                            xfo.tr.x = -xfo.tr.x
                            xfo.ori.mirror(0)

                        newCtrl.xfo = xfo




        return True

    # Not sure I like these callbacks for all cases.
    # There should just be a call to "loadData" or equivalent when building guide rig
    def updateLeftRightPairs(self, LeftRightPairBool):
        self.updateAn1DControls(self.an1DCtrlNames.getValue())
        self.updateAn2DControls(self.an2DCtrlNames.getValue())
        self.updateAn3DControls(self.an3DCtrlNames.getValue())

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
        data = super(OSSFaceComponentGuide, self).saveData()

        data['faceXfo'] = self.faceCtrl.xfo
        data['faceEndXfo'] = self.faceEndCtrl.xfo

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
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        #Grab the guide settings in case we want to use them here (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSFaceComponentGuide, self).loadData( data )

        self.faceCtrl.xfo = data['faceXfo']
        self.faceEndCtrl.xfo = data['faceEndXfo']

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
        data = super(OSSFaceComponentGuide, self).getRigBuildData()

        # Values
        facePosition = self.faceCtrl.xfo.tr
        faceEndPosition = self.faceEndCtrl.xfo.tr

        # Calculate Face Xfo

        # UpVector
        faceUpV= Xfo(Vec3(0.0, 1.0, 0.0)).tr

        rootToEnd = faceEndPosition.subtract(facePosition).unit()

        rootToUpV = faceUpV.subtract(facePosition).unit()
        bone1ZAxis = rootToUpV.cross(rootToEnd).unit()
        bone1Normal = bone1ZAxis.cross(rootToEnd).unit()

        faceXfo = Xfo()
        faceXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, facePosition)

        faceLen = facePosition.subtract(faceEndPosition).length()

        data['faceXfo'] = faceXfo
        data['faceLen'] = faceLen

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

        return OSSFaceComponentRig


class OSSFaceComponentRig(OSSFaceComponent):
    """Face Component"""

    def __init__(self, name=COMPONENT_NAME, parent=None):

        Profiler.getInstance().push("Construct Face Rig Component:" + name)
        super(OSSFaceComponentRig, self).__init__(name, parent)


        # =========
        # Controls
        # =========
        # Face
        self.faceCtrlSpace = CtrlSpace('face', parent=self.ctrlCmpGrp)
        self.ctrlCmpGrp.setComponent(self)
        # ==========
        # Deformers
        # ==========


        # ==============
        # Constrain I/O
        # ==============
        self.faceInputConstraint = self.faceCtrlSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        Profiler.getInstance().pop()



    def createControls(self, anCtrlType, handleNames, data):

        ctrlListName = "an"+str(anCtrlType)+"DCtrls"

        animControlNameList = getAnimControlNameList(handleNames)

        shapesToControlsJSON = data.get("shapesToControlsJSON", "")
        shapesToControlDict = {}
        if shapesToControlsJSON:
            shapesToControlDict = json.loads(shapesToControlsJSON)

        segments = ["base", "tweak"]

        globalScale = data['globalComponentCtrlSize']

        self.RemapScalarValueSolverKLOp = KLOperator(self.getName()+str(anCtrlType), 'OSS_RemapScalarValueSolver', 'OSS_Kraken')
        self.addOperator(self.RemapScalarValueSolverKLOp)
        self.RemapScalarValueSolverKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.RemapScalarValueSolverKLOp.setInput('rigScale', self.rigScaleInputAttr)

        if self.LeftRightPairs:
            sides = ["L", "R"]
        else:
            sides = [self.getLocation()]

        for side in sides:

            for i, handleName in enumerate(animControlNameList):
                parent = self.faceCtrlSpace
                newCtrls = []

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
                            newCtrl.setShape("square")
                            newCtrl.scalePoints(Vec3(.5,.5,.5))
                            newCtrl.lockTranslation(x=False, y=False, z=True)

                        elif anCtrlType==3: # Volume
                            newCtrl.setShape("sphere")
                            newCtrl.scalePoints(Vec3(.5,.5,.5))
                        newCtrl.rotatePoints(90,0,0)

                        location = self.getLocation()
                        if side != location:
                            location = side

                        shapeName = location+"_"+handleName

                        if shapeName in shapesToControlDict.keys():

                            LTOp = KLOperator(self.getName()+handleName, 'OSS_GetLocalTranslateSolver', 'OSS_Kraken', metaData={"altLocation":side})
                            self.addOperator(LTOp)
                            LTOp.setInput('drawDebug', self.drawDebugInputAttr)
                            LTOp.setInput('rigScale', self.rigScaleInputAttr)
                            LTOp.setInput('inMatrix', newCtrl)
                            LTOp.setInput('inBaseMatrix', newCtrlSpace)

                            bsAttrGrp = AttributeGroup("BlendShapes", parent=newCtrl)
                            used_axes = {}
                            shapeInfo = shapesToControlDict[shapeName]
                                #Need something here to extract single local axis value from handleName

                            for direction, shapes in shapeInfo["direction"].iteritems():
                                if 'r' in direction:
                                    sign, axis = direction.split("r")
                                    attrName = 'localRotate'
                                if 't' in direction:
                                    sign, axis = direction.split("t")
                                    attrName = 'localTranslate'

                                if axis not in used_axes.keys():
                                    lvAttr = ScalarAttribute(attrName[:6]+axis, value=0.5, parent=bsAttrGrp)  #can't currently use dcc eulers directly
                                    lvAttr.setLock(True)
                                    LTOp.setOutput(attrName+axis.upper(), lvAttr)

                                    posAttr = ScalarAttribute(axis+"Pos", value=0.5, parent=bsAttrGrp)
                                    posAttr.setLock(True)
                                    negAttr = ScalarAttribute(axis+"Neg", value=0.5, parent=bsAttrGrp)
                                    negAttr.setLock(True)

                                    used_axes[axis] = {"+": posAttr, "-": negAttr}

                                    array = self.RemapScalarValueSolverKLOp.getInput("inputValues") or []
                                    array.append(lvAttr)
                                    self.RemapScalarValueSolverKLOp.setInput('inputValues', array)

                                    array = self.RemapScalarValueSolverKLOp.getOutput("resultPos") or []
                                    array.append(posAttr)
                                    self.RemapScalarValueSolverKLOp.setOutput('resultPos', array)

                                    array = self.RemapScalarValueSolverKLOp.getOutput("resultNeg") or []
                                    array.append(negAttr)
                                    self.RemapScalarValueSolverKLOp.setOutput('resultNeg', array)

                                for shape in shapes:
                                    #we should get rid of this
                                    shapeName = shape + "_bsShape"
                                    bsAttr = ScalarAttribute(shapeName, value=0.0, parent=bsAttrGrp)
                                    bsAttr.setLock(True)
                                    bsAttr.setMetaDataItem("SCALAR_OUTPUT", shapeName)
                                    bsAttr.appendMetaDataListItem("TAGS", self.getDecoratedName())
                                    bsAttr.connect(used_axes[axis][sign])

                    if side != self.getLocation():
                        newCtrl.setMetaDataItem("altLocation", side)
                        newCtrlSpace.setMetaDataItem("altLocation", side)

                        # newCtrl.lockTranslation(x=True, y=True, z=True)
                    newCtrl.lockScale(x=True, y=True, z=True)
                    newCtrl.lockRotation(x=True, y=True, z=False)

                    newCtrls.append(newCtrl)

                    #self.handleConstraints.append(newDef.constrainTo(newCtrl, maintainOffset=False))
                    #controlsList.append(newCtrl)
                    parent = newCtrl

                    if (ctrlListName+"Xfos") in data.keys():
                        if side == "R":
                            indexOffset = len(animControlNameList) * 2
                        else:
                            indexOffset = 0

                        index = indexOffset + (i*len(segments) + j)
                        if index < len(data[ctrlListName+"Xfos"]):
                            newCtrlSpace.xfo = data[ctrlListName+"Xfos"][index]
                            newCtrl.xfo = data[ctrlListName+"Xfos"][index]

            # Add Deformer Joint Constrain
            #self.outputsToDeformersKLOp     = KLOperator(self.getName()+handleName, 'MultiPoseConstraintSolver', 'Kraken')
            #self.addOperator(self.outputsToDeformersKLOp)

            # Add Att Inputs
            #self.outputsToDeformersKLOp.setInput('drawDebug', self.drawDebugInputAttr)
            #self.outputsToDeformersKLOp.setInput('rigScale', self.rigScaleInputAttr)



        return True




    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSFaceComponentRig, self).loadData( data )

        self.LeftRightPairs = data.get("LeftRightPairs", True)
        self.MirrorLeftToRight = data.get("MirrorLeftToRight", True)

        self.faceCtrlSpace.xfo = data['faceXfo']
        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['faceXfo']


        self.parentSpaceInputTgt.childJoints = []

        self.createControls(3, data.get("an3DNames", ""), data)
        self.createControls(2, data.get("an2DNames", ""), data)
        self.createControls(1, data.get("an1DNames", ""), data)
        # Eval Operators
        self.evalOperators()
        self.RemapScalarValueSolverKLOp.evaluate()

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)




def getAnimControlNameList(handleNames):
    """ tokenizes string argument, returns a list"""
    animControlNameList = re.split(r'[ ,:;]+', handleNames.strip())

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
ks.registerComponent(OSSFaceComponentGuide)
ks.registerComponent(OSSFaceComponentRig)
