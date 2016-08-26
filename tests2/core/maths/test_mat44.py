
import unittest

from kraken.core.maths.mat44 import Mat44
from kraken.core.maths.vec4 import Vec4


class TestMat44(unittest.TestCase):

    def testString(self):
        mat44 = Mat44()

        self.assertEquals(str(mat44), "Mat44(Vec4(1.0, 0.0, 0.0, 0.0), Vec4(0.0, 1.0, 0.0, 0.0), Vec4(0.0, 0.0, 1.0, 0.0), Vec4(0.0, 0.0, 0.0, 1.0))")

    def testGetPropertyValues(self):
        mat44 = Mat44()

        self.assertEquals(mat44.row0, Vec4(1, 0, 0))
        self.assertEquals(mat44.row1, Vec4(0, 1, 0))
        self.assertEquals(mat44.row2, Vec4(0, 0, 1))

    def testSetPropertyValues(self):
        mat44 = Mat44()

        mat44.row0 = Vec4(0, 1, 0)
        mat44.row1 = Vec4(0, 0, 1)
        mat44.row2 = Vec4(1, 0, 0)

        self.assertEquals(mat44.row0, Vec4(0, 1, 0))
        self.assertEquals(mat44.row1, Vec4(0, 0, 1))
        self.assertEquals(mat44.row2, Vec4(1, 0, 0))

    def testEquals(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))
        mat2 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        self.assertEqual(mat1, mat2)

    def testNotEquals(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))
        mat2 = Mat33(row0=Vec4(1, 0, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        self.assertNotEqual(mat1, mat2)

    def testAdd(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))
        mat2 = Mat33(row0=Vec4(1, 0, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat3 = mat1 + mat2

        self.assertEqual(mat3.row0, Vec4(1, 1, 0))
        self.assertEqual(mat3.row1, Vec4(0, 0, 2))
        self.assertEqual(mat3.row2, Vec4(2, 0, 0))

    def testSubtract(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))
        mat2 = Mat33(row0=Vec4(1, 0, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat3 = mat1 - mat2

        self.assertEqual(mat3.row0, Vec4(-1, 1, 0))
        self.assertEqual(mat3.row1, Vec4(0, 0, 0))
        self.assertEqual(mat3.row2, Vec4(0, 0, 0))

    def testMultiply(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))
        mat2 = Mat33(row0=Vec4(1, 0, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat3 = mat1 * mat2

        self.assertEqual(mat3.row0, Vec4(0, 0, 1))
        self.assertEqual(mat3.row1, Vec4(1, 0, 0))
        self.assertEqual(mat3.row2, Vec4(1, 0, 0))

    def testClone(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))
        mat2 = mat1.clone()

        self.assertIsNot(mat1, mat2)

        self.assertEqual(mat2.row0, Vec4(0, 1, 0))
        self.assertEqual(mat2.row1, Vec4(0, 0, 1))
        self.assertEqual(mat2.row2, Vec4(1, 0, 0))

    def testSetRows(self):
        mat44 = Mat44()

        mat44.setRows(Vec4(0, 1, 0), Vec4(0, 0, 1), Vec4(1, 0, 0))

        self.assertEqual(mat44.row0, Vec4(0, 1, 0))
        self.assertEqual(mat44.row1, Vec4(0, 0, 1))
        self.assertEqual(mat44.row2, Vec4(1, 0, 0))

    def testSetColumns(self):
        mat44 = Mat44()

        mat44.setColumns(Vec4(0, 1, 0), Vec4(0, 0, 1), Vec4(1, 0, 0))

        self.assertEqual(mat44.row0, Vec4(0, 0, 1))
        self.assertEqual(mat44.row1, Vec4(1, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 1, 0))

    def testSetNull(self):
        mat44 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat44.setNull()

        self.assertEqual(mat44.row0, Vec4(0, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 0, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 0))

    def testSetIdentity(self):
        mat44 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat44.setIdentity()

        self.assertEqual(mat44.row0, Vec4(1, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 1, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 1))

    def testSetDiagonal(self):
        mat44 = Mat44()

        mat44.setDiagonal(2.0)

        self.assertEqual(mat44.row0, Vec4(2, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 2, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 2))

    def testSetDiagonalVec3(self):
        mat44 = Mat44()

        mat44.setDiagonalVec3(Vec4(1, 2, 3))

        self.assertEqual(mat44.row0, Vec4(1, 0, 0))
        self.assertEqual(mat44.row1, Vec4(0, 2, 0))
        self.assertEqual(mat44.row2, Vec4(0, 0, 3))

    def testMultiplyScalar(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat2 = mat1.multiplyScalar(3.0)

        self.assertEqual(mat2.row0, Vec4(0, 3, 0))
        self.assertEqual(mat2.row1, Vec4(0, 0, 3))
        self.assertEqual(mat2.row2, Vec4(3, 0, 0))

    def testMultiplyVector(self):
        mat44 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        vec = mat44.multiplyVector(Vec4(2, 3, 4))

        self.assertEqual(vec, Vec4(3, 4, 2))

    def testDivideScalar(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat2 = mat1.divideScalar(2.0)

        resultMat = Mat33(row0=Vec4(0.0, 0.5, 0.0), row1=Vec4(0.0, 0.0, 0.5), row2=Vec4(0.5, 0.0, 0.0))
        self.assertEqual(mat2, resultMat)

    def testDeterminant(self):
        mat44 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        determinant = mat44.determinant()

        self.assertEqual(determinant, 1.0)

    def testAdjoint(self):
        mat1 = Mat33(row0=Vec4(0, 1, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat2 = mat1.adjoint()
        resultMat = Mat33(row0=Vec4(0.0, 0.0, 1.0), row1=Vec4(1.0, 0.0, 0.0), row2=Vec4(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)

    def testInverse(self):
        mat1 = Mat33(row0=Vec4(0, 2, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat2 = mat1.inverse()
        resultMat = Mat33(row0=Vec4(0.0, 0.0, 1.0), row1=Vec4(0.5, 0.0, 0.0), row2=Vec4(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)

    def testInverse_safe(self):
        mat1 = Mat33(row0=Vec4(0, 2, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat2 = mat1.inverse_safe()
        resultMat = Mat33(row0=Vec4(0.0, 0.0, 1.0), row1=Vec4(0.5, 0.0, 0.0), row2=Vec4(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)

    def testTranspose(self):
        mat1 = Mat33(row0=Vec4(0, 2, 0), row1=Vec4(0, 0, 1), row2=Vec4(1, 0, 0))

        mat2 = mat1.transpose()
        resultMat = Mat33(row0=Vec4(0.0, 0.0, 1.0), row1=Vec4(2.0, 0.0, 0.0), row2=Vec4(0.0, 1.0, 0.0))

        self.assertEqual(mat2, resultMat)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestMat44)


if __name__ == '__main__':
    unittest.main(verbosity=2)
