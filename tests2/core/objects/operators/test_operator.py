
import unittest

from kraken.core.objects.operators.operator import Operator


class TestOperator(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetBuildName(self):
        pass
        # getBuildName

    def testSetFlag(self):
        pass
        # setFlag

    def testTestFlag(self):
        pass
        # testFlag

    def testClearFlag(self):
        pass
        # clearFlag

    def testGetFlags(self):
        pass
        # getFlags

    def testGetSources(self):
        pass
        # getSources

    def testResizeInput(self):
        pass
        # resizeInput

    def testSetInput(self):
        pass
        # setInput

    def testGetInput(self):
        pass
        # getInput

    def testGetInputType(self):
        pass
        # getInputType

    def testGetInputNames(self):
        pass
        # getInputNames

    def testResizeOutput(self):
        pass
        # resizeOutput

    def testSetOutput(self):
        pass
        # setOutput

    def testGetOutput(self):
        pass
        # getOutput

    def testGetOutputType(self):
        pass
        # getOutputType

    def testGetOutputNames(self):
        pass
        # getOutputNames

    def testUpdateTargets(self):
        pass
        # updateTargets

    def testEvaluate(self):
        pass
        # evaluate



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
