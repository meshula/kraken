
import unittest

from kraken.core.objects.constraints.orientation_constraint import OrientationConstraint


class TestOrientationConstraint(unittest.TestCase):

    def testInstance(self):
        constraint = OrientationConstraint('testConstraint')

        self.assertIsNotNone(constraint)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestOrientationConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
