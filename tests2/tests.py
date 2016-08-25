import unittest

from core import test_core
from core import test_builder
from core.configs import test_config
# from core.io import test_loadSave
from core.maths import test_color

coreSuite = test_core.suite()
builderSuite = test_builder.suite()
configSuite = test_config.suite()
# loadSaveSuite = test_loadSave.suite()
loadColorSuite = test_color.suite()

suites = [
    coreSuite,
    builderSuite,
    configSuite,
    # loadSaveSuite,
    loadColorSuite]

alltests = unittest.TestSuite(suites)

if __name__ == '__main__':
    unittest.main(verbosity=2)