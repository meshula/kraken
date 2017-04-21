
import unittest

from kraken.core.maths import Math_degToRad
from kraken.core.maths.mat44 import Mat44
from kraken.core.maths.mat33 import Mat33
from kraken.core.maths.vec3 import Vec3
from kraken.core.maths.vec4 import Vec4
from kraken.core.maths.quat import Quat


class TestMat44(unittest.TestCase):

    def testString(self):
        mat44 = Mat44()

        self.assertEquals(str(mat44),
            "Mat44(Vec4(1.0, 0.0, 0.0, 0.0), Vec4(0.0, 1.0, 0.0, 0.0), Vec4(0.0, 0.0, 1.0, 0.0), Vec4(0.0, 0.0, 0.0, 1.0))")

    def testGetPropertyValues(self):
        mat44 = Mat44()

        self.assertEquals(mat44.row0, Vec4(1, 0, 0, 0))
        self.assertEquals(mat44.row1, Vec4(0, 1, 0, 0))
        self.assertEquals(mat44.row2, Vec4(0, 0, 1, 0))
        self.assertEquals(mat44.row3, Vec4(0, 0, 0, 1))

    def testSetPropertyValues(self):
        mat44 = Mat44()

        mat44.row0 = Vec4(0, 1, 0, 0)
        mat44.row1 = Vec4(0, 0, 1, 0)
        mat44.row2 = Vec4(1, 0, 0, 0)
        mat44.row3 = Vec4(0, 0, 0, 1)

        self.assertEquals(mat44.row0, Vec4(0, 1, 0, 0))
        self.assertEquals(mat44.row1, Vec4(0, 0, 1, 0))
        self.assertEquals(mat44.row2, Vec4(1, 0, 0, 0))
        self.assertEquals(mat44.row3, Vec4(0, 0, 0, 1))

    def testEquals(self):
        mat1 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat2 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        self.assertEqual(mat1, mat2)

    def testNotEquals(self):
        mat1 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat2 = Mat44(
            row0=Vec4(1, 0, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        self.assertNotEqual(mat1, mat2)

    def testAdd(self):
        mat1 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat2 = Mat44(
            row0=Vec4(1, 0, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat3 = mat1 + mat2

        self.assertEqual(mat3.row0, Vec4(1, 1, 0, 0))
        self.assertEqual(mat3.row1, Vec4(0, 0, 2, 0))
        self.assertEqual(mat3.row2, Vec4(2, 0, 0, 0))
        self.assertEqual(mat3.row3, Vec4(0, 0, 0, 2))

    def testSubtract(self):
        mat1 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 2))

        mat2 = Mat44(
            row0=Vec4(1, 0, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat3 = mat1 - mat2

        self.assertEqual(mat3.row0, Vec4(-1, 1, 0, 0))
        self.assertEqual(mat3.row1, Vec4(0, 0, 0, 0))
        self.assertEqual(mat3.row2, Vec4(0, 0, 0, 0))
        self.assertEqual(mat3.row3, Vec4(0, 0, 0, 1))

    def testMultiply(self):
        mat1 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 3))

        mat2 = Mat44(
            row0=Vec4(1, 0, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat3 = mat1 * mat2

        self.assertEqual(mat3.row0, Vec4(0, 0, 1, 0))
        self.assertEqual(mat3.row1, Vec4(1, 0, 0, 0))
        self.assertEqual(mat3.row2, Vec4(1, 0, 0, 0))
        self.assertEqual(mat3.row3, Vec4(0, 0, 0, 3))

    def testClone(self):
        mat1 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat2 = mat1.clone()

        self.assertIsNot(mat1, mat2)

        self.assertEqual(mat2.row0, Vec4(0, 1, 0, 0))
        self.assertEqual(mat2.row1, Vec4(0, 0, 1, 0))
        self.assertEqual(mat2.row2, Vec4(1, 0, 0, 0))
        self.assertEqual(mat2.row3, Vec4(0, 0, 0, 1))

    def testSetRows(self):
        mat44 = Mat44()

        mat44.setRows(
            Vec4(0, 1, 0, 0),
            Vec4(0, 0, 1, 0),
            Vec4(1, 0, 0, 0),
            Vec4(0, 0, 0, 1))

        self.assertEqual(mat44.row0, Vec4(0, 1, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 0, 1, 0))
        self.assertEqual(mat44.row2, Vec4(1, 0, 0, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 1))

    def testSetColumns(self):
        mat44 = Mat44()

        mat44.setColumns(
            Vec4(0, 1, 0, 0),
            Vec4(0, 0, 1, 0),
            Vec4(1, 0, 0, 0),
            Vec4(0, 0, 0, 1))

        self.assertEqual(mat44.row0, Vec4(0, 0, 1, 0))
        self.assertEqual(mat44.row1, Vec4(1, 0, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 1, 0, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 1))

    def testSetNull(self):
        mat44 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat44.setNull()

        self.assertEqual(mat44.row0, Vec4(0, 0, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 0, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 0, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 0))

    def testSetIdentity(self):
        mat44 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat44.setIdentity()

        self.assertEqual(mat44.row0, Vec4(1, 0, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 1, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 1, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 1))

    def testSetDiagonal(self):
        mat44 = Mat44()

        mat44.setDiagonal(2.0)

        self.assertEqual(mat44.row0, Vec4(2, 0, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 2, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 2, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 2))

    def testSetDiagonalVec3(self):
        mat44 = Mat44()

        mat44.setDiagonalVec3(Vec3(1, 2, 3))

        self.assertEqual(mat44.row0, Vec4(1, 0, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 2, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 3, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 1))

    def testSetDiagonalVec4(self):
        mat44 = Mat44()

        mat44.setDiagonalVec4(Vec4(1, 2, 3, 4))

        self.assertEqual(mat44.row0, Vec4(1, 0, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 2, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 3, 0))
        self.assertEqual(mat44.row3, Vec4(0, 0, 0, 4))

    def testMultiplyScalar(self):
        mat1 = Mat44(row0=Vec4(0, 1, 0, 0), row1=Vec4(0, 0, 1, 0), row2=Vec4(1, 0, 0, 0), row3=Vec4(0, 0, 0, 1))

        mat2 = mat1.multiplyScalar(3.0)

        self.assertEqual(mat2.row0, Vec4(0, 3, 0, 0))
        self.assertEqual(mat2.row1, Vec4(0, 0, 3, 0))
        self.assertEqual(mat2.row2, Vec4(3, 0, 0, 0))
        self.assertEqual(mat2.row3, Vec4(0, 0, 0, 3))

    def testMultiplyVector3(self):
        mat44 = Mat44(row0=Vec4(0, 1, 0, 0), row1=Vec4(0, 0, 1, 0), row2=Vec4(1, 0, 0, 0), row3=Vec4(0, 0, 0, 1))

        vec = mat44.multiplyVector3(Vec3(2, 3, 4))

        self.assertEqual(vec, Vec3(3, 4, 2))

    def testMultiplyVector4(self):
        mat44 = Mat44(
            row0=Vec4(0, 1, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        vec = mat44.multiplyVector4(Vec4(2, 3, 4, 1))

        self.assertEqual(vec, Vec4(3, 4, 2, 1))

    def testDivideScalar(self):
        mat1 = Mat44(row0=Vec4(0, 1, 0, 0), row1=Vec4(0, 0, 1, 0), row2=Vec4(1, 0, 0, 0), row3=Vec4(0, 0, 0, 1))

        mat2 = mat1.divideScalar(2.0)

        resultMat = Mat44(
            row0=Vec4(0.0, 0.5, 0.0, 0.0),
            row1=Vec4(0.0, 0.0, 0.5, 0.0),
            row2=Vec4(0.5, 0.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 0.5))

        self.assertEqual(mat2, resultMat)

    def testDeterminant(self):
        mat44 = Mat44(row0=Vec4(0, 1, 0, 0), row1=Vec4(0, 0, 1, 0), row2=Vec4(1, 0, 0, 0), row3=Vec4(0, 0, 0, 3))

        determinant = mat44.determinant()

        self.assertEqual(determinant, 3.0)

    def testAdjoint(self):
        mat1 = Mat44(row0=Vec4(0, 1, 0, 0), row1=Vec4(0, 0, 1, 0), row2=Vec4(1, 0, 0, 0), row3=Vec4(0, 0, 0, 1))

        mat2 = mat1.adjoint()
        resultMat = Mat44(
            row0=Vec4(0.0, 0.0, 1.0, 0.0),
            row1=Vec4(1.0, 0.0, 0.0, 0.0),
            row2=Vec4(0.0, 1.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat2, resultMat)

    def testInverse(self):
        mat1 = Mat44(
            row0=Vec4(0, 2, 0, 0),
            row1=Vec4(0, 0, 1, 0),
            row2=Vec4(1, 0, 0, 0),
            row3=Vec4(0, 0, 0, 1))

        mat2 = mat1.inverse()
        resultMat = Mat44(
            row0=Vec4(0.0, 0.0, 1.0, 0.0),
            row1=Vec4(0.5, 0.0, 0.0, 0.0),
            row2=Vec4(0.0, 1.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat2, resultMat)

    def testInverse_safe(self):
        mat1 = Mat44(
            row0=Vec4(0.0, 2.0, 0.0, 0.0),
            row1=Vec4(0.0, 0.0, 1.0, 0.0),
            row2=Vec4(1.0, 0.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        mat2 = mat1.inverse_safe()
        resultMat = Mat44(
            row0=Vec4(0.0, 0.0, 1.0, 0.0),
            row1=Vec4(0.5, 0.0, 0.0, 0.0),
            row2=Vec4(0.0, 1.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat2, resultMat)

    def testSetTranslation(self):
        mat = Mat44()
        mat.setTranslation(Vec3(2, 4, 3))

        resultMat = Mat44(
            row0=Vec4(1.0, 0.0, 0.0, 2.0),
            row1=Vec4(0.0, 1.0, 0.0, 4.0),
            row2=Vec4(0.0, 0.0, 1.0, 3.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat.row0, resultMat.row0)
        self.assertEqual(mat.row1, resultMat.row1)
        self.assertEqual(mat.row2, resultMat.row2)
        self.assertEqual(mat.row3, resultMat.row3)

    def testSetRotation(self):
        mat = Mat44()
        quat = Quat()
        quat.setFromAxisAndAngle(Vec3(0, 1, 0), Math_degToRad(90))

        mat.setRotation(quat)

        resultMat = Mat44(
            row0=Vec4(5.96046447754e-08, 0.0, 0.999999940395, 0.0),
            row1=Vec4(0.0, 1.0, 0.0, 0.0),
            row2=Vec4(-0.999999940395, 0.0, 5.96046447754e-08, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat.row0, resultMat.row0)
        self.assertEqual(mat.row1, resultMat.row1)
        self.assertEqual(mat.row2, resultMat.row2)
        self.assertEqual(mat.row3, resultMat.row3)

    def testSetScaling(self):
        mat = Mat44()
        mat.setScaling(Vec3(2, 4, 3))

        resultMat = Mat44(
            row0=Vec4(2.0, 0.0, 0.0, 0.0),
            row1=Vec4(0.0, 4.0, 0.0, 0.0),
            row2=Vec4(0.0, 0.0, 3.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat.row0, resultMat.row0)
        self.assertEqual(mat.row1, resultMat.row1)
        self.assertEqual(mat.row2, resultMat.row2)
        self.assertEqual(mat.row3, resultMat.row3)

    def testSetFromMat33(self):
        mat = Mat44()
        mat33 = Mat33(
            row0=Vec3(0, 1, 0),
            row1=Vec3(1, 0, 0),
            row2=Vec3(0, 0, 1))

        mat.setFromMat33(mat33)

        resultMat = Mat44(
            row0=Vec4(0.0, 1.0, 0.0, 0.0),
            row1=Vec4(1.0, 0.0, 0.0, 0.0),
            row2=Vec4(0.0, 0.0, 1.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat, resultMat)

    def testTranslation(self):
        mat44 = Mat44(
            row0=Vec4(1, 0, 0, 2),
            row1=Vec4(0, 1, 0, 5),
            row2=Vec4(0, 0, 1, 8),
            row3=Vec4(0, 0, 0, 1))

        tr = mat44.translation()

        self.assertEqual(tr, Vec3(2, 5, 8))

    def testTranspose(self):
        mat1 = Mat44(
            row0=Vec4(0.0, 2.0, 0.0, 0.0),
            row1=Vec4(0.0, 0.0, 1.0, 0.0),
            row2=Vec4(1.0, 0.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        mat2 = mat1.transpose()
        resultMat = Mat44(
            row0=Vec4(0.0, 0.0, 1.0, 0.0),
            row1=Vec4(2.0, 0.0, 0.0, 0.0),
            row2=Vec4(0.0, 1.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        self.assertEqual(mat2.row0, resultMat.row0)
        self.assertEqual(mat2.row1, resultMat.row1)
        self.assertEqual(mat2.row2, resultMat.row2)
        self.assertEqual(mat2.row3, resultMat.row3)

    def testUpperLeft(self):
        mat1 = Mat44(
            row0=Vec4(0.0, 2.0, 0.0, 0.0),
            row1=Vec4(0.0, 0.0, 1.0, 0.0),
            row2=Vec4(1.0, 0.0, 0.0, 0.0),
            row3=Vec4(0.0, 0.0, 0.0, 1.0))

        mat2 = mat1.upperLeft()
        resultMat = Mat33(
            row0=Vec3(0.0, 2.0, 0.0),
            row1=Vec3(0.0, 0.0, 1.0),
            row2=Vec3(1.0, 0.0, 0.0))

        self.assertEqual(mat2, resultMat)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestMat44)


if __name__ == '__main__':
    unittest.main(verbosity=2)
