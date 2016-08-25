import unittest

from core import test_core
from core import test_builder
from core.configs import test_config

coreSuite = test_core.suite()
builderSuite = test_builder.suite()
configSuite = test_config.suite()

alltests = unittest.TestSuite([coreSuite, builderSuite, configSuite])

if __name__ == '__main__':
    unittest.main(verbosity=2)