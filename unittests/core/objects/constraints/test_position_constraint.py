
import unittest

from kraken.core.objects.constraints.position_constraint import PositionConstraint


class TestPositionConstraint(unittest.TestCase):

    def testInstance(self):
        constraint = PositionConstraint('testConstraint')

        self.assertIsNotNone(constraint)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPositionConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
