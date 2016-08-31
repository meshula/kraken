
import unittest

from kraken.core.objects.constraints.pose_constraint import PoseConstraint


class TestPoseConstraint(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPoseConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
