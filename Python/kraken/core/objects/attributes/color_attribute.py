"""Kraken - objects.Attributes.ColorAttribute module.

Classes:
ColorAttribute - Base Attribute.

"""

from kraken.core.objects.attributes.attribute import Attribute
from kraken.core.kraken_system import ks


class ColorAttribute(Attribute):
    """Color Attribute. Implemented value type checking."""

    def __init__(self, name, value=None, parent=None, metaData=None):
        super(ColorAttribute, self).__init__(name, value=value, parent=parent, metaData=metaData)

        if value is None:
            value = {
                'r': 0.0,
                'g': 0.0,
                'b': 0.0,
                'a': 1.0
            }

        self.setValue(value)


    def setValue(self, color):
        """Sets the value of the attribute..

        Args:
            value (dict): Color values to set the attribute to.

        Returns:
            bool: True if successful.

        """

        assert isinstance(color, dict), "color Value is not of type dict."

        super(ColorAttribute, self).setValue(color)

        return True


    def getRTVal(self):
        """Returns and RTVal object for this attribute.

        Returns:
            RTVal: RTVal object of the attribute.

        """

        return ks.rtVal('Color', self._value)


    def getDataType(self):
        """Returns the name of the data type for this attribute.

        Note:
            This is a localized method specific to the Color Attribute.

        Returns:
            str: Color name of the attribute type.

        """

        return 'Color'
