"""Kraken - objects.operators.canvas_operator module.

Classes:
CanvasOperator - Canvas operator object.

"""

import pprint

from kraken.core.maths import MathObject, Mat44, Vec2, Vec3, Xfo
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.operators.operator import Operator
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.kraken_system import ks
from kraken.log import getLogger

logger = getLogger('kraken')


class CanvasOperator(Operator):
    """Canvas Operator representation."""

    def __init__(self, name, canvasPresetPath, metaData=None):
        super(CanvasOperator, self).__init__(name, metaData=metaData)

        self.canvasPresetPath = canvasPresetPath

        host = ks.getCoreClient().DFG.host
        self.binding = host.createBindingToPreset(self.canvasPresetPath)
        self.node = self.binding.getExec()

        self.portTypeMap = {
            0: 'In',
            1: 'IO',
            2: 'Out'
        }

        # Initialize the inputs and outputs based on the given args.
        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = self.portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portDataType == 'Execute':
                continue

            if portConnectionType == 'In':
                if portDataType.endswith('[]'):
                    self.inputs[portName] = []
                else:
                    self.inputs[portName] = None
            else:
                if portDataType.endswith('[]'):
                    self.outputs[portName] = []
                else:
                    self.outputs[portName] = None

    def getDefaultValue(self, name, RTValDataType, mode="port"):
        """Returns the default RTVal value for this argument
        Only print debug if setting default inputs.  Don't care about outputs, really

        Args:
            name (str): Name of the input to get.
            RTValDataType (?): ?
            mode (str): "inputs" or "outputs"

        Returns:
            RTVal

        """

        rtVal = self.node.getPortDefaultValue(name, RTValDataType)

        logger.debug("Using default value for %s.%s.%s(%s) --> %s" % (self.canvasPresetPath, self.getName(), mode, name, rtVal))

        return rtVal

    def getPresetPath(self):
        """Returns the preset path within the Canvas library for the node used
        by this operator.

        Returns:
            str: Path of the preset files used by this operator.

        """

        return self.canvasPresetPath

    def getGraphDesc(self):
        """Returns the json description of the node used by this operator

        Returns:
            object: A json dict containing the description the operator.

        """

        raise DeprecationWarning("Method 'getGraphDesc' has been deprecated.")

        # return self.graphDesc

    def getInput(self, name):
        """Returns the input with the specified name.

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
            elif rtType == "Xfo":
                return Xfo(rtVal)
            elif rtType == "Mat44":
                return Mat44(rtVal)
            elif rtType == "Vec2":
                return Vec2(rtVal)
            elif rtType == "Vec3":
                return Vec3(rtVal)
            elif type(rtVal) in (bool, str, int, float):
                return rtVal
            else:
                return rtVal.getSimpleType()

        if name not in self.inputs:
            raise Exception("Input with name '" + name +
                            "' was not found in operator: " +
                            self.getName() + ".")

        rtVal = self.binding.getArgValue(name)
        portDataType = rtVal.getTypeName().getSimpleType()

        defaultValue = self.getDefaultValue(name, portDataType, mode='port')
        pyVal = rt2Py(defaultValue, portDataType)

        return pyVal

    def getInputType(self, name):
        """Returns the type of input with the specified name."""

        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = self.portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portConnectionType == 'In' and portName == name:
                return portDataType

        raise Exception("Could not find input port %s in canvas operator %s" % (name, self.getName()))

    def getOutputType(self, name):
        """Returns the type of output with the specified name."""
        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = self.portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portConnectionType == 'Out' and portName == name:
                return portDataType

        raise Exception("Could not find output port '%s' in canvas operator: %s" % (name, self.getName()))

    def evaluate(self):
        """Invokes the Canvas node causing the output values to be computed.

        Returns:
            bool: True if successful.

        """

        super(CanvasOperator, self).evaluate()

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
            elif type(obj) in (int, float, bool, str):
                return obj

        def validateArg(rtVal, portName, portDataType):
            """Validate argument types when passing built in Python types.

            Args:
                rtVal (RTVal): rtValue object.
                portName (str): Name of the argument being validated.
                portDataType (str): Type of the argument being validated.

            """

            # Validate types when passing a built in Python type
            if type(rtVal) in (bool, str, int, float):
                if portDataType in ('Scalar', 'Float32', 'UInt32', 'Integer'):
                    if type(rtVal) not in (float, int):
                        raise TypeError(self.getName() + ".evaluate(): Invalid Arg Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

                elif portDataType == 'Boolean':
                    if type(rtVal) != bool:
                        raise TypeError(self.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

                elif portDataType == 'String':
                    if type(rtVal) != str:
                        raise TypeError(self.getName() + ".evaluate(): Invalid Argument Value: " + str(rtVal) + " (" + type(rtVal).__name__ + "), for Argument: " + portName + " (" + portDataType + ")")

        debug = []
        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = self.portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            portVal = None
            if portDataType == '$TYPE$':
                return

            if portDataType == 'Execute':
                continue

            if portDataType in ('EvalContext', 'time', 'frame'):
                portVal = ks.constructRTVal(portDataType)
                self.binding.setArgValue(portName, portVal, False)
                continue


            if portConnectionType == 'In':
                if str(portDataType).endswith('[]'):
                    if not len(self.inputs[portName]):
                        continue

                    rtValArray = ks.rtVal(portDataType)
                    rtValArray.resize(len(self.inputs[portName]))
                    for j in xrange(len(self.inputs[portName])):
                        if self.inputs[portName][j] is None:
                            continue
                        rtVal = getRTVal(self.inputs[portName][j])

                        validateArg(rtVal, portName, portDataType[:-2])

                        rtValArray[j] = rtVal

                    portVal = rtValArray
                    self.binding.setArgValue(portName, portVal, False)
                else:
                    if self.inputs[portName] is None and portName == 'exec':
                        continue
                    elif self.inputs[portName] is None:
                        rtVal = self.getDefaultValue(portName, portDataType, mode="port")
                    else:
                        rtVal = getRTVal(self.inputs[portName])

                    validateArg(rtVal, portName, portDataType)
                    if rtVal is not None:
                        self.binding.setArgValue(portName, rtVal, False)
            else:
                if str(portDataType).endswith('[]'):
                    if not len(self.outputs[portName]):
                        continue
                    rtValArray = ks.rtVal(portDataType)
                    rtValArray.resize(len(self.outputs[portName]))
                    for j in xrange(len(self.outputs[portName])):
                        if self.outputs[portName][j] is None:
                            continue
                        rtVal = getRTVal(self.outputs[portName][j], asInput=False)

                        validateArg(rtVal, portName, portDataType[:-2])

                        rtValArray[j] = rtVal

                    portVal = rtValArray
                    self.binding.setArgValue(portName, portVal, False)
                else:
                    if self.outputs[portName] is None and portName == 'exec':
                        continue
                    elif self.outputs[portName] is None:
                        rtVal = self.getDefaultValue(portName, portDataType, mode="port")
                    else:
                        rtVal = getRTVal(self.outputs[portName], asInput=False)

                    validateArg(rtVal, portName, portDataType)
                    if rtVal is not None:
                        self.binding.setArgValue(portName, rtVal, False)

            portDebug = {
                portName: [
                    {
                        "portDataType": portDataType,
                        "portConnectionType": portConnectionType
                    },
                    portVal
                ]
            }

            debug.append(portDebug)

        try:
            self.binding.execute()
        except Exception as e:
            logger.error(str(e))
            logger.error(self.binding.getErrors(True))

            errorMsg = "Possible problem with Canvas operator '" + \
                self.getName() + "' port values:"

            logger.error(errorMsg)
            logger.error(pprint.pformat(debug, width=800))

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
                    print "Warning: Trying to set a canvas port item with an array directly."

                print "Warning: Not setting rtval: %s\n\tfor output object: %s\n\ton port: %s\n\tof canvas object: %s\n." % (rtval, obj, portName, self.getName())


        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = self.portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portDataType == 'Execute':
                continue

            if portConnectionType != 'In':
                if portName == 'exec':  # Skip the exec port on each solver
                    continue

                outVal = self.binding.getArgValue(portName)
                if str(portDataType).endswith('[]' or
                                              hasattr(outVal.getSimpleType(),
                                                      '__iter__')):

                    for j in xrange(len(outVal)):
                        setRTVal(self.outputs[portName][j], outVal[j])
                else:
                    setRTVal(self.outputs[portName], outVal)

        return True
