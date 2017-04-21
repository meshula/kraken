
import unittest

from kraken.core.objects.curve import Curve


class TestCurve(unittest.TestCase):

    def testGetCurveData(self):
        testCrv = Curve('testCurve')
        crvData = testCrv.getCurveData()

        self.assertIsNone(crvData)

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrv.setCurveData(testCrvData)
        crvData = testCrv.getCurveData()

        self.assertIsNotNone(crvData)
        self.assertEqual(crvData[0]['points'], [[0.0, 0.5, 0.0]])

    def testSetCurveData(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        setCrvData = testCrv.setCurveData(testCrvData)

        self.assertTrue(setCrvData)

        crvData = testCrv.getCurveData()

        self.assertIsNotNone(crvData)
        self.assertEqual(len(crvData), 1)
        self.assertIn('points', crvData[0])
        self.assertIn('degree', crvData[0])
        self.assertIn('closed', crvData[0])

    def testAppendCurveData(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        self.assertRaises(ValueError, lambda: testCrv.appendCurveData(testCrvData))

        testCrv.setCurveData(testCrvData)
        appendCrvData = testCrv.appendCurveData(testCrvData)
        crvData = testCrv.getCurveData()

        self.assertTrue(appendCrvData)
        self.assertIsNotNone(crvData)
        self.assertEqual(len(crvData), 2)


    def testCheckSubCurveIndex(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrv.setCurveData(testCrvData)

        self.assertTrue(testCrv.checkSubCurveIndex(0))

    def testGetNumSubCurves(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrv.setCurveData(testCrvData)

        self.assertEqual(testCrv.getNumSubCurves(), 1)

    def testGetSubCurveClosed(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrv.setCurveData(testCrvData)

        self.assertFalse(testCrv.getSubCurveClosed(0))

    def testGetSubCurveData(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrv.setCurveData(testCrvData)

        data = testCrv.getSubCurveData(0)
        self.assertTrue(type(data) is dict)
        self.assertTrue('points' in data)
        self.assertTrue('degree' in data)
        self.assertTrue('closed' in data)

    def testSetSubCurveData(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrvData2 = {
            "points": [
                [1.0, 0.0, 0.0]
            ],
            "degree": 1,
            "closed": True
        }

        testCrv.setCurveData(testCrvData)
        testCrv.setSubCurveData(0, testCrvData2)

        crvData = testCrv.getSubCurveData(0)

        self.assertIsNotNone(crvData)
        self.assertTrue('points' in crvData)
        self.assertTrue(crvData['points'], [[1.0, 0.0, 0.0]])
        self.assertTrue('degree' in crvData)
        self.assertTrue('closed' in crvData)

    def testRemoveSubCurveByIndex(self):
        testCrv = Curve('testCurve')

        testCrvData = [{
            "points": [
                [0.0, 0.5, 0.0]
            ],
            "degree": 1,
            "closed": False
        }]

        testCrv.setCurveData(testCrvData)
        testCrv.appendCurveData(testCrvData)

        self.assertEqual(testCrv.getNumSubCurves(), 2)

        testCrv.removeSubCurveByIndex(1)

        self.assertEqual(testCrv.getNumSubCurves(), 1)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCurve)


if __name__ == '__main__':
    unittest.main(verbosity=2)
