import re, os, json
from kraken.core.objects.components.base_example_component import BaseExampleComponent
from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.string_attribute import StringAttribute
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute
from kraken.core.objects.joint import Joint
from kraken.core.objects.locator import Locator
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.control import Control
from kraken.core.maths import *
from kraken.core.maths.constants import *
from collections import defaultdict




class OSS_Component(BaseExampleComponent):
    """OSS Component object."""

    def __init__(self, name='', parent=None):
        super(OSS_Component, self).__init__(name, parent=parent)

        self._color = (155, 155, 200, 255)

        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        if self.getComponentType() == "Guide":
            self.guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
            self.singleDeformerGroupAttr = BoolAttribute('SingleDeformerGroup', value=True, parent=self.guideSettingsAttrGrp)
            self.mocapAttr = BoolAttribute('mocap', value=False, parent=self.guideSettingsAttrGrp)
            self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.0, minValue=0.0,   maxValue=50.0, parent=self.guideSettingsAttrGrp)
            self.tagNamesAttr = StringAttribute('tagNames', value="", parent=self.guideSettingsAttrGrp)
        else: # Rig
            self.deformersLayer = self.getOrCreateLayer('deformers')
            self.deformersParent = self.deformersLayer
            self.deformersParent.setComponent(self)

    def loadData(self, data):

        super(OSS_Component, self).loadData(data)


        if self.getComponentType() == "Guide":
            pass
        else: # Rig
            self.singleDeformerGroup = bool(data.get("SingleDeformerGroup", True))
            if not self.singleDeformerGroup:
                self.defCmpGrp = ComponentGroup(self.getName(), self, parent=self.deformersLayer)
                self.addItem("defCmpGrp", self.defCmpGrp)
                self.deformersParent = self.defCmpGrp

        # make tagNames string a list
        self.tagNames = data.get('tagNames', "").strip().split()



    def convertToStringList(self, inputString):
        """ tokenizes string argument, returns a list"""
        stringList = re.split(r'[ ,:;]+', inputString)

        # These checks should actually prevent the component_inspector from closing maybe?
        for name in stringList:
            if name and not re.match(r'^[\w_]+$', name):
                # Eventaully specific exception just for component class that display component name, etc.
                raise ValueError("inputString \""+name+"\" contains non-alphanumeric characters in component \""+self.getName()+"\"")

        stringList = [x for x in stringList if x != ""]

        if len(stringList) > len(set(stringList)):
            raise ValueError("Duplicate names in inputString in component \""+self.getName()+"\"")

        return stringList


    def convertToScalarList(self, inputString):
        """ tokenizes string argument, returns a list"""
        stringList = re.split(r'[ ,:;]+', inputString)
        scalarList = []
        # These checks should actually prevent the component_inspector from closing maybe?
        for name in stringList:
            if name:
                try:
                    scalarList.append(float(name))
                except ValueError:
                    raise ValueError("inputString \""+name+"\" cannot be converted to float: \""+self.getName()+"\"")


        # scalarList = [x for x in scalarList if x != ""]

        if not scalarList:
            return []

        if len(scalarList) > len(set(scalarList)):
            raise ValueError("Duplicate names in inputString in component \""+self.getName()+"\"")

        return scalarList


    def createPartialJoint(self, joint, baseTranslate=None, baseRotate=None, baseScale=None, blendTranslate=0.5, blendRotate=0.5, blendScale=0.5, name=None, parent=None):
        #Creates a joint as a sibling to the input joint which has a blended interpolation between joint and base


        if not name:
            name = joint.getName()+"_part"

        if not parent:
            parent = joint.getParent()

        if not parent:
            parent = self.deformersParent

        if not baseTranslate:
            baseTranslate = joint
            blendTranslate = -1

        if not baseRotate:
            baseRotate = joint
            blendRotate = -1

        if not baseScale:
            baseScale = joint
            blendScale = -1


        #Since we need to constrain the output as opposed to pumping in direct trs values, create an output transform
        null = Locator(name+"_null" , parent=self.ctrlCmpGrp)
        null.setShapeVisibility(False)

        partialJointDef = Joint(name, parent=parent)
        partialJointDef.setComponent(self)
        partialJointDef.xfo = Xfo(joint.xfo)

        # Should make an orient solver, too or add flags to this one?
        partialBlendSolver = KLOperator(name+'partial', 'OSS_BlendTRSConstraintSolver', 'OSS_Kraken')
        self.addOperator(partialBlendSolver)
        partialBlendSolver.setInput('blendTranslate', blendTranslate)
        partialBlendSolver.setInput('blendRotate', blendRotate)
        partialBlendSolver.setInput('blendScale', blendScale)
        # Add Att Inputs
        partialBlendSolver.setInput('drawDebug', self.drawDebugInputAttr)
        partialBlendSolver.setInput('rigScale', self.rigScaleInputAttr)
        # Add Xfo Inputs
        partialBlendSolver.setInput('constrainerTranslateA', joint)
        partialBlendSolver.setInput('constrainerTranslateB', baseTranslate)
        partialBlendSolver.setInput('constrainerRotateA', joint)
        partialBlendSolver.setInput('constrainerRotateB', baseRotate)
        partialBlendSolver.setInput('constrainerScaleA', joint)
        partialBlendSolver.setInput('constrainerScaleB', baseScale)
        # Add Xfo Outputs
        partialBlendSolver.setOutput('result', null)

        partialJointDef.constrainTo(null).evaluate()


        return partialJointDef


    def invertAxisStr(self, string):

            if "NEG" in string:
                return string.replace("NEG", "POS")
            if "POS" in string:
                return string.replace("POS", "NEG")


    def get_align_from_aim_and_side(self, aimAxisStr="POSX", sideAxisStr="POSY"):

        align = Vec3()

        aim_axis = AXIS_NAME_TO_TUPLE_MAP[aimAxisStr]
        aim_vec = Vec3(aim_axis[0], aim_axis[1], aim_axis[2])

        side_axis = AXIS_NAME_TO_TUPLE_MAP[sideAxisStr]
        side_vec = Vec3(side_axis[0], side_axis[1], side_axis[2])

        nv = aim_vec.cross(side_vec)
        norm_axis = [nv.x, nv.y, nv.z]

        for i in [1, -1]:
            if i in aim_axis:
                align.x = i * (aim_axis.index(i)+1)
            if i in side_axis:
                align.y = i * (side_axis.index(i)+1)
            if i in norm_axis:
                align.z = i * (norm_axis.index(i)+1)

        return align


    def createTwistJoints(self, basename, parentDef, curveCtrls, numDeformers=3, inparams=None, skipStart=False, skipEnd=False, aimAxisStr="POSX", sideAxisStr="POSY", ctrlAimAxisStr="POSX", ctrlNormalAxisStr="POSY"):
        # joint aligns are relative to ctrlAligns,

        jointAlign = self.get_align_from_aim_and_side(aimAxisStr=aimAxisStr, sideAxisStr=sideAxisStr)
        ctrlAlign = self.get_align_from_aim_and_side(aimAxisStr=ctrlAimAxisStr, sideAxisStr=ctrlNormalAxisStr)

        controlRestInputs = [ctrl.xfo for ctrl in curveCtrls]

        rigControlAligns = [ctrlAlign for ctrl in curveCtrls]

        params = inparams or []

        curveOutputs = []
        deformerJoints = []

        defomerSpacing = numDeformers + skipStart + skipEnd -1

        parentDef
        for i in range(numDeformers):

            name = basename + str(i+int(skipStart)).zfill(2)

            if not inparams:
                if skipStart:
                    params.append(float(i+1)/float(defomerSpacing))
                else:
                    params.append(float(i)/float(defomerSpacing))

            #Need dynamic ports branch to be able to see this updated in Graph
            curveOutput = self.createOutput(name, dataType='Xfo', parent=self.outputHrcGrp).getTarget()
            curveOutputs.append(curveOutput)

            if deformerJoints:
                parentDef = deformerJoints[-1]

            curveDef = Joint(name, parent=parentDef)
            curveDef.setComponent(self)
            deformerJoints.append(curveDef)

            curveDef.constrainTo(curveOutput)


        NURBSCurveKLOp = KLOperator(basename, 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
        self.addOperator(NURBSCurveKLOp)

        NURBSCurveKLOp.setInput('drawDebug', self.drawDebugInputAttr)
        NURBSCurveKLOp.setInput('rigScale', self.rigScaleInputAttr)
        NURBSCurveKLOp.setInput('alignX', jointAlign.x)
        NURBSCurveKLOp.setInput('alignY', jointAlign.y)
        NURBSCurveKLOp.setInput('alignZ', jointAlign.z)
        NURBSCurveKLOp.setInput('degree', 3)
        NURBSCurveKLOp.setInput('keepArcLength', 0.0)
        NURBSCurveKLOp.setInput('compressionAmt', 0.4)
        NURBSCurveKLOp.setInput('followCurveTangent', 1.0)
        NURBSCurveKLOp.setInput('followCurveNormal', 1.0)
        NURBSCurveKLOp.setInput('useLocalNormal', 0.0)
        #NURBSCurveKLOp.setInput('altTangent', Vec3(0.0,1.0,0.0))
        NURBSCurveKLOp.setInput('parent', self.ctrlCmpGrp)
        NURBSCurveKLOp.setInput('atVec', self.ctrlCmpGrp) # atVec should be optional, but is not currently in the Solver
        NURBSCurveKLOp.setInput('controlAligns', rigControlAligns)
        NURBSCurveKLOp.setInput('controls', curveCtrls)
        NURBSCurveKLOp.setInput('controlsRest', controlRestInputs)
        NURBSCurveKLOp.setInput('params', params )

        NURBSCurveKLOp.setOutput('outputs', curveOutputs)

        NURBSCurveKLOp.evaluate()

        return NURBSCurveKLOp


    def blend_two_xfos(self, target, sourceA, sourceB, blend=0, blendTranslate=None, blendRotate=None, blendScale=None, name=None):
        """Constrain target to a blend between two source Xfos
        Simplifies OSS_BlendTRSConstraintSolver for many cases

        Args:
            sourceA (Xfo): first xfo
            sourceB (Xfo): second xfo
            target (Xfo): destination xfo
            blend (float): overall blend value
            blendTranslate (float): translate blend override
            blendRotate (float): rotate blend override
            blendScale (float): scale blend override
            parentSpace  (Xfo): return result in local space of this xfo

        Returns:
            The KL constraint operator

        """
        if not name:
            name = target.getName()


        blendTRSConstraint = KLOperator(name, 'OSS_BlendTRSConstraintSolver', 'OSS_Kraken')
        self.addOperator(blendTRSConstraint)

        if blendTranslate is None:
             blendTranslate = blend

        if blendRotate is None:
             blendRotate = blend

        if blendScale is None:
             blendScale = blend

        blendTRSConstraint.setInput('blendTranslate', blendTranslate)
        blendTRSConstraint.setInput('blendRotate', blendRotate)
        blendTRSConstraint.setInput('blendScale', blendScale)
        blendTRSConstraint.setInput('constrainerTranslateA', sourceA)
        blendTRSConstraint.setInput('constrainerTranslateB', sourceB)
        blendTRSConstraint.setInput('constrainerRotateA', sourceA)
        blendTRSConstraint.setInput('constrainerRotateB', sourceB)
        blendTRSConstraint.setInput('constrainerScaleA', sourceA)
        blendTRSConstraint.setInput('constrainerScaleB', sourceB)
        blendTRSConstraint.setOutput('result', target)

        return blendTRSConstraint


    def connectReverse(self, sourceAttribute, destAttribute, name=None, lock=True):

        sourceObject = sourceAttribute.getParent().getParent()
        destObject = destAttribute.getParent().getParent()

        name = sourceObject.getName()+"_"+sourceAttribute.getName()+"_2_"+destObject.getName()+"_"+destAttribute.getName()
        attrGrp = AttributeGroup("Reversed", parent=destObject)
        if destAttribute.isTypeOf("BoolAttribute"):  #Can't pass bool to kl solver so create an intermediate float attribute
            parent = destAttribute.getParent()
            floatAttr = ScalarAttribute(destAttribute.getName()+"_float", value=1.0, minValue=0.0, maxValue=1.0, parent=attrGrp)
        else:
            floatAttr = sourceAttribute

        #############################
        ReverseSolver = KLOperator(name, 'OSS_ReverseSolver', 'OSS_Kraken')
        self.addOperator(ReverseSolver)
        ReverseSolver.setInput('drawDebug', self.drawDebugInputAttr)
        ReverseSolver.setInput('rigScale', self.rigScaleInputAttr)
        ReverseSolver.setInput('input', sourceAttribute)
        ReverseSolver.setOutput('result', floatAttr)

        if destAttribute.isTypeOf("BoolAttribute"):
            destAttribute.connect(floatAttr)
            floatAttr.setLock(True)

        if lock:
            destAttribute.setLock(True)



    def offsetOp(self, references, targets, offsetA, offsetB, amount = 1, name=None):
        """
        outputs Mat44 array of objects tranformed by the delta of OffsetA to OffsetB

        Args:
            amount (Scalar): blend amount
            references (Mat44): reference objects that provide source Mat44
            targets (Mat44): targets after offset
            offsetA (Mat44): First Value for Delta
            offsetB (Mat44): Second Value for Delta
        Returns:
            The KL offset operator

        """

        if not name:
            name = offsetB.getName()+"_offset"

        offsetOp = KLOperator(name, 'OSS_offsetSolver', 'OSS_Kraken')
        self.addOperator(offsetOp)
        offsetOp.setInput('amount', amount)
        offsetOp.setInput('references', references)
        offsetOp.setInput('targetsParents',  [o.getParent() for o in targets])
        offsetOp.setInput('offsetsRest', [offsetA for o in references])
        offsetOp.setInput('offsets',     [offsetB for o in references])
        offsetOp.setOutput('targets', targets)
        return offsetOp


    def insertParentSpace(self, ctrl, name=None):
        """Adds a CtrlSpace object above this object - inserted here to work on Transforms

        Args:
            name (string): optional name for this CtrlSpace, default is same as
                this object

        Returns:
            object: New CtrlSpace object

        """

        if name is None:
            name = ctrl.getName()

        newCtrlSpace = CtrlSpace(name, parent=ctrl.getParent())
        if ctrl.getParent() is not None:
            ctrl.getParent().removeChild(ctrl)

        if ctrl.getMetaDataItem("altLocation"):
            newCtrlSpace.setMetaDataItem("altLocation", ctrl.getMetaDataItem("altLocation"))

        ctrl.setParent(newCtrlSpace)
        newCtrlSpace.addChild(ctrl)

        newCtrlSpace.xfo = Xfo(ctrl.xfo)

        # To ensure that names of control spaces don't clash with controls and
        # if they do, set's the control space's name back to what it was intended
        if ctrl.getName() == name:
            newCtrlSpace.setName(name)

        return newCtrlSpace


    def insertAttachSpace(self, jnt, name=None):
        """Adds a AttachControl object above this object
        """
        if name is None:
            name = jnt.getName()

        self.attachCtrl = Control(name + '_attach', parent=self.ctrlCmpGrp, shape="null")
        self.attachCtrlSpace = self.attachCtrl.insertCtrlSpace()

        self.attachCtrlSpace.constrainTo(jnt, constraintType="Orientation", maintainOffset=False)
        self.attachCtrlSpace.constrainTo(jnt, constraintType="Position",    maintainOffset=False)

        # this is an Space which should not be animated
        self.attachCtrl.lockTranslation(x=True, y=True, z=True)
        self.attachCtrl.lockScale(x=True, y=True, z=True)
        self.attachCtrl.lockRotation(x=True, y=True, z=True)

        return self.attachCtrl


    def tagAllComponentJoints(self, tagNames):

        if not hasattr(tagNames, "__iter__"):
            tagNames = [tagNames]

        joints = self.deformersParent.getDescendents(classType="Joint", inheritedClass=True)
        joints = [joint for joint in joints if joint.getComponent() == self]
        for tagName in tagNames:
            for joint in joints:
                joint.appendMetaDataListItem("TAGS", tagName)

    def createConditionSolver(self, condition, ifTrue, ifFalse, result=None, name=None):

        if not name:
            try:
                name = condition.getName()+"_cond"
            except:
                name = "cond"

        condOp = KLOperator(name, 'OSS_ConditionScalarSolver', 'OSS_Kraken')
        self.addOperator(condOp)
        condOp.setInput('condition', condition)
        condOp.setInput('ifTrue', ifTrue)
        condOp.setInput('ifFalse', ifFalse)
        if result:
            condOp.setOutput('result', result)
        return condOp


    def getAttrMapping(self):

        # SHOULD BE relative TO KRG
        filePath = r"Z:/shows/wolvesProto01/source/assets/_charTemplate/rig/scripts/attrMappings.json"

        if not os.path.exists(filePath):
            print 'Error: No attrMappings json file found at %s'%filePath
            return None
        jsonFile = open(filePath, "r")
        with jsonFile as data_file:
            data = json.load(jsonFile)
        jsonFile.close()

        return data


    def createDistanceSolver(self, name, MatA, MatB, distance, distanceRelative, distanceRest=1.0):
        operator = KLOperator(str(name), 'OSS_distanceSolver', 'OSS_Kraken')
        self.addOperator(operator)
        operator.setInput('drawDebug', self.drawDebugInputAttr)
        operator.setInput('rigScale', self.rigScaleInputAttr)
        operator.setInput('distanceRest', distanceRest)
        operator.setInput('MatA', MatA)
        operator.setInput('MatB', MatB)
        operator.setOutput('distanceRelative', distanceRelative)
        return operator



    def createEvalKeyframesValueSolver(self, name, t, result, keyframeTime=[0.0,1.0], keyframeValue=[0.0,1.0], keyframeTangentIn=[Vec2(0.0,0.01),Vec2(0.0,0.01)], keyframeTangentOut =[Vec2(0.0,0.01),Vec2(0.0,0.01)]):
        operator = KLOperator(str(name), 'OSS_EvalKeyframesValueSolver', 'OSS_Kraken')
        self.addOperator(operator)
        operator.setInput('drawDebug', self.drawDebugInputAttr)
        operator.setInput('rigScale', self.rigScaleInputAttr)
        operator.setInput('t', t)
        operator.setInput('keyframeTime', keyframeTime)
        operator.setInput('keyframeValue', keyframeValue)
        operator.setInput('keyframeTangentIn', keyframeTangentIn)
        operator.setInput('keyframeTangentOut', keyframeTangentOut)
        operator.setOutput('result', result)


    def createRemapScalarValueSolver(self, name, input, result, scale=1.0, clamp=False):
        operator = KLOperator(str(name), 'OSS_RemapScalarValueSolver', 'OSS_Kraken')
        self.addOperator(operator)
        operator.setInput('drawDebug', self.drawDebugInputAttr)
        operator.setInput('rigScale', self.rigScaleInputAttr)
        operator.setInput('input', input)
        operator.setInput('scale', scale)
        operator.setInput('clamp', clamp)
        operator.setOutput('result', result)
        return operator

    def createLocalTransformSolver(self, name, inMatrix):
        TranslateOp = KLOperator(name, 'OSS_GetLocalTranslateSolver', 'OSS_Kraken') #, metaData={"altLocation":side})
        self.addOperator(TranslateOp)
        TranslateOp.setInput('drawDebug', self.drawDebugInputAttr)
        TranslateOp.setInput('rigScale', self.rigScaleInputAttr)
        TranslateOp.setInput('inMatrix', inMatrix)
        TranslateOp.setInput('inBaseMatrix', inMatrix.getParent())
        return TranslateOp

    def createScalarAttribute(self, name, group=None, groupName=None, kObject=None, force=True, lock=True):

        if not group:
            if not groupName:
                raise ("Must provide a groupName if not passing a group.")
            if not kObject:
                raise ("Must provide a kObject if not passing a group.")

            group = kObject.getAttributeGroupByName(groupName)
            if not group:
                group = AttributeGroup(groupName, parent=kObject)

        newAttr = group.getAttributeByName(name)
        if not newAttr:
            newAttr = ScalarAttribute(name, value=0.0, parent=group)
        newAttr.setLock(lock)
        return newAttr


    def isTransformAttribute(self, attrName):
        for attr in ["tx","ty","tz"]:
            if attr in attrName:
                return "t"
        for attr in ["rx","ry","rz"]:
            if attr in attrName:
                return "r"
        for attr in ["sx","sy","sz"]:
            if attr in attrName:
                return "s"
        return False


    def createAttrMappings(self, attrMappingsData):

        #shapeName = location+"_"+handleName

        controlsWithLocalTranslateSolvers = []
        controlsWithAttrGroup = []
        used_axes = {}
        opDict = defaultdict()
        # assuming attributes just live on controls should be expanded to all Nodes
        controls = self.getHierarchyNodes(classType="Control")
        connectionList = []

        # we unfortunately need to structure our dict to be per source node, not source Attr
        remapDict = {}

        hasTransformOp = []
        needsRemapOp = False
        attrGrpName = "customAttr"

        for mapping in attrMappingsData:
            source = mapping["source"]
            sourceSplt = mapping["source"].split('.')
            targetSplt = mapping["target"].split('.')

            if not source in remapDict.keys():
                remapDict[source] = {}

            if len(sourceSplt) < 2:
                continue
            else:
                srcNode = sourceSplt[0]
                srcAttr = sourceSplt[1]

            if len(targetSplt) > 1:
                tgtNode = targetSplt[0]
                tgtAttr = targetSplt[1]
            else:
                tgtNode = None
                tgtAttr = targetSplt[0]

            for control in controls:
                controlName = control.getBuildName()

                if controlName == srcNode:

                    customAttrGrp = control.getAttributeGroupByName(attrGrpName)
                    if not customAttrGrp:
                        customAttrGrp = AttributeGroup(attrGrpName, parent=control)

                    # drivingAttr  = self.createScalarAttribute(srcAttr, customAttrGrp)

                    # 1 - - - - -
                    # set up local transofmAttrs
                    transformAttrs = self.isTransformAttribute(srcAttr)
                    # we currently only support transform Attrs
                    if not transformAttrs:
                        print "Warning: We currently don't support transform attributes"
                        continue
                    else:
                        drivingAttrName = 'local' + srcAttr
                        drivingAttr  = self.createScalarAttribute(drivingAttrName, customAttrGrp)

                    if control not in hasTransformOp:
                        # if we get any transform Attrs, we need to build a LocalTransformSolver to get the local space from the src node
                        TranslateOp = self.createLocalTransformSolver(controlName, control)
                        hasTransformOp.append(control)

                    try:
                        TranslateOp.setOutput(srcAttr, drivingAttr)
                    except:
                        pass

                    drivingAttrName = 'local' + srcAttr

                    target = mapping["target"]
                    customAttrGrp = control.getAttributeGroupByName(attrGrpName)
                    #we should get rid of this
                    toTargetName = target + "_bsShape"
                    toTargetAttr = self.createScalarAttribute(toTargetName, customAttrGrp)
                    toTargetAttr.setMetaDataItem("SCALAR_OUTPUT", toTargetName)
                    toTargetAttr.appendMetaDataListItem("TAGS", self.getDecoratedName())

                    # 2 - - - - -
                    # set up Scalar Attrs
                    if mapping["operator"]["type"] == "OSS_RemapScalarValueSolver":
                        if not "clamp" in mapping["operator"].keys():
                            mapping["operator"]["clamp"] = True
                        self.createRemapScalarValueSolver(controlName+srcAttr+target, input = drivingAttr, result = toTargetAttr, scale = mapping["operator"]["scale"], clamp = mapping["operator"]["clamp"] )
                    # else:
                    #     toTargetAttr.connect(drivingAttr)
        # print json.dumps(opDict, indent=4, sort_keys=True)

    def createRBFWeightsSolver(self, driver, driverParent, attrParent=None, kernel=0, keyType=3, eulerPoses=None, eulerRotationOrder=None, poseAttrs=None,  useTwist=True,  attrPrefix=None, attrSuffix = None, twistAxis = 0, name=None):  # RadialBasisKernel_Multiquadric, Quat / Color

        if not name:
            try:
                name = condition.getName()
            except:
                name = "rbf"

        if not attrParent:
            attrParent = driver

        if not eulerPoses:
            eulerPoses = {
                "default": [0, 0, 0],
                "down": [0, 0, 90],
                "up": [0, 0, -90],
                "forward": [0, 90, 0],
                "back": [0, -90, 0]
            }

        if attrPrefix is None:
            attrPrefix = name+"_RBF_"

        if attrSuffix is None:
            attrSuffix = "_rbf"

        rbfOp = KLOperator(name+"_rbf", 'OSS_RBFWeightSolver', 'OSS_Kraken')
        self.addOperator(rbfOp)

        rbfAttrGroup = AttributeGroup("RBF", parent=attrParent)

        # Add Att Inputs
        rbfOp.setInput('drawDebug', self.drawDebugInputAttr)
        rbfOp.setInput('rigScale', self.rigScaleInputAttr)

        # Add Xfo Inputs
        rbfOp.setInput('kernel', ScalarAttribute("kernel", value=3, parent=rbfAttrGroup))  # RadialBasisKernel_Gaussian
        rbfOp.setInput('keyType', 3)  # 2=Vec3 , 3=Quat
        rbfOp.setInput('epsilon', ScalarAttribute("epsilon", value=-1.0, parent=rbfAttrGroup))
        rbfOp.setInput('useTwist',  BoolAttribute("useTwist", value=useTwist, parent=rbfAttrGroup))
        rbfOp.setInput('twistAxis', IntegerAttribute("twistAxis", value=twistAxis, parent=rbfAttrGroup))
        rbfOp.setInput('drivers', [driver])
        rbfOp.setInput('driverParents', [driverParent])

        # Note, sources to diver and driverParent must be evaluated before this call!
        rbfOp.setInput('driverLocalOffsets', [driverParent.xfo.inverse() * driver.xfo])

        xfoPoses = []
        if not poseAttrs:
            poseAttrs = []
        for posename, euler in eulerPoses.iteritems():
            xfo = Xfo()
            xfo.ori.setFromEulerAnglesWithRotOrder(
                Vec3(
                    Math_degToRad(euler[0]),
                    Math_degToRad(euler[1]),
                    Math_degToRad(euler[2])),
                    eulerRotationOrder
                    )
            xfoPoses.append(xfo)
            if len(poseAttrs) < len(eulerPoses):
                poseAttrs.append(ScalarAttribute(('').join([attrPrefix,posename,attrSuffix]), value=0.0, parent=rbfAttrGroup))

        rbfOp.setInput('poses', xfoPoses)
        # Add weight attr Outputs
        rbfOp.setOutput('weights', poseAttrs)

        return rbfOp


    def createSimpleMathSolver(self, inputA, inputB, mode="ADD", output=None, name=None):

        if not name:
            name = mode

        mathOp = KLOperator('addVis', 'OSS_SimpleMathSolver', 'OSS_Kraken')

        self.addOperator(mathOp)

        mathOp.setInput('rigScale', self.rigScaleInputAttr)
        mathOp.setInput('drawDebug', self.drawDebugInputAttr)
        mathOp.setInput('inputA', inputA)
        mathOp.setInput('inputB', inputB)

        if mode == "ADD":
            mathOp.setInput('mode', 0)
        elif mode == "SUB":
            mathOp.setInput('mode', 1)
        elif mode == "MUL":
            mathOp.setInput('mode', 2)
        elif mode == "DIV":
            mathOp.setInput('mode', 3)

        if output:
            mathOp.setOutput('result', output)

        return mathOp


    def insertCtrlSpace(self, ctrl, name=None):
        """Adds a CtrlSpace object above this object - inserted here to work on Transforms

        Args:
            name (string): optional name for this CtrlSpace, default is same as
                this object

        Returns:
            object: New CtrlSpace object

        """

        if name is None:
            name = ctrl.getName()

        newCtrlSpace = CtrlSpace(name, parent=ctrl.getParent())
        if ctrl.getParent() is not None:
            ctrl.getParent().removeChild(ctrl)

        if ctrl.getMetaDataItem("altLocation"):
            newCtrlSpace.setMetaDataItem("altLocation", ctrl.getMetaDataItem("altLocation"))

        ctrl.setParent(newCtrlSpace)
        newCtrlSpace.addChild(ctrl)

        newCtrlSpace.xfo = Xfo(ctrl.xfo)

        # To ensure that names of control spaces don't clash with controls and
        # if they do, set's the control space's name back to what it was intended
        if ctrl.getName() == name:
            newCtrlSpace.setName(name)

        return newCtrlSpace



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
