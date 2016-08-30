
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup


class TestAttributeGroup(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAttributeGroup)


if __name__ == '__main__':
    unittest.main(verbosity=2)
