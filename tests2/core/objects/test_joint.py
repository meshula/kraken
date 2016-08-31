
import unittest

from kraken.core.objects.joint import Joint


class TestJoint(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetRadius(self):
        pass
        # getRadius

    def testSetRadius(self):
        pass
        # setRadius



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestJoint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
