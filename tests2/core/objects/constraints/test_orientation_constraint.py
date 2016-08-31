
import unittest

from kraken.core.objects.constraints.orientation_constraint import OrientationConstraint


class TestOrientationConstraint(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestOrientationConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
