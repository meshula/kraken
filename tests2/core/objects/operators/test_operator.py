
import unittest

from kraken.core.objects.operators.operator import Operator


class TestOperator(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
