
import unittest

from kraken.core.maths import Math_degToRad
from kraken.core.maths.quat import Quat
from kraken.core.maths.mat33 import Mat33
from kraken.core.maths.vec3 import Vec3
from kraken.core.maths.euler import Euler
from kraken.core.maths.rotation_order import RotationOrder


class TestQuat(unittest.TestCase):

    def testString(self):
        quat = Quat()

        self.assertEquals(str(quat),
            "Quat(Vec3(0.0, 0.0, 0.0), 1.0)")

    def testGetPropertyValues(self):
        quat = Quat()

        self.assertEquals(quat.v, Vec3(0, 0, 0))
        self.assertEquals(quat.w, 1.0)

    def testSetPropertyValues(self):
        quat = Quat()

        quat.v = Vec3(1, 0, 0)
        quat.w = 2.0

        self.assertEquals(quat.v, Vec3(1, 0, 0))
        self.assertEquals(quat.w, 2.0)

    def testEquals(self):
        quat1 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        quat2 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        self.assertEqual(quat1, quat2)

    def testNotEquals(self):
        quat1 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        quat2 = Quat(
            v=Vec3(0, 1, 0),
            w=2.3)

        self.assertEqual(quat1, quat2)

    def testAdd(self):
        quat1 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        quat2 = Quat(
            v=Vec3(0, 1, 0),
            w=2.3)

        quat3 = quat1 + quat2

        self.assertEqual(quat3.v, Vec3(0, 1, 1))
        self.assertEqual(quat3.w, 3.799999952316284)

    def testSubtract(self):
        quat1 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        quat2 = Quat(
            v=Vec3(0, 1, 0),
            w=2.3)

        quat3 = quat1 - quat2

        self.assertEqual(quat3.v, Vec3(0, -1, 1))
        self.assertEqual(quat3.w, -0.7999999523162842)

    def testMultiply(self):
        quat1 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        quat2 = Quat(
            v=Vec3(0, 1, 0),
            w=2.3)

        quat3 = quat1 * quat2

        self.assertEqual(quat3.v, Vec3(-1.0, 1.5, 2.29999995232))
        self.assertEqual(quat3.w, 3.4499998092651367)

    def testClone(self):
        quat1 = Quat(
            v=Vec3(0, 0, 1),
            w=1.5)

        quat2 = quat1.clone()

        self.assertIsNot(quat1, quat2)

        self.assertEqual(quat2.v, Vec3(0, 0, 1))
        self.assertEqual(quat2.w, 1.5)

    def testSet(self):
        quat = Quat()

        quat.set(
            Vec3(0, 0, 1),
            1.5)

        self.assertEqual(quat.v, Vec3(0, 0, 1))
        self.assertEqual(quat.w, 1.5)

    def testSetIdentity(self):
        quat = Quat()

        quat.set(
            Vec3(0, 0, 1),
            1.5)

        quat.setIdentity()

        self.assertEqual(quat.v, Vec3(0, 0, 0))
        self.assertEqual(quat.w, 1.0)

    def testSetFromEuler(self):
        quat = Quat()
        euler = Euler(x=0, y=90, z=0)

        quat.setFromEuler(euler)

        self.assertEqual(quat.v, Vec3(0, 0.850903511047, 0))
        self.assertEqual(quat.w, 0.5253219604492188)

    def testSetFromEulerAnglesWithRotOrder(self):
        quat = Quat()
        vec = Vec3(0.0, 90.0, 0.0)
        ro = RotationOrder(3)

        quat.setFromEulerAnglesWithRotOrder(vec, ro)

        self.assertEqual(quat.v, Vec3(0, 0.850903511047, 0))
        self.assertEqual(quat.w, 0.5253219604492188)

    def testSetFromEulerAngles(self):
        quat = Quat()
        vec = Vec3(0.0, 90.0, 0.0)

        quat.setFromEulerAngles(vec)

        self.assertEqual(quat.v, Vec3(0, 0.850903511047, 0))
        self.assertEqual(quat.w, 0.5253219604492188)

    def testSetFromAxisAndAngle(self):
        quat = Quat()

        quat.setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(90))

        self.assertEqual(quat.v, Vec3(0, 0.707106769085, 0))
        self.assertEqual(quat.w, 0.7071067690849304)

    def testSetFromMat33(self):
        quat = Quat()
        mat = Mat33(
            row0=Vec3(0, 1, 0),
            row1=Vec3(0, 0, 1),
            row2=Vec3(1, 0, 0))

        result = quat.setFromMat33(mat)

        self.assertEqual(result.v, Vec3(0.5, 0.5, 0.5))
        self.assertEqual(result.w, -0.5)

    def testSetFrom2Vectors(self):
        quat = Quat()
        vec1 = Vec3(0, 1, 0)
        vec2 = Vec3(1, 0, 0)

        quat.setFrom2Vectors(vec1, vec2, arbitraryIfAmbiguous=True)

        self.assertEqual(quat.v, Vec3(0.0, 0.0, -0.707106769085))
        self.assertEqual(quat.w, 0.7071067690849304)

    def testSetFromDirectionAndUpvector(self):
        quat = Quat()
        vec1 = Vec3(0.5, 0.5, 0)
        vec2 = Vec3(0, 1, 0)

        quat.setFromDirectionAndUpvector(vec1, vec2)

        self.assertEqual(quat.v, Vec3(-0.270598053932, 0.653281509876, 0.270598053932))
        self.assertEqual(quat.w, 0.6532815098762512)

    def testAlmostEqualWithPrecision(self):
        quat1 = Quat(v=Vec3(0, 1, 0), w=1.0)
        quat2 = Quat(v=Vec3(0, 1.001, 0), w=1.0)

        result = quat1.almostEqualWithPrecision(quat2, precision=0.1)

        self.assertTrue(result)

    def testAlmostEqual(self):
        quat1 = Quat(v=Vec3(0, 1, 0), w=1.0)
        quat2 = Quat(v=Vec3(0, 1.1, 0), w=1.0)

        result = quat1.almostEqual(quat2)

        self.assertTrue(result)

    def testMultiplyScalar(self):
        quat = Quat(v=Vec3(0, 1, 0), w=1.0)

        result = quat.multiplyScalar(2.0)

        self.assertEqual(result.v, Vec3(0, 2.0, 0))
        self.assertEqual(result.w, 2.0)

    def testDivideScalar(self):
        quat = Quat(v=Vec3(0, 1, 0), w=1.0)

        result = quat.divideScalar(2.0)

        self.assertEqual(result.v, Vec3(0, 0.5, 0))
        self.assertEqual(result.w, 0.5)

    def testRotateVector(self):
        quat = Quat()
        quat.setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))

        vec = quat.rotateVector(Vec3(0.0, 1.0, 0.0))

        self.assertEqual(vec, Vec3(0.0, 0.0, 0.999999940395))

    def testDot(self):
        quat1 = Quat()
        quat1.setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))

        quat2 = Quat()

        result = quat1.dot(quat2)

        self.assertEquals(result, 0.7071067690849304)

    def testConjugate(self):
        quat1 = Quat()
        quat1.setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))

        quat2 = quat1.conjugate()

        self.assertEqual(quat2.v, Vec3(-0.707106769085, -0.0, -0.0))
        self.assertEqual(quat2.w, 0.7071067690849304)

    def testLengthSquared(self):
        quat = Quat()
        quat.setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))

        result = quat.lengthSquared()

        self.assertEquals(result, 0.9999999403953552)

    def testLength(self):
        quat = Quat()
        quat.setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))

        result = quat.length()

        self.assertEquals(result, 0.9999999403953552)

    def testUnit(self):
        quat1 = Quat()
        quat1.setFromAxisAndAngle(Vec3(2, 0, 0), Math_degToRad(90))

        quat2 = quat1.unit()

        self.assertEquals(quat2.v, Vec3(0.70710682869, 0.0, 0.0))
        self.assertEquals(quat2.w, 0.7071068286895752)

    def testUnit_safe(self):
        quat1 = Quat()
        quat1.setFromAxisAndAngle(Vec3(2, 0, 0), Math_degToRad(90))

        quat2 = quat1.unit_safe()

        self.assertEquals(quat2.v, Vec3(0.70710682869, 0.0, 0.0))
        self.assertEquals(quat2.w, 0.7071068286895752)

    def testSetUnit(self):
        quat = Quat()
        mat = Mat33(
            row0=Vec3(0, 2, 0),
            row1=Vec3(0, 0, 3),
            row2=Vec3(1, 0, 0))

        quat = quat.setFromMat33(mat)
        result = quat.setUnit()

        self.assertEquals(result, 1.0)

    def testInverse(self):
        quat = Quat()
        mat = Mat33(
            row0=Vec3(0, 2, 0),
            row1=Vec3(0, 0, 3),
            row2=Vec3(1, 0, 0))

        quat = quat.setFromMat33(mat)
        inv = quat.inverse()

        self.assertEquals(inv.v, Vec3(-0.25819888711, -0.774596691132, -0.25819888711))
        self.assertEquals(inv.w, -0.5163977742195129)

    def testAlignWith(self):
        quat1 = Quat()
        quat2 = Quat()

        quat2 = quat2.setFromAxisAndAngle(Vec3(1, 0, 0), Math_degToRad(90))

        result = quat1.alignWith(quat2)

        print result.v
        print result.w

        self.assertEquals(result.v, Vec3(-0.25819888711, -0.774596691132, -0.25819888711))
        self.assertEquals(result.w, -0.5163977742195129)

    def testGetAngle(self):
        quat = Quat()

    def testGetXaxis(self):
        quat = Quat()

    def testGetYaxis(self):
        quat = Quat()

    def testGetZaxis(self):
        quat = Quat()

    def testMirror(self):
        quat = Quat()

    def testToMat33(self):
        quat = Quat()

    def testToEuler(self):
        quat = Quat()

    def testToEulerAnglesWithRotOrder(self):
        quat = Quat()

    def testToEulerAngles(self):
        quat = Quat()

    def testSphericalLinearInterpolate(self):
        quat = Quat()

    def testLinearInterpolate(self):
        quat = Quat()



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestQuat)


if __name__ == '__main__':
    unittest.main(verbosity=2)
