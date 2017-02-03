
import unittest

from kraken.core.maths.euler import Euler
from kraken.core.maths.mat33 import Mat33
from kraken.core.maths.rotation_order import RotationOrder


class TestEuler(unittest.TestCase):

    def testString(self):
        euler = Euler()

        self.assertEquals(str(euler), "Euler(0.0, 0.0, 0.0, RotationOrder(order='4'))")

    def testGetPropertyValues(self):
        euler = Euler()

        self.assertEquals(euler.x, 0.0)
        self.assertEquals(euler.y, 0.0)
        self.assertEquals(euler.z, 0.0)
        self.assertEquals(euler.ro, RotationOrder())

    def testSetPropertyValues(self):
        euler = Euler()

        euler.x = 1.0
        euler.y = 2.0
        euler.z = 3.0
        euler.ro = RotationOrder(3)

        self.assertEquals(euler.x, 1.0)
        self.assertEquals(euler.y, 2.0)
        self.assertEquals(euler.z, 3.0)
        self.assertEquals(euler.ro, RotationOrder(3))

    def testEquals(self):
        euler1 = Euler(x=1.0, y=0.0, z=1.0, ro=RotationOrder(3))
        euler2 = Euler(x=1.0, y=0.0, z=1.0, ro=RotationOrder(3))

        self.assertEqual(euler1, euler2)

    def testNotEquals(self):
        euler1 = Euler(x=1.0, y=0.0, z=1.0, ro=RotationOrder(3))
        euler2 = Euler(x=1.0, y=1.0, z=1.0, ro=RotationOrder(1))

        self.assertNotEqual(euler1, euler2)

    def testClone(self):
        euler1 = Euler(x=2.0, y=0.5, z=3.0, ro=RotationOrder(3))
        euler2 = euler1.clone()

        self.assertIsNot(euler1, euler2)

        self.assertEqual(euler2.x, 2.0)
        self.assertEqual(euler2.y, 0.5)
        self.assertEqual(euler2.z, 3.0)
        self.assertEqual(euler2.ro, RotationOrder(3))

    def testSet(self):
        euler = Euler()

        euler.set(1.0, 0.75, 0.5, RotationOrder(2))

        self.assertEqual(euler.x, 1.0)
        self.assertEqual(euler.y, 0.75)
        self.assertEqual(euler.z, 0.5)
        self.assertEqual(euler.ro, RotationOrder(2))

    def testAlmostEqual(self):
        euler1 = Euler(x=1.0, y=0.0, z=1.0, ro=RotationOrder(3))
        euler2 = Euler(x=1.0, y=0.0, z=1.0, ro=RotationOrder(3))

        self.assertTrue(euler1.almostEqual(euler2, 0.001))

    def testToMat33(self):
        euler = Euler()

        self.assertEqual(euler.toMat33(), Mat33())


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestEuler)


if __name__ == '__main__':
    unittest.main(verbosity=2)
