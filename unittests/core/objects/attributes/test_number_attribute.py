
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.number_attribute import NumberAttribute


class TestIntegerAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = NumberAttribute('test', parent=cls._attributeGroup)

    def getAttributeGroup(self):
        return self._attributeGroup

    def getAttribute(self):
        return self._attribute

    # ======
    # Tests
    # ======
    def testSetValue(self):
        attribute = self.getAttribute()

        self.assertRaises(NotImplementedError, lambda: attribute.setValue(1))

    def testGetMin(self):
        attribute = self.getAttribute()
        attribute.setMin(0.0)

        minValue = attribute.getMin()

        self.assertEqual(minValue, 0.0)

        # Reset
        attribute._min = None

    def testSetMin(self):
        attribute = self.getAttribute()
        attribute.setMin(2.0)

        minValue = attribute.getMin()

        self.assertEqual(minValue, 2.0)

        # Reset
        attribute._min = None

    def testGetMax(self):
        attribute = self.getAttribute()
        attribute.setMax(0.0)

        maxValue = attribute.getMax()

        self.assertEqual(maxValue, 0.0)

        # Reset
        attribute._max = None

    def testSetMax(self):
        attribute = self.getAttribute()
        attribute.setMax(3.0)

        maxValue = attribute.getMax()

        self.assertEqual(maxValue, 3.0)

        # Reset
        attribute._max = None

    def testGetUIMin(self):
        attribute = self.getAttribute()

        uiMin = attribute.getUIMin()

        self.assertEqual(uiMin, None)

    def testSetUIMin(self):
        attribute = self.getAttribute()

        self.assertRaises(TypeError, lambda: attribute.setUIMin(1.0))

    def testGetUIMax(self):
        attribute = self.getAttribute()

        uiMax = attribute.getUIMax()

        self.assertEqual(uiMax, None)

    def testSetUIMax(self):
        attribute = self.getAttribute()

        self.assertRaises(TypeError, lambda: attribute.setUIMax(1.0))



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestIntegerAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
