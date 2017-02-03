
import unittest

from kraken.core.maths.vec2 import Vec2


class TestVec2(unittest.TestCase):

    def testString(self):
        vec = Vec2()

        self.assertEquals(str(vec),
                          "Vec2(0.0, 0.0)")

    def testGetPropertyValues(self):
        vec = Vec2(0.0, 1.0)

        self.assertEquals(vec.x, 0.0)
        self.assertEquals(vec.y, 1.0)

    def testSetPropertyValues(self):
        vec = Vec2()

        vec.x = 2
        vec.y = 3

        self.assertEquals(vec.x, 2.0)
        self.assertEquals(vec.y, 3.0)

    def testEquals(self):
        vec1 = Vec2(0.0, 1.0)
        vec2 = Vec2(0.0, 1.0)

        self.assertEqual(vec1, vec2)

    def testNotEquals(self):
        vec1 = Vec2(0.0, 1.0)
        vec2 = Vec2(2.0, 1.0)

        self.assertNotEqual(vec1, vec2)

    def testAdd(self):
        vec1 = Vec2(0.0, 1.0)
        vec2 = Vec2(0.0, 1.0)

        vec3 = vec1 + vec2
        result = Vec2(0.0, 2.0)

        self.assertEqual(vec3, result)

    def testSubtract(self):
        vec1 = Vec2(3.0, 1.0)
        vec2 = Vec2(1.0, 0.25)

        vec3 = vec1 - vec2
        result = Vec2(2.0, 0.75)

        self.assertEqual(vec3, result)

    def testMultiply(self):
        vec1 = Vec2(3.0, 1.0)
        vec2 = Vec2(1.0, 0.25)

        vec3 = vec1 * vec2
        result = Vec2(3.0, 0.25)

        self.assertEqual(vec3, result)

    def testDivide(self):
        vec1 = Vec2(3.0, 1.0)
        vec2 = Vec2(1.0, 0.25)

        vec3 = vec1 / vec2
        result = Vec2(3.0, 4.0)

        self.assertEqual(vec3, result)

    def testClone(self):
        vec1 = Vec2(3.0, 1.0)
        vec2 = vec1.clone()

        self.assertIsNot(vec1, vec2)

        self.assertEqual(vec1, vec2)

    def testSet(self):
        vec = Vec2()

        vec.set(0.25, -1.05)
        self.assertEquals(vec.x, 0.25)
        self.assertEquals(round(vec.y, 2), -1.05)

    def testSetNull(self):
        vec = Vec2(1.0, 2.0)

        vec.setNull()

        self.assertEquals(vec, Vec2())

    def testAlmostEqualWithPrecision(self):
        vec1 = Vec2(1.01, 2.0)
        vec2 = Vec2(1.0, 2.0)

        result = vec1.almostEqualWithPrecision(vec2, 0.1)
        self.assertTrue(result)

    def testAlmostEqual(self):
        vec1 = Vec2(1.000001, 2.0)
        vec2 = Vec2(1.0, 2.0)

        self.assertTrue(vec1.almostEqual(vec2))

    def testComponent(self):
        vec = Vec2(1.0, 2.0)

        self.assertEquals(vec.component(0), 1.0)
        self.assertEquals(vec.component(1), 2.0)

    def testSetComponent(self):
        vec = Vec2()

        vec.setComponent(0, 1.0)
        vec.setComponent(1, 2.0)

        self.assertEquals(vec.x, 1.0)
        self.assertEquals(vec.y, 2.0)

    def testMultiplyScalar(self):
        vec = Vec2(1.0, 1.0)

        result = vec.multiplyScalar(3)

        self.assertEquals(result.x, 3.0)
        self.assertEquals(result.y, 3.0)

    def testDivideScalar(self):
        vec = Vec2(1.0, 1.0)

        result = vec.divideScalar(2)

        self.assertEquals(result.x, 0.5)
        self.assertEquals(result.y, 0.5)

    def testNegate(self):
        vec = Vec2(3.0, 4.0)

        result = vec.negate()

        self.assertEquals(result.x, -3.0)
        self.assertEquals(result.y, -4.0)

    def testInverse(self):
        vec = Vec2(3.0, 4.0)

        result = vec.inverse()

        self.assertEquals(result.x, 0.3333333432674408)
        self.assertEquals(result.y, 0.25)

    def testDot(self):
        vec1 = Vec2(0.0, 1.0)
        vec2 = Vec2(1.0, 0.0)

        result = vec1.dot(vec2)

        self.assertEqual(result, 0.0)

    def testCross(self):
        vec1 = Vec2(0.0, 1.0)
        vec2 = Vec2(1.0, 0.0)

        result = vec1.cross(vec2)

        self.assertEqual(result, Vec2(-1.0, -1.0))

    def testLengthSquared(self):
        vec = Vec2(2.0, 2.0)

        result = vec.lengthSquared()

        self.assertEquals(result, 8.0)

    def testLength(self):
        vec = Vec2(1.0, 1.0)

        result = vec.length()

        self.assertEquals(result, 1.4142135381698608)

    def testUnit(self):
        vec = Vec2(1.5, 3.0)

        result = vec.unit()

        self.assertEquals(result, Vec2(0.447213590145, 0.89442718029))

    def testUnit_safe(self):
        vec = Vec2(0.001, 0.001)

        result = vec.unit_safe()
        self.assertEquals(result, Vec2(0.707106769085, 0.707106769085))

    def testSetUnit(self):
        vec = Vec2(0.001, 0.001)

        result = vec.setUnit()

        self.assertEquals(result, 0.0014142136787995696)

    def testNormalize(self):
        vec = Vec2(1.5, 3.0)

        vec.normalize()

        self.assertEquals(vec, Vec2(0.447213590145, 0.89442718029))

    def testClamp(self):
        vec = Vec2(1.5, 3.0)

        result = vec.clamp(Vec2(0.5, 0.5), Vec2(1.75, 1.75))

        self.assertEquals(result, Vec2(1.5, 1.75))

    def testUnitsAngleTo(self):
        vec1 = Vec2(0.0, 1.0)
        vec2 = Vec2(1.0, 0.0)

        result = vec1.unitsAngleTo(vec2)

        self.assertEquals(result, 1.5707963705062866)

    def testAngleTo(self):
        vec1 = Vec2(1.5, 3.0)
        vec2 = Vec2(0.5, 7.0)

        result = vec1.angleTo(vec2)

        self.assertEquals(result, 0.3923399746417999)

    def testDistanceTo(self):
        vec1 = Vec2(0.0, 0.0)
        vec2 = Vec2(0.0, 1.0)

        result = vec1.distanceTo(vec2)

        self.assertEquals(result, 1.0)

    def testLinearInterpolate(self):
        vec1 = Vec2(0.0, 0.0)
        vec2 = Vec2(0.0, 1.0)

        result = vec1.linearInterpolate(vec2, 0.5)

        self.assertEquals(result, Vec2(0.0, 0.5))

    def testDistanceToLine(self):
        vec1 = Vec2(1.0, 3.5)
        line1Vec = Vec2(0.0, 0.0)
        line2Vec = Vec2(2.0, 2.0)

        result = vec1.distanceToLine(line1Vec, line2Vec)

        self.assertEquals(result, 1.7677669525146484)

    def testDistanceToSegment(self):
        vec1 = Vec2(0.0, 3.5)
        line1Vec = Vec2(0.0, 0.0)
        line2Vec = Vec2(2.0, 2.0)

        result = vec1.distanceToSegment(line1Vec, line2Vec)

        self.assertEquals(result, 2.4748737812042236)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestVec2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
