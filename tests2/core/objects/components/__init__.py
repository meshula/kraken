
import unittest

import test_component
import test_component_input
import test_component_input_port
import test_component_output
import test_component_output_port

loadAttributeGroupSuite = test_component.suite()
loadComponentInputSuite = test_component_input.suite()
loadComponentInputPortSuite = test_component_input_port.suite()
loadComponentOutputSuite = test_component_output.suite()
loadComponentOutputPortSuite = test_component_output_port.suite()


def suite():
    suites = [
        loadAttributeGroupSuite,
        loadComponentInputSuite,
        loadComponentInputPortSuite,
        loadComponentOutputSuite,
        loadComponentOutputPortSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
