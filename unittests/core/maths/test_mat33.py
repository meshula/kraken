
import unittest

from kraken.core.maths.mat33 import Mat33
from kraken.core.maths.vec3 import Vec3


class TestMat33(unittest.TestCase):

    def testString(self):
        mat33 = Mat33()

        self.assertEquals(str(mat33), "Mat33(Vec3(1.0, 0.0, 0.0), Vec3(0.0, 1.0, 0.0), Vec3(0.0, 0.0, 1.0))")

    def testGetPropertyValues(self):
        mat33 = Mat33()

        self.assertEquals(mat33.row0, Vec3(1, 0, 0))
        self.assertEquals(mat33.row1, Vec3(0, 1, 0))
        self.assertEquals(mat33.row2, Vec3(0, 0, 1))

    def testSetPropertyValues(self):
        mat33 = Mat33()

        mat33.row0 = Vec3(0, 1, 0)
        mat33.row1 = Vec3(0, 0, 1)
        mat33.row2 = Vec3(1, 0, 0)

        self.assertEquals(mat33.row0, Vec3(0, 1, 0))
        self.assertEquals(mat33.row1, Vec3(0, 0, 1))
        self.assertEquals(mat33.row2, Vec3(1, 0, 0))

    def testEquals(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))
        mat2 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        self.assertEqual(mat1, mat2)

    def testNotEquals(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))
        mat2 = Mat33(row0=Vec3(1, 0, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        self.assertNotEqual(mat1, mat2)

    def testAdd(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))
        mat2 = Mat33(row0=Vec3(1, 0, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat3 = mat1 + mat2

        self.assertEqual(mat3.row0, Vec3(1, 1, 0))
        self.assertEqual(mat3.row1, Vec3(0, 0, 2))
        self.assertEqual(mat3.row2, Vec3(2, 0, 0))

    def testSubtract(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))
        mat2 = Mat33(row0=Vec3(1, 0, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat3 = mat1 - mat2

        self.assertEqual(mat3.row0, Vec3(-1, 1, 0))
        self.assertEqual(mat3.row1, Vec3(0, 0, 0))
        self.assertEqual(mat3.row2, Vec3(0, 0, 0))

    def testMultiply(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))
        mat2 = Mat33(row0=Vec3(1, 0, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat3 = mat1 * mat2

        self.assertEqual(mat3.row0, Vec3(0, 0, 1))
        self.assertEqual(mat3.row1, Vec3(1, 0, 0))
        self.assertEqual(mat3.row2, Vec3(1, 0, 0))

    def testClone(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))
        mat2 = mat1.clone()

        self.assertIsNot(mat1, mat2)

        self.assertEqual(mat2.row0, Vec3(0, 1, 0))
        self.assertEqual(mat2.row1, Vec3(0, 0, 1))
        self.assertEqual(mat2.row2, Vec3(1, 0, 0))

    def testSetRows(self):
        mat33 = Mat33()

        mat33.setRows(Vec3(0, 1, 0), Vec3(0, 0, 1), Vec3(1, 0, 0))

        self.assertEqual(mat33.row0, Vec3(0, 1, 0))
        self.assertEqual(mat33.row1, Vec3(0, 0, 1))
        self.assertEqual(mat33.row2, Vec3(1, 0, 0))

    def testSetColumns(self):
        mat33 = Mat33()

        mat33.setColumns(Vec3(0, 1, 0), Vec3(0, 0, 1), Vec3(1, 0, 0))

        self.assertEqual(mat33.row0, Vec3(0, 0, 1))
        self.assertEqual(mat33.row1, Vec3(1, 0, 0))
        self.assertEqual(mat33.row2, Vec3(0, 1, 0))

    def testSetNull(self):
        mat33 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat33.setNull()

        self.assertEqual(mat33.row0, Vec3(0, 0, 0))
        self.assertEqual(mat33.row1, Vec3(0, 0, 0))
        self.assertEqual(mat33.row2, Vec3(0, 0, 0))

    def testSetIdentity(self):
        mat33 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat33.setIdentity()

        self.assertEqual(mat33.row0, Vec3(1, 0, 0))
        self.assertEqual(mat33.row1, Vec3(0, 1, 0))
        self.assertEqual(mat33.row2, Vec3(0, 0, 1))

    def testSetDiagonal(self):
        mat33 = Mat33()

        mat33.setDiagonal(2.0)

        self.assertEqual(mat33.row0, Vec3(2, 0, 0))
        self.assertEqual(mat33.row1, Vec3(0, 2, 0))
        self.assertEqual(mat33.row2, Vec3(0, 0, 2))

    def testSetDiagonalVec3(self):
        mat33 = Mat33()

        mat33.setDiagonalVec3(Vec3(1, 2, 3))

        self.assertEqual(mat33.row0, Vec3(1, 0, 0))
        self.assertEqual(mat33.row1, Vec3(0, 2, 0))
        self.assertEqual(mat33.row2, Vec3(0, 0, 3))

    def testMultiplyScalar(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat2 = mat1.multiplyScalar(3.0)

        self.assertEqual(mat2.row0, Vec3(0, 3, 0))
        self.assertEqual(mat2.row1, Vec3(0, 0, 3))
        self.assertEqual(mat2.row2, Vec3(3, 0, 0))

    def testMultiplyVector(self):
        mat33 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        vec = mat33.multiplyVector(Vec3(2, 3, 4))

        self.assertEqual(vec, Vec3(3, 4, 2))

    def testDivideScalar(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat2 = mat1.divideScalar(2.0)

        resultMat = Mat33(row0=Vec3(0.0, 0.5, 0.0), row1=Vec3(0.0, 0.0, 0.5), row2=Vec3(0.5, 0.0, 0.0))
        self.assertEqual(mat2, resultMat)

    def testDeterminant(self):
        mat33 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        determinant = mat33.determinant()

        self.assertEqual(determinant, 1.0)

    def testAdjoint(self):
        mat1 = Mat33(row0=Vec3(0, 1, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat2 = mat1.adjoint()
        resultMat = Mat33(row0=Vec3(0.0, 0.0, 1.0), row1=Vec3(1.0, 0.0, 0.0), row2=Vec3(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)

    def testInverse(self):
        mat1 = Mat33(row0=Vec3(0, 2, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat2 = mat1.inverse()
        resultMat = Mat33(row0=Vec3(0.0, 0.0, 1.0), row1=Vec3(0.5, 0.0, 0.0), row2=Vec3(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)

    def testInverse_safe(self):
        mat1 = Mat33(row0=Vec3(0, 2, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat2 = mat1.inverse_safe()
        resultMat = Mat33(row0=Vec3(0.0, 0.0, 1.0), row1=Vec3(0.5, 0.0, 0.0), row2=Vec3(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)

    def testTranspose(self):
        mat1 = Mat33(row0=Vec3(0, 2, 0), row1=Vec3(0, 0, 1), row2=Vec3(1, 0, 0))

        mat2 = mat1.transpose()
        resultMat = Mat33(row0=Vec3(0.0, 0.0, 1.0), row1=Vec3(2.0, 0.0, 0.0), row2=Vec3(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestMat33)


if __name__ == '__main__':
    unittest.main(verbosity=2)
