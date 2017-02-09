
import unittest

from kraken.core.maths.vec4 import Vec4


class TestVec4(unittest.TestCase):

    def testString(self):
        vec = Vec4()

        self.assertEquals(str(vec),
                          "Vec4(0.0, 0.0, 0.0, 0.0)")

    def testGetPropertyValues(self):
        vec = Vec4(0.0, 1.0, 2.0, 3.0)

        self.assertEquals(vec.x, 0.0)
        self.assertEquals(vec.y, 1.0)
        self.assertEquals(vec.z, 2.0)
        self.assertEquals(vec.t, 3.0)

    def testSetPropertyValues(self):
        vec = Vec4()

        vec.x = 2
        vec.y = 3
        vec.z = 4
        vec.t = 4

        self.assertEquals(vec.x, 2.0)
        self.assertEquals(vec.y, 3.0)
        self.assertEquals(vec.z, 4.0)
        self.assertEquals(vec.t, 4.0)

    def testEquals(self):
        vec1 = Vec4(0.0, 1.0, 0.0, 3.0)
        vec2 = Vec4(0.0, 1.0, 0.0, 3.0)

        self.assertEqual(vec1, vec2)

    def testNotEquals(self):
        vec1 = Vec4(0.0, 1.0, 0.0, 0.0)
        vec2 = Vec4(2.0, 1.0, 0.0, 0.0)

        self.assertNotEqual(vec1, vec2)

    def testAdd(self):
        vec1 = Vec4(0.0, 1.0, 0.0, 3.0)
        vec2 = Vec4(0.0, 1.0, 0.0, 3.0)

        vec3 = vec1 + vec2
        result = Vec4(0.0, 2.0, 0.0, 6.0)

        self.assertEqual(vec3, result)

    def testSubtract(self):
        vec1 = Vec4(3.0, 1.0, 2.0, 3.0)
        vec2 = Vec4(1.0, 0.25, 1.0, 3.0)

        vec3 = vec1 - vec2
        result = Vec4(2.0, 0.75, 1.0, 0.0)

        self.assertEqual(vec3, result)

    def testMultiply(self):
        vec1 = Vec4(3.0, 1.0, 0.0, 2.0)
        vec2 = Vec4(1.0, 0.25, 0.0, 2.0)

        vec3 = vec1 * vec2
        result = Vec4(3.0, 0.25, 0.0, 4.0)

        self.assertEqual(vec3, result)

    def testDivide(self):
        vec1 = Vec4(3.0, 1.0, 2.0, 6.0)
        vec2 = Vec4(1.0, 0.25, 1.0, 3.0)

        vec3 = vec1 / vec2
        result = Vec4(3.0, 4.0, 2.0, 2.0)

        self.assertEqual(vec3, result)

    def testClone(self):
        vec1 = Vec4(3.0, 1.0, 2.0, 4.0)
        vec2 = vec1.clone()

        self.assertIsNot(vec1, vec2)

        self.assertEqual(vec1, vec2)

    def testSet(self):
        vec = Vec4()

        vec.set(0.25, -1.05, 0.0, 4.0)
        self.assertEquals(vec.x, 0.25)
        self.assertEquals(round(vec.y, 2), -1.05)
        self.assertEquals(vec.z, 0.0)
        self.assertEquals(vec.t, 4.0)

    def testSetNull(self):
        vec = Vec4(1.0, 2.0, 3.0, 4.0)

        vec.setNull()

        self.assertEquals(vec, Vec4())

    def testAlmostEqualWithPrecision(self):
        vec1 = Vec4(1.01, 2.0, 0.0, 4.0)
        vec2 = Vec4(1.0, 2.0, 0.0, 4.0)

        result = vec1.almostEqualWithPrecision(vec2, 0.1)
        self.assertTrue(result)

    def testAlmostEqual(self):
        vec1 = Vec4(1.000001, 2.0, 0.0, 4.0)
        vec2 = Vec4(1.0, 2.0, 0.0, 4.0)

        self.assertTrue(vec1.almostEqual(vec2))

    def testComponent(self):
        vec = Vec4(1.0, 2.0, 3.0, 4.0)

        self.assertEquals(vec.component(0), 1.0)
        self.assertEquals(vec.component(1), 2.0)
        self.assertEquals(vec.component(2), 3.0)
        self.assertEquals(vec.component(3), 4.0)

    def testSetComponent(self):
        vec = Vec4()

        vec.setComponent(0, 1.0)
        vec.setComponent(1, 2.0)
        vec.setComponent(2, 3.0)
        vec.setComponent(3, 4.0)

        self.assertEquals(vec.x, 1.0)
        self.assertEquals(vec.y, 2.0)
        self.assertEquals(vec.z, 3.0)
        self.assertEquals(vec.t, 4.0)

    def testMultiplyScalar(self):
        vec = Vec4(1.0, 1.0, 1.0, 1.0)

        result = vec.multiplyScalar(3)

        self.assertEquals(result.x, 3.0)
        self.assertEquals(result.y, 3.0)
        self.assertEquals(result.z, 3.0)
        self.assertEquals(result.t, 3.0)

    def testDivideScalar(self):
        vec = Vec4(1.0, 1.0, 1.0, 1.0)

        result = vec.divideScalar(2)

        self.assertEquals(result.x, 0.5)
        self.assertEquals(result.y, 0.5)
        self.assertEquals(result.z, 0.5)
        self.assertEquals(result.t, 0.5)

    def testNegate(self):
        vec = Vec4(3.0, 4.0, 5.0, 6.0)

        result = vec.negate()

        self.assertEquals(result.x, -3.0)
        self.assertEquals(result.y, -4.0)
        self.assertEquals(result.z, -5.0)
        self.assertEquals(result.t, -6.0)

    def testInverse(self):
        vec = Vec4(3.0, 4.0, 10.0, 15.0)

        result = vec.inverse()

        self.assertEquals(result.x, 0.3333333432674408)
        self.assertEquals(result.y, 0.25)
        self.assertEquals(result.z, 0.10000000149011612)
        self.assertEquals(result.t, 0.06666667014360428)

    def testDot(self):
        vec1 = Vec4(0.0, 1.0, 0.0, 0.0)
        vec2 = Vec4(1.0, 0.0, 0.0, 0.0)

        result = vec1.dot(vec2)

        self.assertEqual(result, 0.0)

    def testLengthSquared(self):
        vec = Vec4(2.0, 2.0, 2.0, 2.0)

        result = vec.lengthSquared()

        self.assertEquals(result, 16.0)

    def testLength(self):
        vec = Vec4(1.0, 1.0, 1.0, 1.0)

        result = vec.length()

        self.assertEquals(result, 2.0)

    def testUnit(self):
        vec = Vec4(1.5, 3.0, 1.0, 2.0)

        result = vec.unit()
        testResult = Vec4(0.3721041977405548,
                          0.7442083954811096,
                          0.24806946516036987,
                          0.49613893032073975)

        self.assertEquals(result.x, testResult.x)
        self.assertEquals(result.y, testResult.y)
        self.assertEquals(result.z, testResult.z)
        self.assertEquals(result.t, testResult.t)

    def testSetUnit(self):
        vec = Vec4(0.001, 0.001, 0.001, 0.001)

        result = vec.setUnit()

        self.assertEquals(result, 0.0020000000949949026)

    def testNormalize(self):
        vec = Vec4(0.001, 0.001, 0.001, 0.001)

        vec.normalize()
        testResult = Vec4(0.5,
                          0.5,
                          0.5,
                          0.5)

        self.assertEquals(vec.x, testResult.x)
        self.assertEquals(vec.y, testResult.y)
        self.assertEquals(vec.z, testResult.z)
        self.assertEquals(vec.t, testResult.t)

    def testClamp(self):
        vec = Vec4(1.5, 3.0, 2.6, 4.6)

        result = vec.clamp(Vec4(0.25, 0.5, 0.75, 0.0), Vec4(1.75, 2.75, 3.75, 2.0))

        self.assertEquals(result, Vec4(1.5, 2.75, 2.6, 2.0))

    def testUnitsAngleTo(self):
        vec1 = Vec4(0.0, 1.0, -1.0, 0.0).unit()
        vec2 = Vec4(1.0, 0.0, 2.0, 0.0).unit()

        result = vec1.unitsAngleTo(vec2)

        self.assertEquals(result, 2.2555155754089355)

    def testAngleTo(self):
        vec1 = Vec4(0.0, 1.0, -1.0, 4.0)
        vec2 = Vec4(1.0, 0.0, 2.0, 4.0)

        result = vec1.angleTo(vec2)

        self.assertEquals(result, 0.7668754458427429)

    def testDistanceTo(self):
        vec1 = Vec4(0.0, 0.0, 0.0, 0.0)
        vec2 = Vec4(0.0, 1.0, 0.0, 0.0)

        result = vec1.distanceTo(vec2)

        self.assertEquals(result, 1.0)

    def testLinearInterpolate(self):
        vec1 = Vec4(0.0, 0.0, 0.0, 0.0)
        vec2 = Vec4(0.0, 1.0, 0.0, 0.0)

        result = vec1.linearInterpolate(vec2, 0.5)

        self.assertEquals(result, Vec4(0.0, 0.5, 0.0, 0.0))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestVec4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
