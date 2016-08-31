
import unittest

from kraken.core.objects.curve import Curve


class TestCurve(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetCurveData(self):
        pass
        # getCurveData

    def testSetCurveData(self):
        pass
        # setCurveData

    def testAppendCurveData(self):
        pass
        # appendCurveData

    def testCheckSubCurveIndex(self):
        pass
        # checkSubCurveIndex

    def testGetNumSubCurves(self):
        pass
        # getNumSubCurves

    def testGetSubCurveClosed(self):
        pass
        # getSubCurveClosed

    def testGetSubCurveData(self):
        pass
        # getSubCurveData

    def testSetSubCurveData(self):
        pass
        # setSubCurveData

    def testRemoveSubCurveByIndex(self):
        pass
        # removeSubCurveByIndex



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCurve)


if __name__ == '__main__':
    unittest.main(verbosity=2)
