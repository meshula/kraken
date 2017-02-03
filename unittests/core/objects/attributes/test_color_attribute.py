
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.color_attribute import ColorAttribute


class TestColorAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = ColorAttribute('test', parent=cls._attributeGroup)

    def getAttributeGroup(self):
        return self._attributeGroup

    def getAttribute(self):
        return self._attribute

    # ======
    # Tests
    # ======
    def testSetValue(self):
        attribute = self.getAttribute()

        origValue = attribute.getValue()

        newColorValue = {
            'r': 0.5,
            'g': 0.5,
            'b': 0.5,
            'a': 0.5,
        }

        attribute.setValue(newColorValue)

        value = attribute.getValue()

        self.assertIsNotNone(value)
        self.assertEquals(value, newColorValue)

        attribute.setValue(origValue)

    def testGetRTVal(self):
        attribute = self.getAttribute()
        rtVal = attribute.getRTVal()

        self.assertEqual(type(rtVal).__name__, 'PyRTValObject')
        self.assertIs(rtVal.getSimpleType(), None)
        self.assertEqual(rtVal.r.getSimpleType(), 0.0)
        self.assertEqual(rtVal.g.getSimpleType(), 0.0)
        self.assertEqual(rtVal.b.getSimpleType(), 0.0)
        self.assertEqual(rtVal.a.getSimpleType(), 1.0)

    def testGetDataType(self):
        attribute = self.getAttribute()

        self.assertEqual(attribute.getDataType(), 'Color')



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestColorAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
