
import unittest

import test_color
import test_euler
import test_mat33

loadColorSuite = test_color.suite()
loadEulerSuite = test_euler.suite()
loadMat33Suite = test_mat33.suite()


def suite():
    suites = [
        loadColorSuite,
        loadEulerSuite,
        loadMat33Suite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
