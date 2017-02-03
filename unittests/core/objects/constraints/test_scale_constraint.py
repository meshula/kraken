
import unittest

from kraken.core.objects.constraints.scale_constraint import ScaleConstraint


class TestScaleConstraint(unittest.TestCase):

    def testInstance(self):
        constraint = ScaleConstraint('testConstraint')

        self.assertIsNotNone(constraint)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestScaleConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
