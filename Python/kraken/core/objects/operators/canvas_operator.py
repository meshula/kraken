"""Kraken - objects.operators.kl_operator module.

Classes:
CanvasOperator - Splice operator object.

"""
import json
from kraken.core.maths import Mat44, Xfo
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.operators.operator import Operator
from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.kraken_system import ks


class CanvasOperator(Operator):
    """Splice Operator representation."""

    def __init__(self, name, canvasPresetPath):
        super(CanvasOperator, self).__init__(name)

        self.canvasPresetPath = canvasPresetPath

        host = ks.getCoreClient().DFG.host
        self.binding = host.createBindingToPreset(self.canvasPresetPath)
        self.node = self.binding.getExec()

        portTypeMap = {
            0: 'In',
            1: 'IO',
            2: 'Out'
        }

        ownerOutPortData = {
            'name': None,
            'typeSpec': None,
            'execPortType': None
        }

        # Initialize the inputs and outputs based on the given args.
        for i in xrange(self.node.getExecPortCount()):

            portName = self.node.getExecPortName(i)
            print("TTPrint: portName:"),
            print(portName)
            portConnectionType = portTypeMap[self.node.getExecPortType(i)]
            print("TTPrint: portConnectionType:"),
            print(portConnectionType)
            rtVal = self.binding.getArgValue(portName)
            print("TTPrint: rtVal:"),
            print(rtVal)
            portDataType = rtVal.getTypeName().getSimpleType()
            print("TTPrint: portDataType:"),
            print(portDataType)

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


    def getPresetPath(self):
        """Returns the preset path within the Canvas library for the node used by this operator.

        Returns:
            str: Path of the preset files used by this operator.

        """

        return self.canvasPresetPath


    def getGraphDesc(self):
        """Returns the json description of the node used by this operator

        Returns:
            object: A json dict containing the description the operator.

        """

        return self.graphDesc


    def evaluate(self):
        """invokes the Canvas node causing the output values to be computed.

        Returns:
            bool: True if successful.

        """

        def getRTVal(obj):
            if isinstance(obj, Object3D):
                return obj.xfo.getRTVal().toMat44('Mat44')
            elif isinstance(obj, Xfo):
                return obj.getRTVal().toMat44('Mat44')
            elif isinstance(obj, Attribute):
                return obj.getRTVal()
            else: # Must be a numerical, or string, etc.
                return obj  ###### TTHACK Pass this through, we are setting a value directly, not makeing a connection

        portTypeMap = {
            0: 'In',
            1: 'IO',
            2: 'Out'
        }
        debug = []
        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portDataType == '$TYPE$':
                # TODO: test for inputs[portName] is iterable, if so change dataType to based on elements and do the rest
                return

            if portDataType in ('EvalContext', 'time', 'frame'):
                self.binding.setArgValue(portName, ks.constructRTVal(portDataType), False)
                continue

            if portConnectionType == 'In':
                if str(portDataType).endswith('[]'):
                    rtValArray = ks.rtVal(portDataType)
                    rtValArray.resize(len(self.inputs[portName]))
                    for j in xrange(len(self.inputs[portName])):
                        rtValArray[j] = getRTVal(self.inputs[portName][j])

                    self.binding.setArgValue(portName, rtValArray, False)
                else:
                    self.binding.setArgValue(portName, getRTVal(self.inputs[portName]), False)
            else:
                if str(portDataType).endswith('[]'):
                    rtValArray = ks.rtVal(portDataType)
                    rtValArray.resize(len(self.outputs[portName]))
                    for j in xrange(len(self.outputs[portName])):
                        rtValArray[j] = getRTVal(self.outputs[portName][j])

                    self.binding.setArgValue(portName, rtValArray, False)
                else:
                    self.binding.setArgValue(portName, getRTVal(self.outputs[portName]), False)

            debug.append({portName : [{"portDataType": portDataType, "portConnectionType": portConnectionType}, self.binding.getArgValue(portName)]})

        try:
            self.binding.execute()

        except:
            print("Possible problem with Canvas operator \""+self.getName()+"\" port values:")
            import pprint
            pprint.pprint(debug, width=800)
            raise

        # Now put the computed values out to the connected output objects.
        def setRTVal(obj, rtval):
            if isinstance(obj, Object3D):
                obj.xfo.setFromMat44(Mat44(rtval))
            elif isinstance(obj, Xfo):
                obj.setFromMat44(Mat44(rtval))
            elif isinstance(obj, Attribute):
                obj.setValue(rtval)
            else:
                print ("Warning: Not setting rtval "+str(rtval)+" for object "+str(obj))

        for i in xrange(self.node.getExecPortCount()):
            portName = self.node.getExecPortName(i)
            portConnectionType = portTypeMap[self.node.getExecPortType(i)]
            rtVal = self.binding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portConnectionType != 'In':
                outVal = self.binding.getArgValue(portName)
                if hasattr(outVal, '__iter__') or portDataType.endswith('[]'): #type could be "$TYPE$" so don't test for brackets
                    for j in xrange(len(outVal)):
                        setRTVal(self.outputs[portName][j], outVal[j])
                else:
                    setRTVal(self.outputs[portName], outVal)

        return True