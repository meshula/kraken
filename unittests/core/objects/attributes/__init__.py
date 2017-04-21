
import unittest

import test_attribute
import test_bool_attribute
import test_color_attribute
import test_integer_attribute
import test_scalar_attribute
import test_string_attribute
import test_attribute_group

loadAttributeSuite = test_attribute.suite()
loadBoolAttributeSuite = test_bool_attribute.suite()
loadColorAttributeSuite = test_color_attribute.suite()
loadIntegerAttributeSuite = test_integer_attribute.suite()
loadScalarAttributeSuite = test_scalar_attribute.suite()
loadStringAttributeSuite = test_string_attribute.suite()
loadAttributeGroupSuite = test_attribute_group.suite()


def suite():
    suites = [
        loadAttributeSuite,
        loadBoolAttributeSuite,
        loadColorAttributeSuite,
        loadIntegerAttributeSuite,
        loadScalarAttributeSuite,
        loadStringAttributeSuite,
        loadAttributeGroupSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
