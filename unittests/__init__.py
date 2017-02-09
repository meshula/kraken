import unittest

from core import test_core
from core import test_builder
from core.configs import test_config
from core.maths import suite as mathTestSuite
from core.objects import suite as objectTestSuite

coreSuite = test_core.suite()
builderSuite = test_builder.suite()
configSuite = test_config.suite()
mathSuite = mathTestSuite()
objectSuite = objectTestSuite()


def suites():
    suites = [
        coreSuite,
        builderSuite,
        configSuite,
        mathSuite,
        objectSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suites())
