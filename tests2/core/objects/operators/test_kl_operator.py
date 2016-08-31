
import unittest

from kraken.core.objects.operators.kl_operator import KLOperator


class TestKLOperator(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestKLOperator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
