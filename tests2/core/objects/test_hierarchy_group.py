
import unittest

from kraken.core.objects.hierarchy_group import HierarchyGroup


class TestHierarchyGroup(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestHierarchyGroup)


if __name__ == '__main__':
    unittest.main(verbosity=2)
