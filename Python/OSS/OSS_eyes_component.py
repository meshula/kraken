import re

from kraken.core.maths import Vec3
from kraken.core.maths.xfo import Xfo, xfoFromDirAndUpV

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
from kraken.core.objects.space import Space
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
        self.EyeCtrlName = StringAttribute('EyeName', value="Eye", parent=self.guideSettingsAttrGrp)
        self.EyeCtrlName.setValueChangeCallback(self.updateEyesControls)
        self.LeftRightPair = BoolAttribute('LeftRightPair', value=True, parent=self.guideSettingsAttrGrp)
        self.LeftRightPair.setValueChangeCallback(self.updateLeftRightPair)

        # =========
        # Controls
        # =========
        # Guide Controls

        self.eyesCtrl = Control('eye', parent=self.ctrlCmpGrp, shape="null")
        self.eyesEndCtrl = Control('eyeEnd', parent=self.eyesCtrl, shape="square")
        self.eyesEndCtrl.rotatePoints(0,90,0)

        self.eyesCtrls = []

        self.globalScale = self.globalComponentCtrlSizeInputAttr.getValue()
        self.globalScaleVec = Vec3(self.globalScale, self.globalScale, self.globalScale)

        data = {
                "name": name,
                "location": "M",
                "eyeXfo": Xfo(Vec3(0, 15, 0)),
                "eyeEndXfo": Xfo(Vec3(0, 15, 10)),
               }

        # find out how to properly access data in updateAnControls
        self.eyesCtrl.xfo = data['eyeXfo']
        self.eyesEndCtrl.xfo = data['eyeEndXfo']


        self.loadData(data)

        Profiler.getInstance().pop()



    def updateAnControls(self, controlsList, handleName):
        """Load a saved guide representation from persisted data.

        Arguments:
        numtweakers -- object, The number of palm/toes

        Return:
        True if successful.

        """
        self.controlXforms = []
        self.controlXfos = {}

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
        if self.LeftRightPair.getValue():
            sides = ["L", "R"]
        else:
            sides = [self.getLocation()]

        segments = ["fk", "ik"]
        offset = 2
        lSideIdx= 0
        rSideIdx= 0
        sideIdx = 0

        for i, side in enumerate(sides):
            parent = self.eyesCtrl
            for j, segment in enumerate(segments):

                sideIdx = 0
                if side == "L":
                    lSideIdx += 1
                    sideIdx = lSideIdx
                elif side == "R":
                    rSideIdx += 1
                    sideIdx = -rSideIdx


                if segment == "fk":
                    metaData = {"altType": "FKControl"}
                    if side != self.getLocation():
                        metaData["altLocation"] = side

                    newCtrl = Control(handleName, parent= self.eyesCtrl, shape="direction", metaData=metaData)
                    newMidCtrl = Control(handleName+'Mid', parent= newCtrl,  metaData=metaData)
                    newCtrl.setShape("direction")
                    newCtrl.setColor("yellow")
                    newCtrl.rotatePoints(90,0,0)
                    newCtrl.translatePoints(Vec3(0,0,1))
                    newCtrl.scalePoints(Vec3(self.globalScale,self.globalScale,self.EyeRadius.getValue()))
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(sideIdx*offset, 0, 0)))
                    newMidCtrl.xfo = newCtrl.xfo.multiply(Xfo(Vec3(0, 0, 5)))
                    parent = newCtrl

                    self.controlXfos[newCtrl.getName()] = newCtrl.xfo
                    self.controlXfos[newMidCtrl.getName()] = newMidCtrl.xfo
                    controlsList.append(newCtrl)
                    # controlsList.append(newMidCtrl)

                else:
                    metaData = {"altType": "IKControl"}
                    if side != self.getLocation():
                        metaData["altLocation"] = side
                    newCtrl = Control(handleName, parent=parent, shape="square", metaData=metaData)
                    newCtrl.setShape("square")
                    newCtrl.setColor("red")
                    newCtrl.lockTranslation(x=True, y=True, z=True)
                    newCtrl.lockRotation(x=True, y=True, z=True)
                    newCtrl.lockScale(x=True, y=True, z=True)
                    newCtrl.scalePoints(Vec3(.5,.5,.5))

                    newCtrl.rotatePoints(90,0,0)
                    newCtrl.translatePoints(Vec3(0,0,10))
                    newCtrl.xfo = parent.xfo.multiply(Xfo(Vec3(0, 0, 0)))
                    if side != self.getLocation():
                        newCtrl.setMetaDataItem("altLocation", side)

                    controlsList.append(newCtrl)
                # parent = newCtrl
                    self.controlXfos[newCtrl.getName()] = newCtrl.xfo

        return True

    # Not sure I like these callbacks for all cases.
    # There should just be a call to "loadData" or equivalent when building guide rig
    def updateLeftRightPair(self, LeftRightPairBool):
        self.updateAnControls(self.eyesCtrls, self.EyeCtrlName.getValue())

    def updateEyesControls(self, handleName):
        self.updateAnControls(self.eyesCtrls, handleName)


    # =============
    # Data Methods
    # =============
    def saveData(self):
        """Save the data for the component to be persisted.

        Return:
        The JSON data object

        """

        data = super(OSSEyesComponentGuide, self).saveData()

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


        #Reset all shapes, but really we should just recreate all controls from loadData instead of init
        for ctrl in self.getHierarchyNodes(classType="Control"):
            ctrl.setShape(ctrl.getShape())

        #saveData() will grab the guide settings values (and are not stored in data arg)
        existing_data = self.saveData()
        existing_data.update(data)
        data = existing_data

        super(OSSEyesComponentGuide, self).loadData( data )

        self.loadAllObjectData(data, "Control")
        self.loadAllObjectData(data, "Transform")

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

        eyeXfo = Xfo()

        # eyeXfo.setFromVectors(rootToEnd, bone1Normal, bone1ZAxis, eyesPosition)



        data = super(OSSEyesComponentGuide, self).getRigBuildData()

        # should include getCurveData
        data = self.saveAllObjectData(data, "Control")
        data = self.saveAllObjectData(data, "Transform")
        data["eyesLen"] =  eyesPosition.subtract(eyesEndPosition).length()
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
        self.eyesSpace = Space('eyes', parent=self.ctrlCmpGrp)
        # self.eyesCtrl = Control('eyes', parent=self.ctrlCmpGrp, shape="square")
        # self.eyesCtrl.alignOnXAxis()


        self.eyeTrackerSpace = Space('eyeTracker', parent=self.ctrlCmpGrp)
        self.eyeTracker = Control('eyeTracker', parent=self.eyeTrackerSpace, shape="circle")
        self.eyeTrackerUpSpace = Space('eyeTrackerUp', parent=self.eyesSpace)
        self.eyeTrackerIKSpace = Space('eyeTrackerIK', parent=self.ctrlCmpGrp)
        self.eyeTracker.rotatePoints(90,0,0)
        self.eyeTracker.lockRotation(x=True, y=True, z=True)
        # ==========
        # Deformers
        # ==========

        # ==============
        # Constrain I/O
        # ==============
        # Constraint inputs
        self.eyeCtrlConstraint = self.eyesSpace.constrainTo(self.parentSpaceInputTgt, maintainOffset=True)
        # self.eyeTrackerIKSpaceConstraint = self.eyeTrackerIKSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)
        self.eyeTrackerSpaceConstraint = self.eyeTrackerSpace.constrainTo(self.globalSRTInputTgt, maintainOffset=True)

        # ===============
        # Add Fabric Ops
        # ===============
        # Add Spine Canvas Op
        self.EyeAutoAimKLOp = KLOperator('EyeAutoAim', 'OSS_AimKLSolver', 'OSS_Kraken')
        self.addOperator(self.EyeAutoAimKLOp)

        # Add Att Inputs
        self.EyeAutoAimKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        self.EyeAutoAimKLOp.setInput('rigScale', self.rigScaleInputAttr)
        self.EyeAutoAimKLOp.setInput('blend',  1)

        self.EyeAutoAimKLOp.setOutput('result', self.eyeTrackerIKSpace)
        self.EyeAutoAimKLOp.setInput('rest', self.eyeTracker)
        self.EyeAutoAimKLOp.setInput('ik', self.eyesSpace)
        self.EyeAutoAimKLOp.setInput('up', self.eyeTrackerUpSpace)
        # temp now until handles are swapped

        Profiler.getInstance().pop()



    def createControls(self, handleName, data):

        globalScale = data['globalComponentCtrlSize']


        # Lets build all new handles
        if self.LeftRightPairBool:
            sides = ["L", "R"]
        else:
            sides = [self.getLocation()]

        segments = ["fk", "ik"]
        for i, side in enumerate(sides):
            parent = self.eyesSpace
            for j, segment in enumerate(segments):
                #Eventually, we need outputs and ports for this component for each handle segment
                #spineOutput = ComponentOutput(handleName+"_"+segment, parent=self.outputHrcGrp)


                if segment == "fk":

                    metaData = {"altType": "FKControl"}
                    if side != self.getLocation():
                        metaData["altLocation"] = side

                    baseDef = Joint(handleName+"Base", parent=self.deformersLayer, metaData={"altLocation": side})
                    baseDef.setComponent(self)
                    self.parentSpaceInputTgt.childJoints.append(baseDef)

                    # socketCtrl = Control(handleName+'Socket', parent=parent, shape="cube", metaData=metaData)
                    # socketSpace = socketCtrl.insertSpace()
                    eyeRegionCtrl = Control(handleName+"Region", parent=parent, shape="cube", metaData=metaData)
                    eyeRegionCtrlSpace = eyeRegionCtrl.insertSpace()
                    eyeRegionDef = Joint(handleName+'Region', parent=baseDef, metaData={"altLocation": side})
                    eyeRegionDef.constrainTo(eyeRegionCtrl)


                    eyeMidCtrl = Control(handleName+'Mid', parent=eyeRegionCtrl, metaData=metaData)



                    eyeSocketSpace = Transform(handleName+'Socket', parent=eyeMidCtrl, metaData=metaData)
                    eyeSocketDef = Joint(handleName+'Socket', parent=baseDef, metaData={"altLocation": side})
                    eyeSocketDef.constrainTo(eyeSocketSpace)

                    eyeSocketRefSpace = Transform(handleName+'SocketRef', parent=parent, metaData=metaData)

                    # newSocketConstraint = newSocket.constrainTo(socketCtrl)

                    fkCtrl = Control(handleName, parent=eyeSocketRefSpace, shape="direction", metaData=metaData)
                    fkCtrlSpace = fkCtrl.insertSpace()
                    upSpace = Transform(handleName+"_up", parent=eyeSocketRefSpace, metaData=metaData)



                    fkCtrl.setShape("direction")
                    fkCtrl.setColor("yellow")
                    # fkCtrl.lockTranslation(x=True, y=True, z=True)
                    fkCtrl.rotatePoints(90,0,0)
                    fkCtrl.translatePoints(Vec3(0,0,1))
                    fkCtrl.scalePoints(Vec3(self.globalScale,self.globalScale,data['EyeRadius']))

                    # fkCtrlSpace.constrainTo(socketCtrl, constraintType="Position")

                    # alignOpt = self.createWeightedMatrixConstraint(eyeSocketSpace, parent, fkCtrl,  translation = 1, scale = 1, rotation = 0, name=handleName + side +'_fkAlign')




                    # newCtrls.append(fkCtrl)
                    newRef = Joint(handleName+"Ref", parent=baseDef, metaData={"altLocation": side, "altType":"RefJoint"})
                    newRef.setComponent(self)
                    newRef.constrainTo(eyeSocketSpace)

                    newLoc = Transform(handleName+"_fk", parent=self.ctrlCmpGrp)
                    newDef = Joint(handleName, parent=baseDef, metaData={"altLocation": side})
                    newDef.setComponent(self)
                    newDefConstraint = newDef.constrainTo(newLoc)

                    nameSettingsAttrGrp = AttributeGroup(handleName+"DisplayInfo_nameSettingsAttrGrp", parent=fkCtrl)
                    self.ikBlendAttr = ScalarAttribute(handleName+'IK', value=0.0, minValue=0.0, maxValue=1.0, parent=nameSettingsAttrGrp)

                    for obj in [eyeSocketSpace, eyeSocketRefSpace,  eyeRegionCtrl, eyeRegionCtrlSpace, fkCtrl, newDef, baseDef]:
                        obj.xfo  = data[side + '_' + handleName + 'Xfo']
                    eyeMidCtrl.xfo =  data[side + '_' + handleName + 'MidXfo']
                    upSpace.xfo = fkCtrl.xfo.multiply(Xfo(Vec3(0.0, 1, 0)))

                    eyeMidCtrl.xfo = xfoFromDirAndUpV(eyeMidCtrl.xfo.tr, eyeSocketSpace.xfo.tr, upSpace.xfo.tr)
                    eyeMidCtrlSpace = eyeMidCtrl.insertSpace()

                    # Aligning Head
                    alignOpt = self.createWeightedMatrixConstraint(eyeSocketRefSpace, parent, eyeSocketSpace,  translation = 1, scale = 1, rotation = 0, name=handleName + side +'fkCtrl2SocketSpace')



                if segment == "ik":
                    metaData = {"altType": "IKControl"}
                    if side != self.getLocation():
                        metaData["altLocation"] = side
                    # break these out more explicitly
                    ikCtrl = Control(handleName, parent=self.eyeTrackerIKSpace, shape="square", metaData=metaData)
                    ikCtrlEndSpace = ikCtrl.insertSpace(name=handleName+"_ik_end")  # Need way to get multiple type tokens like "ik" and "space"
                    ikCtrl.setShape("square")
                    ikCtrl.setColor("red")
                    ikCtrl.lockRotation(x=True, y=True, z=True)
                    ikCtrl.rotatePoints(90,0,0)
                    ikCtrl.scalePoints(Vec3(.5,.5,.5))
                    # newCtrls.append(ikCtrl)
                    ikCtrlSpace = ikCtrl.insertSpace(name=handleName+"_ik", shareXfo=False)



                    ikCtrlSpace.xfo =  data[side + '_' + handleName + 'Xfo'].multiply(Xfo(Vec3(0.0, 0.0, data['eyesLen'])))
                    ikCtrl.xfo =       data[side + '_' + handleName + 'Xfo'].multiply(Xfo(Vec3(0.0, 0.0, data['eyesLen'])))


                ctrlListName = "eyesCtrls"

                # # solve this properly
                # if "eyesCtrlsXfos" in data.keys():
                #     index = i*len(segments) + j

                #     if (i + j) < len(data["eyesCtrlsXfos"]):
                #         if segment == "fk":
                #             print
                #             # newSocket.xfo = data["eyesCtrlsXfos"][index]
                #             fkCtrl.xfo = data["eyesCtrlsXfos"][index]
                #             # eyeMidCtrl.xfo = data["eyesCtrlsXfos"][index+1]
                #             newRef.xfo = data["eyesCtrlsXfos"][index]
                #             # socketCtrl.xfo = data["eyesCtrlsXfos"][index]
                #             eyeSocketSpace.xfo = data["eyesCtrlsXfos"][index]
                #             upSpace.xfo = data["eyesCtrlsXfos"][index].multiply(Xfo(Vec3(0.0, 1, 0)))
                #         if segment == "ik":
                #             ikCtrl.xfo = data["eyesCtrlsXfos"][index]
                #             newXfo = data["eyesCtrlsXfos"][index].multiply(Xfo(Vec3(0.0, 0.0, data['eyesLen'])))
                #             ikCtrl.xfo = newXfo




            # ===============
            # Add Fabric Ops
            # ===============
            # Add Spine Canvas Op
            self.EyeIkFkBlendKLOp = KLOperator('EyeIkFkBlendKLOp'+"_"+handleName+"_"+side, 'OSS_AimKLSolver', 'OSS_Kraken')
            self.addOperator(self.EyeIkFkBlendKLOp)

            # Add Att Inputs

            self.EyeIkFkBlendKLOp.setInput('blend',   self.ikBlendAttr)
            self.EyeIkFkBlendKLOp.setInput('rest',    fkCtrl)
            self.EyeIkFkBlendKLOp.setInput('ik',      ikCtrl)
            self.EyeIkFkBlendKLOp.setInput('up',      upSpace)
            self.EyeIkFkBlendKLOp.setOutput('result', newLoc)


        return True




    def loadData(self, data=None):
        """Load a saved guide representation from persisted data.

        Arguments:
        data -- object, The JSON data object.

        Return:
        True if successful.

        """

        super(OSSEyesComponentRig, self).loadData( data )

        self.LeftRightPairBool = data.get("LeftRightPair", True)

        parent = self.eyesSpace
        self.eyesSpace.xfo = data['eyeXfo']
        # ============
        # Set IO Xfos
        # ============
        self.parentSpaceInputTgt.xfo = data['eyeXfo']
        self.eyesEndOutputTgt.xfo = data['eyeEndXfo']

        self.eyeTrackerUpSpace.xfo = data['eyeXfo'].multiply(Xfo(Vec3(0.0, -1, 0)))
        self.eyeTrackerSpace.xfo = data['eyeEndXfo']
        self.eyeTracker.xfo = data['eyeEndXfo']
        self.eyeTrackerIKSpace.xfo = data['eyeEndXfo']

        self.globalScale = data['globalComponentCtrlSize']
        self.globalScaleVec = Vec3(self.globalScale, self.globalScale, self.globalScale)

        self.createControls(data["EyeName"], data)

        # Eval Operators
        self.evalOperators()

        self.tagAllComponentJoints([self.getDecoratedName()] + self.tagNames)


def getAnimControlNameList(handleName):
    """ tokenizes string argument, returns a list"""
    animControlNameList = re.split(r'[ ,:;]+', handleName)

    # These checks should actually prevent the component_inspector from closing maybe?
    for name in animControlNameList:
        if name and not re.match(r'^[\w_]+$', name):
            # Eventaully specific exception just for component class that display component name, etc.
            raise ValueError("handleName \""+name+"\" contains non-alphanumeric characters in component \""+self.getName()+"\"")

    animControlNameList = [x for x in animControlNameList if x != ""]

    if not animControlNameList:
        return []

    if len(animControlNameList) > len(set(animControlNameList)):
        raise ValueError("Duplicate names in handleName in component \""+self.getName()+"\"")

    return animControlNameList

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerComponent(OSSEyesComponentGuide)
ks.registerComponent(OSSEyesComponentRig)