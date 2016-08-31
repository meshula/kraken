
import unittest

from kraken.core.objects.operators.canvas_operator import CanvasOperator


class TestCanvasOperator(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCanvasOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
