"""Kraken - objects.operators.kl_operator module.

Classes:
KLOperator - Splice operator object.

"""

import pprint
import re

from kraken.core.maths import MathObject, Mat44, Xfo, Vec2, Vec3
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.operators.operator import Operator
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.kraken_system import ks
from kraken.log import getLogger

logger = getLogger('kraken')


class KLOperator(Operator):
    """KL Operator representation."""

    def __init__(self, name, solverTypeName, extension, metaData=None):
        super(KLOperator, self).__init__(name, metaData=metaData)

        self.solverTypeName = solverTypeName
        self.extension = extension

        # Load the Fabric Engine client and construct the RTVal for the Solver
        ks.loadCoreClient()
        ks.loadExtension('Kraken')
        if self.extension != 'Kraken':
            ks.loadExtension(self.extension)
        self.solverRTVal = ks.constructRTVal('%s::%s' % (self.extension, self.solverTypeName))

        # logger.debug("Creating kl operator object [%s] of type [%s] from extension [%s]:" % (self.getName(), self.solverTypeName, self.extension))

        self.args = self.solverRTVal.getArguments('Kraken::KrakenSolverArg[]')

        # Initialize the inputs and outputs based on the given args.
        for i in xrange(len(self.args)):
            arg = self.args[i]
            argName = arg.name.getSimpleType()
            argDataType = arg.dataType.getSimpleType()
            argConnectionType = arg.connectionType.getSimpleType()

            # Note, do not create empty arrays here as we need to know later whether or not
            # to create default values if input/output is None
            if argConnectionType == 'In':
                self.inputs[argName] = None
            else:
                self.outputs[argName] = None


    def getSolverTypeName(self):
        """Returns the solver type name for this operator.

        Returns:
            str: Name of the solver type this operator uses.

        """

        return self.solverTypeName

    def getExtension(self):
        """Returns the extention this operator uses.

        Returns:
            str: Name of the extension this solver uses.

        """

        return self.extension

    def getSolverArgs(self):
        """Returns the args array defined by the KL Operator.

        Returns:
            RTValArray: Args array defined by the KL Operator.

        """

        return self.args

    def getInputType(self, name):
        """Returns the type of input with the specified name."""
        for arg in self.args:
            if arg.connectionType.getSimpleType() == "In" and arg.name.getSimpleType() == name:
                return arg.dataType.getSimpleType()

        raise Exception("Could not find input argument %s in kl operator %s" % (name, self.getName()))

    def getOutputType(self, name):
        """Returns the type of output with the specified name."""
        for arg in self.args:
            if arg.connectionType.getSimpleType() == "Out" and arg.name.getSimpleType() == name:
                return arg.dataType.getSimpleType()

        raise Exception("Could not find output argument %s in kl operator %s" % (name, self.getName()))

    def getDefaultValue(self, name, RTValDataType, mode="arg"):
        """Returns the default RTVal value for this argument
        Only print debug if setting default inputs.  Don't care about outputs, really

        Args:
            name (str): Name of the input to get.
            mode (str): "inputs" or "outputs"

        Returns:
            RTVal

        """

        def isFixedArrayType(string):
            return bool(re.search(r'\[\d', string))

        # If attribute has a default value
        if self.solverRTVal.defaultValues.has("Boolean", name).getSimpleType():

            RTVal = ks.convertFromRTVal(self.solverRTVal.defaultValues[name])

            if RTVal.isArray():
                # If RTValDataType is variable array, but default value is fixed array, convert it
                if isFixedArrayType(RTVal.getTypeName().getSimpleType()) and not isFixedArrayType(RTValDataType):
                    RTValArray = ks.rtVal(RTValDataType)
                    if len(RTVal):
                        RTValArray.resize(len(RTVal))

                    for i in range(len(RTVal)):
                        RTValArray[i] = RTVal[i]

                    RTVal = RTValArray
            else:
                # Not totally sure why we need to do this, but we get None from getSimpleType from the RTVal
                # when we run it on it's own and use the type that we query.  Gotta investigate this further...
                RTVal = ks.convertFromRTVal(self.solverRTVal.defaultValues[name], RTTypeName=RTValDataType)

            logger.debug("Using default value for %s.%s.%s(%s) --> %s" % (self.solverTypeName, self.getName(), mode, name, RTVal))

            return RTVal

        defaultValue = ks.rtVal(RTValDataType)
        if name in self.inputs:  # Only warn for input types, OK that we generate default outputs, I think.  Maybe even safer.
            logger.warn("    Creating default value by generating new RTVal object of type: %s. You should set default values for %s.%s(%s) in your KL Operator." %
                (RTValDataType, self.solverTypeName, mode, name))

        return defaultValue

    def getInput(self, name):
        """Returns the input with the specified name.

        If there is no input value, it get the default RTVal and converts to
        python data

        Args:
            name (str): Name of the input to get.

        Returns:
            object: Input object.

        """

        if name in self.inputs and self.inputs[name] is not None:
            return self.inputs[name]

        def rt2Py(rtVal, rtType):

            if "[" in rtType:
                return []
            if rtType == "Xfo":
                return Xfo(rtVal)
            if rtType == "Mat44":
                return Mat44(rtVal)
            if rtType == "Vec2":
                return Vec2(rtVal)
            if rtType == "Vec3":
                return Vec3(rtVal)
            else:
                return rtVal.getSimpleType()

            #raise ValueError("Cannot convert rtval %s from %s" (rtVal, rtType))

        argDataType = None
        for arg in self.args:
            if arg.name.getSimpleType() == name:
                argDataType = arg.dataType.getSimpleType()
                break
        if argDataType is None:
            raise Exception("Cannot find arg %s for object %s" (arg, self.getName()))

        defaultVal = self.getDefaultValue(name, argDataType, mode="arg")
        pyVal = rt2Py(defaultVal, argDataType)

        return pyVal

    def generateSourceCode(self):
        """Returns the source code for a stub operator that will invoke the KL operator

        Returns:
            str: The source code for the stub operator.

        """

        # Start constructing the source code.
        opSourceCode = "dfgEntry {\n"

        # In SpliceMaya, output arrays are not resized by the system prior to
        # calling into Splice, so we explicily resize the arrays in the
        # generated operator stub code.
        for i in xrange(len(self.args)):
            arg = self.args[i]
            argName = arg.name.getSimpleType()
            argDataType = arg.dataType.getSimpleType()
            argConnectionType = arg.connectionType.getSimpleType()

            if argDataType.endswith('[]') and argConnectionType == 'Out':
                arraySize = len(self.getOutput(argName))
                opSourceCode += "  " + argName + ".resize(" + str(arraySize) + \
                    ");\n"

        opSourceCode += "  if(solver == null)\n"
        opSourceCode += "    solver = " + self.solverTypeName + "();\n"
        opSourceCode += "  solver.solve(\n"
        for i in xrange(len(self.args)):
            argName = self.args[i].name.getSimpleType()
            if i == len(self.args) - 1:
                opSourceCode += "    " + argName + "\n"
            else:
                opSourceCode += "    " + argName + ",\n"

        opSourceCode += "  );\n"
        opSourceCode += "}\n"

        return opSourceCode

    def evaluate(self):
        """Invokes the KL operator causing the output values to be computed.

        Returns:
            bool: True if successful.

        """

        # logger.debug("\nEvaluating kl operator [%s] of type [%s] from extension [%s]..." % (self.getName(), self.solverTypeName, self.extension))

        super(KLOperator, self).evaluate()

        def getRTVal(obj, asInput=True):
            if isinstance(obj, Object3D):
                if asInput:
                    return obj.globalXfo.getRTVal().toMat44('Mat44')
                else:
                    return obj.xfo.getRTVal().toMat44('Mat44')
            elif isinstance(obj, Xfo):
                return obj.getRTVal().toMat44('Mat44')
            elif isinstance(obj, MathObject):
                return obj.getRTVal()
            elif isinstance(obj, Attribute):
                return obj.getRTVal()
            elif type(obj) is bool:
                return ks.rtVal('Boolean', obj)
            elif type(obj) is int:
                return ks.rtVal('Integer', obj)
            elif type(obj) is float:
                return ks.rtVal('Scalar', obj)
            elif type(obj) is str:
                return ks.rtVal('String', obj)
            else:
                return obj #

        def validateArg(rtVal, argName, argDataType):
            """Validate argument types when passing built in Python types.

            Args:
                rtVal (RTVal): rtValue object.
                argName (str): Name of the argument being validated.
                argDataType (str): Type of the argument being validated.

            """

            # Validate types when passing a built in Python type
            if type(rtVal) in (bool, str, int, float):
                if argDataType in ('Scalar', 'Float32', 'UInt32', 'Integer'):
                    if type(rtVal) not in (float, int):
                        raise TypeError(self.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + argName + " (" + argDataType + ")")

                elif argDataType == 'Boolean':
                    if type(rtVal) != bool:
                        raise TypeError(self.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + argName + " (" + argDataType + ")")

                elif argDataType == 'String':
                    if type(rtVal) != str:
                        raise TypeError(self.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + argName + " (" + argDataType + ")")

        argVals = []
        debug = []
        for i in xrange(len(self.args)):
            arg = self.args[i]
            argName = arg.name.getSimpleType()
            argDataType = arg.dataType.getSimpleType()
            argConnectionType = arg.connectionType.getSimpleType()

            if argDataType == 'EvalContext':
                argVals.append(ks.constructRTVal(argDataType))
                continue
            if argName == 'time':
                argVals.append(ks.constructRTVal(argDataType))
                continue
            if argName == 'frame':
                argVals.append(ks.constructRTVal(argDataType))
                continue

            if argConnectionType == 'In':
                if str(argDataType).endswith('[]'):
                    if argName in self.inputs and self.inputs[argName] is not None:
                        rtValArray = ks.rtVal(argDataType)
                        rtValArray.resize(len(self.inputs[argName]))
                        for j in xrange(len(self.inputs[argName])):
                            if self.inputs[argName][j] is None:
                                continue
                            rtVal = getRTVal(self.inputs[argName][j])

                            validateArg(rtVal, argName, argDataType[:-2])

                            rtValArray[j] = rtVal
                    else:
                        rtValArray = self.getDefaultValue(argName, argDataType, mode="arg")

                    argVals.append(rtValArray)
                else:
                    if argName in self.inputs and self.inputs[argName] is not None:
                        rtVal = getRTVal(self.inputs[argName])
                    else:
                        rtVal = self.getDefaultValue(argName, argDataType, mode="arg")

                    validateArg(rtVal, argName, argDataType)
                    argVals.append(rtVal)

            elif argConnectionType in ('IO', 'Out'):
                if str(argDataType).endswith('[]'):
                    if argName in self.outputs and self.outputs[argName] is not None:
                        rtValArray = ks.rtVal(argDataType)
                        rtValArray.resize(len(self.outputs[argName]))
                        for j in xrange(len(self.outputs[argName])):
                            if self.outputs[argName][j] is None:
                                continue
                            rtVal = getRTVal(self.outputs[argName][j], asInput=False)

                            validateArg(rtVal, argName, argDataType[:-2])

                            rtValArray[j] = rtVal
                    else:
                        rtValArray = self.getDefaultValue(argName, argDataType, mode="output")

                    argVals.append(rtValArray)
                else:
                    if argName in self.outputs and self.outputs[argName] is not None:
                        rtVal = getRTVal(self.outputs[argName], asInput=False)
                    else:
                        rtVal = self.getDefaultValue(argName, argDataType, mode="output")

                    validateArg(rtVal, argName, argDataType)

                    argVals.append(rtVal)
            else:
                raise Exception("Operator:'" + self.getName() + " has an invalid 'argConnectionType': " + argConnectionType)

            debug.append(
                {
                    argName: [
                        {
                            "dataType": argDataType,
                            "connectionType": argConnectionType
                        },
                        argVals[-1]
                    ]
                })

        try:
            # argstr = [str(arg) for arg in argVals]
            # logger.debug("%s.solve('', %s)" % (self.solverTypeName, ", ".join(argstr)))
            self.solverRTVal.solve('', *argVals)
        except Exception as e:

            errorMsg = "\nPossible problem with KL operator [%s]. Arguments:\n" % self.getName()
            errorMsg += pprint.pformat(debug, indent=4, width=800)
            logger.error(errorMsg)
            raise e

        # Now put the computed values out to the connected output objects.
        def setRTVal(obj, rtval):

            if isinstance(obj, Object3D):
                obj.xfo.setFromMat44(Mat44(rtval))
            elif isinstance(obj, Xfo):
                obj.setFromMat44(Mat44(rtval))
            elif isinstance(obj, Mat44):
                obj.setFromMat44(rtval)
            elif isinstance(obj, Attribute):
                if ks.isRTVal(rtval):
                    obj.setValue(rtval.getSimpleType())
                else:
                    obj.setValue(rtval)
            else:
                if hasattr(obj, '__iter__'):
                    logger.warning("Warning: Trying to set a KL port with an array directly.")

                logger.warning("Not setting rtval: %s\n\tfor output object: %s\n\tof KL object: %s\n." % \
                    (rtval, obj.getName(), self.getName()))

        for i in xrange(len(argVals)):
            arg = self.args[i]
            argName = arg.name.getSimpleType()
            argDataType = arg.dataType.getSimpleType()
            argConnectionType = arg.connectionType.getSimpleType()

            if argConnectionType != 'In':
                if argName in self.outputs and self.outputs[argName] is not None:
                    if str(argDataType).endswith('[]'):
                        for j in xrange(len(argVals[i])):
                            if len(self.outputs[argName]) > j and self.outputs[argName][j] is not None:
                                setRTVal(self.outputs[argName][j], argVals[i][j])
                    else:
                        setRTVal(self.outputs[argName], argVals[i])

        return True
