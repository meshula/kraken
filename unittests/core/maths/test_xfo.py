
import unittest

from kraken.core.maths import Math_degToRad
from kraken.core.maths.vec3 import Vec3
from kraken.core.maths.xfo import Xfo
from kraken.core.maths.quat import Quat
from kraken.core.maths.mat44 import Mat44


class TestXfo(unittest.TestCase):

    def testString(self):
        xfo = Xfo()

        self.assertEquals(str(xfo),
                          "Xfo(Vec3(0.0, 0.0, 0.0), Quat(Vec3(0.0, 0.0, 0.0), 1.0), Vec3(1.0, 1.0, 1.0))")

    def testGetPropertyValues(self):
        xfo = Xfo(tr=Vec3(0.0, 1.0, 0.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))

        self.assertEquals(xfo.tr, Vec3(0.0, 1.0, 0.0))
        self.assertEquals(xfo.ori, Quat())
        self.assertEquals(xfo.sc, Vec3(1.0, 2.0, 1.0))

    def testSetPropertyValues(self):
        xfo = Xfo()

        xfo.tr = Vec3(0.0, 1.0, 0.0)
        xfo.ori = Quat(Vec3(0, 1, 0), 1.0)
        xfo.sc = Vec3(2.0, 1.0, 1.0)

        self.assertEquals(xfo.tr, Vec3(0.0, 1.0, 0.0))
        self.assertEquals(xfo.ori, Quat(Vec3(0, 1, 0), 1.0))
        self.assertEquals(xfo.sc, Vec3(2.0, 1.0, 1.0))

    def testEquals(self):
        xfo1 = Xfo(tr=Vec3(0.0, 1.0, 0.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))
        xfo2 = Xfo(tr=Vec3(0.0, 1.0, 0.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))

        self.assertEqual(xfo1, xfo2)

    def testNotEquals(self):
        xfo1 = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))
        xfo2 = Xfo(tr=Vec3(2.0, 1.0, 0.0), ori=Quat(), sc=Vec3(1.0, 5.0, 1.0))

        self.assertNotEqual(xfo1, xfo2)

    def testMultiply(self):
        xfo1 = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=Quat(), sc=Vec3(1.0, 1.0, 1.0))
        xfo2 = Xfo(tr=Vec3(2.0, 1.0, 0.0), ori=Quat(), sc=Vec3(1.0, 1.0, 1.0))

        xfo = xfo1 * xfo2
        result = Xfo(tr=Vec3(2.0, 2.0, 3.0), ori=Quat(), sc=Vec3(1.0, 1.0, 1.0))

        self.assertEqual(xfo.tr, result.tr)
        self.assertEqual(xfo.ori, result.ori)
        self.assertEqual(xfo.sc, result.sc)

    def testClone(self):
        xfo1 = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))
        xfo2 = xfo1.clone()

        self.assertIsNot(xfo1, xfo2)

        self.assertEqual(xfo1, xfo2)

    def testSet(self):
        xfo = Xfo()

        xfo.set(Vec3(0.0, 1.0, 3.0), Quat(), Vec3(1.0, 2.0, 1.0))
        self.assertEquals(xfo.tr, Vec3(0.0, 1.0, 3.0))
        self.assertEquals(xfo.ori, Quat())
        self.assertEquals(xfo.sc, Vec3(1.0, 2.0, 1.0))

    def testSetIdentity(self):
        xfo = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))

        xfo.setIdentity()

        self.assertEquals(xfo.tr, Vec3())
        self.assertEquals(xfo.ori, Quat())
        self.assertEquals(xfo.sc, Vec3(1, 1, 1))

    def testSetFromMat44(self):
        xfo = Xfo()
        mat44 = Mat44()
        mat44.setTranslation(Vec3(0, 1, 0))
        xfo.setFromMat44(mat44)

        self.assertTrue(mat44.translation, xfo.tr)

    def testToMat44(self):
        xfo = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=Quat(), sc=Vec3(1.0, 2.0, 1.0))

        mat44 = xfo.toMat44()

        self.assertEquals(mat44.row0.t, 0.0)
        self.assertEquals(mat44.row1.t, 1.0)
        self.assertEquals(mat44.row2.t, 3.0)
        self.assertEquals(mat44.row1.y, 2.0)

    def testTransformVector(self):
        ori = Quat().setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(-90))

        xfo = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=ori, sc=Vec3(1.0, 1.0, 1.0))
        vec = Vec3(0, 0, 1)

        result = xfo.transformVector(vec)

        self.assertEquals(round(result.x, 2), -1.0)
        self.assertEquals(result.y, 1.0)
        self.assertEquals(result.z, 3.0)

    def testInverse(self):
        xfo = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=Quat(), sc=Vec3(1.0, 1.0, 1.0))

        result = xfo.inverse()

        self.assertEqual(Vec3(0.0, -1.0, -3.0), result.tr)
        self.assertEqual(Quat(), result.ori)
        self.assertEqual(Vec3(1.0, 1.0, 1.0), result.sc)

    def testInverseTransformVector(self):
        ori = Quat().setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(-90))

        xfo = Xfo(tr=Vec3(0.0, 1.0, 3.0), ori=ori, sc=Vec3(1.0, 1.0, 1.0))
        vec = Vec3(0, 0, 1)

        result = xfo.inverseTransformVector(vec)

        self.assertEquals(round(result.x, 2), -2.0)
        self.assertEquals(round(result.y, 2), -1.0)
        self.assertEquals(result.z, 0.0)

    def testLinearInterpolate(self):
        ori = Quat().setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(90))

        xfo1 = Xfo(tr=Vec3(0.0, 0.0, 0.0), ori=Quat(), sc=Vec3(1.0, 1.0, 1.0))
        xfo2 = Xfo(tr=Vec3(0.0, 5.0, 0.0), ori=ori, sc=Vec3(2.0, 2.0, 2.0))

        result = xfo1.linearInterpolate(xfo2, 0.5)
        resultOri = Quat(Vec3(0.0, 0.382683426142, 0.0), 0.923879563808)

        self.assertEqual(result.tr, Vec3(0, 2.5, 0))
        self.assertEqual(result.ori, resultOri)
        self.assertEqual(result.sc, Vec3(1.5, 1.5, 1.5))

    def testSetFromVectors(self):
        xfo = Xfo()

        xfo.setFromVectors(Vec3(1, 0, 0),
                           Vec3(0, 1, 0),
                           Vec3(0, 0, 1),
                           Vec3(2, 3, 4))

        self.assertEqual(xfo.tr, Vec3(2, 3, 4))
        self.assertEqual(xfo.ori, Quat())
        self.assertEqual(xfo.sc, Vec3(1, 1, 1))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestXfo)


if __name__ == '__main__':
    unittest.main(verbosity=2)
