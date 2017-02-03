
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute


class TestScalarAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = ScalarAttribute('test', parent=cls._attributeGroup)

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
        self.assertTrue(type(rtVal.getSimpleType()) is float)
        self.assertEqual(rtVal.getSimpleType(), 0.0)

    def testValidateValue(self):
        attribute = self.getAttribute()

        self.assertFalse(attribute.validateValue(True))
        self.assertFalse(attribute.validateValue({}))
        self.assertFalse(attribute.validateValue('One'))

    def testGetDataType(self):
        attribute = self.getAttribute()

        self.assertEqual(attribute.getDataType(), 'Scalar')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestScalarAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
