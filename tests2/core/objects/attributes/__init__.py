
import unittest

import test_attribute_group
import test_bool_attribute
import test_color_attribute
import test_integer_attribute
import test_scalar_attribute
import test_string_attribute

loadAttributeGroupSuite = test_attribute_group.suite()
loadBoolAttributeSuite = test_bool_attribute.suite()
loadColorAttributeSuite = test_color_attribute.suite()
loadIntegerAttributeSuite = test_integer_attribute.suite()
loadScalarAttributeSuite = test_scalar_attribute.suite()
loadStringAttributeSuite = test_string_attribute.suite()


def suite():
    suites = [
        loadAttributeGroupSuite,
        loadBoolAttributeSuite,
        loadColorAttributeSuite,
        loadIntegerAttributeSuite,
        loadScalarAttributeSuite,
        loadStringAttributeSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
