"""Kraken KL - KL Builder module.

Classes:
Builder -- Component representation.

"""

import os
import json
import logging

import FabricEngine.Core as core

from kraken.core.kraken_system import ks
from kraken.core.builder import Builder
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.scene_item import SceneItem
from kraken.core.objects.control import Control
from kraken.core.objects.ctrlSpace import CtrlSpace
from kraken.core.objects.joint import Joint
from kraken.core.objects.rig import Rig
from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.components.component_input import ComponentInput
from kraken.core.objects.components.component_output import ComponentOutput
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.operators.operator import Operator
from kraken.core.objects.operators.kl_operator import KLOperator
from kraken.core.objects.operators.canvas_operator import CanvasOperator
from kraken.core.objects.constraints.constraint import Constraint
from kraken.core.objects.constraints.pose_constraint import PoseConstraint
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.maths.vec2 import Vec2
from kraken.core.maths.vec3 import Vec3
from kraken.core.maths.quat import Quat
from kraken.core.maths.color import Color
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.mat44 import Mat44

from kraken.plugins.canvas_plugin.graph_manager import GraphManager

from kraken.log import getLogger

logger = getLogger('kraken')
logger.setLevel(logging.INFO)

def Boolean(b):
  return str(b).lower()

class Builder(Builder):
    """Builder object for building Kraken objects in KL."""

    __debugMode = None
    __outputFolder = None
    __rigTitle = None
    __canvasGraph = None
    __names = None
    __objectIdToUid = None
    __uidToName = None
    __itemByUniqueId = None
    __klMembers = None
    __klMaxUniqueId = None
    __klObjects = None
    __klAttributes = None
    __klConstraints = None
    __klSolvers = None
    __klCanvasOps = None
    __klPreCode = None
    __klConstants = None
    __klExtExecuted = None
    __klArgs = None
    __krkItems = None
    __krkAttributes = None
    __krkDeformers = None
    __krkScalarOutput = None
    __krkGlueObjectData = {}

    def __init__(self):
        super(Builder, self).__init__()

    def report(self, message):
        print "KL Builder: %s" % str(message)

    def reportError(self, error):
        self.report("Error: "+str(error))

    def hasOption(self, option):
        return self.getConfig().getMetaData(option, False)

    # ========================
    # IO Methods
    # ========================
    def setOutputFolder(self, folder):
        self.__outputFolder = folder

    # ========================
    # KL related Methods
    # ========================
    def getUniqueId(self, item, earlyExit=False):
        objectId = id(item)
        if objectId in self.__objectIdToUid:
          return self.__objectIdToUid[objectId]
        if earlyExit:
          return None
        self.__objectIdToUid[objectId] = self.__klMaxUniqueId
        self.__klMaxUniqueId = self.__klMaxUniqueId + 1
        return self.__objectIdToUid[objectId]

    def getUniqueName(self, item, earlyExit=False):
        """These are going to be KL vairable names.  Only Alphanumeric and underscores"""

        uid = self.getUniqueId(item)
        if uid in self.__uidToName:
            return self.__uidToName[uid]
        name = None

        """
        if isinstance(item, AttributeGroup):
            name = self.getUniqueName(item.getParent(), earlyExit = True) + '_' + item.getName()
        elif isinstance(item, Attribute):
            name = self.getUniqueName(item.getParent(), earlyExit = True) + '_' + item.getName()
        """
        if isinstance(item, Attribute):
            owner = item.getParent().getParent() # get 3d obj, skip attrgroup
            # owner KLItem should already exist as all 3d objects are built before any attributes
            # so getting uniqueId here will get the already exiting one for owner
            name = self.getUniqueName(owner)+'__DOT__'+item.getName()

        elif hasattr(item, 'getBuildName'):
            name = item.getBuildName()
        else:
            name = item.getName()

        if earlyExit:
            return name

        if name in self._clashingNameItems and item.isTypeOf("Object3D"):

            clashitems = self._clashingNameItems[name]
            otheritems = list(clashitems)
            otheritems.remove(item)
            tokens = item.getBuildPath().split('.')
            newBuildname = tokens.pop()
            valid = False
            while (not valid):
                valid = True
                #print("TTPrint: newBuildname: %s" % newBuildname)
                for other in otheritems:
                    #print("TTPrint: other.getBuildPath(): %s" % other.getBuildPath())

                    if other.getBuildPath().endswith(newBuildname):
                        valid = False
                        break

                if not valid:
                    newBuildname = tokens.pop()+'|'+newBuildname  # double underscores for node hier sep
            print("  Name \"%s\" clashes" % name),
            name = newBuildname.replace('|', '__PIPE__')
            print("  -- new buildName name: %s" % name.replace("__PIPE__", "|").replace("__DOT__", ".")),
            print("  -- new var name: %s" % name)


        namePrefix = name
        nameSuffix = 1
        while name in self.__names:
            name = namePrefix + str(nameSuffix)
            nameSuffix += 1

        self.__names[name] = item.getBuildPath()
        self.__uidToName[uid] = name

        return name


    def getUniqueArgMember(self, item, arg, argType):
        member = self.getUniqueName(item)

        argLookup = member + ' | ' + arg
        if argLookup in self.__klArgs['lookup']:
            return self.__klArgs['lookup'][argLookup]

        typedArgs = self.__klArgs['members'].get(argType, [])
        index = len(typedArgs)
        typedArgs.append(argLookup)

        baseArgType = argType
        if argType.find('[') > -1:
          baseArgType = argType[0:argType.find('[')]+'Array'
        argMember = 'arg_%s[%d]' % (baseArgType, index)

        self.__klArgs['lookup'][argLookup] = argMember
        self.__klArgs['members'][argType] = typedArgs

        return argMember

    def getUniqueObjectMember(self, item, argType):
        name = self.getUniqueName(item)

        if name in self.__klMembers['lookup']:
            return self.__klMembers['lookup'][name]

        if argType is None:
            return None

        # Not totally sure we want to keep the "driven" distinction around anymore...
        if isinstance(item, ScalarAttribute) and isinstance(item.getCurrentSource(), Attribute):
          argType = argType+'_Driven'

        typedArgs = self.__klMembers['members'].get(argType, [])
        index = len(typedArgs)
        typedArgs.append(name)

        constantName = str(index)
        if self.__useRigConstants:
            constantName = '%s_%s' % (self.getKLExtensionName(), name)
            self.__klConstants[constantName] = index

        member = '_%s[%s]' % (argType, constantName)
        self.__klMembers['lookup'][name] = member
        self.__klMembers['members'][argType] = typedArgs

        return member

    def getSolveMethodName(self, item):
        return 'solve_%s' % (self.getUniqueName(item))

    def __getXfoAsStr(self, xfo):
        valueStr = "Xfo(Vec3(%.4g, %.4g, %.4g), Quat(%.4g, %.4g, %.4g, %.4g), Vec3(%.4g, %.4g, %.4g))" % (
            round(xfo.tr.x, 4),
            round(xfo.tr.y, 4),
            round(xfo.tr.z, 4),
            round(xfo.ori.v.x, 4),
            round(xfo.ori.v.y, 4),
            round(xfo.ori.v.z, 4),
            round(xfo.ori.w, 4),
            round(xfo.sc.x, 4),
            round(xfo.sc.y, 4),
            round(xfo.sc.z, 4)
          )
        return valueStr

    def getKLExtensionName(self):
        return self.getConfig().getMetaData('ExtensionName')

    def __visitItem(self, item, indent=""):

        def codeItemValueFromSolver(sourceSolver):
            kOperator = sourceSolver['sceneItem']
            sourceMember = sourceSolver['member']
            sourceName = self.getUniqueName(kOperator)
            eventSolverName = sourceMember.replace('[', '').replace(']', '')
            args = kOperator.getSolverArgs()

            # output to the results!
            for i in xrange(len(args)):
                arg = args[i]
                argName = arg.name.getSimpleType()
                argDataType = arg.dataType.getSimpleType()
                argConnectionType = arg.connectionType.getSimpleType()
                if argConnectionType == 'In':
                  continue
                argMember = self.getUniqueArgMember(kOperator, argName, argDataType)
                connectedObjects = kOperator.getOutput(argName)
                if not argDataType.endswith('[]'):
                    connectedObjects = [connectedObjects]

                for j in xrange(len(connectedObjects)):
                    connected = connectedObjects[j]
                    if connected is None:
                      continue

                    if connected.getDecoratedPath() == item['sceneItem'].getDecoratedPath():
                        sourceId = self.getUniqueId(sourceSolver['sceneItem'])
                        item['sourceIds'] += [sourceId]
                        if len(sourceSolver['solveCode']) > 0:
                            item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(sourceSolver['sceneItem']))]
                        item['solveCode'] += ["", "// retrieving value for %s from solver %s of data type %s" % (member, sourceName, argDataType)]
                        if argDataType.endswith('[]'):
                            if argDataType == 'Mat44[]':
                                item['solveCode'] += ["this.%s.global = this.%s[%d];" % (member, argMember, j)]
                            elif argDataType == 'Xfo[]':
                                item['solveCode'] += ["this.%s.global = this.%s[%d].toMat44();" % (member, argMember, j)]
                            else:
                                item['solveCode'] += ["this.%s.value = this.%s[%d];" % (member, argMember, j)]
                        else:
                            if argDataType == 'Mat44':
                                item['solveCode'] += ["this.%s.global = this.%s;" % (member, argMember)]
                            elif argDataType == 'Xfo':
                                item['solveCode'] += ["this.%s.global = this.%s.toMat44();" % (member, argMember)]
                            else:
                                item['solveCode'] += ["this.%s.value = this.%s;" % (member, argMember)]
        #if item is None:
        #    print("Why is this item None?  This happens a few times, how?"
        if item is None or item.get('visited', False):
            return
        item['visited'] = True

        member = item['member']
        name = self.getUniqueName(item['sceneItem'])
        sources = item['sceneItem'].getSources()

        if isinstance(item['sceneItem'], Attribute):
            for source in sources:
                sourceItem = self.findKLItem(source)
                self.__visitItem(sourceItem)

                if source.isTypeOf("Attribute"):
                    sourceId = self.getUniqueId(sourceItem['sceneItem'])
                    item['sourceIds'] += [sourceId]
                    if len(sourceItem['solveCode']) > 0:
                        item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(sourceItem['sceneItem']))]
                    item['solveCode'] += ["this.%s.value = this.%s.value;" % (item['member'], sourceItem['member'])]
                elif source.isTypeOf("Operator"):
                    codeItemValueFromSolver(sourceItem)

        elif isinstance(item['sceneItem'], Object3D):

            #print "object  " + item['member']
            if not sources:
                item['solveCode'] += ["", "// solving global transform %s" % name]
                item['solveCode'] += ["this.%s.global = this.%s.local;" % (member, member)]
                return

            # If a 3D object is a source, it is a parent
            objects = [self.findKLObject(obj) for obj in sources if self.findKLObject(obj)]
            if len(objects) > 1:
                print ("WARNING: object %s has more than one object source: %s (Parenting to last)." % (item['sceneItem'], [o["member"] for o in objects]))

            # let's check if this objects has a source pose constraint or not, if so, it does not need to be "parented" to the above object
            # This should be more thorough because a combo position, orient, scale constraint would also satisfy this condition...
            needParentMultiply = True
            hasConstraints = False
            constraints = [self.findKLConstraint(constraint) for constraint in sources if self.findKLConstraint(constraint)]
            for sourceConstraint in constraints:
                if sourceConstraint:
                    hasConstraints = True
            solvers = [self.findKLSolver(solver) for solver in sources if self.findKLSolver(solver)]
            for sourceSolver in solvers:
                if sourceSolver:
                  needParentMultiply = False

            if len(objects) and needParentMultiply:  # if there are any sources beyond initialization and global is solved by mult w/ parent
                parent = objects[-1]
                self.__visitItem(parent)
                sourceId = self.getUniqueId(parent['sceneItem'])
                item['sourceIds'] += [sourceId]
                if len(parent['solveCode']) > 0:
                    item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(parent['sceneItem']))]
                item['solveCode'] += ["", "// solving parent child constraint %s. Possibly remove this if using a pose and scale constraint" % name]
                if self.__debugMode:
                    item['solveCode'] += ["report(\"solving parent child constraint %s\");" % name]
                item['solveCode'] += ["this.%s.global = this.%s.global * this.%s.local;" % (member, parent['member'], member)]
                item['solveCode'] += [""]

            constraints = [self.findKLConstraint(constraint) for constraint in sources if self.findKLConstraint(constraint)]
            for sourceConstraint in constraints:
                if not sourceConstraint:
                    continue

                self.__visitItem(sourceConstraint)
                sourceMember = sourceConstraint['member']
                sourceId = self.getUniqueId(sourceConstraint['sceneItem'])
                item['sourceIds'] += [sourceId]
                if len(sourceConstraint['solveCode']) > 0:
                    item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(sourceConstraint['sceneItem']))]

                #item['solveCode'] += ['this.%s.global = this.%s.compute(this.%s.global);  # This line should be in the solve!' % (member, sourceMember, member)]

            solvers = [self.findKLSolver(solver) for solver in sources if self.findKLSolver(solver)]
            for sourceSolver in solvers:
                if not sourceSolver:
                    continue

                self.__visitItem(sourceSolver)
                codeItemValueFromSolver(sourceSolver)



        elif isinstance(item['sceneItem'], Constraint):

            constraint = item['sceneItem']

            item['solveCode'] += ["", "// solving inputs for %s constraint %s" % (constraint.__class__.__name__, self.getUniqueName(constraint))]
            if self.__debugMode:
                item['solveCode'] += ["report(\"solving %s constraint %s\");" % (constraint.__class__.__name__, self.getUniqueName(constraint))]
            for i in range(len(item['constrainers'])):
                constrainer = item['constrainers'][i]
                constrainerItem = self.findKLObject(constrainer)
                self.__visitItem(constrainerItem)
                sourceId = self.getUniqueId(constrainerItem['sceneItem'])
                item['sourceIds'] += [sourceId]
                if len(constrainerItem['solveCode']) > 0:
                    item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(constrainerItem['sceneItem']))]
                item['solveCode'] += ['this.%s.constrainers[%d] = this.%s.global;' % (member, i, constrainerItem['member'])]
            constraineeItem = self.findKLObject(item['constrainee'])
            if self.__profilingFrames > 0:
                item['solveCode'] += ["{ AutoProfilingEvent scopedEvent(\"%s.compute\");" % (constraint.__class__.__name__)]
            item['solveCode'] += ['this.%s.global = this.%s.compute(this.%s.global);' % (constraineeItem['member'], item['member'], constraineeItem['member'])]
            if self.__profilingFrames > 0:
                item['solveCode'] += ["}"]


        elif isinstance(item['sceneItem'], KLOperator):

            sourceSolver = item
            kOperator = sourceSolver['sceneItem']
            sourceMember = sourceSolver['member']
            solverName = sourceSolver['buildName']
            solveMethodName = self.getSolveMethodName(kOperator)
            eventSolverName = sourceMember.replace('[', '').replace(']', '')
            args = kOperator.getSolverArgs()

            if self.__debugMode:
                logger.debug(indent+"sourceSolver: %s for item %s" % (sourceSolver['member'], item['member']))
            sourceSolver['visited'] = True

            item['solveCode'] += ["", "// solving KLSolver %s" % (solverName)]
            if self.__debugMode:
                item['solveCode'] += ["report(\"solving KLSolver %s\");" % (solverName)]
            if self.__profilingFrames > 0:
                item['solveCode'] += ["{ //AutoProfilingEvent solverEvent_%s(\"%s\");" % (solveMethodName, solveMethodName)]

            def getSolveCodeForConstantValue(argMember, argDataType, value):
                code = []
                if isinstance(value, (float, int)):
                    code += ["this.%s = %.4g;" % (argMember, value)]
                elif isinstance(value, str):
                    code += ["this.%s = '%s';" % (argMember, value)]
                elif isinstance(value, bool):
                    if value:
                        code += ["this.%s = true;" % (argMember, j)]
                    else:
                        code += ["this.%s = false;" % (argMember, j)]
                elif isinstance(value, Vec2):
                    code += ["this.%s = Vec2(%.4g, %.4g);" % (argMember, value.x, value.y)]
                elif isinstance(value, Vec3):
                    code += ["this.%s = Vec3(%.4g, %.4g, %.4g);" % (argMember, value.x, value.y, value.z)]
                elif isinstance(value, Quat):
                    code += ["this.%s = Quat(%.4g, %.4g, %.4g, %.4g);" % (argMember, value.v.x, value.v.y, value.v.z, value.w)]
                elif isinstance(value, Color):
                    code += ["this.%s = Color(%.4g, %.4g, %.4g, %.4g);" % (argMember, value.r, value.g, value.b, value.a)]
                elif isinstance(value, Xfo):
                    valueStr = 'Xfo(Vec3(%.4g, %.4g, %.4g), Quat(%.4g, %.4g, %.4g, %.4g), Vec3(%.4g, %.4g, %.4g))' % (
                        value.tr.x, value.tr.y, value.tr.z,
                        value.ori.v.x, value.ori.v.y, value.ori.v.z, value.ori.w,
                        value.sc.x, value.sc.y, value.sc.z
                        )
                    if argDataType.startswith('Mat44'):
                        code += ["this.%s = %s.toMat44();" % (argMember, valueStr)]
                    else:
                        code += ["this.%s = %s;" % (argMember, valueStr)]
                elif isinstance(value, Mat44):
                    valueStr = 'Mat44(Vec4(%.4g, %.4g, %.4g, %.4g), Vec4(%.4g, %.4g, %.4g, %.4g), Vec4(%.4g, %.4g, %.4g, %.4g), Vec4(%.4g, %.4g, %.4g, %.4g))' % (
                        value.row0.x, value.row0.y, value.row0.z, value.row0.t,
                        value.row1.x, value.row1.y, value.row1.z, value.row1.t,
                        value.row2.x, value.row2.y, value.row2.z, value.row2.t,
                        value.row3.x, value.row3.y, value.row3.z, value.row3.t
                        )
                    code += ['this.%s = %s;' % (argMember, valueStr)]
                else:
                    raise Exception("Constant value has an unsupported type: %s" % value)

                return code

            # first let's find all args which are arrays and prepare storage
            for i in xrange(len(args)):
                arg = args[i]
                argName = arg.name.getSimpleType()
                argDataType = arg.dataType.getSimpleType()
                argConnectionType = arg.connectionType.getSimpleType()
                connectedObjects = None
                argMember = self.getUniqueArgMember(kOperator, argName, argDataType)
                isArray = argDataType.endswith('[]')

                if argConnectionType == 'In':
                    connectedObjects = kOperator.getInput(argName)
                elif argConnectionType in ['IO', 'Out']:
                    connectedObjects = kOperator.getOutput(argName)

                if isArray:
                    item['solveCode'] += ["this.%s.resize(%d);" % (argMember, len(connectedObjects))]
                    if argConnectionType == 'Out':
                        continue
                    for j in xrange(len(connectedObjects)):
                        connected = connectedObjects[j]
                        if connected is None:
                            continue

                        if not isinstance(connected, SceneItem):
                            item['solveCode'] += getSolveCodeForConstantValue('%s[%d]' % (argMember, j), argDataType, connected)
                            continue

                        self.__visitItem(self.findKLItem(connected))
                        sourceId = self.getUniqueId(connected)
                        item['sourceIds'] += [sourceId]
                        if len(self.findKLItem(connected)['solveCode']) > 0:
                            item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(connected))]

                        if isinstance(connected, Attribute):
                            connectedObj = self.findKLAttribute(connected)
                            item['solveCode'] += ["this.%s[%d] = this.%s.value;" % (argMember, j, connectedObj['member'])]
                            continue
                        elif isinstance(connected, SceneItem):
                            connectedObj = self.findKLObject(connected)
                            item['solveCode'] += ["this.%s[%d] = this.%s.global;" % (argMember, j, connectedObj['member'])]
                        elif isinstance(connected, Xfo):
                            if argDataType == "Mat44[]":
                                item['solveCode'] += ["this.%s[%d] = %s.toMat44();" % (argMember, j, self.__getXfoAsStr(connected))]
                            else:
                                item['solveCode'] += ["this.%s[%d] = %s;" % (argMember, j, self.__getXfoAsStr(connected))]
                        elif isinstance(connected, str):
                            item['solveCode'] += ["this.%s[%d] = \"%s\";" % (argMember, j, connected)]
                        else:
                            item['solveCode'] += ["this.%s[%d] = %s;" % (argMember, j, str(connected))]

                    continue

                if argConnectionType == 'Out':
                    continue

                connected = connectedObjects
                if connected is None:
                    continue

                if not isinstance(connected, SceneItem):
                    item['solveCode'] += getSolveCodeForConstantValue(argMember, argDataType, connected)
                    continue

                self.__visitItem(self.findKLItem(connected))
                sourceId = self.getUniqueId(connected)
                item['sourceIds'] += [sourceId]
                if len(self.findKLItem(connected)['solveCode']) > 0:
                    item['solveCode'] += ["this.%s();" % (self.getSolveMethodName(connected))]

                if isinstance(connected, Attribute):
                    connectedObj = self.findKLAttribute(connected)
                    item['solveCode'] += ["this.%s = this.%s.value;" % (argMember, connectedObj['member'])]

                elif isinstance(connected, SceneItem):
                    connectedObj = self.findKLObject(connected)
                    item['solveCode'] += ["this.%s = this.%s.global;" % (argMember, connectedObj['member'])]

                elif isinstance(connected, Xfo):
                    if argDataType == "Mat44":
                        item['solveCode'] += ["this.%s = %s.toMat44();" % (argMember, self.__getXfoAsStr(connected))]
                    else:
                        item['solveCode'] += ["this.%s = %s;" % (argMember, self.__getXfoAsStr(connected))]
                elif isinstance(connected, str):
                    item['solveCode'] += ["this.%s = \"%s\";" % (argMember, connected)]
                elif isinstance(connected, bool):
                    item['solveCode'] += ["this.%s = %s;" % (argMember, str(connected).lower())]
                else:
                    item['solveCode'] += ["this.%s = %s;" % (argMember, str(connected))]

            # perform the solve
            if self.__debugMode:
                for i in xrange(len(args)):
                    arg = args[i]
                    argName = arg.name.getSimpleType()
                    argDataType = arg.dataType.getSimpleType()
                    argConnectionType = arg.connectionType.getSimpleType()
                    if argConnectionType != 'In':
                        continue
                    item['solveCode'] += ["report(\"arg %s \" + this.%s);" % (argName, argMember)]

            if self.__profilingFrames > 0:
                item['solveCode'] += ["{ AutoProfilingEvent scopedEvent(\"%s.solve\");" % (sourceSolver["type"])]

            item['solveCode'] += ["this.%s.solve(" % sourceMember]
            for i in xrange(len(args)):
                arg = args[i]
                argName = arg.name.getSimpleType()
                argDataType = arg.dataType.getSimpleType()
                argMember = self.getUniqueArgMember(kOperator, argName, argDataType)
                comma = ""
                if i < len(args) - 1:
                    comma = ","

                item['solveCode'] += ["  this.%s%s" % (argMember, comma)]

            item['solveCode'] += [");"]

            if self.__profilingFrames > 0:
                item['solveCode'] += ["}", "}"]

        else:
            raise Exception('Item is of unsupported type: '+str(item['sceneItem']))

        # canvases = [self.findKLCanvasOp(canvas) for canvas in sources if self.findKLCanvasOp(canvas)]
        # for sourceCanvasOp in canvases:

        #     sourceMember = sourceCanvasOp['member']
        #     kOperator = sourceCanvasOp['sceneItem']

        #     # todo...
        #     # if not sourceCanvasOp.get('visited', False):
        #     #     sourceCanvasOp['visited'] = True
        #     #     kl += ["", "  // TODO: Canvas solver %s missing!" % sourceMember]

        #     # todo: canvas operators


    def generateKLCode(self):

        # ensure to generate a unique id for everything (except AttributeGroup which are ignored in KL for now)
        allItems = self.__klObjects + self.__klConstraints + self.__klSolvers + self.__klCanvasOps + self.__klAttributes

        self.__itemByUniqueId = {}
        for item in allItems:
            self.__itemByUniqueId[self.getUniqueId(item['sceneItem'])] = item
            item['targetIds'] = []
            item['sourceIds'] = []
            item['visited'] = False
            item['solveCode'] = []
            item['solveSources'] = []
            item['solveTargets'] = []

        for item in allItems:
            self.__visitItem(item)
            # Now that we've visited items in order and established unique names, convert back to "DCC"-like names
            item["buildName"] = self.getUniqueName(item['sceneItem']).replace("__PIPE__", "|").replace("__DOT__", ".")

        # create a map of all of the target / source relation ships
        for id in self.__itemByUniqueId:
            item = self.__itemByUniqueId[id]
            for sourceId in item['sourceIds']:
                if not sourceId in self.__itemByUniqueId:
                    continue
                if self.__debugMode:
                    print '%s (%d) is driven by %s (%d)' % (self.getUniqueName(item['sceneItem']), id, self.getUniqueName(self.__itemByUniqueId[sourceId]['sceneItem']), sourceId)
                self.__itemByUniqueId[sourceId]['targetIds'] += [id]

        controls = []
        for obj in self.__klObjects:
            if obj['sceneItem'].isTypeOf('Control'):
                controls.append(obj)

        scalarAttributes = []
        scalarAttributesDriven = []
        for attr in self.__klAttributes:
            if attr['sceneItem'].getCurrentSource():
                scalarAttributes.append(attr)
            else:
                scalarAttributesDriven.append(attr)

        for solver in self.__klSolvers:
            args = solver['sceneItem'].getSolverArgs()
            for i in xrange(len(args)):
                arg = args[i]
                argName = arg.name.getSimpleType()
                argDataType = arg.dataType.getSimpleType()
                argMember = self.getUniqueArgMember(solver['sceneItem'], argName, argDataType)

        kl = []
        kl += ["require Util;"]
        kl += ["require Math;"]
        kl += ["require Geometry;"]
        kl += ["require Kraken;"]
        kl += ["require KrakenForCanvas;"]
        kl += ["require KrakenAnimation;"]
        if self.__profilingFrames > 0:
            kl += ["require FabricStatistics;"]
            if self.__profilingLogFile:
                kl += ["require FileIO;"]
        for extension in self.__klExtensions:
            kl += ["require %s;" % extension]
        kl += [""]
        for constant in self.__klConstants:
            kl += ["const UInt32 %s = %d;" % (constant, self.__klConstants[constant])]
        kl += [""]
        kl += ["object %s : KrakenKLRig {" % self.getKLExtensionName()]
        kl += ["  Boolean useClip;"]
        kl += ["  UInt32 debugIter;"]
        kl += ["  Boolean debugSolve;"]
        kl += ["  Boolean debugDirectDrive;"]
        kl += ["  UInt32 profilingFrames;"]
        kl += ["  String solveDepthSpaces;  // used for indenting while debugSolve printing"]
        kl += ["  UInt64 evalVersion;"]
        kl += ["  Mat44 inPoseJointValues[%d];  // A pose of world-space matrices may be set here, or may not" % len(self.__klMembers['members']['KrakenJoint'])]  # IDs of joints with incoming direct drive mat44, otherwise -1
        kl += ["  SInt32 directDriveJointIDs[%d];" % len(self.__klMembers['members']['KrakenJoint'])]  # IDs of joints with incoming direct drive mat44, otherwise -1
        kl += ["  UInt32 directDriveObject3Ds[String]; // key: KrakenItem name value: index uniqueID"]
        kl += ["  Mat44 directDriveObject3DValues[];  // size AND order same as directDriveObject3Ds"]
        kl += ["  UInt32 directDriveAttrs[String]; // key: KrakenItem name value: index uniqueID"]
        kl += ["  Scalar directDriveAttrValues[];  // size AND order same as directDriveAttrs"]
        kl += ["  SInt32 solveItemIDs[]; // Rig items to call solveItem() on"]
        kl += ["  SInt32 glueControlIDs[]; // Rig controls that will be constrained to their associated joint in directDriveJointIDs[]"]
        kl += ["  SInt32 glueJointIndexes[];  // List of joints required for evaluating glueControlIDs"]
        kl += ["  UInt32 nameToUniqueID[String];"]
        kl += ["  Boolean isItemDirty[%d];" % self.__klMaxUniqueId]
        if self.__profilingFrames > 0:
            kl += ["  SInt32 profilingFrame;"]
        kl += ["  KrakenClip clip; // the default clip of the rig"]
        for argType in self.__klMembers['members']:
            kl += ["  %s _%s[%d];" % (argType.replace('_Driven', ''), argType, len(self.__klMembers['members'][argType]))]
        kl += ["  KrakenItem _KrakenItem[%d];" % len(allItems)]

        for argType in self.__klArgs['members']:
            prefix = argType
            midfix = ""
            suffix = ""
            if argType.find('[') > -1:
              prefix = argType[:-2]
              midfix = "Array"
              suffix = "[]"
            kl += ["  %s arg_%s%s[%d]%s;" % (prefix, prefix, midfix, len(self.__klArgs['members'][argType]), suffix)]
        if hasattr(self, "__klGlueConstraints") and self.__klGlueConstraints:
            kl += ["  KrakenPoseConstraint _KrakenGlueConstraint[%d];" % len(self.__klGlueConstraints)]
        kl += ["};"]
        kl += [""]

        kl += ["inline function %s() {" % self.getKLExtensionName()]
        kl += ["  this.init();"]
        kl += ["}", ""]

        kl += ["inline function UInt64 %s.getEvalVersion() {" % self.getKLExtensionName()]
        kl += ["  return this.evalVersion;"]
        kl += ["}", ""]

        kl += ["inline function %s.setDebugIterations!(in UInt32 iterations) {" % self.getKLExtensionName()]
        kl += ["  this.debugIter = iterations;"]
        kl += ["}", ""]

        kl += ["inline function %s.setDebugSolve!(in Boolean solve) {" % self.getKLExtensionName()]
        kl += ["  this.debugSolve = solve;"]
        kl += ["}", ""]

        kl += ["inline function %s.setUseClip!(in Boolean useClip) {" % self.getKLExtensionName()]
        kl += ["  this.useClip = useClip;"]
        kl += ["}", ""]

        kl += ["inline function %s.resetPose!() {" % self.getKLExtensionName()]
        kl += ["  // reset objects"]
        for obj in self.__klObjects:
            kl += ["  this.%s.local = %s.toMat44();" % (obj['member'], self.__getXfoAsStr(obj['sceneItem'].localXfo))]
        kl += ["  // reset attributes"]
        for attr in scalarAttributes:
            kl += ["  this.%s.value = %.4g;" % (attr['member'], attr['value'])]
        kl += ["}", ""]

        kl += ["inline function %s.solve!(KrakenClipContext context) {" % self.getKLExtensionName()]
        if self.__profilingFrames > 0:
            kl += ["  AutoProfilingEvent methodEvent(\"%s.solve\");" % self.getKLExtensionName()]

        kl += self.__klPreCode

        kl += ["    if (Boolean(this.debugIter) && this.debugSolve)"]
        kl += ["      report(\"this.solveItemIDs.size(): \"+this.solveItemIDs.size());"]
        kl += ["    if (this.solveItemIDs.size() == 0) {  //If we haven't set any solveItemIDs, solve all items tagged with SOLVE by  default"]
        for item in self.__krkTags.get("SOLVE", []):
            kl += ["      if (this.debugIter)"]
            kl += ["        this.solveDepthSpaces = \"\";"]
            kl += ["      this.%s();" % (self.getSolveMethodName(item['sceneItem']))]
        kl += ["    } else {"]
        kl += ["      if (Boolean(this.debugIter) && this.debugSolve)"]
        kl += ["        report(\"Solving specific solveItemIDs...\");"]
        kl += ["      for (Count i=0; i < this.solveItemIDs.size(); i++)"]
        kl += ["      {"]
        kl += ["        if (Boolean(this.debugIter) && this.debugSolve)"]
        kl += ["          this.solveDepthSpaces = \"\";"]
        kl += ["        this.solveItem(this.solveItemIDs[i]);"]
        kl += ["      }"]
        kl += ["    }"]

        kl += ["}", ""]

        kl += ["inline function %s.evaluate!(KrakenClipContext context) {" % self.getKLExtensionName()]
        if self.__profilingFrames > 0:
            kl += ["  if(this.profilingFrame >= 0)"]
            kl += ["    FabricProfilingBeginFrame(this.profilingFrame++, Float32(context.time));"]
            kl += ["  AutoProfilingEvent methodEvent(\"%s.evaluate\");" % self.getKLExtensionName()]
        kl += ["  if(this.useClip && this.clip != null) {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.clip.apply\");" % self.getKLExtensionName()]
        kl += ["    Ref<KrakenKLRig> rig = this;"]
        kl += ["    this.clip.apply(rig, context, 1.0);"]
        kl += ["  }"]
        kl += [""]
        kl += ["  this.solve(context);   // Let's do this"]
        kl += [""]
        kl += ["  this.evalVersion++;"]
        kl += [""]
        kl += ["  if (this.debugIter)"]
        kl += ["    this.debugIter -= 1;"]
        kl += [""]
        if self.__profilingFrames > 0:
            kl += ["  this.processProfiling();"]
        kl += ["}", ""]
        kl += [""]
        kl += ["inline function %s.evaluate!(KrakenClipContext context, io Mat44 joints<>) {" % self.getKLExtensionName()]
        kl += [""]
        if self.__profilingFrames > 0:
            kl += ["  if(this.profilingFrame >= 0)"]
            kl += ["    FabricProfilingBeginFrame(this.profilingFrame++, Float32(context.time));"]
            kl += ["  AutoProfilingEvent methodEvent(\"%s.evaluate\");" % self.getKLExtensionName()]
        kl += [""]
        kl += ["  if(joints.size() != %d)" % len(self.__krkDeformers)]
        kl += ["    throw(\"%s.evaluate: Expected number of joints does not match (\"+joints.size()+\" given, %d expected).\");" % (self.getKLExtensionName(), len(self.__krkDeformers))]
        kl += [""]
        kl += ["  if(this.useClip && this.clip != null) {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.clip.apply\");" % self.getKLExtensionName()]
        kl += ["    Ref<KrakenKLRig> rig = this;"]
        kl += ["    this.clip.apply(rig, context, 1.0);"]
        kl += ["  }"]
        kl += [""]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SettingDirectDriveJoints\");" % self.getKLExtensionName()]
        kl += ["    // Set Direct Drive Xfo Values if any"]
        kl += ["    for(Count j=0; j<this.directDriveJointIDs.size(); j++) {"]
        kl += ["      if (this.directDriveJointIDs[j] == -1)"]
        kl += ["        continue;"]
        kl += ["       this.setObject3DGlobalMat44ById(this.directDriveJointIDs[j], context.directDriveJoints[j]); "]
        kl += ["       for (Count i=0; i < KrakenJoint(this._KrakenItem[this.directDriveJointIDs[j]]).identicalSourceObject3DUniquIds.size(); i++)   // Hack"]
        kl += ["         this.setObject3DGlobalMat44ById(KrakenJoint(this._KrakenItem[this.directDriveJointIDs[j]]).identicalSourceObject3DUniquIds[i], context.directDriveJoints[j]);  // Hack"]
        kl += ["      "]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SettingDDJointsCleanSecondTime\");" % self.getKLExtensionName()]
        kl += ["    // Again, set the direct drive joints to be clean because the setObject3DGlobalMat44ById may have dirtied some"]
        kl += ["    for(Count j=0; j<this.directDriveJointIDs.size(); j++) {"]
        kl += ["      if (this.directDriveJointIDs[j] == -1)"]
        kl += ["        continue;"]
        kl += ["      if (this.debugIter)"]
        kl += ["          report(\"Debug: %s.evaluate() : this.isItemDirty[this.directDriveJointIDs[\"+j+\"]] = false; // \"+this._KrakenItem[this.directDriveJointIDs[j]].name);" % (self.getKLExtensionName())]
        kl += ["      this.isItemDirty[this.directDriveJointIDs[j]] = false;"]
        kl += ["      for (Count i=0; i < KrakenJoint(this._KrakenItem[this.directDriveJointIDs[j]]).identicalSourceObject3DUniquIds.size(); i++)   // Hack"]
        kl += ["      {"]
        kl += ["        if (this.debugIter)"]
        kl += ["          report(\"Debug: %s.evaluate() : this.isItemDirty[this._KrakenItem[this.directDriveJointIDs[\"+j+\"]].identicalSourceObject3DUniquIds[\"+i+\"]]= false; // \"+this._KrakenItem[KrakenJoint(this._KrakenItem[this.directDriveJointIDs[j]]).identicalSourceObject3DUniquIds[i]].name);" % (self.getKLExtensionName())]
        kl += ["        this.isItemDirty[KrakenJoint(this._KrakenItem[this.directDriveJointIDs[j]]).identicalSourceObject3DUniquIds[i]] = false;  // Hack"]
        kl += ["      }"]
        kl += ["    }"]
        kl += ["  }"]
        kl += [""]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SetDirectDriveObject3DValues\");" % self.getKLExtensionName()]
        kl += ["  // Set Direct Drive Object3D Values if any.  directDriveObject3DValues[] order is same as setObject3DGlobalMat44ById order"]
        kl += ["    Index i = 0;"]
        kl += ["    for (name, id in this.directDriveObject3Ds)  //Should iterate in insert order"]
        kl += ["    {"]
        kl += ["      this.setObject3DGlobalMat44ById(id, this.directDriveObject3DValues[i++]);"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SettingDDObject3dCleanSecondTime\");" % self.getKLExtensionName()]
        kl += ["  // Again, Set Direct Drive Object3D Values as clean.  directDriveObject3DValues[] order is same as setObject3DGlobalMat44ById order"]
        kl += ["    for (name, id in this.directDriveObject3Ds)  //Should iterate in insert order"]
        kl += ["    {"]
        kl += ["      this.isItemDirty[id] = false;"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SetDirectDriveAttributeValues\");" % self.getKLExtensionName()]
        kl += ["  // Set Direct Drive Attribute Values if any.  directDriveAttrValues[] order is same as setScalarAttributeById order"]
        kl += ["    Index i = 0;"]
        kl += ["    for (name, id in this.directDriveAttrs)  //Should iterate in insert order"]
        kl += ["    {"]
        kl += ["      this.setScalarAttributeById(id, this.directDriveAttrValues[i++]);"]
        kl += ["    }"]
        kl += ["  }"]
        kl += [""]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SettingDDAttrsCleanSecondTime\");" % self.getKLExtensionName()]
        kl += ["  // Again, Set attrValues as clean.  directDriveAttrs[] order is same as setObject3DGlobalMat44ById order"]
        kl += ["    for (name, id in this.directDriveAttrs)  //Should iterate in insert order"]
        kl += ["    {"]
        kl += ["      this.isItemDirty[id] = false;"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  {"]
        if self.__profilingFrames > 0:
            kl += ["    AutoProfilingEvent scopedEvent(\"%s.glue_controls\");" % self.getKLExtensionName()]
        kl += ["    this.glue_controls(context);"]
        kl += ["  }"]
        kl += [""]
        kl += ["  this.solve(context);  // Let's do this"]
        kl += [""]
        if len(self.__krkDeformers) > 0:
            kl += ["  {"]
            if self.__profilingFrames > 0:
                kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:transferingJoints\");" % self.getKLExtensionName()]
            kl += ["    for(Size j=0;j<%d;j++)" % len(self.__krkDeformers)]
            kl += ["      joints[j] = this._KrakenJoint[j].global;"]
            kl += ["  }"]
        kl += ["  this.evalVersion++;"]
        kl += [""]
        kl += ["  if (this.debugIter)"]
        kl += ["    this.debugIter -= 1;"]
        kl += [""]
        if self.__profilingFrames > 0:
            kl += ["  this.processProfiling();"]
        kl += ["}", ""]


        # Only create dirtyItem lists for controls, attributes that drive things, but are not driven, and any item that has a tag
        dirtiableItems = [item for item in allItems if isinstance(item['sceneItem'], (Control, Attribute)) and len(item['targetIds'])]
        for items in self.__krkTags.values():
            dirtiableItems += [item for item in items if item not in dirtiableItems]

        kl += ["inline function %s.dirtyItem!(Index uniqueId) {" % self.getKLExtensionName()]
        if self.__profilingFrames > 0:
            kl += ["  AutoProfilingEvent methodEvent(\"%s.dirtyItem\");" % self.getKLExtensionName()]
        kl += ["  if(this.isItemDirty[uniqueId])"]
        kl += ["    return;"]
        kl += ["  this.isItemDirty[uniqueId] = true;"]
        kl += ["  switch(uniqueId) {"]

        def appendUidsToDirty(item, uidsToDirty):
            for targetId in item['targetIds']:
                if targetId not in uidsToDirty:
                    uidsToDirty.append(targetId)

            # For now, let's assume that joints and their identical xfo ancestors are one in the same.  Ideally, we don't have these inbetweens
            # after the rig is optimized.  This is not ideal or infallible, but I think it will work OK for now...
            if item['sceneItem'].isTypeOf("Joint"):
                poseConstraintSource = item['sceneItem'].getCurrentSource()
                while poseConstraintSource and poseConstraintSource.isTypeOf('PoseConstraint'):
                    transformSource = poseConstraintSource.getCurrentSource()  # PoseConstraint must have a source
                    for targetId in self.findKLItem(transformSource)['targetIds']:
                        if targetId not in uidsToDirty:
                            uidsToDirty.append(targetId)
                    poseConstraintSource = transformSource.getCurrentSource()

        for item in dirtiableItems:
            kl += ["    case %d: { // %s" % (self.getUniqueId(item['sceneItem']), self.getUniqueName(item['sceneItem']))]
            uidsToDirty = []
            appendUidsToDirty(item, uidsToDirty)
            for uidToDirty in uidsToDirty:
                targetItem = self.__itemByUniqueId[uidToDirty]
                kl += ["      this.isItemDirty[%d] = true; // %s" % (uidToDirty, self.getUniqueName(targetItem['sceneItem']))]
                appendUidsToDirty(targetItem, uidsToDirty)

            kl += ["      break;"]
            kl += ["    }"]
        kl += ["  }"]
        kl += ["}", ""]

        kl += ["inline function %s.cleanItem!(Index uniqueId) {" % self.getKLExtensionName()]
        kl += ["  this.isItemDirty[uniqueId] = false;"]
        kl += ["}", ""]

        kl += ["inline function %s.dirtyAllItems!() {" % self.getKLExtensionName()]
        kl += ["  for(Size i=0;i<%d;i++)" % self.__klMaxUniqueId]
        kl += ["    this.isItemDirty[i] = true;"]
        kl += ["}", ""]

        kl += ["inline function %s.cleanAllItems!() {" % self.getKLExtensionName()]
        kl += ["  for(Size i=0;i<%d;i++)" % self.__klMaxUniqueId]
        kl += ["    this.isItemDirty[i] = false;"]
        kl += ["}", ""]

        # These are for setting values for controls and dirtying their dependents
        kl += ["inline function Mat44 %s.getControlLocalMat44(Index index) {" % self.getKLExtensionName()]
        kl += ["  return this._KrakenControl[index].local;"]
        kl += ["}", ""]

        kl += ["inline function %s.setControlLocalMat44!(Index index, Mat44 value) {" % self.getKLExtensionName()]
        kl += ["  this._KrakenControl[index].local = value;"]
        kl += ["  this.dirtyItem(this._KrakenControl[index].uniqueId);  // dirty all dependencies"]
#        kl += ["  this.isItemDirty[this._KrakenControl[index].uniqueId] = false;  // clean this"]
        kl += ["}", ""]

        kl += ["inline function Scalar %s.getScalarAttribute(Index index) {" % self.getKLExtensionName()]
        kl += ["  return this._KrakenScalarAttribute[index].value;"]
        kl += ["}", ""]

        kl += ["inline function %s.setScalarAttribute!(Index index, Scalar value) {" % self.getKLExtensionName()]
        kl += ["  this._KrakenScalarAttribute[index].value = value;"]
        kl += ["  this.dirtyItem(this._KrakenScalarAttribute[index].uniqueId);    // dirty all dependencies"]
#        kl += ["  this.isItemDirty[this._KrakenScalarAttribute[index].uniqueId] = false;  // clean this"]
        kl += ["}", ""]

        # These are for setting values for solve assuming rig is reset to all be dirty
        kl += ["inline function %s.setBoolAttributeById!(Index uniqueId, Boolean value) {" % self.getKLExtensionName()]
        kl += ["  if (this.debugIter)"]
        kl += ["  {"]
        kl += ["      report(\"Debug: %s.setBoolAttributeById() :\"+this._KrakenItem[uniqueId].name + \": \" + value);" % (self.getKLExtensionName())]
        kl += ["  }"]
        kl += ["  KrakenBoolAttribute(this._KrakenItem[uniqueId]).value = value;"]
        kl += ["  this.dirtyItem(uniqueId);  // dirty all dependencies"]
        kl += ["  this.isItemDirty[uniqueId] = false;  // clean this"]
        kl += ["}", ""]

        kl += ["inline function %s.setIntegerAttributeById!(Index uniqueId, SInt32 value) {" % self.getKLExtensionName()]
        kl += ["  if (this.debugIter)"]
        kl += ["  {"]
        kl += ["      report(\"Debug: %s.setIntegerAttributeById() :\"+this._KrakenItem[uniqueId].name + \": \" + value);" % (self.getKLExtensionName())]
        kl += ["  }"]
        kl += ["  KrakenIntegerAttribute(this._KrakenItem[uniqueId]).value = value;"]
        kl += ["  this.dirtyItem(uniqueId);  // dirty all dependencies"]
        kl += ["  this.isItemDirty[uniqueId] = false;  // clean this"]
        kl += ["}", ""]

        kl += ["inline function %s.setScalarAttributeById!(Index uniqueId, Scalar value) {" % self.getKLExtensionName()]
        kl += ["  if (this.debugIter)"]
        kl += ["  {"]
        kl += ["      report(\"Debug: \"+FUNC+\" :\"+this._KrakenItem[uniqueId].name + \": \" + value);"]
        kl += ["  }"]
        kl += ["  KrakenScalarAttribute(this._KrakenItem[uniqueId]).value = value;"]
        kl += ["  this.dirtyItem(uniqueId);  // dirty all dependencies"]
        kl += ["  this.isItemDirty[uniqueId] = false;  // clean this"]
        kl += ["}", ""]

        kl += ["inline function %s.setObject3DGlobalMat44ById!(Index uniqueId, Mat44 value) {" % self.getKLExtensionName()]
#        kl += ["if (this.debugIter)"]
#        kl += ["      report(\"Debug: %s.setObject3DGlobalMat44ById: name: \"+this._KrakenItem[uniqueId].name+\" uniqueId: \"+uniqueId+\" value: \"+value);" % self.getKLExtensionName()]
        kl += ["  if (this.debugIter)"]
        kl += ["  {"]
        kl += ["      report(\"Debug: %s.setObject3DGlobalMat44ById() this._KrakenItem[\"+uniqueId+\"].global :\"+KrakenObject3D(this._KrakenItem[uniqueId]).global);" % self.getKLExtensionName()]
        kl += ["      report(\"Debug: %s.setObject3DGlobalMat44ById() :\"+this._KrakenItem[uniqueId].name + \": \" + value);" % self.getKLExtensionName()]
        kl += ["  }"]
        kl += ["  KrakenObject3D(this._KrakenItem[uniqueId]).global = value;"]
        kl += ["  this.dirtyItem(uniqueId);  // dirty all dependencies"]
        kl += ["  this.isItemDirty[uniqueId] = false;  // clean this"]
        kl += ["}", ""]

        kl += ["inline function %s.setObject3DLocalMat44ById!(Index uniqueId, Mat44 value) {" % self.getKLExtensionName()]
        kl += ["  KrakenObject3D(this._KrakenItem[uniqueId]).local = value;"]
        kl += ["  this.dirtyItem(uniqueId);  // dirty all dependencies"]
        kl += ["  this.isItemDirty[uniqueId] = false;  // clean this"]
        kl += ["}", ""]


        kl += ["inline function %s.glue_controls!(KrakenClipContext context) {" % self.getKLExtensionName()]
        kl += ["  {"]
        kl += ["  // Note this function also sets the global value of the space items.  Not sure if that's an issue, a little more optimized that way, but we can easily fix later"]
        kl += ["    AutoProfilingEvent scopedEvent(\"%s.evaluate:SettingGlueControls\");" % self.getKLExtensionName()]
        kl += [""]
        kl += ["    KrakenObject3D control = null;  // Most likely a KrakenControl now, but maybe we use it for other things later"]
        kl += ["    KrakenJoint control_joint = null;"]
        kl += ["    KrakenObject3D space = null;"]
        kl += ["    KrakenJoint space_joint = null;"]
        kl += ["    Mat44 space_global;  // Use this instead of space.global.  We really should only be affecting the \"control\" objects"]
        kl += [""]
        kl += ["    for(Index i=0; i<this.glueControlIDs.size(); i++)"]
        kl += ["    {"]
        kl += ["        control = KrakenObject3D(this._KrakenItem[this.glueControlIDs[i]]);"]
        kl += ["        if (this.debugIter)"]
        kl += ["        {"]
        kl += ["        report(\"TTPrint: control.name: \" + control.name);"]
        kl += ["        report(\"TTPrint: control.glue_joint_index: \" + control.glue_joint_index);"]
        kl += ["        }"]
        kl += ["        if (control.glue_joint_index == -1) {"]
        kl += ["            report(\"Attempting to glue control \\\"\"+control.name+\"\\\" without specifying a driving joint.  Skipping.\");"]
        kl += ["            continue;"]
        kl += ["        }"]
        kl += ["        if (this.debugIter)"]
        kl += ["        {"]
        kl += ["          report(\"TTPrint: context.directDriveJoints[control.glue_joint_index]: \" + context.directDriveJoints[control.glue_joint_index]);"]
        kl += ["          report(\"TTPrint: control.glue_offset: \" + control.glue_offset);"]
        kl += ["        }"]
        kl += ["        control.global = context.directDriveJoints[control.glue_joint_index] * control.glue_offset;"]
        kl += ["        if (control.glue_local_or_global == false)  // local"]
        kl += ["        {"]
        kl += ["            if (control.glue_space_uniqueId != -1)"]
        kl += ["            {"]
        kl += ["                space = KrakenObject3D(this._KrakenItem[control.glue_space_uniqueId]);"]
        kl += ["                if (space.glue_joint_index != -1)"]
        kl += ["                {"]
        kl += ["                    space_global = context.directDriveJoints[space.glue_joint_index] * space.glue_offset;"]
        kl += ["                }"]
        kl += ["                else"]
        kl += ["                {"]
        kl += ["                    space_global = space.glue_offset;"]
        kl += ["                }"]
        kl += ["                control.local = space_global.inverse() * control.global;"]
        kl += ["            }"]
        kl += ["            else"]
        kl += ["            {"]
        kl += ["                control.local = Mat44(control.global);  // copy"]
        kl += ["            }"]
        kl += ["            if (this.debugIter)"]
        kl += ["            {"]
        kl += ["                report(\"Setting control \"+control.name+\" local to: \"+control.local);"]
        kl += ["            }        "]
        kl += ["        }"]
        kl += ["        this.dirtyItem(control.uniqueId);  // dirty all dependencies"]
        kl += ["    }"]
        kl += [""]
        kl += ["    for(Index i=0; i<this.glueControlIDs.size(); i++)"]
        kl += ["    {"]
        kl += ["        control = KrakenObject3D(this._KrakenItem[this.glueControlIDs[i]]);"]
        kl += ["        if (control.glue_local_or_global == true)"]
        kl += ["            this.isItemDirty[control.uniqueId] = false;  // clean if global"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["}"]


        for item in allItems:
            if len(item['solveCode']) == 0:
              continue
            sceneItem = item['sceneItem']
            kl += ["inline function %s.%s!() {" % (self.getKLExtensionName(), self.getSolveMethodName(sceneItem))]
            kl += ["  if (Boolean(this.debugIter) && this.debugSolve)"]
            kl += ["  {"]
            kl += ["    this.solveDepthSpaces = this.solveDepthSpaces+\" \";"]
            kl += ["    if(this.isItemDirty[%d])" % self.getUniqueId(sceneItem)]
            kl += ["      report(\"Debug: \"+this.solveDepthSpaces+\"%s.%s: \");" % (self.getKLExtensionName(), self.getSolveMethodName(sceneItem))]
            kl += ["    else"]
            kl += ["      report(\"Debug: \"+this.solveDepthSpaces+\"// %s.%s (CLEAN): \");" % (self.getKLExtensionName(), self.getSolveMethodName(sceneItem))]
            kl += ["  }"]
            kl += ["  if(!this.isItemDirty[%d])" % self.getUniqueId(sceneItem)]
            kl += ["  {"]
            kl += ["    if (Boolean(this.debugIter) && this.debugSolve)"]
            kl += ["      this.solveDepthSpaces = this.solveDepthSpaces.rightStrip(1);"]
            kl += ["    return;"]
            kl += ["  }"]
            kl += ["  this.isItemDirty[%d] = false;" % self.getUniqueId(sceneItem)]
            if self.__debugMode:
                kl += ["  report(\"solving %s\ (%d)\");" % (self.getUniqueName(sceneItem), self.getUniqueId(sceneItem))]
            for solveLine in item['solveCode']:
                kl += ["  " + solveLine]
            kl += ["  if (Boolean(this.debugIter) && this.debugSolve)"]
            kl += ["  {"]
            kl += ["    this.solveDepthSpaces = this.solveDepthSpaces.rightStrip(1);"]
            kl += ["  }"]
            kl += ["}", ""]

        kl += ["inline function %s.solveItem!(Index uniqueId) {" % self.getKLExtensionName()]
        kl += ["  if (Boolean(this.debugIter) && this.debugSolve)"]
        kl += ["  {"]
        kl += ["    if(this.isItemDirty[uniqueId])"]
        kl += ["      report(\"\\nDebug: %s.solveItem: \\\"\"+this._KrakenItem[uniqueId].name+\"\\\"\");" % self.getKLExtensionName()]
        kl += ["    else"]
        kl += ["      report(\"\\nDebug: //%s.solveItem (CLEAN): \\\"\"+this._KrakenItem[uniqueId].name+\"\\\"\");" % self.getKLExtensionName()]
        kl += ["  }"]
        kl += ["  if(!this.isItemDirty[uniqueId])"]
        kl += ["    return;"]
        kl += ["  switch(uniqueId) {"]
        for item in allItems:
            if len(item['solveCode']) == 0:
                continue
            kl += ["    case %d: {" % self.getUniqueId(item['sceneItem'])]
            kl += ["      this.%s();" % self.getSolveMethodName(item['sceneItem'])]
            kl += ["      break;"]
            kl += ["    }"]
        kl += ["  }"]
        kl += ["}", ""]


        # May not need this now that KrakenItems are objects...
        kl += ["inline function %s.buildItemDict!() {" % self.getKLExtensionName()]
        kl += ["  // Build name lookup"]
        for i in range(len(allItems)):
            kl += ["  this.nameToUniqueID[\"%s\"] = %d;" % (allItems[i]['buildName'], self.getUniqueId(allItems[i]['sceneItem']))]
        kl += ["}", ""]

        allItemsSortedByUniqueIDs = [None] * len(allItems)
        kl += ["inline function %s.init!() {" % self.getKLExtensionName()]
        kl += ["    this.useClip = true;"]
        kl += ["    this.debugIter = 0;"]
        kl += ["    this.debugSolve = 0;"]
        kl += ["    this.debugDirectDrive = 0;"]
        kl += ["    this.profilingFrames = %d;" % self.__profilingFrames]
        kl += ["    this.profilingFrame = -1;"]
        kl += ["    this.solveDepthSpaces = \"\";"]
        kl += ["  Float32 floatAnimation[String];"]
        kl += [""]
        kl += ["  for(Count j=0; j<this.directDriveJointIDs.size(); j++)"]
        kl += ["    this.directDriveJointIDs[j] = -1;  //no entry for this index"]
        kl += [""]
        if self.__debugMode:
            kl += ["  // build 3D objects"]
        for obj in self.__klObjects:
            uniqueId = self.getUniqueId(obj['sceneItem'])
            allItemsSortedByUniqueIDs[uniqueId] = obj
            memberName = obj['member']
            kl += ["  this.%s = %s();" % (memberName, obj['type'])]
            kl += ["  this.%s.name = \"%s\";" % (memberName, obj['buildName'])]
            kl += ["  this.%s.uniqueId = %d;" % (memberName, uniqueId)]
            if obj["buildName"] in self.__krkGlueObjectData.keys():
                jointIndex = self.__krkGlueObjectData[obj["buildName"]].get("jointIndex")
                if jointIndex is not None:
                    kl += ["  this.%s.glue_joint_index = %d;" % (memberName, jointIndex)]
                mat44Str = self.__getXfoAsStr(self.__krkGlueObjectData[obj["buildName"]].get("offsetXfo"))+".toMat44()"
                kl += ["  this.%s.glue_offset = %s;" % (memberName, mat44Str)]
                spaceId = self.__krkGlueObjectData[obj["buildName"]].get("spaceId")
                if spaceId is not None:
                    kl += ["  this.%s.glue_space_uniqueId = %d;" % (memberName, spaceId)]

            # Hack to treat the xfo sources of a joint like the joint in dg // Ideally this is gone if/when we add optimization to kraken
            if obj['sceneItem'].isTypeOf("Joint"):
                poseConstraintSource = obj['sceneItem'].getCurrentSource()
                while poseConstraintSource and poseConstraintSource.isTypeOf('PoseConstraint'):
                    transformSource = poseConstraintSource.getCurrentSource()  # PoseConstraint must have a source
                    kl += ["  this.%s.identicalSourceObject3DUniquIds.push(%d);  // %s" % (memberName, self.getUniqueId(transformSource), self.findKLItem(transformSource)['buildName'])]
                    poseConstraintSource = transformSource.getCurrentSource()

            if self.__debugMode:
                kl += ["  this.%s.buildName = \"%s\";" % (memberName, obj['buildName'])]
                kl += ["  this.%s.path = \"%s\";" % (memberName, obj['path'])]
                kl += ["  this.%s.layer = \"%s\";" % (memberName, obj.get('layer', ''))]
                kl += ["  this.%s.component = \"%s\";" % (memberName, obj.get('component', ''))]
                kl += ["  this.%s.visibility = %s;" % (memberName, Boolean(obj.get('visibility', False)))]
                kl += ["  this.%s.color = %s;" % (memberName, obj.get('color', 'Color(0.0, 0.0, 0.0, 1.0)'))]

        kl += ["", "  // build constraints"]
        for constraint in self.__klConstraints:
            uniqueId = self.getUniqueId(constraint['sceneItem'])
            allItemsSortedByUniqueIDs[uniqueId] = constraint
            memberName = constraint['member']
            kl += ["  this.%s = %s();" % (memberName, constraint['type'])]
            kl += ["  this.%s.name = \"%s\";" % (memberName, constraint['buildName'])]
            kl += ["  this.%s.uniqueId = %d;" % (memberName, uniqueId)]
            if constraint['sceneItem'].getMaintainOffset():
                kl += ["  this.%s.offset = %s.toMat44();" % (memberName, self.__getXfoAsStr(constraint['sceneItem'].computeOffset()))]
            kl += ["  this.%s.constrainers.resize(%d);" % (memberName, len(constraint['constrainers']))]

        kl += ["", "  // build kl solvers"]
        for solver in self.__klSolvers:
            uniqueId = self.getUniqueId(solver['sceneItem'])
            allItemsSortedByUniqueIDs[uniqueId] = solver
            memberName = solver['member']
            kl += ["  this.%s = %s();" % (memberName, solver['type'])]
            kl += ["  this.%s.name = \"%s\";" % (memberName, solver['buildName'])]
            kl += ["  this.%s.uniqueId = %d;" % (memberName, uniqueId)]

        kl += ["", "  // build kl canvas ops"]
        for canvasOp in self.__klCanvasOps:
            uniqueId = self.getUniqueId(canvasOp['sceneItem'])
            allItemsSortedByUniqueIDs[uniqueId] = canvasOp
            memberName = canvasOp['member']
            # todo....
            kl += ["  // todo: this.%s = CanvasSolver?();" % (memberName)]

        kl += ["", "  // build attributes"]
        for attr in self.__klAttributes:
            uniqueId = self.getUniqueId(attr['sceneItem'])
            allItemsSortedByUniqueIDs[uniqueId] = attr
            memberName = attr['member']

            path = attr['path']
            if not self.__debugMode:
              path = ""

            if attr['cls'] == "BoolAttribute":
                kl += ["  this.%s = Kraken%s(\"%s\", \"%s\", %s, %s, %s);" % (
                    attr['member'],
                    attr['cls'],
                    attr['buildName'],
                    path,
                    Boolean(attr['keyable']),
                    Boolean(attr['animatable']),
                    Boolean(attr['value'])
                )]
            elif attr['cls'] == "ColorAttribute":
                kl += ["  this.%s = Kraken%s(\"%s\", \"%s\", %s, %s, %s);" % (
                    attr['member'],
                    attr['cls'],
                    attr['buildName'],
                    path,
                    Boolean(attr['keyable']),
                    Boolean(attr['animatable']),
                    "Color(%.4g, %.4g, %.4g, %.4g)" % (
                        attr['value'].r,
                        attr['value'].g,
                        attr['value'].b,
                        attr['value'].a
                    )
                )]
            elif attr['cls'] == "IntegerAttribute":
                kl += ["  this.%s = Kraken%s(\"%s\", \"%s\", %s, %s, %s, %s, %d);" % (
                    attr['member'],
                    attr['cls'],
                    attr['buildName'],
                    path,
                    Boolean(attr['keyable']),
                    Boolean(attr['animatable']),
                    attr.get('min', "-SCALAR_INFINITE"),
                    attr.get('max', "SCALAR_INFINITE"),
                    attr['value']
                )]
            elif attr['cls'] == "ScalarAttribute":
                kl += ["  this.%s = Kraken%s(\"%s\", \"%s\", %s, %s, %s, %s, %.4g, floatAnimation);" % (
                    attr['member'],
                    attr['cls'],
                    attr['buildName'],
                    path,
                    Boolean(attr['keyable']),
                    Boolean(attr['animatable']),
                    attr.get('min', "-SCALAR_INFINITE"),
                    attr.get('max', "SCALAR_INFINITE"),
                    attr['value']
                )]
            elif attr['cls'] == "StringAttribute":
                kl += ["  this.%s = Kraken%s(\"%s\", \"%s\", %s, %s, \"%s\");" % (
                    attr['member'],
                    attr['cls'],
                    attr['buildName'],
                    path,
                    Boolean(attr['keyable']),
                    Boolean(attr['animatable']),
                    attr['value']
                )]
            kl += ["  this.%s.uniqueId = %d;" % (memberName, uniqueId)]

        kl += [""]
        kl += ["  // All KrakenItems sorted by uniqueId"]
        if None in allItemsSortedByUniqueIDs:
            raise Exception("There is a None in allItemsSortedByUniqueIDs.  Somethings is weird with uniqueIds.  :(")
        for i, item in enumerate(allItemsSortedByUniqueIDs):
            kl += ["  this._KrakenItem[%d] = this.%s;" % (i, item['member'])]
        kl += [""]
        kl += ["  this.resetPose();"]
        kl += ["  this.dirtyAllItems();"]
        kl += [""]
        kl += ["  this.buildItemDict();"]
        kl += ["}", ""]

        kl += ["inline function %s.setProfilingFrames!(UInt32 numFrames) {" % self.getKLExtensionName()]
        if self.__profilingFrames > 0:
            kl += ["  this.profilingFrames = numFrames;"]
        else:
            kl += ["  report(\"*** %s.setProfilingFrames: RIG NOT BUILT WITH PROFILING CODE\");" % self.getKLExtensionName()]
        kl += ["}", ""]

        kl += ["inline function %s.startProfilingFrames!() {" % self.getKLExtensionName()]
        if self.__profilingFrames > 0:
            kl += ["  report(\"*** START %s RIG PROFILING FOR \"+ this.profilingFrames +\" Frames\");" % self.getKLExtensionName()]
            kl += ["  this.profilingFrame = 0;"]
            kl += ["  StartFabricProfilingFrames(this.profilingFrames+1);"]
        else:
            kl += ["  report(\"*** %s.startProfilingFrames RIG NOT BUILT WITH PROFILING CODE\");" % self.getKLExtensionName()]
        kl += ["}", ""]


        kl += ["inline function Boolean int_array_has(in SInt32 array[], in SInt32 search) {"]
        kl += ["    // Would be nice if KL provided this in arrays..."]
        kl += ["    Boolean found = false;"]
        kl += ["    for(Count i=0; i<array.size(); i++) {"]
        kl += ["        if (array[i] == search)"]
        kl += ["            return true;"]
        kl += ["    }"]
        kl += ["    return false;"]
        kl += ["}"]

        kl += ["inline function Xfo[] %s.getJointXfos() {" % self.getKLExtensionName()]
        kl += ["  Xfo result[](%d);" % len(self.__krkDeformers)]
        if len(self.__krkDeformers) > 0:
            kl += ["  for(Size i=0;i<%d;i++)" % len(self.__krkDeformers)]
            kl += ["    result[i] = this._KrakenJoint[i].global;"]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function String[] %s.getJointNames() {" % self.getKLExtensionName()]
        kl += ["  String result[](%d);" % len(self.__krkDeformers)]
        if len(self.__krkDeformers) > 0:
            kl += ["  for(Size i=0;i<%d;i++)" % len(self.__krkDeformers)]
            kl += ["    result[i] = this._KrakenJoint[i].name;"]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function Xfo[] %s.getAllXfos() {" % self.getKLExtensionName()]
        kl += ["  Xfo result[](%d);" % len(self.__klObjects)]
        for i in range(len(self.__klObjects)):
            kl += ["  result[%d] = this.%s.global;" % (i, self.__klObjects[i]['member'])]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function Xfo[] %s.getAllParentXfos() {" % self.getKLExtensionName()]
        kl += ["  Xfo result[](%d);" % len(self.__klObjects)]
        for i in range(len(self.__klObjects)):
            objParent = self.__klObjects[i]['sceneItem'].getParent()
            if objParent:
                kl += ["  result[%d] = this.%s.global;" % (i,self.findKLObject(objParent)['member']) ]
            else:
                kl += ["  result[%d] = Xfo();" % (i)]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function String[] %s.getAllXfoNames() {" % self.getKLExtensionName()]
        kl += ["  String result[](%d);" % len(self.__klObjects)]
        for i in range(len(self.__klObjects)):
            kl += ["  result[%d] = \"%s\";" % (i, self.__klObjects[i]['buildName'])]
        kl += ["  return result;"]
        kl += ["}", ""]



        kl += ["inline function String[] %s.getTagNames() {" % self.getKLExtensionName()]
        kl += ["  String result[](%d);" % len(self.__krkTags.keys())]
        for i, tag in enumerate(self.__krkTags.keys()):
            kl += ["  result[%d] = \"%s\";" % (i, tag)]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function String[] %s.getTagItemNames(in String tagNames[]) {" % self.getKLExtensionName()]
        kl += ["  Boolean dict[String];"]
        kl += ["  for(Count i=0; i<tagNames.size(); i++) {"]
        kl += ["    switch (tagNames[i]) {"]
        for tag, items in self.__krkTags.iteritems():
            kl += ["       case \"%s\": {" % tag]
            for item in items:
                kl += ["         dict[\"%s\"] = true;" % item['buildName']]
            kl += ["         break;"]
            kl += ["       }"]
        kl += ["     }"]
        kl += ["  }"]
        kl += ["  String result[];"]
        kl += ["  for (k, v in dict)"]
        kl += ["    result.push(k);"]
        kl += ["  return result;"]
        kl += ["}", ""]

        # To have scalar attributes drive blendShapes or anything else in the KL build,
        # assign a "SCALAR_OUTPUT" metaData string to the driver attribute and the kl builder will pick it up
        # e.g.  blendShapeAttr.setMetaDataItem("SCALAR_OUTPUT", "L_brow_out_dn_blendShape")
        if self.__krkScalarOutput:
            kl += ["inline function String[] %s.getScalarOutputNames() {" % self.getKLExtensionName()]
            kl += ["  String result[](%d);" % len(self.__krkScalarOutput)]
            for i in range(len(self.__krkScalarOutput)):
                kl += ["  result[%d] = \"%s\";" % (i, self.__krkScalarOutput[i]['sceneItem'].getMetaDataItem("SCALAR_OUTPUT"))]
            kl += ["  return result;"]
            kl += ["}", ""]

            kl += ["inline function %s.getScalarOutputValues(io Float32 weights<>) {" % self.getKLExtensionName()]
            kl += [""]
            kl += ["  if(weights.size() != %d) {" % len(self.__krkScalarOutput)]
            kl += ["    report(\"Warning: %s.getScalarOutputValues: input weights size is not 76, it is \"+weights.size());" % self.getKLExtensionName()]
            kl += ["    return;"]
            kl += ["  }"]
            for i in range(len(self.__krkScalarOutput)):
                kl += ["  weights[%d] = this.%s.value;" % (i, self.__krkScalarOutput[i]['member'])]
            kl += ["  if (this.debugIter)"]
            kl += ["    report(\"Debug: %s.getScalarOutputValues: weights = \"+weights);" % self.getKLExtensionName()]
            kl += ["}", ""]
        else:
            kl += ["inline function String[] %s.getScalarOutputNames() {" % self.getKLExtensionName()]
            kl += ["  String result[](%d);" % len(self.__krkScalarOutput)]
            kl += ["  return result;"]
            kl += ["}", ""]
            kl += ["inline function %s.getScalarOutputValues(io Float32 weights<>) {" % self.getKLExtensionName()]
            kl += ["}", ""]

        kl += ["inline function KrakenScalarAttribute<> %s.getScalarAttributes() {" % self.getKLExtensionName()]
        if len(scalarAttributes) == 0:
          kl += ["  KrakenScalarAttribute result<>;"]
        else:
          kl += ["  KrakenScalarAttribute result<>(this._KrakenScalarAttribute);"]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function KrakenScalarAttribute<> %s.getScalarAttributesDriven() {" % self.getKLExtensionName()]
        if len(scalarAttributesDriven) == 0:
          kl += ["  KrakenScalarAttribute result<>;"]
        else:
          kl += ["  KrakenScalarAttribute result<>(this._KrakenScalarAttribute_Driven);"]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function KrakenControl<> %s.getControls() {" % self.getKLExtensionName()]
        if len(controls) == 0:
          kl += ["  KrakenControl result<>;"]
        else:
          kl += ["  KrakenControl result<>(this._KrakenControl);"]
        kl += ["  return result;"]
        kl += ["}"]
        kl += [""]
        kl += ["inline function String[] %s.getControlNames() {" % self.getKLExtensionName()]
        kl += ["  String result[](this._KrakenControl.size());"]
        kl += ["  for(Count i=0; i<this._KrakenControl.size(); i++)"]
        kl += ["  {"]
        kl += ["    result[i] = this._KrakenControl[i].name;"]
        kl += ["  }"]
        kl += ["  return result;"]
        kl += ["}"]
        kl += [""]
        kl += ["inline function String[] %s.getGlueControlNames() {" % self.getKLExtensionName()]
        kl += ["  // Return the names of the controls that can be \"glue\" constrained to the inPoseJointValues skeleton"]
        kl += ["  String result[];"]
        kl += ["  for(Count i=0; i<this._KrakenControl.size(); i++)"]
        kl += ["  {"]
        kl += ["    report(\"TTPrint: this._KrakenControl[i].glue_joint_index: \" + this._KrakenControl[i].glue_joint_index);"]
        kl += ["    report(\"TTPrint: this._KrakenControl[i].name: \" + this._KrakenControl[i].name);"]
        kl += ["    if (this._KrakenControl[i].glue_joint_index != -1)"]
        kl += ["    {"]
        kl += ["     report(\"TTPrint: Pushed: \" + this._KrakenControl[i].name);"]
        kl += ["      result.push(this._KrakenControl[i].name);"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  return result;"]
        kl += ["}"]
        kl += [""]
        kl += ["inline function SInt32 %s.getUniqueID(in String name) {" % self.getKLExtensionName()]
        kl += ["     // Hmmmm... any way we can avoid double lookup?  Can we catch exception? 8|"]
        kl += ["  if (!this.nameToUniqueID.has(name))"]
        kl += ["   return -1;"]
        kl += [""]
        kl += ["  return this.nameToUniqueID[name];"]
        kl += ["}", ""]
        kl += [""]
        kl += ["inline function %s.setSolveItemIDsByNames!(in String names[], in Boolean append) {" % self.getKLExtensionName()]
        kl += ["  // Not meant to be fast!"]
        kl += ["  if (!append)"]
        kl += ["    this.solveItemIDs.resize(0);"]
        kl += [""]
        kl += ["  for(Count i=0; i<names.size(); i++) {"]
        kl += ["    SInt32 id = this.getUniqueID(names[i]);"]
        kl += ["    if (this.debugIter)"]
        kl += ["      report(\"Debug: %s.setSolveItemIDsByNames: Solve item name and uniqueId: \"+names[i]+\" = \"+id);" % self.getKLExtensionName()]
        kl += ["    if (id == -1)"]
        kl += ["        report(\"Warning: %s.setSolveItemIDsByNames joint \\\"\"+names[i]+\"\\\" not found in rig.\");" % self.getKLExtensionName()]
        kl += ["    else"]
        kl += ["        this.solveItemIDs.push(id);"]
        kl += ["  }"]
        kl += ["  if (this.debugIter)"]
        kl += ["    report(\"Debug: %s.setSolveItemIDsByNames: this.solveItemIDs: \"+this.solveItemIDs);" % self.getKLExtensionName()]
        kl += ["}", ""]


        kl += ["inline function %s.setDirectDriveJointIDsByNames!(in String names[]) {" % self.getKLExtensionName()]
        kl += ["  // Not meant to be fast!"]
        kl += ["  for(Count j=0; j<this.directDriveJointIDs.size(); j++) {"]
        kl += ["    if (this.debugIter)"]
        kl += ["      report(\"Debug: %s.setDirectDriveJointIDsByNames: Joint: \"+this._KrakenJoint[j].name);" % self.getKLExtensionName()]
        kl += ["    this.directDriveJointIDs[j] = -1;  //no entry for this index"]
        kl += ["    for(Count n=0; n<names.size(); n++) {"]
        kl += ["      SInt32 id = this.getUniqueID(names[n]);"]
        kl += ["      if (id == -1) {" ]
        kl += ["          report(\"Warning:  %s.setDirectDriveJointIDsByNames joint \\\"\"+names[n]+\"\\\" not found in rig.\");" % self.getKLExtensionName()]
        kl += ["          break;"]
        kl += ["      }"]
        kl += ["      if (this._KrakenJoint[j].uniqueId == id) {"]
        kl += ["        this.directDriveJointIDs[j] = id;"]
        kl += ["        if (this.debugIter)"]
        kl += ["          report(\"Debug: %s.setDirectDriveJointIDsByNames: yes:\");" % self.getKLExtensionName()]
        kl += ["        break;"]
        kl += ["      }"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  if (this.debugIter)"]
        kl += ["    report(\"Debug: %s.setDirectDriveJointIDsByNames: this.directDriveJointIDs: \"+this.directDriveJointIDs);" % self.getKLExtensionName()]
        kl += ["}", ""]

        kl += [""]
        kl += ["inline function String[] %s.setGlueControlIDsByNames!(in String names[], in Boolean local_or_global, in Boolean append) {" % self.getKLExtensionName()]
        kl += ["  // Not meant to be fast!"]
        kl += ["  if (!append)"]
        kl += ["    this.glueControlIDs.resize(0);"]
        kl += ["    this.glueJointIndexes.resize(0);"]
        kl += [""]
        kl += ["  String namesInOrder[];"]
        kl += ["  for(Count i=0; i<this.glueControlIDs.size(); i++) {"]
        kl += ["    namesInOrder.push(this._KrakenItem[this.glueControlIDs[i]].name);"]
        kl += ["  }"]
        kl += [""]
        kl += ["  for(Count n=0; n<names.size(); n++) {"]
        kl += ["    SInt32 id = this.getUniqueID(names[n]);"]
        kl += ["    if (this.debugIter)"]
        kl += ["      report(\"Debug: %s.setGlueControlIDsByNames: Solve item name and uniqueId: \"+names[n]+\" = \"+id);" % self.getKLExtensionName()]
        kl += ["    if (id == -1)"]
        kl += ["    {"]
        kl += ["      report(\"Warning: %s.setGlueControlIDsByNames control \\\"\"+names[n]+\"\\\" not found in rig.\");" % self.getKLExtensionName()]
        kl += ["    }"]
        kl += ["    else"]
        kl += ["    {"]
        kl += ["        KrakenObject3D control = KrakenObject3D(this._KrakenItem[id]);"]
        kl += ["        SInt32 glue_joint_index = control.glue_joint_index;"]
        kl += ["        if (glue_joint_index == -1)"]
        kl += ["        {"]
        kl += ["            report(\"Warning: %s.setGlueControlIDsByNames control \"+names[n]+\" does not have glue_joint to constrain to. Skipping.\");" % self.getKLExtensionName()]
        kl += ["            continue;"]
        kl += ["        }"]
        kl += ["        control.glue_local_or_global = local_or_global;"]
        kl += ["        namesInOrder.push(names[n]);"]
        kl += ["        this.glueControlIDs.push(id);"]
        kl += ["        {"]
        kl += ["            if (!int_array_has(this.glueJointIndexes, glue_joint_index))"]
        kl += ["                this.glueJointIndexes.push(glue_joint_index);"]
        kl += ["        }"]
        kl += ["        SInt32 spaceId = KrakenObject3D(this._KrakenItem[id]).glue_space_uniqueId;"]
        kl += ["        if (spaceId != -1)"]
        kl += ["        {"]
        kl += ["            glue_joint_index = KrakenObject3D(this._KrakenItem[spaceId]).glue_joint_index;"]
        kl += ["            if (glue_joint_index != -1)"]
        kl += ["            {"]
        kl += ["                if (!int_array_has(this.glueJointIndexes, glue_joint_index))"]
        kl += ["                    this.glueJointIndexes.push(glue_joint_index);"]
        kl += ["            }"]
        kl += ["        }"]
        kl += ["    }"]
        kl += ["  }"]
        kl += ["  if (this.debugIter)"]
        kl += ["  {"]
        kl += ["    report(\"Debug:  %s.setGlueControlIDsByNames: this.glueControlIDs: \"+this.glueControlIDs);" % self.getKLExtensionName()]
        kl += ["    report(\"Debug:  %s.setGlueControlIDsByNames: this.glueJointIndexes: \"+this.glueJointIndexes);" % self.getKLExtensionName()]
        kl += ["  }"]
        kl += [""]
        kl += ["    return namesInOrder;"]
        kl += ["}"]

        kl += [""]
        kl += ["inline function String[]   %s.getGlueJointNames()" % self.getKLExtensionName()]
        kl += ["{"]
        kl += ["    String namesInOrder[];"]
        kl += ["    for(Count i=0; i<this.glueJointIndexes.size(); i++)"]
        kl += ["    {"]
        kl += ["        if (this.glueJointIndexes[i] == -1)"]
        kl += ["            throw(\"%s.setGlueControlIDsByNames glueJointIndex is -1;  Should never happen.\");" % self.getKLExtensionName()]
        kl += ["        namesInOrder.push(this._KrakenJoint[this.glueJointIndexes[i]].name);"]
        kl += ["    }"]
        kl += ["    return namesInOrder;"]
        kl += ["}"]
        kl += [""]
        kl += ["inline function String[]  %s.setDirectDriveScalarIDsByNames!(in String names[]) {" % self.getKLExtensionName()]
        kl += ["  // Add names to the directDriveAttrs and expands directDriveAttrValues array size to match"]
        kl += ["  // Returns all directDriveAttrs names in the canonical order  this order is crucial when setting directDriveAttrValues[]"]
        kl += ["  String namesInOrder[];"]
        kl += [""]
        kl += ["    for(Count n=0; n<names.size(); n++) {"]
        kl += ["      SInt32 id = this.getUniqueID(names[n]);"]
        kl += ["      if (id == -1) {"]
        kl += ["          report(\"Warning: %s.setDirectDriveScalarIDsByNames attribute \\\"\"+names[n]+\"\\\" not found in rig.\");" % self.getKLExtensionName()]
        kl += ["          continue;"]
        kl += ["      }"]
        kl += ["      if (!this.directDriveAttrs.has(names[n])) {"]
        kl += [""]
        kl += ["        this.directDriveAttrs[names[n]] = id;"]
        kl += ["        if (this.debugIter)"]
        kl += ["          report(\"Debug: %s.setDirectDriveScalarIDsByNames: name=\"+names[n]+\" id=\"+id);" % self.getKLExtensionName()]
        kl += ["      }"]
        kl += ["    }"]
        kl += ["    for (name, id in this.directDriveAttrs)"]
        kl += ["        namesInOrder.push(name);"]
        kl += [""]
        kl += ["    this.directDriveAttrValues.resize(this.directDriveAttrs.size());"]
        kl += [""]
        kl += ["    // Return all valid names in the canonical order, this order is crucial when setting directDriveAttrValues[]"]
        kl += ["    return namesInOrder;"]
        kl += [""]
        kl += ["}"]
        kl += [""]
        kl += ["inline function String[]  %s.setDirectDriveObject3DIDsByNames!(in String names[]) {" % self.getKLExtensionName()]
        kl += ["  // Add names to the directDriveObject3Ds and expands directDriveObject3DValues array size to match"]
        kl += ["  // Returns all directDriveObject3Ds names in the canonical order  this order is crucial when setting setDirectDriveObject3DValues[]"]
        kl += ["  String namesInOrder[];"]
        kl += [""]
        kl += ["    for(Count n=0; n<names.size(); n++) {"]
        kl += ["      SInt32 id = this.getUniqueID(names[n]);"]
        kl += ["      if (id == -1) {"]
        kl += ["          report(\"Warning: %s.setDirectDriveObject3DIDsByNames Object3D \\\"\"+names[n]+\"\\\" not found in rig.\");" % self.getKLExtensionName()]
        kl += ["          continue;"]
        kl += ["      }"]
        kl += ["      if (!this.directDriveObject3Ds.has(names[n])) {"]
        kl += [""]
        kl += ["        this.directDriveObject3Ds[names[n]] = id;"]
        kl += ["        if (this.debugIter)"]
        kl += ["          report(\"Debug: %s.setDirectDriveObject3DIDsByNames: name=\"+names[n]+\" id=\"+id);" % self.getKLExtensionName()]
        kl += ["      }"]
        kl += ["    }"]
        kl += ["    for (name, id in this.directDriveObject3Ds)"]
        kl += ["        namesInOrder.push(name);"]
        kl += [""]
        kl += ["    this.directDriveObject3DValues.resize(this.directDriveObject3Ds.size());"]

        kl += ["    if (this.directDriveObject3DValues.size() > 0)"]
        kl += ["    {"]
        kl += ["        this.directDriveObject3DValues[0] = Mat44(1.0,0.0,0.0,33.0,0.0,1.0,0.0,66.0,0.0,0.0,1.0,99.0,0.0,0.0,0.0,1.0);"]
        kl += ["    }"]

        kl += [""]
        kl += ["    // Return all valid names in the canonical order, this order is crucial when setting setDirectDriveObject3DValues[]"]
        kl += ["    return namesInOrder;"]
        kl += [""]
        kl += ["}"]
        kl += [""]

        kl += ["inline function Xfo[] %s.getControlXfos() {" % self.getKLExtensionName()]
        kl += ["  Xfo result[](%d);" % len(controls)]
        if len(controls) > 0:
          kl += ["  KrakenControl controls<>(this._KrakenControl);"]
          kl += ["  for(Size i=0;i<%s;i++)" % len(controls)]
          kl += ["    result[i] = controls[i].global;"]
        kl += ["  return result;"]
        kl += ["}", ""]

        kl += ["inline function %s.setClip!(KrakenClip clip) {" % self.getKLExtensionName()]
        kl += ["  this.clip = clip;"]
        kl += ["}", ""]

        kl += ["inline function %s.loadClipFromFile!(String filePath) {" % self.getKLExtensionName()]
        kl += ["  this.clip = KrakenClip_loadFromFile(filePath);"]
        kl += ["}", ""]

        # kl += ["inline function %s.evaluateClip!(KrakenClipContext context, Ref<KrakenClip> clip) {" % self.getKLExtensionName()]
        # kl += ["  if(!clip)", "    return;"]
        # kl += ["  KrakenClip mutableClip = clip;"]
        # kl += ["  for(UInt32 i=0;i<mutableClip.getChannelCount();i++) {"]
        # kl += ["    switch(mutableClip.getChannelType(i)) {"]
        # kl += ["      case KrakenClipChannel_Float32: {"]
        # kl += ["        switch(mutableClip.getChannelName(i)) {"]
        # for attr in self.__klAttributes:
        #     if attr['cls'] != "ScalarAttribute":
        #         continue
        #     kl += ["          case \"%s.%s\": {" % (attr['sceneItem'].getParent().getParent().getBuildName(), attr['sceneItem'].getName())]
        #     kl += ["            this.%s.value = mutableClip.evaluateFloat32(i, context);" % (attr['member'])]
        #     kl += ["            break;"]
        #     kl += ["          }"]
        # kl += ["        }"]
        # kl += ["        break;"]
        # kl += ["      }"]
        # kl += ["      case KrakenClipChannel_Xfo: {"]
        # kl += ["        switch(mutableClip.getChannelName(i)) {"]
        # for obj in self.__klObjects:
        #     if not obj['sceneItem'].isTypeOf('Control'):
        #         continue
        #     kl += ["          case \"%s\": {" % obj['sceneItem'].getBuildName()]
        #     kl += ["            this.%s.xfo = mutableClip.evaluateXfo(i, context);" % (obj['member'])]
        #     kl += ["            break;"]
        #     kl += ["          }"]
        # kl += ["        }"]
        # kl += ["        break;"]
        # kl += ["      }"]
        # kl += ["    }"]
        # kl += ["  }"]
        # kl += ["}", ""]

        # kl += ["inline function %s.evaluateJointsForUnreal!(KrakenClipContext context, io Float32 result<>) {" % self.getKLExtensionName()]
        # kl += ["  Xfo xfos[];"]
        # kl += ["  this.evaluateJoints(context, xfos);"]
        # kl += ["  if(xfos.dataSize() != result.dataSize())"]
        # kl += ["    throw(\"Provided float array has incorrect size. Should be \"+xfos.size() * 10+\" floats.\");"]
        # kl += ["  UInt32 offset = 0;"]
        # kl += ["  for(Size i=0;i<xfos.size();i++) {"]
        # kl += ["    Xfo xfo = xfos[i];"]
        # kl += ["    // todo: unreal space conversion!"]
        # kl += ["    result[offset++] = xfo.ori.v.x;"]
        # kl += ["    result[offset++] = xfo.ori.v.y;"]
        # kl += ["    result[offset++] = xfo.ori.v.z;"]
        # kl += ["    result[offset++] = xfo.ori.w;"]
        # kl += ["    result[offset++] = xfo.tr.x;"]
        # kl += ["    result[offset++] = xfo.tr.y;"]
        # kl += ["    result[offset++] = xfo.tr.z;"]
        # kl += ["    result[offset++] = xfo.sc.x;"]
        # kl += ["    result[offset++] = xfo.sc.y;"]
        # kl += ["    result[offset++] = xfo.sc.z;"]
        # kl += ["  }"]
        # kl += ["}", ""]

        if self.__profilingFrames > 0:
            kl += [""]
            kl += ["inline function %s.populateOrderedEvents!(String eventName, io String sortedEvents[], String combinedEventsChildren[String][])" % self.getKLExtensionName()]
            kl += ["{"]
            kl += ["   sortedEvents.push(eventName);"]
            kl += [""]
            kl += ["   for (Count i=0; i<combinedEventsChildren[eventName].size(); i++)"]
            kl += ["   {"]
            kl += ["      this.populateOrderedEvents(combinedEventsChildren[eventName][i], sortedEvents, combinedEventsChildren);"]
            kl += ["   }"]
            kl += ["}"]
            kl += [""]
            kl += ["inline function %s.processProfiling!() {" % self.getKLExtensionName()]
            kl += ["  if(this.profilingFrame != this.profilingFrames)"]
            kl += ["    return;"]
            kl += ["  this.profilingFrame = -1;"]
            kl += ["  report(\"*** END %s RIG PROFILING\");" % self.getKLExtensionName()]
            kl += [""]
            kl += ["  ProfilingEvent events[] = GetProfilingEvents();"]
            kl += ["  if(events.size() == 0)"]
            kl += ["    return;"]
            kl += [""]
            kl += ["  // Documentation says events are not returend in order, but for now let's assume they are..."]
            kl += ["  ProfilingEvent combinedEvents[String];"]
            kl += ["  String combinedEventsChildren[String][];"]
            kl += ["  // Slower, but more flexible"]
            kl += ["  // We assume every event type happens on every frame"]
            kl += [""]

            kl += ["     String previousEvent = \"\";"]
            kl += ["     String ancestors[];"]
            kl += ["     Count currentLevel = 0;"]
            kl += ["     for(Size i=0;i<events.size();i++)"]
            kl += ["     {"]
            kl += ["  "]
            kl += ["      if (events[i].level > currentLevel)"]
            kl += ["      {"]
            kl += ["       ancestors.push(previousEvent);"]
            kl += ["      }"]
            kl += ["      else if (events[i].level < currentLevel)"]
            kl += ["      {"]
            kl += ["       for (Count l=0; l < (currentLevel - events[i].level); l++)"]
            kl += ["        ancestors.pop();"]
            kl += ["      }"]
            kl += ["  "]
            kl += ["      if (combinedEvents.has(events[i].label))"]
            kl += ["      {"]
            kl += ["       combinedEvents[events[i].label].duration += events[i].duration;"]
            kl += ["      }"]
            kl += ["      else"]
            kl += ["      {"]
            kl += ["       combinedEvents[events[i].label] = ProfilingEvent(events[i]);  // keeps properties of first instance"]
            kl += ["       String temp[];  // is there another way to create an empty string array?"]
            kl += ["       combinedEventsChildren[events[i].label] = temp;"]
            kl += ["       if (ancestors.size())"]
            kl += ["        combinedEventsChildren[ancestors[ancestors.size()-1]].push(events[i].label);"]
            kl += ["      }"]
            kl += ["      currentLevel = events[i].level;"]
            kl += ["      previousEvent = events[i].label;"]
            kl += ["     }"]
            kl += ["  "]
            kl += ["     for (eventName, children in combinedEventsChildren)"]
            kl += ["     {"]
            kl += ["      for(Count i=0; i < children.size(); i++)"]
            kl += ["      {"]
            kl += ["       Count j = i;"]
            kl += ["       while (j > 0 && combinedEvents[children[j-1]].duration < combinedEvents[children[j]].duration)"]
            kl += ["       {"]
            kl += ["        children.swap(j, j-1);"]
            kl += ["        j -= 1;"]
            kl += ["       }"]
            kl += ["      }"]
            kl += ["     }"]
            kl += [""]
            kl += ["   String orderedEventNames[];"]
            kl += ["   this.populateOrderedEvents(\"%s.evaluate\", orderedEventNames, combinedEventsChildren);" % self.getKLExtensionName()]
            kl += [""]
            kl += ["  ProfilingEvent sortedEvents[];"]
            kl += ["  for(Count i=0; i < orderedEventNames.size(); i++)"]
            kl += ["  {"]
            kl += ["    sortedEvents.push(combinedEvents[orderedEventNames[i]]);"]
            kl += ["  }"]
            kl += [""]
            kl += ["  String profilingReport = \"%s Profiling Report:\\n\";" % self.getKLExtensionName()]
            kl += ["  for(Count i=0; i < sortedEvents.size(); i++)"]
            kl += ["  {"]
            kl += ["    sortedEvents[i].duration /= %d.0;" % self.__profilingFrames]
            kl += ["    for( Size j = 0; j < sortedEvents[i].level; ++j )"]
            kl += ["      profilingReport += '  ';"]
            kl += ["    Float64 durationms = Scalar(sortedEvents[i].duration)*1000.0;"]
            kl += ["    Size ms = Size(durationms);"]
            kl += ["    durationms -= Float64(ms) / 1000.0;"]
            kl += ["    durationms *= 9999.99;"]
            kl += ["    Size msfract = Size(durationms);"]
            kl += ["    String msfractStr = msfract;"]
            kl += ["    if(durationms < 1000)"]
            kl += ["      msfractStr = \"0\" + msfractStr;"]
            kl += ["    if(durationms < 100)"]
            kl += ["      msfractStr = \"0\" + msfractStr;"]
            kl += ["    if(durationms < 10)"]
            kl += ["      msfractStr = \"0\" + msfractStr;"]
            kl += ["    profilingReport += sortedEvents[i].label + \": duration=\"+ms+\".\"+msfractStr+\" ms\\n\";"]
            kl += ["  }"]
            kl += [""]


            if self.__profilingLogFile:
                kl += ["  TextWriter writer(\"%s\");" % self.__profilingLogFile.replace('\\', '/')]
                kl += ["  writer.write(profilingReport);"]
                kl += ["  writer.close();"]
                kl += ["  report(\"Profiling log saved to '%s'\");" % self.__profilingLogFile.replace('\\', '/')]
            else:
                kl += ["  report(profilingReport);"]

            kl += ["  StopFabricProfiling();"]
            kl += ["}"]


        return "\n".join(kl)

    def getKLTestCode(self):
        kl = []
        kl += ["require %s;" % self.getKLExtensionName()]
        kl += [""]
        kl += ["operator entry() {"]
        kl += [" %s rig();" % self.getKLExtensionName()]
        kl += ["  KrakenClipContext context;"]
        if self.__profilingFrames > 0:
            kl += ["  for(SInt32 i=0;i<%d;i++) {" % self.__profilingFrames]
            kl += ["    context.time = 1.0;"]
            for obj in self.__klObjects:
                if obj['sceneItem'].isTypeOf('Control'):
                    kl += ["    rig.dirtyItem(%d);" % self.getUniqueId(obj['sceneItem'])]
                    break
            kl += ["    rig.evaluate(context);"]
            kl += ["  };"]
        else:
            kl += ["  context.time = 1.0;"]
            kl += ["  rig.evaluate(context);"]
        kl += ["}"]
        return "\n".join(kl)

    def generateKLExtension(self):
        if not self.__outputFolder:
            raise Exception("KL Builder: OutputFolder not specified!")
            return False

        klCode = self.generateKLCode()
        extName = self.getKLExtensionName()
        return [{
            "filename": "%s.kl" % extName,
            "sourceCode": klCode
        }]

    def loadKLExtension(self, reloadExt = False):
        ext = self.generateKLExtension()
        client = ks.getCoreClient()
        client.registerKLExtension(
            self.getKLExtensionName(),
            ext,
            version="1.0.0",
            loadExt=True,
            reloadExt=reloadExt
        )

    def reloadKLExtension(self):
        return self.loadKLExtension( reloadExt = True)

    def __ensureFolderExists(self, filePath):
        folder = os.path.split(filePath)[0]
        if not os.path.exists(folder):
            os.makedirs(folder)

    def saveKLExtension(self):
        ext = self.generateKLExtension()
        fpmFilePath = os.path.join(self.__outputFolder, "%s.fpm.json" % self.getKLExtensionName())
        klFilePath = os.path.join(self.__outputFolder, ext[0]['filename'])
        testFilePath = os.path.join(self.__outputFolder, "test.kl")
        fpm = """{
  \"code\": [\"%s\"],
  \"dfgPresets\": {
    \"dir\": \"DFG\",
    \"presetPath\": \"Kraken.KLRigs.%s\"
  },
  \"autoNamespace\": true
}""" % (ext[0]['filename'], self.getKLExtensionName())
        self.__ensureFolderExists(fpmFilePath)
        self.__ensureFolderExists(klFilePath)
        self.__ensureFolderExists(testFilePath)
        open(fpmFilePath, "w").write(fpm)
        open(klFilePath, "w").write(ext[0]['sourceCode'])
        open(testFilePath, "w").write(self.getKLTestCode())
        self.saveDFGPresets()
        return True

    def saveDFGPresets(self):
        client = ks.getCoreClient()
        dfgHost = client.getDFGHost()
        rigType = str(self.getKLExtensionName())

        presetFolder = os.path.join(self.__outputFolder, 'DFG')
        if not os.path.exists(presetFolder):
          os.makedirs(presetFolder)

        requireCode = "require Kraken;\nrequire KrakenAnimation;\nrequire KrakenForCanvas;\nrequire %s;\n" % self.getKLExtensionName()

        # Create preset
        filePath = os.path.join(presetFolder, 'Create.canvas')
        dfgBinding = dfgHost.createBindingToNewGraph()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("Create")
        dfgExec.addExtDep(rigType)
        var = dfgExec.addVar("rig", '%s::%s' % (self.getKLExtensionName(), rigType), rigType)
        varResult = dfgExec.addExecPort('result', client.DFG.PortTypes.Out)
        dfgExec.connectTo(var+'.value', varResult)
        func = dfgExec.addInstWithNewFunc("constructor")
        subExec = dfgExec.getSubExec(func)
        subExec.addExtDep(rigType)
        funcResult = subExec.addExecPort('result', client.DFG.PortTypes.Out, rigType)
        subExec.setCode(requireCode + "dfgEntry {\n  %s = %s();\n}\n" % (funcResult, rigType))
        dfgExec.connectTo(func+'.'+funcResult, var+'.value')
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # SetClip preset
        filePath = os.path.join(presetFolder, 'SetClip.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("SetClip")
        dfgExec.addExtDep(rigType)
        dfgExec.addExtDep('KrakenAnimation')
        funcResult = dfgExec.addExecPort('rig', client.DFG.PortTypes.IO, rigType)
        clipInput = dfgExec.addExecPort('clip', client.DFG.PortTypes.In, "KrakenClip")
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s.setClip(%s);\n}\n" % (funcResult, clipInput))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # Solve preset
        filePath = os.path.join(presetFolder, 'Solve.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("Solve")
        dfgExec.addExtDep(rigType)
        dfgExec.addExtDep('KrakenAnimation')
        funcResult = dfgExec.addExecPort('rig', client.DFG.PortTypes.IO, rigType)
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s.solve(KrakenClipContext());\n}\n" % (funcResult))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # Evaluate preset
        filePath = os.path.join(presetFolder, 'Evaluate.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("Evaluate")
        dfgExec.addExtDep(rigType)
        dfgExec.addExtDep('KrakenAnimation')
        funcResult = dfgExec.addExecPort('rig', client.DFG.PortTypes.IO, rigType)
        contextInput = dfgExec.addExecPort('context', client.DFG.PortTypes.In, "KrakenClipContext")
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s.evaluate(%s);\n}\n" % (funcResult, contextInput))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # ResetPose preset
        filePath = os.path.join(presetFolder, 'ResetPose.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("ResetPose")
        dfgExec.addExtDep(rigType)
        funcResult = dfgExec.addExecPort('rig', client.DFG.PortTypes.IO, rigType)
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s.resetPose();\n}\n" % (funcResult))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # GetJointXfos preset
        filePath = os.path.join(presetFolder, 'GetJointXfos.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("GetJointXfos")
        dfgExec.addExtDep(rigType)
        funcInput = dfgExec.addExecPort('rig', client.DFG.PortTypes.In, rigType)
        funcResult = dfgExec.addExecPort('result', client.DFG.PortTypes.Out, 'Xfo[]')
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s = %s.getJointXfos();\n}\n" % (funcResult, funcInput))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # GetAllXfos preset
        filePath = os.path.join(presetFolder, 'GetAllXfos.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("GetAllXfos")
        dfgExec.addExtDep(rigType)
        funcInput = dfgExec.addExecPort('rig', client.DFG.PortTypes.In, rigType)
        funcResult = dfgExec.addExecPort('result', client.DFG.PortTypes.Out, 'Xfo[]')
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s = %s.getAllXfos();\n}\n" % (funcResult, funcInput))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # GetJointNames preset
        filePath = os.path.join(presetFolder, 'GetJointNames.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("GetJointNames")
        dfgExec.addExtDep(rigType)
        funcInput = dfgExec.addExecPort('rig', client.DFG.PortTypes.In, rigType)
        funcResult = dfgExec.addExecPort('result', client.DFG.PortTypes.Out, 'String[]')
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s = %s.getJointNames();\n}\n" % (funcResult, funcInput))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)

        # getAllXfoNames preset
        filePath = os.path.join(presetFolder, 'GetAllXfoNames.canvas')
        dfgBinding = dfgHost.createBindingToNewFunc()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle("GetAllXfoNames")
        dfgExec.addExtDep(rigType)
        funcInput = dfgExec.addExecPort('rig', client.DFG.PortTypes.In, rigType)
        funcResult = dfgExec.addExecPort('result', client.DFG.PortTypes.Out, 'String[]')
        dfgExec.setCode(requireCode + "dfgEntry {\n  %s = %s.getAllXfoNames();\n}\n" % (funcResult, funcInput))
        content = dfgBinding.exportJSON()
        open(filePath, "w").write(content)


    def findKLItem(self, kSceneItem):
        if isinstance(kSceneItem, Attribute):
          return self.findKLAttribute(kSceneItem)
        if isinstance(kSceneItem, Constraint):
          return self.findKLConstraint(kSceneItem)
        if isinstance(kSceneItem, Operator):
          return self.findKLSolver(kSceneItem) # or findKLCanvasOp(kSceneItem)
        return self.findKLObject(kSceneItem)

    def findKLObject(self, kSceneItem):
        member = self.getUniqueObjectMember(kSceneItem, None)
        for obj in self.__klObjects:
            if obj['member'] == member:
                return obj
        return None

    def findKLAttribute(self, kAttribute):
        member = self.getUniqueObjectMember(kAttribute, None)
        for attr in self.__klAttributes:
            if attr['member'] == member:
                return attr
        return None

    def findKLConstraint(self, kConstraint):
        member = self.getUniqueObjectMember(kConstraint, None)
        for constraint in self.__klConstraints:
            if constraint['member'] == member:
                return constraint
        return None

    def findKLSolver(self, kOperator):
        member = self.getUniqueObjectMember(kOperator, None)
        for solver in self.__klSolvers:
            if solver['member'] == member:
                return solver
        return None

    """
    def findKLCanvasOp(self, kOperator):
        member = self.getUniqueObjectMember(kOperator, None)
        for canvasOp in self.__klCanvasOps:
            if canvasOp['member'] == member:
                return canvasOp
        return None
    """



    def tagKLSceneItem(self, KLItem):
        tagNames = KLItem['sceneItem'].getMetaDataItem("TAGS") or []
        for tagName in tagNames:
            if tagName not in self.__krkTags.keys():
                self.__krkTags[tagName] = [KLItem]
            elif KLItem not in self.__krkTags[tagName]:
                self.__krkTags[tagName].append(KLItem)


    def buildKLSceneItem(self, kSceneItem, buildName):

        if isinstance(kSceneItem, Rig):
            if self.getConfig().getMetaData('RigTitle', None) is None:
                self.__rigTitle = kSceneItem.getName()

        cls = kSceneItem.__class__.__name__

        if kSceneItem.isTypeOf('ComponentGroup'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('ComponentInput'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('ComponentOutput'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('Rig'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('Layer'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('CtrlSpace'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('Space'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('Curve'):
            cls = 'Control'
        elif kSceneItem.isTypeOf('Control'):
            cls = 'Control'
        elif kSceneItem.isTypeOf('Joint'):
            cls = 'Joint'
        elif kSceneItem.isTypeOf('Locator'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('HierarchyGroup'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('Container'):
            cls = 'Transform'
        elif kSceneItem.isTypeOf('Transform'):
            cls = 'Transform'
        else:
            self.reportError("buildKLSceneItem: Unexpected class " + cls)
            return False

        obj = {
            'sceneItem': kSceneItem,
            'member': self.getUniqueObjectMember(kSceneItem, "Kraken%s" % cls),
            'name': kSceneItem.getName(),
            'buildName': buildName,
            'type': "Kraken%s" % cls,
            'path': kSceneItem.getDecoratedPath(),
            'parent': None
        }

        if kSceneItem.isTypeOf('Joint'):
          self.__krkDeformers.append(obj)

        for parentName in ['layer', 'component']:
            getMethod = 'get%s' % parentName.capitalize()
            if not hasattr(kSceneItem, getMethod):
                continue
            parent = getattr(kSceneItem, getMethod)()
            if not parent:
                continue
            obj[parentName] = parent.getDecoratedPath()

        if hasattr(kSceneItem, 'getParent'):
            parent = kSceneItem.getParent()
            if not parent is None:
                obj['parent'] = parent.getDecoratedPath()

        # we should solve for all joints by default
        if kSceneItem.isTypeOf('Joint'):
            kSceneItem.appendMetaDataListItem("TAGS", "SOLVE")
        self.tagKLSceneItem(obj)

        self.__klObjects.append(obj)
        return True

    def buildKLAttribute(self, kAttribute):

        cls = kAttribute.__class__.__name__
        if kAttribute.isTypeOf('BoolAttribute'):
            cls = 'BoolAttribute'
        elif kAttribute.isTypeOf('ColorAttribute'):
            cls = 'ColorAttribute'
        elif kAttribute.isTypeOf('IntegerAttribute'):
            cls = 'IntegerAttribute'
        elif kAttribute.isTypeOf('ScalarAttribute'):
            cls = 'ScalarAttribute'
        elif kAttribute.isTypeOf('StringAttribute'):
            cls = 'StringAttribute'
        else:
            self.reportError("buildNodeAttribute: Unexpected class " + cls)
            return False

        ownerItem = self.findKLItem(kAttribute.getParent().getParent()) # get 3d obj, skip attrgroup
        # ownerItem should definitely exist as all 3d objects are built before any attributes
        # Note, buildName may be not exactly correlate to item[member], etc. as buildName takes hierarchy into account
        # Keeping both as we are needing to interface with DCC created assets (e.g. fbx skeletons)
        attr = {
            'member': self.getUniqueObjectMember(kAttribute, 'Kraken'+cls),
            'sceneItem': kAttribute,
            'name': kAttribute.getName(),
            'buildName': ownerItem['buildName']+'.'+kAttribute.getName(),
            'path': kAttribute.getDecoratedPath(),
            'cls': cls,
            'keyable': kAttribute.getKeyable(),
            'animatable': kAttribute.getAnimatable(),
            'value': kAttribute.getValue()
        }

        if cls in ['IntegerAttribute', 'ScalarAttribute']:
            if not kAttribute.getMin() is None:
              attr['min'] = kAttribute.getMin()
            if not kAttribute.getMax() is None:
              attr['max'] = kAttribute.getMax()

        self.__klAttributes.append(attr)

        if kAttribute.isTypeOf("ScalarAttribute") and kAttribute.getMetaDataItem("SCALAR_OUTPUT") is not None:
            self.__krkScalarOutput.append(attr)

        #ownerName = attr['sceneItem'].getParent().getParent().getBuildName()
        #name = "%s.%s" % (ownerName, attr['name'])

        # By default, add the scalar output attributes to the solve list.
        # They may not have any dependents, so this might be the only way they are solved
        if kAttribute.getMetaDataItem("SCALAR_OUTPUT"):
            kAttribute.appendMetaDataListItem("TAGS", "SOLVE")
        self.tagKLSceneItem(attr)

        return kAttribute

    def buildKLConstraint(self, kConstraint, buildName):
        cls = kConstraint.__class__.__name__

        constraintObj = self.findKLConstraint(kConstraint)
        if constraintObj:
            return None

        constraint = {
            'sceneItem': kConstraint,
            'member': self.getUniqueObjectMember(kConstraint, 'Kraken'+cls),
            'name': kConstraint.getName(),
            'buildName': buildName,
            'type': "Kraken%s" % cls,
            'path': kConstraint.getDecoratedPath(),
            'constrainee': kConstraint.getConstrainee(),
            'constrainers': kConstraint.getConstrainers()
        }

        self.tagKLSceneItem(constraint)

        self.__klConstraints.append(constraint)
        return kConstraint

    # ========================
    # Object3D Build Methods
    # ========================
    def buildContainer(self, kSceneItem, buildName):
        """Builds a container / namespace object.

        Args:
            kSceneItem (Object): kSceneItem that represents a container to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None


    def buildLayer(self, kSceneItem, buildName):
        """Builds a layer object.

        Args:
            kSceneItem (Object): kSceneItem that represents a layer to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None


    def buildHierarchyGroup(self, kSceneItem, buildName):
        """Builds a hierarchy group object.

        Args:
            kSceneItem (Object): kSceneItem that represents a group to be built.
            buildName (str): The name to use on the built object.

        Return:
            object: DCC Scene Item that is created.

        """

        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None


    def buildGroup(self, kSceneItem, buildName):
        """Builds a group object.

        Args:
            kSceneItem (Object): kSceneItem that represents a group to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """

        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None

    def buildJoint(self, kSceneItem, buildName):
        """Builds a joint object.

        Args:
            kSceneItem (Object): kSceneItem that represents a joint to be built.
            buildName (str): The name to use on the built object.

        Return:
            object: DCC Scene Item that is created.

        """

        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None

    def buildLocator(self, kSceneItem, buildName):
        """Builds a locator / null object.

        Args:
            kSceneItem (Object): locator / null object to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """
        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None

    def buildCurve(self, kSceneItem, buildName):
        """Builds a Curve object.

        Args:
            kSceneItem (Object): kSceneItem that represents a curve to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """
        if self.buildKLSceneItem(kSceneItem, buildName):
            return kSceneItem

        return None

    def buildControl(self, kSceneItem, buildName):
        """Builds a Control object.

        Args:
            kSceneItem (Object): kSceneItem that represents a control to be built.
            buildName (str): The name to use on the built object.

        Returns:
            object: Node that is created.

        """
        if not self.buildKLSceneItem(kSceneItem, buildName):
            return None
        return kSceneItem

    # ========================
    # Attribute Build Methods
    # ========================
    def buildBoolAttribute(self, kAttribute):
        """Builds a Bool attribute.

        Args:
            kAttribute (Object): kAttribute that represents a boolean attribute to be built.

        Return:
            bool: True if successful.

        """
        # Not great.  Technically even though vis is currently meaningless, connections/values could go through to other things in theory...
        # Later, make this more robust and check for anything that has these as source and let through...
        if kAttribute.getParent().getName() == 'implicitAttrGrp' and kAttribute.getName().lower() in ['visibility', 'shapevisibility']:
            return True
        return self.buildKLAttribute(kAttribute)

    def buildScalarAttribute(self, kAttribute):
        """Builds a Float attribute.

        Args:
            kAttribute (Object): kAttribute that represents a float attribute to be built.

        Return:
            bool: True if successful.

        """
        return self.buildKLAttribute(kAttribute)

    def buildIntegerAttribute(self, kAttribute):
        """Builds a Integer attribute.

        Args:
            kAttribute (Object): kAttribute that represents a integer attribute to be built.

        Return:
            bool: True if successful.

        """
        return self.buildKLAttribute(kAttribute)

    def buildStringAttribute(self, kAttribute):
        """Builds a String attribute.

        Args:
            kAttribute (Object): kAttribute that represents a string attribute to be built.

        Return:
            bool: True if successful.

        """
        return self.buildKLAttribute(kAttribute)

    def buildAttributeGroup(self, kAttributeGroup):
        """Builds attribute groups on the DCC object.

        Args:
            kAttributeGroup (object): Kraken object to build the attribute group on.

        Return:
            bool: True if successful.

        """
        # No such think in KL build
        return True

    def connectAttribute(self, kAttribute):
        """Connects the driver attribute to this one.

        Args:
            kAttribute (Object): Attribute to connect.

        Return:
            bool: True if successful.

        """

        # we rely completely on the SceneItem source mechanism for this
        return True


    # =========================
    # Constraint Build Methods
    # =========================
    def buildOrientationConstraint(self, kConstraint, buildName):
        """Builds an orientation constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """
        return self.buildKLConstraint(kConstraint, buildName)

    def buildPoseConstraint(self, kConstraint, buildName):
        """Builds an pose constraint represented by the kConstraint.

        Args:
            kConstraint (Object): kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """
        return self.buildKLConstraint(kConstraint, buildName)


    def buildParentConstraint(self, kConstraint, buildName):
        """Builds an parent constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """
        return self.buildKLConstraint(kConstraint, buildName)


    def buildPositionConstraint(self, kConstraint, buildName):
        """Builds an position constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """
        return self.buildKLConstraint(kConstraint, buildName)

    def buildScaleConstraint(self, kConstraint, buildName):
        """Builds an scale constraint represented by the kConstraint.

        Args:
            kConstraint (Object): Kraken constraint object to build.

        Return:
            object: dccSceneItem that was created.

        """
        return self.buildKLConstraint(kConstraint, buildName)


    # =========================
    # Operator Builder Methods
    # =========================
    def buildKLOperator(self, kOperator, buildName):
        """Builds Splice Operators on the components.

        Args:
            kOperator (Object): Kraken operator that represents a Splice operator.

            buildName (str): Name to use for built object.  Not used in KL build yet

        Return:
            bool: True if successful.

        """

        solverTypeName = kOperator.getSolverTypeName()

        solver = {
          "sceneItem": kOperator,
          "name": kOperator.getName(),
          "buildName": buildName,
          "member": self.getUniqueObjectMember(kOperator, solverTypeName),
          "path": kOperator.getDecoratedPath(),
          "type": kOperator.getSolverTypeName(),
          "buildName": buildName
        }

        self.__klSolvers.append(solver)

        if kOperator.extension != "Kraken" and kOperator.extension not in self.__klExtensions:
            self.__klExtensions.append(kOperator.extension)


        return True


    def buildCanvasOperator(self, kOperator, buildName):
        """Builds KL Operators on the components.

        Args:
            kOperator (Object): Kraken operator that represents a KL operator.

        Return:
            bool: True if successful.

        """

        raise Exception("The KL builder does not support Canvas Operators yet. (%s)" % kOperator.getDecoratedPath())

        # todo: we should only instaniate each preset once
        # and we should add functions to the kl code for each ONCE
        node = self.__canvasGraph.createNodeFromPresetSI(kOperator, kOperator.getPresetPath(), title='constructor')
        subExec = self.__canvasGraph.getSubExec(node)

        portTypeMap = {
            0: 'In',
            1: 'IO',
            2: 'Out'
        }

        canvasOp = {
          "sceneItem": kOperator,
          "name": kOperator.getName(),
          "node": node,
          "exec": subExec,
          "member": self.getUniqueName(kOperator),
          "path": kOperator.getDecoratedPath(),
          "buildName": buildName
        }
        self.__klCanvasOps.append(canvasOp)

        return False

    # ==================
    # Parameter Methods
    # ==================
    def lockParameters(self, kSceneItem):
        """Locks flagged SRT parameters.

        Args:
            kSceneItem (Object): Kraken object to lock the SRT parameters on.

        Return:
            bool: True if successful.

        """

        return True

    # ===================
    # Visibility Methods
    # ===================
    def setVisibility(self, kSceneItem):
        """Sets the visibility of the object after its been created.

        Args:
            kSceneItem (Object): The scene item to set the visibility on.

        Return:
            bool: True if successful.

        """

        obj = self.findKLObject(kSceneItem)
        if obj is None:
            return False

        obj['visibility'] = kSceneItem.getVisibility()
        return True

    # ================
    # Display Methods
    # ================
    def setObjectColor(self, kSceneItem):
        """Sets the color on the dccSceneItem.

        Args:
            kSceneItem (Object): kraken object to set the color on.

        Return:
            bool: True if successful.

        """

        obj = self.findKLObject(kSceneItem)
        if obj is None:
            return False

        value = kSceneItem.getColor()
        if value is None:
            value = self.getBuildColor(kSceneItem)
        if value:
            colors = self.config.getColors()
            c = colors[value]
            if isinstance(c, Color):
              value = c
            elif isinstance(c, list):
              value = Color(r = c[0], g = c[1], b = c[2], a = 1.0)
            else:
              value = None

        if value is None:
          return True

        valueStr = "Color(%.4g, %.4g, %.4g, %.4g)" % (
            value.r,
            value.g,
            value.b,
            value.a
          )
        obj['color'] = valueStr

        return True

    # ==================
    # Transform Methods
    # ==================
    def setTransform(self, kSceneItem):
        """Translates the transform to Maya transform.

        Args:
            kSceneItem -- Object: object to set the transform on.

        Return:
            bool: True if successful.

        """

        obj = self.findKLObject(kSceneItem)
        if obj is None:
            return False

        valueStr = self.__getXfoAsStr(kSceneItem.xfo)
        obj['initialXfo'] = kSceneItem.xfo.getRTVal().clone('Xfo')
        obj['initialXfo'].sc.x = round(obj['initialXfo'].sc.x.getSimpleType(), 4)
        obj['initialXfo'].sc.y = round(obj['initialXfo'].sc.y.getSimpleType(), 4)
        obj['initialXfo'].sc.z = round(obj['initialXfo'].sc.z.getSimpleType(), 4)

        if obj['sceneItem'].getCurrentSource() is None:
            obj['xfo'] = valueStr
        else:
            obj['globalXfo'] = valueStr
        return True

    # ==============
    # Build Methods
    # ==============
    def _preBuild(self, kSceneItem):
        """Pre-Build commands.

        Args:
            kSceneItem (Object): Kraken kSceneItem object to build.

        Return:
            bool: True if successful.

        """

        self.__rigTitle = self.getConfig().getMetaData('RigTitle', 'Rig')
        self.getConfig().setMetaData('ExtensionName', "KRK_" + self.__rigTitle.replace(' ', ''))
        self.__useRigConstants = self.getConfig().getMetaData('UseRigConstants', False)
        self.__profilingFrames = self.getConfig().getMetaData('ProfilingFrames', 0)
        self.__profilingLogFile = self.getConfig().getMetaData('ProfilingLogFile', None)
        self.__controlGlueJSONFile = self.getConfig().getMetaData('ControlGlueJSONFile', None)
        self.__canvasGraph = GraphManager()
        self.__debugMode = False
        self.__names = {}
        self.__objectIdToUid = {}
        self.__uidToName = {}
        self.__itemByUniqueId = None
        self.__klExtensions = []
        self.__klMembers = {'members': {}, 'lookup': {}}
        self.__klMaxUniqueId = 0
        self.__klObjects = []
        self.__klAttributes = []
        self.__klConstraints = []
        self.__klSolvers = []
        self.__klCanvasOps = []
        self.__klConstants = {}
        self.__klExtExecuted = False
        self.__klArgs = {'members': {}, 'lookup': {}}
        self.__klPreCode = []
        self.__krkItems = {}
        self.__krkAttributes = {}
        self.__krkDeformers = []
        self.__krkScalarOutput = []
        self.__krkTags = {}

        return True


    def _postBuild(self, kSceneItem):
        """Post-Build commands.

        Args:
            kSceneItem (object): kraken kSceneItem object to run post-build
                operations on.

        Return:
            bool: True if successful.

        """

        super(Builder, self)._postBuild(kSceneItem)

        self.loadGlueData()

        return self.saveKLExtension()

    def logOrphanedGraphItems(self, kSceneItem):
        pass  # override default. KL build doesn't build any dcc objects


    def loadGlueData(self):
        data = None
        if self.__controlGlueJSONFile:
            if not os.path.exists(self.__controlGlueJSONFile):
                raise Exception('Error: No json file found at %s' % self.__controlGlueJSONFile)
            with open(self.__controlGlueJSONFile, "r") as data_file:
                data = json.load(data_file)

        if not data:
            return

        def findKLItemByBuildName(buildName):
            for klo in self.__klObjects:
                if klo["buildName"] == buildName:
                    return klo

        controls = data.get("controls")

        self.__krkGlueObjectData = {}

        for control in controls:

            controlObj = findKLItemByBuildName(control.get("control"))
            if not controlObj:
                raise Exception("Cannot find control \"%s\"." % control["control"])

            controlJointObj = findKLItemByBuildName(control["control_joint"])
            if not controlJointObj:
                raise Exception("Cannot find control_joint \"%s\" for control \"%s\"." % (control["control_joint"], control["control"]))

            controlName = controlObj['buildName']
            self.__krkGlueObjectData[controlName] = {}
            self.__krkGlueObjectData[controlName]["jointIndex"] = self.__krkDeformers.index(controlJointObj)
            controlOffsetXfo = (controlJointObj["sceneItem"].xfo.inverse() * controlObj["sceneItem"].xfo)
            self.__krkGlueObjectData[controlName]["offsetXfo"] = controlOffsetXfo

            spaceObj = findKLItemByBuildName(control.get("space"))
            if spaceObj:
                spaceName = spaceObj["buildName"]
                self.__krkGlueObjectData[controlName]["spaceId"] = self.getUniqueId(spaceObj['sceneItem'])
                spaceJointObj = findKLItemByBuildName(control.get("space_joint"))
                if spaceName not in self.__krkGlueObjectData:
                    self.__krkGlueObjectData[spaceName] = {}
                    if spaceJointObj:
                        self.__krkGlueObjectData[spaceName]["jointIndex"] = self.__krkDeformers.index(spaceJointObj)
                        spaceOffsetXfo = (spaceJointObj["sceneItem"].xfo.inverse() * spaceObj["sceneItem"].xfo)
                    else:
                        spaceOffsetXfo = spaceObj["sceneItem"].xfo
                    self.__krkGlueObjectData[spaceName]["offsetXfo"] = spaceOffsetXfo


