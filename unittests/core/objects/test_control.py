
import unittest

from kraken.core.maths.vec3 import Vec3
from kraken.core.objects.control import Control


class TestControl(unittest.TestCase):

    def testGetShape(self):
        testCtrl = Control('testControl')
        ctrlShape = testCtrl.getShape()

        self.assertEqual(ctrlShape, 'null')

    def testSetShape(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('sphere')

        self.assertEqual(testCtrl.getShape(), 'sphere')

    def testAlignOnXAxis(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('square')
        testAlign = testCtrl.alignOnXAxis()

        self.assertTrue(testAlign)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for eachPoint in eachSubCurve["points"]:
                self.assertTrue(eachPoint[0] >= 0.0)

    def testAlignOnXAxisNegative(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('square')
        testAlign = testCtrl.alignOnXAxis(negative=True)

        self.assertTrue(testAlign)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for eachPoint in eachSubCurve["points"]:
                self.assertTrue(eachPoint[0] <= 0.0)

    def testAlignOnYAxis(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('cube')
        testAlign = testCtrl.alignOnYAxis()

        self.assertTrue(testAlign)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for eachPoint in eachSubCurve["points"]:
                self.assertTrue(eachPoint[1] >= 0.0)

    def testAlignOnYAxisNegative(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('cube')
        testAlign = testCtrl.alignOnYAxis(negative=True)

        self.assertTrue(testAlign)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for eachPoint in eachSubCurve["points"]:
                self.assertTrue(eachPoint[1] <= 0.0)

    def testAlignOnZAxis(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('cube')
        testAlign = testCtrl.alignOnZAxis()

        self.assertTrue(testAlign)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for eachPoint in eachSubCurve["points"]:
                self.assertTrue(eachPoint[2] >= 0.0)

    def testAlignOnZAxisNegative(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('cube')
        testAlign = testCtrl.alignOnZAxis(negative=True)

        self.assertTrue(testAlign)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for eachPoint in eachSubCurve["points"]:
                self.assertTrue(eachPoint[2] <= 0.0)

    def testScalePointsOnAxis(self):
        testCtrl = Control('testControl')

        # X Axis
        testCtrl.setShape('square')
        testCtrl.alignOnXAxis()
        testScale = testCtrl.scalePointsOnAxis(2, scaleAxis="POSX")

        self.assertTrue(testScale)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for i, eachPoint in enumerate(eachSubCurve["points"]):
                if i < 2:
                    self.assertEqual(eachPoint[0], 2.0)

        # Y Axis
        testCtrl.setShape('cube')
        testCtrl.alignOnYAxis()
        testScale = testCtrl.scalePointsOnAxis(2, scaleAxis="POSY")

        self.assertTrue(testScale)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for i, eachPoint in enumerate(eachSubCurve["points"]):
                if i == 2:
                    self.assertTrue(eachPoint[1] >= 0.0 and eachPoint[1] <= 2.0)

        # Z Axis
        testCtrl.setShape('square')
        testCtrl.alignOnZAxis()
        testScale = testCtrl.scalePointsOnAxis(2, scaleAxis="POSZ")

        self.assertTrue(testScale)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for i, eachPoint in enumerate(eachSubCurve["points"]):
                if i < 2:
                    self.assertTrue(eachPoint[2] >= 0.0 and eachPoint[2] <= 2.0)

    def testScalePoints(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('square')
        testScale = testCtrl.scalePoints(Vec3(2.0, 2.0, 2.0))

        self.assertTrue(testScale)

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for i, eachPoint in enumerate(eachSubCurve["points"]):
                self.assertEqual(abs(eachPoint[0]), 1.0)
                self.assertEqual(abs(eachPoint[2]), 1.0)

    def testRotatePoints(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('square')
        testRot = testCtrl.rotatePoints(0, 45, 0)

        self.assertTrue(testRot)

        testPointValues = [
            [-0.0, 0.0, -0.71],
            [0.71, 0.0, -0.0],
            [0.0, 0.0, 0.71],
            [-0.71, 0.0, 0.0]
        ]

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for i, eachPoint in enumerate(eachSubCurve["points"]):
                roundedValues = [round(x, 2) for x in eachPoint]

                self.assertEqual(roundedValues, testPointValues[i])

    def testTranslatePoints(self):
        testCtrl = Control('testControl')
        testCtrl.setShape('square')
        testRot = testCtrl.translatePoints(Vec3(0.5, 0.5, 0.5))

        self.assertTrue(testRot)

        testPointValues = [
            [1.0, 0.5, 0.0],
            [1.0, 0.5, 1.0],
            [0.0, 0.5, 1.0],
            [0.0, 0.5, 0.0]
        ]

        curveData = list(testCtrl.getCurveData())
        for eachSubCurve in curveData:
            for i, eachPoint in enumerate(eachSubCurve["points"]):
                self.assertEqual(eachPoint, testPointValues[i])

    def testInsertCtrlSpace(self):
        testCtrl = Control('testControl')
        self.assertIsNone(testCtrl.getParent())

        ctrlSpace = testCtrl.insertCtrlSpace()

        self.assertIsNotNone(ctrlSpace)
        self.assertTrue(ctrlSpace.isTypeOf('CtrlSpace'))
        self.assertIsNotNone(testCtrl.getParent())


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestControl)


if __name__ == '__main__':
    unittest.main(verbosity=2)
