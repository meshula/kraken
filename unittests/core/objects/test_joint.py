
import unittest

from kraken.core.objects.joint import Joint


class TestJoint(unittest.TestCase):

    def testGetRadius(self):
        testJoint = Joint('testJoint')

        self.assertEqual(testJoint.getRadius(), 1.0)

    def testSetRadius(self):
        testJoint = Joint('testJoint')

        self.assertRaises(AssertionError, lambda: testJoint.setRadius(True))
        self.assertTrue(testJoint.setRadius(0.25))
        self.assertEqual(testJoint.getRadius(), 0.25)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestJoint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
