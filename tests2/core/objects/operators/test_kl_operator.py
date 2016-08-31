
import unittest

from kraken.core.objects.operators.kl_operator import KLOperator


class TestKLOperator(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetSolverTypeName(self):
        pass
        # getSolverTypeName

    def testGetExtension(self):
        pass
        # getExtension

    def testGetSolverArgs(self):
        pass
        # getSolverArgs

    def testGetInputType(self):
        pass
        # getInputType

    def testGetOutputType(self):
        pass
        # getOutputType

    def testGetDefaultValue(self):
        pass
        # getDefaultValue

    def testGetInput(self):
        pass
        # getInput

    def testGenerateSourceCode(self):
        pass
        # generateSourceCode

    def testEvaluate(self):
        pass
        # evaluate



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestKLOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
