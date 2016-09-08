
import unittest

from kraken.core.objects.operators.operator import Operator


class TestOperator(unittest.TestCase):

    def testGetBuildName(self):
        testOp = Operator('testOp')
        buildName = testOp.getBuildName()

        self.assertEqual(buildName, 'testOpnull')

    def testSetFlag(self):
        testOp = Operator('testOp')
        testOp.setFlag('TEST_FLAG')

        self.assertTrue('TEST_FLAG' in testOp._flags)

    def testTestFlag(self):
        testOp = Operator('testOp')
        testOp.setFlag('TEST_FLAG')

        self.assertTrue(testOp.testFlag('TEST_FLAG'))

    def testClearFlag(self):
        testOp = Operator('testOp')
        testOp.setFlag('TEST_FLAG')
        testOp.clearFlag('TEST_FLAG')

        self.assertFalse(testOp.testFlag('TEST_FLAG'))

    def testGetFlags(self):
        testOp = Operator('testOp')
        testOp.setFlag('TEST_FLAG')

        self.assertEqual(len(testOp.getFlags()), 1)

    def testGetSources(self):
        # TODO: Helge Implement this test
        pass

    def testResizeInput(self):
        testOp = Operator('testOp')
        testOp.inputs['testInput'] = []

        self.assertRaises(DeprecationWarning, lambda: testOp.resizeInput('testInput', 2))

    def testSetInput(self):
        testOp = Operator('testOp')
        testOp.inputs['testInput'] = None

        self.assertRaises(NotImplementedError, lambda: testOp.setInput('testInput', 1))

    def testGetInput(self):
        testOp = Operator('testOp')
        testOp.inputs['testInput'] = None

        self.assertEqual(testOp.getInput('testInput'), None)

    def testGetInputType(self):
        testOp = Operator('testOp')
        testOp.inputs['testInput'] = None

        self.assertRaises(NotImplementedError, lambda: testOp.getInputType('testInput'))

    def testGetInputNames(self):
        testOp = Operator('testOp')
        testOp.inputs['testInput1'] = None
        testOp.inputs['testInput2'] = None

        self.assertEqual(testOp.getInputNames(), ['testInput2', 'testInput1'])

    def testResizeOutput(self):
        testOp = Operator('testOp')
        testOp.outputs['testOutput'] = []

        self.assertRaises(DeprecationWarning, lambda: testOp.resizeOutput('testOutput', 2))

    def testSetOutput(self):
        testOp = Operator('testOp')
        testOp.outputs['testOutput'] = None

        self.assertRaises(NotImplementedError, lambda: testOp.setOutput('testOutput', 1))

    def testGetOutput(self):
        testOp = Operator('testOp')
        testOp.outputs['testOutput'] = None

        self.assertEqual(testOp.getOutput('testOutput'), None)

    def testGetOutputType(self):
        testOp = Operator('testOp')
        testOp.outputs['testOutput'] = None

        self.assertRaises(NotImplementedError, lambda: testOp.getOutputType('testOutput'))

    def testGetOutputNames(self):
        testOp = Operator('testOp')
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
