
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup


class TestAttributeGroup(unittest.TestCase):

    def testGetName(self):
        pass

    def testAddAttribute(self):
        pass
        # addAttribute

    def testRemoveAttributeByIndex(self):
        pass
        # removeAttributeByIndex

    def testRemoveAttributeByName(self):
        pass
        # removeAttributeByName

    def testGetNumAttributes(self):
        pass
        # getNumAttributes

    def testGetAttributeByIndex(self):
        pass
        # getAttributeByIndex

    def testGetAttributeByName(self):
        pass
        # getAttributeByName



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAttributeGroup)


if __name__ == '__main__':
    unittest.main(verbosity=2)
