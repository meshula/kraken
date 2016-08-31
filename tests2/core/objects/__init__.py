
import unittest

from attributes import suite as attributeSuite
from components import suite as componentSuite
from constraints import suite as constraintSuite
from operators import suite as operatorSuite

loadAttributeSuite = attributeSuite()
loadComponentSuite = componentSuite()
loadConstraintSuite = constraintSuite()
loadOperatorSuite = operatorSuite()


def suite():
    suites = [
        loadAttributeSuite,
        loadComponentSuite,
        loadConstraintSuite,
        loadOperatorSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
