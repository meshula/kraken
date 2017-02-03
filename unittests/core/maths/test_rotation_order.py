
import unittest

from kraken.core.maths.rotation_order import RotationOrder


class TestRotationOrder(unittest.TestCase):

    def testString(self):
        rotationOrder = RotationOrder()

        self.assertEquals(str(rotationOrder),
            "RotationOrder(order='4')")

    def testGetPropertyValues(self):
        rotationOrder = RotationOrder(2)

        self.assertEquals(rotationOrder.order, 2)

    def testSetPropertyValues(self):
        rotationOrder = RotationOrder()

        rotationOrder.order = 2

        self.assertEquals(rotationOrder.order, 2.0)

    def testEquals(self):
        rotationOrder1 = RotationOrder(1)
        rotationOrder2 = RotationOrder(1)

        self.assertEqual(rotationOrder1, rotationOrder2)

    def testNotEquals(self):
        rotationOrder1 = RotationOrder(1)
        rotationOrder2 = RotationOrder(2)

        self.assertNotEqual(rotationOrder1, rotationOrder2)

    def testClone(self):
        rotationOrder1 = RotationOrder(1)
        rotationOrder2 = rotationOrder1.clone()

        self.assertIsNot(rotationOrder1, rotationOrder2)

        self.assertEqual(rotationOrder1, rotationOrder2)

    def testSet(self):
        rotationOrder = RotationOrder()

        # Test setting from lowercase strings
        rotationOrder.set('xyz')
        self.assertEquals(rotationOrder.order, 4)

        rotationOrder.set('yzx')
        self.assertEquals(rotationOrder.order, 3)

        rotationOrder.set('zxy')
        self.assertEquals(rotationOrder.order, 5)

        rotationOrder.set('xzy')
        self.assertEquals(rotationOrder.order, 1)

        rotationOrder.set('zyx')
        self.assertEquals(rotationOrder.order, 0)

        rotationOrder.set('yxz')
        self.assertEquals(rotationOrder.order, 2)

        # Test setting from lowercase strings
        rotationOrder.set('XYZ')
        self.assertEquals(rotationOrder.order, 4)

        rotationOrder.set('YZX')
        self.assertEquals(rotationOrder.order, 3)

        rotationOrder.set('ZXY')
        self.assertEquals(rotationOrder.order, 5)

        rotationOrder.set('XZY')
        self.assertEquals(rotationOrder.order, 1)

        rotationOrder.set('ZYX')
        self.assertEquals(rotationOrder.order, 0)

        rotationOrder.set('YXZ')
        self.assertEquals(rotationOrder.order, 2)

        # Test setting from integers
        rotationOrder.set(0)
        self.assertEquals(rotationOrder.order, 0)

        rotationOrder.set(1)
        self.assertEquals(rotationOrder.order, 1)

        rotationOrder.set(2)
        self.assertEquals(rotationOrder.order, 2)

        rotationOrder.set(3)
        self.assertEquals(rotationOrder.order, 3)

        rotationOrder.set(4)
        self.assertEquals(rotationOrder.order, 4)

        rotationOrder.set(5)
        self.assertEquals(rotationOrder.order, 5)

        # Test out of range
        rotationOrder.set(6)
        self.assertEquals(rotationOrder.order, 4)

    def testIsXYZ(self):
        rotationOrder = RotationOrder()

        self.assertTrue(rotationOrder.isXYZ())

    def testIsYZX(self):
        rotationOrder = RotationOrder(3)

        self.assertTrue(rotationOrder.isYZX())

    def testIsZXY(self):
        rotationOrder = RotationOrder(5)

        self.assertTrue(rotationOrder.isZXY())

    def testIsXZY(self):
        rotationOrder = RotationOrder(1)

        self.assertTrue(rotationOrder.isXZY())

    def testIsZYX(self):
        rotationOrder = RotationOrder(0)

        self.assertTrue(rotationOrder.isZYX())

    def testIsYXZ(self):
        rotationOrder = RotationOrder(2)

        self.assertTrue(rotationOrder.isYXZ())

    def testIsReversed(self):
        rotationOrder = RotationOrder()
        rotationOrder.set('XZY')
        self.assertTrue(rotationOrder.isReversed())

        rotationOrder.set('ZYX')
        self.assertTrue(rotationOrder.isReversed())

        rotationOrder.set('YXZ')
        self.assertTrue(rotationOrder.isReversed())

        # False
        rotationOrder.set('YZX')
        self.assertFalse(rotationOrder.isReversed())

        rotationOrder.set('XYZ')
        self.assertFalse(rotationOrder.isReversed())

        rotationOrder.set('ZXY')
        self.assertFalse(rotationOrder.isReversed())

    def testSetXYZ(self):
        rotationOrder = RotationOrder()
        rotationOrder.setXYZ()

        self.assertEquals(rotationOrder.order, 4)

    def testSetYZX(self):
        rotationOrder = RotationOrder()
        rotationOrder.setYZX()

        self.assertEquals(rotationOrder.order, 3)

    def testSetZXY(self):
        rotationOrder = RotationOrder()
        rotationOrder.setZXY()

        self.assertEquals(rotationOrder.order, 5)

    def testSetXZY(self):
        rotationOrder = RotationOrder()
        rotationOrder.setXZY()

        self.assertEquals(rotationOrder.order, 1)

    def testSetZYX(self):
        rotationOrder = RotationOrder()
        rotationOrder.setZYX()

        self.assertEquals(rotationOrder.order, 0)

    def testSetYXZ(self):
        rotationOrder = RotationOrder()
        rotationOrder.setYXZ()

        self.assertEquals(rotationOrder.order, 2)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestRotationOrder)


if __name__ == '__main__':
    unittest.main(verbosity=2)
