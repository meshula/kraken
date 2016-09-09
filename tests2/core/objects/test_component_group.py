
import unittest

from kraken.core.objects.components.component import Component
from kraken.core.objects.component_group import ComponentGroup


class TestComponentGroup(unittest.TestCase):

    def testGetName(self):
        testComp = Component('testComponent', location='L')
        testCmpGrp = ComponentGroup('testCmpGrp', testComp)
        getName = testCmpGrp.getName()

        self.assertTrue(type(getName is str))
        self.assertEqual(getName, 'testComponent')

    def testGetNameDecoration(self):
        testComp = Component('testComponent', location='L')
        testCmpGrp = ComponentGroup('testCmpGrp', testComp)
        getNameDec = testCmpGrp.getNameDecoration()

        self.assertTrue(type(getNameDec is str))
        self.assertEqual(getNameDec, ':L')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentGroup)


if __name__ == '__main__':
    unittest.main(verbosity=2)
