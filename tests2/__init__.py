import unittest

from core import test_core
from core import test_builder
from core.configs import test_config
from core.maths import suite as mathSuite

coreSuite = test_core.suite()
builderSuite = test_builder.suite()
configSuite = test_config.suite()
mathSuite = mathSuite()


def suites():
    suites = [
        coreSuite,
        builderSuite,
        configSuite,
        mathSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suites())
