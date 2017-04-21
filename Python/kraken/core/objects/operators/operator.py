"""Kraken - objects.operators.operator module.

Classes:
Operator - Base operator object.

"""
import re
from kraken.core.configs.config import Config
from kraken.core.objects.scene_item import SceneItem


class Operator(SceneItem):
    """Operator representation."""

    def __init__(self, name, parent=None, metaData=None):
        super(Operator, self).__init__(name, parent, metaData=metaData)

        self.inputs = {}
        self.outputs = {}
        self._flags = {}

    # =============
    # Name Methods
    # =============
    def getBuildName(self):
        """Returns the build name for the object.

        Returns:
            str: Name to be used in the DCC.

        """

        typeNameHierarchy = self.getTypeHierarchyNames()

        config = Config.getInstance()

        # If flag is set on object to use explicit name, return it.
        if config.getExplicitNaming() is True or \
                self.testFlag('EXPLICIT_NAME'):
                return self.getName()

        nameTemplate = config.getNameTemplate()

        # Get the token list for this type of object
        format = None
        for typeName in nameTemplate['formats'].keys():
            if typeName in typeNameHierarchy:
                format = nameTemplate['formats'][typeName]
                break

        if format is None:
            format = nameTemplate['formats']['default']

        objectType = None
        for eachType in typeNameHierarchy:
            if eachType in nameTemplate['types'].keys():
                objectType = eachType
                break

        altType = self.getMetaDataItem("altType")
        if altType is not None and nameTemplate['types'].get(altType, None) is not None:
            objectType = altType

        if objectType is None:
            objectType = 'default'

        # Generate a name by concatenating the resolved tokens together.
        builtName = ""
        skipSep = False
        for token in format:

            if token is 'sep':
                if not skipSep:
                    builtName += nameTemplate['separator']

            elif token is 'location':
                parent = self.getParent()
                if parent is None:
                    raise ValueError("operator [%s] does not have a parent." % self.getName())
                location = parent.getLocation()

                if location not in nameTemplate['locations']:
                    raise ValueError("Invalid location on: " + self.getPath())

                altLocation = self.getMetaDataItem("altLocation")
                if altLocation is not None and altLocation in nameTemplate['locations']:
                    location = altLocation

                builtName += location

            elif token is 'type':
                builtName += nameTemplate['types'][objectType]

            elif token is 'name':
                builtName += self.getName()

            elif token is 'component':
                if self.getParent() is None:
                    skipSep = True
                    continue

                builtName += self.getParent().getName()

            elif token is 'container':
                if self.getContainer() is None:
                    skipSep = True
                    continue

                builtName += self.getContainer().getName()

            elif token is 'solverName':
                if self.isTypeOf("KLOperator"):
                    builtName += self.solverTypeName
                else:
                    builtName += self.canvasPresetPath.rpartition('.')[-1]

            elif token is 'solverSource':
                if self.isTypeOf("KLOperator"):
                    builtName += self.extension
                else:
                    builtName += re.sub("[\W\d]", "", self.canvasPresetPath.rpartition('.')[0])


            else:
                raise ValueError("Unresolvabled token '" + token +
                    "' used on: " + self.getPath())

        return builtName

    # =============
    # Flag Methods
    # =============
    def setFlag(self, name):
        """Sets the flag of the specified name.

        Returns:
            bool: True if successful.

        """

        self._flags[name] = True

        return True

    def testFlag(self, name):
        """Tests if the specified flag is set.

        Args:
            name (str): Name of the flag to test.

        Returns:
            bool: True if flag is set.

        """

        return name in self._flags

    def clearFlag(self, name):
        """Clears the flag of the specified name.

        Args:
            name (str): Name of the flag to clear.

        Returns:
            bool: True if successful.

        """

        if name in self._flags:
            del self._flags[name]
            return True

        return False

    def getFlags(self):
        """Returns all flags set on this object.

        Returns:
            list: Flags set on this object.

        """

        return self._flags.keys()

    # ===============
    # Source Methods
    # ===============
    def getSources(self):
        """Returns the sources of the object.

        Returns:
            list: All sources of this object.

        """

        sources = []
        for name in self.getInputNames():
            inputTargets = self.getInput(name)
            if not isinstance(inputTargets, list):
                inputTargets = [inputTargets]
            for inputTarget in inputTargets:
                if not isinstance(inputTarget, SceneItem):
                    continue
                sources.append(inputTarget)

        return super(Operator, self).getSources() + sources

    # ==============
    # Input Methods
    # ==============
    def resizeInput(self, name, count):
        """Resizes and array output to a given size.

        Args:
            name (str): Name of the output.
            count (Object): Output object.

        Returns:
            bool: True if successful.

        """
        raise DeprecationWarning("Method 'resizeInput' has been deprecated!")

        # if name not in self.inputs:
        #     raise Exception("Input with name '" + name +
        #                     "' was not found in operator: " + self.getName() +
        #                     ".")
        # if isinstance(self.inputs[name], list):
        #     while len(self.inputs[name]) < count:
        #         self.inputs[name].append(None)
        # else:
        #     raise Exception("Input is not an array input: " + name + ".")
        # return True

    def setInput(self, name, operatorInput, index=0):
        """Sets the input by the given name.

        Args:
            name (str): Name of the input.
            operatorInput (Object): Input object.

        Returns:
            bool: True if successful.

        """

        if name not in self.inputs:
            raise Exception("Input with name '" + name +
                            "' was not found in operator: " + self.getName() +
                            ".\nValid inputs are:\n" +
                            "\n".join(self.inputs.keys()))

        if self.inputs[name] is None and self.getInputType(name).endswith('[]'):
            self.inputs[name] = []

        if isinstance(self.inputs[name], list):

            # Set the entire output array
            if isinstance(operatorInput, list):
                self.inputs[name] = operatorInput

            else:
                if index >= len(self.inputs[name]):
                    raise Exception(
                        "Out of range index for array output index: " +
                        str(index) + " size: " + str(len(self.inputs[name])) +
                        ".")

                self.inputs[name][index] = operatorInput

        else:
            self.inputs[name] = operatorInput

        return True

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

        return self.inputs[name]

    def getInputType(self, name):
        """Returns the type of input with the specified name."""
        pass

    def getInputNames(self):
        """Returns the names of all inputs.

        Returns:
            list: Names of all inputs.

        """

        return self.inputs.keys()

    # ==============
    # Output Methods
    # ==============
    def resizeOutput(self, name, count):
        """Resizes and array output to a given size.

        Args:
            name (str): Name of the output.
            count (object): Output object.

        Returns:
            bool: True if successful.

        """

        raise DeprecationWarning("Method 'resizeOutput' has been deprecated!")

        # if name not in self.outputs:
        #     raise Exception("Output with name '" + name +
        #                     "' was not found in operator: " + self.getName() +
        #                     ".")

        # if isinstance(self.outputs[name], list):
        #     while len(self.outputs[name]) < count:
        #         self.outputs[name].append(None)
        # else:
        #     raise Exception("Output is not an array output: " + name + ".")
        # return True


    def setOutput(self, name, operatorOutput, index=0):
        """Sets the output by the given name.

        Args:
            name (str): Name of the output.
            operatorOutput (object): Output object.

        Returns:
            bool: True if successful.

        """

        if name not in self.outputs:
            raise Exception("Output with name '" + name +
                            "' was not found in operator: " + self.getName() +
                            ".")

        if self.outputs[name] is None and self.getOutputType(name).endswith('[]'):
            self.outputs[name] = []

        if isinstance(self.outputs[name], list):
            # Set the entire output array
            if isinstance(operatorOutput, list):
                self.outputs[name] = operatorOutput
                for outputItem in operatorOutput:
                    outputItem.addSource(self)
            else:
                if index >= len(self.outputs[name]):
                    raise Exception("Out of range index for array output:" +
                                    "index(" + str(index) + ") size(" +
                                    str(len(self.outputs[name])) + ").")

                self.outputs[name][index] = operatorOutput
                operatorOutput.addSource(self)
        else:
            self.outputs[name] = operatorOutput
            operatorOutput.addSource(self)

        return True

    def getOutput(self, name):
        """Returns the output with the specified name.

        Args:
            name (str): Name of the output to get.

        Returns:
            object: Output object.

        """

        if name not in self.outputs.keys():
            raise Exception("Output with name '" + name +
                            "' was not found in operator: " + self.getName() +
                            ".")

        if self.outputs[name] is None and self.getOutputType(name).endswith('[]'):
            self.outputs[name] = []

        return self.outputs[name]

    def getOutputType(self, name):
        """Returns the type of input with the specified name."""
        pass

    def getOutputNames(self):
        """Returns the names of all outputs.

        Returns:
            list: Names of all outputs.

        """

        return self.outputs.keys()

    # ==================
    # Evaluation Methods
    # ==================
    def updateTargets(self):
        """Updates all targets so that they have a hold on this operator."""

        for name in self.getOutputNames():
            outputTargets = self.getOutput(name)
            if not isinstance(outputTargets, list):
                outputTargets = [outputTargets]

            for outputTarget in outputTargets:
                if not isinstance(outputTarget, SceneItem):
                    continue

                outputTarget.addSource(self)

    def evaluate(self):
        """Invokes the operator causing the output values to be computed.

        Returns:
            bool: True if successful.

        """

        self.updateTargets()
        self.setFlag("HAS_EVALUATED")

        return True
