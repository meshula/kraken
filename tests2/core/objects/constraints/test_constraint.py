
import unittest

from kraken.core.objects.locator import Locator
from kraken.core.objects.constraints.constraint import Constraint


class TestConstraint(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._locator1 = Locator('locator1')
        cls._locator2 = Locator('locator2')
        cls._constraint = Constraint('test')
        cls._constraint.setFlag('EXPLICIT_NAME')

        cls._constraint.setConstrainee(cls._locator1)
        cls._constraint.addConstrainer(cls._locator2)

    def getConstraint(self):
        return self._constraint

    def getLocator1(self):
        return self._locator1

    def getLocator2(self):
        return self._locator2

    # ======
    # Tests
    # ======
    def testGetBuildName(self):
        constraint = self.getConstraint()
        # locator1 = self.getLocator1()
        # locator2 = self.getLocator2()

        buildName = constraint.getBuildName()

        self.assertEqual(buildName, 'test')

    def testSetFlag(self):
        constraint = self.getConstraint()
        setFlag = constraint.setFlag('TESTFLAG')

        self.assertTrue(setFlag)

        constraint.clearFlag('TESTFLAG')

    def testTestFlag(self):
        constraint = self.getConstraint()
        constraint.setFlag('TESTFLAG')

        self.assertTrue(constraint.testFlag('TESTFLAG'))

        constraint.clearFlag('TESTFLAG')

    def testClearFlag(self):
        constraint = self.getConstraint()
        constraint.setFlag('TESTFLAG')
        constraint.clearFlag('TESTFLAG')

        self.assertFalse(constraint.testFlag('TESTFLAG'))

    def testGetFlags(self):
        constraint = self.getConstraint()
        constraint.setFlag('TESTFLAG')

        flags = constraint.getFlags()
        self.assertEqual(flags, ['TESTFLAG', 'EXPLICIT_NAME'])

        constraint.clearFlag('TESTFLAG')

    def testGetSources(self):
        constraint = self.getConstraint()
        locator2 = self.getLocator2()
        sources = constraint.getSources()

        self.assertIsNotNone(sources)
        self.assertEqual(sources, [locator2])

    def testGetMaintainOffset(self):
        constraint = self.getConstraint()
        maintainOffset = constraint.getMaintainOffset()

        self.assertFalse(maintainOffset)

    def testSetMaintainOffset(self):
        constraint = self.getConstraint()
        constraint.setMaintainOffset(True)
        maintainOffset = constraint.getMaintainOffset()

        self.assertTrue(maintainOffset)

        self.assertRaises(TypeError, lambda: constraint.setMaintainOffset(4))

    def testSetConstrainee(self):
        constraint = Constraint('test')
        locator = Locator('testLocator')
        setTest = constraint.setConstrainee(locator)

        self.assertTrue(setTest)

    def testGetConstrainee(self):
        constraint = Constraint('test')
        locator = Locator('testLocator')

        constraint.setConstrainee(locator)

        getTest = constraint.getConstrainee()

        self.assertIsNotNone(getTest)
        self.assertIs(getTest, locator)

    def testAddConstrainer(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')

        constraint.setConstrainee(locator1)

        testAdd = constraint.addConstrainer(locator2)

        self.assertTrue(testAdd)

    def testSetConstrainer(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')
        locator3 = Locator('testLocator3')

        constraint.setConstrainee(locator1)
        constraint.addConstrainer(locator2)

        testSet = constraint.setConstrainer(locator3, index=0)

        self.assertTrue(testSet)
        self.assertEqual(constraint.getConstrainers(), [locator3])

    def testRemoveConstrainerByIndex(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')
        locator3 = Locator('testLocator3')

        constraint.setConstrainee(locator1)
        constraint.addConstrainer(locator2)
        constraint.addConstrainer(locator3)

        testRemoveByIndex = constraint.removeConstrainerByIndex(0)

        self.assertTrue(testRemoveByIndex)
        self.assertEqual(constraint.getConstrainers(), [locator3])

    def testGetConstrainers(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')
        locator3 = Locator('testLocator3')

        constraint.setConstrainee(locator1)
        constraint.addConstrainer(locator2)
        constraint.addConstrainer(locator3)

        testGet = constraint.getConstrainers()

        self.assertEqual(testGet, [locator2, locator3])

    def testCompute(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')
        locator3 = Locator('testLocator3')

        constraint.setConstrainee(locator1)
        constraint.addConstrainer(locator2)
        constraint.addConstrainer(locator3)

        # The KrakenConstraint KL object does not have the addConstrainer method
        self.assertRaises(AttributeError, lambda: constraint.compute())

    def testComputeOffset(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')
        locator3 = Locator('testLocator3')

        locator2.xfo.tr.x = 4

        constraint.setConstrainee(locator1)
        constraint.addConstrainer(locator2)
        constraint.addConstrainer(locator3)
        constraint.setMaintainOffset(True)

        # The KrakenConstraint KL object does not have the addConstrainer method
        self.assertRaises(AttributeError, lambda: constraint.computeOffset())

    def testEvaluate(self):
        constraint = Constraint('test')
        locator1 = Locator('testLocator1')
        locator2 = Locator('testLocator2')
        locator3 = Locator('testLocator3')

        constraint.setConstrainee(locator1)
        constraint.addConstrainer(locator2)
        constraint.addConstrainer(locator3)

        # The KrakenConstraint KL object does not have the addConstrainer method
        self.assertRaises(AttributeError, lambda: constraint.evaluate())


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
