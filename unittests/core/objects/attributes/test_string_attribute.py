
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.string_attribute import StringAttribute


class TestStringAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = StringAttribute('test', parent=cls._attributeGroup)

    def getAttributeGroup(self):
        return self._attributeGroup

    def getAttribute(self):
        return self._attribute

    # ======
    # Tests
    # ======
    def testSetValue(self):
        attribute = self.getAttribute()
        attribute.setValue('test')

        value = attribute.getValue()

        self.assertIsNotNone(value)
        self.assertEquals(value, 'test')
        self.assertRaises(TypeError, lambda: attribute.setValue(True))
        self.assertRaises(TypeError, lambda: attribute.setValue(8))

        attribute.setValue('')

    def testGetRTVal(self):
        attribute = self.getAttribute()
        rtVal = attribute.getRTVal()

        self.assertEqual(type(rtVal).__name__, 'PyRTValObject')
        self.assertTrue(type(rtVal.getSimpleType()) is str)
        self.assertEqual(rtVal.getSimpleType(), '')

    def testGetDataType(self):
        attribute = self.getAttribute()

        self.assertEqual(attribute.getDataType(), 'String')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestStringAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
