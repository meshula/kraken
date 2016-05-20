"""Kraken - objects.operators.kl_operator module.

Classes:
KLOperator - Splice operator object.

"""

import pprint


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
                    self.inputs[argName] = self.getInput(argName)
            else:
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

    def getInput(self, name):
        """Returns the input with the specified name.

        Args:
            name (str): Name of the input to get.

        Returns:
            object: Input object.

        """
        if name not in self.inputs:
            raise Exception("Input with name '" + name +
                            "' was not found in operator: " +
                            self.getName() + ".")

        if self.inputs[name] is None:
            for arg in self.args:
                if arg.name.getSimpleType() == name and arg.defaultValue.getSimpleType() != "":
                    argDefaultValue = eval(arg.defaultValue.getSimpleType())
                    logger.debug("Using default value for %s.%s.inputs[%s] to %s." % (self.solverTypeName, self.getName(), name, argDefaultValue))
                    return argDefaultValue


        return self.inputs[name]


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
            argDefaultValue = None
            if arg.defaultValue.getSimpleType() != "":
                argDefaultValue = eval(arg.defaultValue.getSimpleType())



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
                    rtValArray = ks.rtVal(argDataType)
                    rtValArray.resize(len(self.inputs[argName]))
                    for j in xrange(len(self.inputs[argName])):
                        if self.inputs[argName][j] is None:
                            continue
                        rtVal = getRTVal(self.inputs[argName][j])

                        validateArg(rtVal, argName, argDataType[:-2])

                        rtValArray[j] = rtVal

                    argVals.append(rtValArray)
                else:
                    if self.inputs[argName] is None and argDefaultValue is not None:
                        try:
                            rtVal = getRTVal(argDefaultValue)
                        except Exception as e:
                            logger.error("Problems setting default value for input argument [%s] of object [%s] : %s" % (self.inputs[argName], self.getName(), argDefaultValue))
                            raise e
                    else:
                        rtVal = getRTVal(self.inputs[argName])

                    validateArg(rtVal, argName, argDataType)

                    argVals.append(rtVal)
            else:
                if str(argDataType).endswith('[]'):
                    rtValArray = ks.rtVal(argDataType)
                    rtValArray.resize(len(self.outputs[argName]))
                    for j in xrange(len(self.outputs[argName])):
                        if self.outputs[argName][j] is None:
                            continue
                        rtVal = getRTVal(self.outputs[argName][j],
                                         asInput=False)

                        validateArg(rtVal, argName, argDataType[:-2])

                        rtValArray[j] = rtVal

                    argVals.append(rtValArray)
                else:
                    rtVal = getRTVal(self.outputs[argName],
                                     asInput=False)

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

                logger.warning("Warning: Not setting rtval: %s\n\tfor output object: %s\n\ton port: %s\n\tof KL object: %s\n." % \
                    (rtval, obj, self.getName()))

        for i in xrange(len(argVals)):
            arg = self.args[i]
            argName = arg.name.getSimpleType()
            argDataType = arg.dataType.getSimpleType()
            argConnectionType = arg.connectionType.getSimpleType()

            if argConnectionType != 'In':
                if str(argDataType).endswith('[]'):
                    for j in xrange(len(argVals[i])):
                        setRTVal(self.outputs[argName][j], argVals[i][j])
                else:
                    setRTVal(self.outputs[argName], argVals[i])

        return True
