
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.integer_attribute import IntegerAttribute


class TestIntegerAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = IntegerAttribute('test', parent=cls._attributeGroup)

    def getAttributeGroup(self):
        return self._attributeGroup

    def getAttribute(self):
        return self._attribute

    # ======
    # Tests
    # ======
    def testGetRTVal(self):
        attribute = self.getAttribute()
        rtVal = attribute.getRTVal()

        self.assertEqual(type(rtVal).__name__, 'PyRTValObject')
        self.assertTrue(type(rtVal.getSimpleType()) is int)
        self.assertEqual(rtVal.getSimpleType(), 0)

    def testValidateValue(self):
        attribute = self.getAttribute()

        self.assertRaises(TypeError, lambda: attribute.validateValue(True))
        self.assertRaises(TypeError, lambda: attribute.validateValue(2.0))
        self.assertRaises(TypeError, lambda: attribute.validateValue('One'))

    def testGetDataType(self):
        attribute = self.getAttribute()

        self.assertEqual(attribute.getDataType(), 'Integer')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestIntegerAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
