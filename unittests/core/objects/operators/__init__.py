
import unittest

import test_operator
import test_kl_operator
import test_canvas_operator

loadOperatorSuite = test_operator.suite()
loadKLOperatorSuite = test_kl_operator.suite()
loadCanvasOperatorSuite = test_canvas_operator.suite()


def suite():
    suites = [
        loadOperatorSuite,
        loadKLOperatorSuite,
        loadCanvasOperatorSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
