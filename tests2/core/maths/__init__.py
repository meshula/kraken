
import unittest

import test_color
import test_euler
import test_mat33
import test_mat44
import test_quat
import test_rotation_order

loadColorSuite = test_color.suite()
loadEulerSuite = test_euler.suite()
loadMat33Suite = test_mat33.suite()
loadMat44Suite = test_mat44.suite()
loadQuatSuite = test_quat.suite()
loadRotationOrderSuite = test_rotation_order.suite()


def suite():
    suites = [
        loadColorSuite,
        loadEulerSuite,
        loadMat33Suite,
        loadMat44Suite,
        loadQuatSuite,
        loadRotationOrderSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
