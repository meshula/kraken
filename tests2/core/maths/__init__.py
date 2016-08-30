
import unittest

import test_vec2
import test_vec3
import test_vec4
import test_color
import test_euler
import test_mat33
import test_mat44
import test_quat
import test_rotation_order
import test_xfo

loadVec2Suite = test_vec2.suite()
loadVec3Suite = test_vec3.suite()
loadVec4Suite = test_vec4.suite()
loadColorSuite = test_color.suite()
loadEulerSuite = test_euler.suite()
loadMat33Suite = test_mat33.suite()
loadMat44Suite = test_mat44.suite()
loadQuatSuite = test_quat.suite()
loadRotationOrderSuite = test_rotation_order.suite()
loadXfoSuite = test_xfo.suite()


def suite():
    suites = [
        loadVec2Suite,
        loadVec3Suite,
        loadVec4Suite,
        loadColorSuite,
        loadEulerSuite,
        loadMat33Suite,
        loadMat44Suite,
        loadQuatSuite,
        loadRotationOrderSuite,
        loadXfoSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
