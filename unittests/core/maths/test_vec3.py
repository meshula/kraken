
import unittest

from kraken.core.maths.vec3 import Vec3


class TestVec3(unittest.TestCase):

    def testString(self):
        vec = Vec3()

        self.assertEquals(str(vec),
                          "Vec3(0.0, 0.0, 0.0)")

    def testGetPropertyValues(self):
        vec = Vec3(0.0, 1.0, 2.0)

        self.assertEquals(vec.x, 0.0)
        self.assertEquals(vec.y, 1.0)
        self.assertEquals(vec.z, 2.0)

    def testSetPropertyValues(self):
        vec = Vec3()

        vec.x = 2
        vec.y = 3
        vec.z = 4

        self.assertEquals(vec.x, 2.0)
        self.assertEquals(vec.y, 3.0)
        self.assertEquals(vec.z, 4.0)

    def testEquals(self):
        vec1 = Vec3(0.0, 1.0, 0.0)
        vec2 = Vec3(0.0, 1.0, 0.0)

        self.assertEqual(vec1, vec2)

    def testNotEquals(self):
        vec1 = Vec3(0.0, 1.0, 0.0)
        vec2 = Vec3(2.0, 1.0, 0.0)

        self.assertNotEqual(vec1, vec2)

    def testAdd(self):
        vec1 = Vec3(0.0, 1.0, 0.0)
        vec2 = Vec3(0.0, 1.0, 0.0)

        vec3 = vec1 + vec2
        result = Vec3(0.0, 2.0, 0.0)

        self.assertEqual(vec3, result)

    def testSubtract(self):
        vec1 = Vec3(3.0, 1.0, 0.0)
        vec2 = Vec3(1.0, 0.25, 0.0)

        vec3 = vec1 - vec2
        result = Vec3(2.0, 0.75, 0.0)

        self.assertEqual(vec3, result)

    def testMultiply(self):
        vec1 = Vec3(3.0, 1.0, 0.0)
        vec2 = Vec3(1.0, 0.25, 0.0)

        vec3 = vec1 * vec2
        result = Vec3(3.0, 0.25, 0.0)

        self.assertEqual(vec3, result)

    def testDivide(self):
        vec1 = Vec3(3.0, 1.0, 2.0)
        vec2 = Vec3(1.0, 0.25, 1.0)

        vec3 = vec1 / vec2
        result = Vec3(3.0, 4.0, 2.0)

        self.assertEqual(vec3, result)

    def testClone(self):
        vec1 = Vec3(3.0, 1.0, 2.0)
        vec2 = vec1.clone()

        self.assertIsNot(vec1, vec2)

        self.assertEqual(vec1, vec2)

    def testSet(self):
        vec = Vec3()

        vec.set(0.25, -1.05, 0.0)
        self.assertEquals(vec.x, 0.25)
        self.assertEquals(round(vec.y, 2), -1.05)
        self.assertEquals(vec.z, 0.0)

    def testSetNull(self):
        vec = Vec3(1.0, 2.0, 3.0)

        vec.setNull()

        self.assertEquals(vec, Vec3())

    def testAlmostEqualWithPrecision(self):
        vec1 = Vec3(1.01, 2.0, 0.0)
        vec2 = Vec3(1.0, 2.0, 0.0)

        result = vec1.almostEqualWithPrecision(vec2, 0.1)
        self.assertTrue(result)

    def testAlmostEqual(self):
        vec1 = Vec3(1.000001, 2.0, 0.0)
        vec2 = Vec3(1.0, 2.0, 0.0)

        self.assertTrue(vec1.almostEqual(vec2))

    def testComponent(self):
        vec = Vec3(1.0, 2.0, 3.0)

        self.assertEquals(vec.component(0), 1.0)
        self.assertEquals(vec.component(1), 2.0)
        self.assertEquals(vec.component(2), 3.0)

    def testSetComponent(self):
        vec = Vec3()

        vec.setComponent(0, 1.0)
        vec.setComponent(1, 2.0)
        vec.setComponent(2, 3.0)

        self.assertEquals(vec.x, 1.0)
        self.assertEquals(vec.y, 2.0)
        self.assertEquals(vec.z, 3.0)

    def testMultiplyScalar(self):
        vec = Vec3(1.0, 1.0, 1.0)

        result = vec.multiplyScalar(3)

        self.assertEquals(result.x, 3.0)
        self.assertEquals(result.y, 3.0)
        self.assertEquals(result.z, 3.0)

    def testDivideScalar(self):
        vec = Vec3(1.0, 1.0, 1.0)

        result = vec.divideScalar(2)

        self.assertEquals(result.x, 0.5)
        self.assertEquals(result.y, 0.5)
        self.assertEquals(result.z, 0.5)

    def testNegate(self):
        vec = Vec3(3.0, 4.0, 5.0)

        result = vec.negate()

        self.assertEquals(result.x, -3.0)
        self.assertEquals(result.y, -4.0)
        self.assertEquals(result.z, -5.0)

    def testInverse(self):
        vec = Vec3(3.0, 4.0, 10.0)

        result = vec.inverse()

        self.assertEquals(result.x, 0.3333333432674408)
        self.assertEquals(result.y, 0.25)
        self.assertEquals(round(result.z, 2), 0.1)

    def testDot(self):
        vec1 = Vec3(0.0, 1.0, 0.0)
        vec2 = Vec3(1.0, 0.0, 0.0)

        result = vec1.dot(vec2)

        self.assertEqual(result, 0.0)

    def testCross(self):
        vec1 = Vec3(0.0, 1.0, 0.0)
        vec2 = Vec3(1.0, 0.0, 0.0)

        result = vec1.cross(vec2)

        self.assertEqual(result, Vec3(0.0, 0.0, -1.0))

    def testLengthSquared(self):
        vec = Vec3(2.0, 2.0, 2.0)

        result = vec.lengthSquared()

        self.assertEquals(result, 12.0)

    def testLength(self):
        vec = Vec3(1.0, 1.0, 1.0)

        result = vec.length()

        self.assertEquals(result, 1.7320507764816284)

    def testUnit(self):
        vec = Vec3(1.5, 3.0, 1.0)

        result = vec.unit()

        self.assertEquals(result, Vec3(0.428571432829, 0.857142865658, 0.285714298487))

    def testUnit_safe(self):
        vec = Vec3(0.001, 0.001, 0.001)

        result = vec.unit_safe()

        self.assertEquals(result, Vec3(0.577350258827, 0.577350258827, 0.577350258827))

    def testSetUnit(self):
        vec = Vec3(0.001, 0.001, 0.001)

        result = vec.setUnit()

        self.assertEquals(result, 0.0017320509068667889)

    def testNormalize(self):
        vec = Vec3(0.001, 0.001, 0.001)

        vec.normalize()

        self.assertEquals(vec, Vec3(0.577350258827, 0.577350258827, 0.577350258827))

    def testClamp(self):
        vec = Vec3(1.5, 3.0, 2.6)

        result = vec.clamp(Vec3(0.25, 0.5, 0.75), Vec3(1.75, 2.75, 3.75))

        self.assertEquals(result, Vec3(1.5, 2.75, 2.6))

    def testUnitsAngleTo(self):
        vec1 = Vec3(0.0, 1.0, -1.0).unit()
        vec2 = Vec3(1.0, 0.0, 2.0).unit()

        result = vec1.unitsAngleTo(vec2)

        self.assertEquals(result, 2.2555155754089355)

    def testAngleTo(self):
        vec1 = Vec3(0.0, 1.0, -1.0)
        vec2 = Vec3(1.0, 0.0, 2.0)

        result = vec1.angleTo(vec2)

        self.assertEquals(result, 2.2555155754089355)

    def testDistanceTo(self):
        vec1 = Vec3(0.0, 0.0, 0.0)
        vec2 = Vec3(0.0, 1.0, 0.0)

        result = vec1.distanceTo(vec2)

        self.assertEquals(result, 1.0)

    def testLinearInterpolate(self):
        vec1 = Vec3(0.0, 0.0, 0.0)
        vec2 = Vec3(0.0, 1.0, 0.0)

        result = vec1.linearInterpolate(vec2, 0.5)

        self.assertEquals(result, Vec3(0.0, 0.5))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestVec3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
