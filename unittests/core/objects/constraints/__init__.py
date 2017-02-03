
import unittest

import test_constraint
import test_orientation_constraint
import test_pose_constraint
import test_position_constraint
import test_scale_constraint

loadConstraintSuite = test_constraint.suite()
loadOrientationConstraintSuite = test_orientation_constraint.suite()
loadPoseConstraintSuite = test_pose_constraint.suite()
loadPositionConstraintSuite = test_position_constraint.suite()
loadScaleConstraintSuite = test_scale_constraint.suite()


def suite():
    suites = [
        loadConstraintSuite,
        loadOrientationConstraintSuite,
        loadPoseConstraintSuite,
        loadPositionConstraintSuite,
        loadScaleConstraintSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
