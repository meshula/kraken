import re
from kraken.core.objects.components.base_example_component import BaseExampleComponent
from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.operators.kl_operator import KLOperator

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute
from kraken.core.objects.joint import Joint
from kraken.core.objects.locator import Locator
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.maths import *



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
        partialBlendSolver = KLOperator(name+'partial_OSS_BlendTRSConstraintSolver', 'OSS_BlendTRSConstraintSolver', 'OSS_Kraken')
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
        side_axis = AXIS_NAME_TO_TUPLE_MAP[sideAxisStr]
        nv = AXIS_NAME_TO_VEC3_MAP[aimAxisStr].cross(AXIS_NAME_TO_VEC3_MAP[sideAxisStr])
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


        NURBSCurveKLOp = KLOperator(basename+'TwistNURBSCurveKLOp', 'OSS_NURBSCurveXfoKLSolver', 'OSS_Kraken')
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


    def blend_two_xfos(self, target, sourceA, sourceB, blend=0, blendTranslate=None, blendRotate=None, blendScale=None, parentSpace=None, name=None):
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
            name = target.getName()+"_blendTRSConstraint"

        blendTRSConstraint = KLOperator(name, 'OSS_BlendTRSConstraintSolver', 'OSS_Kraken')
        self.addOperator(blendTRSConstraint)

        if parentSpace is None:
            parentSpace = self.ctrlCmpGrp

        if blendTranslate is None:
             blendTranslate = blend

        if blendRotate is None:
             blendRotate = blend

        if blendScale is None:
             blendScale = blend

        blendTRSConstraint.setInput('blendTranslate', blendTranslate)
        blendTRSConstraint.setInput('blendRotate', blendRotate)
        blendTRSConstraint.setInput('blendScale', blendScale)
        blendTRSConstraint.setInput('parentSpace', parentSpace)
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

        name = sourceObject.getName()+"_"+sourceAttribute.getName()+"_2_"+destObject.getName()+"_"+destAttribute.getName()+'_RemapScalarValueSolver'
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



    def offsetOp(self, objects, targets, offsetA, offsetB, name=None):
        """Constrain target to a blend between two source Xfos
        outputs Mat44 array of objects tranformed by the delta of OffsetA to OffsetB

        Args:
            objects (Mat44): objects that provide source Mat44
            targets (Mat44): targets after offset 
            offsetA (Mat44): First Value for Delta
            offsetB (Mat44): Second Value for Delta
        Returns:
            The KL constraint operator

        """

        if not name:
            name = offsetB.getName()+"OffsetOp"

        offsetOpp = KLOperator(name, 'OSS_offsetSolver', 'OSS_Kraken')
        self.addOperator(offsetOpp)
        offsetOpp.setInput('objects', objects)
        offsetOpp.setInput('objectsParent', [o.getParent() for o in objects])
        offsetOpp.setInput('offsetsRest', [offsetA for o in objects])
        offsetOpp.setInput('offsets', [offsetB for o in objects])
        offsetOpp.setOutput('result', targets)
        return offsetOpp


    # should 
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