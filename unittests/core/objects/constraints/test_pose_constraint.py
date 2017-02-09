
import unittest

from kraken.core.objects.constraints.pose_constraint import PoseConstraint


class TestPoseConstraint(unittest.TestCase):

    def testInstance(self):
        constraint = PoseConstraint('testConstraint')

        self.assertIsNotNone(constraint)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestPoseConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
