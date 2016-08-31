
import unittest

from kraken.core.objects.constraints.constraint import Constraint


class TestConstraint(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetBuildName(self):
        pass
        # getBuildName

    def testSetFlag(self):
        pass
        # setFlag

    def testTestFlag(self):
        pass
        # testFlag

    def testClearFlag(self):
        pass
        # clearFlag

    def testGetFlags(self):
        pass
        # getFlags

    def testGetSources(self):
        pass
        # getSources

    def testGetMaintainOffset(self):
        pass
        # getMaintainOffset

    def testSetMaintainOffset(self):
        pass
        # setMaintainOffset

    def testSetConstrainee(self):
        pass
        # setConstrainee

    def testGetConstrainee(self):
        pass
        # getConstrainee

    def testAddConstrainer(self):
        pass
        # addConstrainer

    def testSetConstrainer(self):
        pass
        # setConstrainer

    def testRemoveConstrainerByIndex(self):
        pass
        # removeConstrainerByIndex

    def testGetConstrainers(self):
        pass
        # getConstrainers

    def testCompute(self):
        pass
        # compute

    def testComputeOffset(self):
        pass
        # computeOffset

    def testEvaluate(self):
        pass
        # evaluate


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
