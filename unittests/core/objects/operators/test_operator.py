
import unittest

from kraken.core.objects.components.component import Component
from kraken.core.objects.operators.operator import Operator


class TestOperator(unittest.TestCase):

    def testGetBuildName(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        buildName = testOp.getBuildName()

        self.assertEqual(buildName, 'testCmp_M_testOp_null')

    def testSetFlag(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.setFlag('TEST_FLAG')

        self.assertTrue('TEST_FLAG' in testOp._flags)

    def testTestFlag(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.setFlag('TEST_FLAG')

        self.assertTrue(testOp.testFlag('TEST_FLAG'))

    def testClearFlag(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.setFlag('TEST_FLAG')
        testOp.clearFlag('TEST_FLAG')

        self.assertFalse(testOp.testFlag('TEST_FLAG'))

    def testGetFlags(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.setFlag('TEST_FLAG')

        self.assertEqual(len(testOp.getFlags()), 1)

    def testGetSources(self):
        # TODO: Helge Implement this test
        pass

    def testResizeInput(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.inputs['testInput'] = []

        self.assertRaises(DeprecationWarning, lambda: testOp.resizeInput('testInput', 2))

    @unittest.expectedFailure
    def testSetInput(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.inputs['testInput'] = None

        # TODO: Create a valid test
        self.assertTrue(testOp.setInput('testInput', 1))

    def testGetInput(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.inputs['testInput'] = None

        self.assertEqual(testOp.getInput('testInput'), None)

    @unittest.expectedFailure
    def testGetInputType(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.inputs['testInput'] = None

        # TODO: Create a valid test
        self.assertRaises(NotImplementedError, lambda: testOp.getInputType('testInput'))

    def testGetInputNames(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.inputs['testInput1'] = None
        testOp.inputs['testInput2'] = None

        self.assertEqual(testOp.getInputNames(), ['testInput2', 'testInput1'])

    def testResizeOutput(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.outputs['testOutput'] = []

        self.assertRaises(DeprecationWarning, lambda: testOp.resizeOutput('testOutput', 2))

    @unittest.expectedFailure
    def testSetOutput(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.outputs['testOutput'] = None

        # TODO: Create a valid test
        self.assertRaises(NotImplementedError, lambda: testOp.setOutput('testOutput', 1))

    @unittest.expectedFailure
    def testGetOutput(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.outputs['testOutput'] = None

        # TODO: Create a valid test
        self.assertEqual(testOp.getOutput('testOutput'), None)

    @unittest.expectedFailure
    def testGetOutputType(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.outputs['testOutput'] = None

        # TODO: Create a valid test
        self.assertRaises(NotImplementedError, lambda: testOp.getOutputType('testOutput'))

    def testGetOutputNames(self):
        comp = Component('testCmp')
        testOp = Operator('testOp', parent=comp)
        testOp.outputs['testOutput1'] = None
        testOp.outputs['testOutput2'] = None

        self.assertEqual(testOp.getOutputNames(), ['testOutput2', 'testOutput1'])

    def testUpdateTargets(self):
        # TODO: Helge Implement this test
        pass

    def testEvaluate(self):
        testOp = Operator('testOp')
        testOp.evaluate()

        self.assertTrue(testOp.testFlag('HAS_EVALUATED'))



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
