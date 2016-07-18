"""Kraken - objects.Attributes.ScalarAttribute module.

Classes:
ScalarAttribute - Base Attribute.

"""

from kraken.core.objects.attributes.number_attribute import NumberAttribute
from kraken.core.kraken_system import ks


class ScalarAttribute(NumberAttribute):
    """Float Attribute. Implemented value type checking and limiting."""

    def __init__(self, name, value=0.0, minValue=None, maxValue=None, isBlendShape=False, parent=None):
        super(ScalarAttribute, self).__init__(name, value=value, minValue=minValue,
              maxValue=maxValue, parent=parent)

        assert type(self._value) in (int, float), "Value is not of type 'int' or 'float'."

        self._isBlendShape = isBlendShape


    # ==============
    # Value Methods
    # ==============
    def getRTVal(self):
        """Returns and RTVal object for this attribute.

        Returns:
            RTVal: RTVal object of the attribute.

        """

        return ks.rtVal('Scalar', self._value)


    def validateValue(self, value):
        """Validates the incoming value is the correct type.

        Note:
            This is a localized method specific to the Scalar Attribute.

        Args:
            value (int): value to check the type of.

        Returns:
            bool: True if valid.

        """

        if type(value) not in (int, float):
            return False

        return True


    # ==============
    # Value Methods
    # ==============
    def isBlendShape(self):
        """Returns whether or not this attribute may be used to drive a blendShape

        Returns:
            Bool
        """
        return self._isBlendShape


    def setIsBlendShape(self, isBlendShape):
        """Sets the blendShape status of this attribute

        Returns:
            None

        """
        self._isBlendShape = isBlendShape


    def getDataType(self):
        """Returns the name of the data type for this attribute.

        Returns:
            str: String name of the attribute type.

        """

        return 'Scalar'