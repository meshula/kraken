
import unittest

from kraken.core.objects.operators.canvas_operator import CanvasOperator


class TestCanvasOperator(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetDefaultValue(self):
        pass
        # getDefaultValue

    def testGetPresetPath(self):
        pass
        # getPresetPath

    def testGetGraphDesc(self):
        pass
        # getGraphDesc

    def testGetInput(self):
        pass
        # getInput

    def testGetInputType(self):
        pass
        # getInputType

    def testGetOutputType(self):
        pass
        # getOutputType

    def testEvaluate(self):
        pass
        # evaluate



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCanvasOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
