"""Kraken - objects.operators.kl_operator module.

Classes:
KLOperator - Splice operator object.

"""

import pprint
import json

from kraken.core.maths import MathObject, Mat44, Xfo
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.operators.operator import Operator
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.kraken_system import ks
from kraken.log import getLogger

logger = getLogger('kraken')


class KLOperator(Operator):
    """Splice Operator representation."""

    # TODO: Look in to expanding the Splice operator to be able to handle more
    # than one extension / operator. Need to change extension to extensions and
    # figure out how to differentiate the solver types per operator. Maybe have
    # an attirbute array called 'klOperators' that contains sets of what we
    # currently have setup.

    def __init__(self, name, solverTypeName, extension):
        super(KLOperator, self).__init__(name)

        self.solverTypeName = solverTypeName
        self.extension = extension

        # Load the Fabric Engine client and construct the RTVal for the Solver
        ks.loadCoreClient()
        ks.loadExtension('Kraken')
        if self.extension != 'Kraken':
            ks.loadExtension(self.extension)
        self.solverRTVal = ks.constructRTVal(self.solverTypeName)
        try:
          self.json = json.loads(self.solverRTVal.getJSON().getSimpleType())
        except:
          self.json = None
        logger.debug("Creating kl operator object [%s] of type [%s] from extension [%s]:" % (self.getName(), self.solverTypeName, self.extension))
        #logger.debug(pprint.pformat(self.json))  Too much for standard debug.  Hopefully we can get more granular. Uncomment if you want to see object properties

        self.args = self.solverRTVal.getArguments('KrakenSolverArg[]')

        # Initialize the inputs and outputs based on the given args.
        for i in xrange(len(self.args)):
            arg = self.args[i]
            argName = arg.name.getSimpleType()
            argDataType = arg.dataType.getSimpleType()
            argConnectionType = arg.connectionType.getSimpleType()

            if argConnectionType == 'In':
                if argDataType.endswith('[]'):
                    self.inputs[argName] = []
                else:
                    self.inputs[argName] = None
            else:  # argConnectionType == 'Out':
                if argDataType.endswith('[]'):
                    self.outputs[argName] = []
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




    def getDefaultValue(self, name, mode="inputs", fallback=None):
        """Returns the default RTVal value for this argument
        Only print debug if setting default inputs.  Don't care about outputs, really

        Args:
            name (str): Name of the input to get.
            mode (str): "inputs" or "outputs"

        Returns:
            RTVal

        """
        if fallback is None:
            fallback = ks.rtVal("null")

        if self.json is not None:
            if "defaults" in self.json and name in self.json["defaults"]:
                defaultValue = getattr(self.solverRTVal.defaults, name)
                if mode == "inputs":
                    logger.warn("Using default value for %s.%s.%s[%s] --> %s." % (self.solverTypeName, self.getName(), name, mode, defaultValue))
                return defaultValue
            else:
                if mode == "inputs":  #Only report a warning if default value is not provided for inputs
                    logger.warn("No default value for %s.%s.%s[%s]." % (self.solverTypeName, self.getName(), mode, name))
        else:
            if mode == "inputs":
                logger.warn("No default value struct named \"defauts\" found for solver %s.%s.inputs[]." % (self.solverTypeName, self.getName()))

        if mode == "inputs":
            logger.warn("Using fallback default value: %s" % fallback)
        return fallback


    def getInput(self, name):
        """Returns the input with the specified name.
        If there is no input value, it get the default RTVal and converts to python data

        Args:
            name (str): Name of the input to get.

        Returns:
            object: Input object.

        """
        if name in self.inputs and self.inputs[name] is not None:
            return self.inputs[name]

        def rt2Py(rtVal, rtType):

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

        defaultVal = self.getDefaultValue(name, mode="inputs", fallback=ks.rtVal(argDataType))
        pyVal = rt2Py(defaultVal, argDataType)
        return pyVal


    def generateSourceCode(self, arraySizes={}):
        """Returns the source code for a stub operator that will invoke the KL operator

        Returns:
            str: The source code for the stub operator.

        """

        # Start constructing the source code.
        opSourceCode = "dfgEntry {\n"

        # In SpliceMaya, output arrays are not resized by the system prior to
        # calling into Splice, so we explicily resize the arrays in the
        # generated operator stub code.
        for argName, arraySize in arraySizes.iteritems():
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
        logger.debug("Evaluating kl operator [%s] of type [%s] from extension [%s]..." % (self.getName(), self.solverTypeName, self.extension))
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
                        rtValArray = self.getDefaultValue(argName, mode="inputs", fallback=ks.rtVal(argDataType))

                    argVals.append(rtValArray)
                else:
                    if argName in self.inputs and self.inputs[argName] is not None:
                        rtVal = getRTVal(self.inputs[argName])
                    else:
                        rtVal = self.getDefaultValue(argName, mode="inputs", fallback=ks.rtVal(argDataType))

                    validateArg(rtVal, argName, argDataType)
                    argVals.append(rtVal)
            else:  # argConnectionType == 'Out':
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
                        rtValArray = self.getDefaultValue(argName, mode="outputs", fallback=ks.rtVal(argDataType))

                    argVals.append(rtValArray)
                else:
                    if argName in self.outputs and self.outputs[argName] is not None:
                        rtVal = getRTVal(self.outputs[argName], asInput=False)
                    else:
                        rtVal = self.getDefaultValue(argName, mode="outputs", fallback=ks.rtVal(argDataType))

                    validateArg(rtVal, argName, argDataType)

                    argVals.append(rtVal)

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
            argstr = [str(arg) for arg in argVals]
            logger.debug("%s.solve('', %s)" % (self.solverTypeName, ", ".join(argstr)))
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
                if str(argDataType).endswith('[]'):
                    for j in xrange(len(argVals[i])):
                        setRTVal(self.outputs[argName][j], argVals[i][j])
                elif argName in self.outputs and self.outputs[argName] is not None:
                        setRTVal(self.outputs[argName], argVals[i])

        return True
