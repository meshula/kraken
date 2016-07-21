"""Kraken - objects.Attributes.ScalarAttribute module.

Classes:
ScalarAttribute - Base Attribute.

"""

from kraken.core.objects.attributes.number_attribute import NumberAttribute
from kraken.core.kraken_system import ks


class ScalarAttribute(NumberAttribute):
    """Float Attribute. Implemented value type checking and limiting."""

    def __init__(self, name, value=0.0, minValue=None, maxValue=None, blendShapeName='', parent=None):
        super(ScalarAttribute, self).__init__(name, value=value, minValue=minValue,
              maxValue=maxValue, parent=parent)

        assert type(self._value) in (int, float), "Value is not of type 'int' or 'float'."

        self._blendShapeName = blendShapeName


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
    def setBlendShapeName(self, blendShapeName):
        """Sets the blendShape status of this attribute

        Args:
            blendShapeName (str): name of driven blend shape (seen in kl builder getShapeNames)


        """
        self._blendShapeName = isBlendShapeName


    def getBlendShapeName(self):
        """Sets the blendShape status of this attribute

        Returns:
            str: name of driven blend shape (seen in kl builder getShapeNames)

        """
        return self._blendShapeName


    def getDataType(self):
        """Returns the name of the data type for this attribute.

        Returns:
            str: String name of the attribute type.

        """

        return 'Scalar'