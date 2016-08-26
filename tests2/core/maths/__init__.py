
import unittest

import test_color
import test_euler

loadColorSuite = test_color.suite()
loadEulerSuite = test_euler.suite()


def suite():
    suites = [
        loadColorSuite,
        loadEulerSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
