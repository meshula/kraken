
import unittest

from kraken.core.maths.color import Color


class TestColor(unittest.TestCase):

    def testString(self):
        color = Color()

        self.assertEquals(str(color), 'Color(0.0, 0.0, 0.0, 1.0)')

    def testGetPropertyValues(self):
        color = Color()

        self.assertEquals(color.r, 0.0)
        self.assertEquals(color.g, 0.0)
        self.assertEquals(color.b, 0.0)
        self.assertEquals(color.a, 1.0)

    def testSetPropertyValues(self):
        color = Color()

        color.r = 1.0
        color.g = 1.0
        color.b = 1.0
        color.a = 0.5

        self.assertEquals(color.r, 1.0)
        self.assertEquals(color.g, 1.0)
        self.assertEquals(color.b, 1.0)
        self.assertEquals(color.a, 0.5)

    def testEquals(self):
        color1 = Color(r=1.0, g=0.0, b=1.0, a=1.0)
        color2 = Color(r=1.0, g=0.0, b=1.0, a=1.0)

        self.assertEqual(color1, color2)

    def testNotEquals(self):
        color1 = Color(r=1.0, g=0.0, b=1.0, a=1.0)
        color2 = Color(r=1.0, g=0.5, b=1.0, a=1.0)

        self.assertNotEqual(color1, color2)

    def testAdd(self):
        color1 = Color(r=1.0, g=0.0, b=1.0, a=1.0)
        color2 = Color(r=1.0, g=0.5, b=1.0, a=1.0)

        color3 = color1 + color2

        self.assertEqual(color3.r, 2.0)
        self.assertEqual(color3.g, 0.5)
        self.assertEqual(color3.b, 2.0)
        self.assertEqual(color3.a, 2.0)

    def testSubtract(self):
        color1 = Color(r=1.0, g=0.0, b=1.0, a=1.0)
        color2 = Color(r=1.0, g=0.5, b=1.0, a=1.0)

        color3 = color1 - color2

        self.assertEqual(color3.r, 0.0)
        self.assertEqual(color3.g, -0.5)
        self.assertEqual(color3.b, 0.0)
        self.assertEqual(color3.a, 0.0)

    def testMultiply(self):
        color1 = Color(r=1.0, g=0.0, b=1.0, a=1.0)
        color2 = Color(r=1.0, g=0.5, b=1.0, a=1.0)

        color3 = color1 * color2

        self.assertEqual(color3.r, 1.0)
        self.assertEqual(color3.g, 0.0)
        self.assertEqual(color3.b, 1.0)
        self.assertEqual(color3.a, 1.0)

    def testDivide(self):
        color1 = Color(r=2.0, g=0.5, b=3.0, a=1.0)
        color2 = Color(r=1.0, g=0.25, b=1.0, a=2.0)

        color3 = color1 / color2

        self.assertEqual(color3.r, 2.0)
        self.assertEqual(color3.g, 2.0)
        self.assertEqual(color3.b, 3.0)
        self.assertEqual(color3.a, 0.5)

    def testClone(self):
        color1 = Color(r=2.0, g=0.5, b=3.0, a=1.0)
        color2 = color1.clone()

        self.assertIsNot(color1, color2)

        self.assertEqual(color2.r, 2.0)
        self.assertEqual(color2.g, 0.5)
        self.assertEqual(color2.b, 3.0)
        self.assertEqual(color2.a, 1.0)

    def testSet(self):
        color = Color()

        color.set(1.0, 0.75, 0.5, 0.25)

        self.assertEqual(color.r, 1.0)
        self.assertEqual(color.g, 0.75)
        self.assertEqual(color.b, 0.5)
        self.assertEqual(color.a, 0.25)

    def testComponent(self):
        color = Color(r=2.0, g=0.5, b=3.0, a=1.0)

        r = color.component(0)
        g = color.component(1)
        b = color.component(2)
        a = color.component(3)

        self.assertEqual(r, 2.0)
        self.assertEqual(g, 0.5)
        self.assertEqual(b, 3.0)
        self.assertEqual(a, 1.0)

    def testSetComponent(self):
        color = Color()

        color.setComponent(0, 2.0)
        color.setComponent(1, 0.5)
        color.setComponent(2, 3.0)
        color.setComponent(3, 1.0)

        self.assertEqual(color.r, 2.0)
        self.assertEqual(color.g, 0.5)
        self.assertEqual(color.b, 3.0)
        self.assertEqual(color.a, 1.0)

    def testMultiplyScalar(self):
        color1 = Color(r=2.0, g=0.5, b=3.0, a=1.0)

        color2 = color1.multiplyScalar(2.0)

        self.assertEqual(color2.r, 4.0)
        self.assertEqual(color2.g, 1.0)
        self.assertEqual(color2.b, 6.0)
        self.assertEqual(color2.a, 2.0)

    def testDivideScalar(self):
        color1 = Color(r=2.0, g=1.0, b=3.0, a=1.0)

        color2 = color1.divideScalar(2.0)

        self.assertEqual(color2.r, 1.0)
        self.assertEqual(color2.g, 0.5)
        self.assertEqual(color2.b, 1.5)
        self.assertEqual(color2.a, 0.5)

    def testLinearInterpolate(self):
        color1 = Color(r=0.0, g=0.0, b=0.0, a=1.0)
        color2 = Color(r=1.0, g=1.0, b=1.0, a=1.0)

        color3 = color1.linearInterpolate(color2, 0.75)

        self.assertEqual(color3.r, 0.75)
        self.assertEqual(color3.g, 0.75)
        self.assertEqual(color3.b, 0.75)
        self.assertEqual(color3.a, 1.0)

    def testRandom(self):
        color1 = Color.randomColor(0.5)
        color2 = Color.randomColor(0.5)

        self.assertNotEqual(color1, color2)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestColor)


if __name__ == '__main__':
    unittest.main(verbosity=2)
