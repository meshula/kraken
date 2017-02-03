
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.bool_attribute import BoolAttribute


class TestBoolAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = BoolAttribute('test', parent=cls._attributeGroup)

    def getAttributeGroup(self):
        return self._attributeGroup

    def getAttribute(self):
        return self._attribute

    # ======
    # Tests
    # ======
    def testSetValue(self):
        attribute = self.getAttribute()
        attribute.setValue(True)

        value = attribute.getValue()

        self.assertIsNotNone(value)
        self.assertEquals(value, True)

        attribute.setValue(False)

    def testGetRTVal(self):
        attribute = self.getAttribute()
        rtVal = attribute.getRTVal()

        self.assertEqual(type(rtVal).__name__, 'PyRTValObject')
        self.assertTrue(type(rtVal.getSimpleType()) is bool)
        self.assertEqual(rtVal.getSimpleType(), False)

    def testGetDataType(self):
        attribute = self.getAttribute()

        self.assertEqual(attribute.getDataType(), 'Boolean')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBoolAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
