
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.attribute import Attribute


class TestAttributeGroup(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')

    def getAttributeGroup(self):
        return self._attributeGroup

    # ======
    # Tests
    # ======
    def testAddAttribute(self):
        attributeGroup = self.getAttributeGroup()
        attribute = Attribute('test', True)

        attributeGroup.addAttribute(attribute)

        self.assertTrue(attribute in attributeGroup._attributes)

        attributeGroup.removeAttributeByIndex(0)

    def testRemoveAttributeByIndex(self):
        attributeGroup = self.getAttributeGroup()
        attribute1 = Attribute('test1', True)
        attribute2 = Attribute('test2', True)

        attributeGroup.addAttribute(attribute1)
        attributeGroup.addAttribute(attribute2)

        removed = attributeGroup.removeAttributeByIndex(1)

        self.assertTrue(removed)
        self.assertTrue(attribute2 not in attributeGroup._attributes)

        attributeGroup.removeAttributeByIndex(0)

    def testRemoveAttributeByName(self):
        attributeGroup = self.getAttributeGroup()
        attribute1 = Attribute('test1', True)
        attribute2 = Attribute('test2', True)

        attributeGroup.addAttribute(attribute1)
        attributeGroup.addAttribute(attribute2)

        removed = attributeGroup.removeAttributeByName('test2')

        self.assertTrue(removed)
        self.assertTrue(attribute2 not in attributeGroup._attributes)

        removed = attributeGroup.removeAttributeByName('test1')

    def testGetNumAttributes(self):
        attributeGroup = self.getAttributeGroup()
        attribute1 = Attribute('test1', True)
        attribute2 = Attribute('test2', True)

        attributeGroup.addAttribute(attribute1)
        attributeGroup.addAttribute(attribute2)
        numAttributes = attributeGroup.getNumAttributes()

        self.assertEquals(numAttributes, 2)

        attributeGroup.removeAttributeByName('test1')
        attributeGroup.removeAttributeByName('test2')

        self.assertEquals(attributeGroup.getNumAttributes(), 0)

    def testGetAttributeByIndex(self):
        attributeGroup = self.getAttributeGroup()
        attribute1 = Attribute('test1', True)
        attribute2 = Attribute('test2', True)

        attributeGroup.addAttribute(attribute1)
        attributeGroup.addAttribute(attribute2)

        attr2 = attributeGroup.getAttributeByIndex(1)

        self.assertIs(attribute2, attr2)

        attributeGroup.removeAttributeByName('test1')
        attributeGroup.removeAttributeByName('test2')

    def testGetAttributeByName(self):
        attributeGroup = self.getAttributeGroup()
        attribute1 = Attribute('test1', True)

        attributeGroup.addAttribute(attribute1)

        attr1 = attributeGroup.getAttributeByName('test1')

        self.assertIs(attribute1, attr1)

        attributeGroup.removeAttributeByName('test1')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAttributeGroup)


if __name__ == '__main__':
    unittest.main(verbosity=2)
