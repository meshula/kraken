
import unittest

from kraken.core.objects.control import Control


class TestControl(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetShape(self):
        pass
        # getShape

    def testSetShape(self):
        pass
        # setShape

    def testAlignOnXAxis(self):
        pass
        # alignOnXAxis

    def testAlignOnYAxis(self):
        pass
        # alignOnYAxis

    def testAlignOnZAxis(self):
        pass
        # alignOnZAxis

    def testScalePointsOnAxis(self):
        pass
        # scalePointsOnAxis

    def testScalePoints(self):
        pass
        # scalePoints

    def testRotatePoints(self):
        pass
        # rotatePoints

    def testTranslatePoints(self):
        pass
        # translatePoints

    def testInsertCtrlSpace(self):
        pass
        # insertCtrlSpace


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestControl)


if __name__ == '__main__':
    unittest.main(verbosity=2)
