
import unittest

from kraken.core.objects.constraints.scale_constraint import ScaleConstraint


class TestScaleConstraint(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestScaleConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
