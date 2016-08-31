
import unittest

from kraken.core.objects.curve import Curve


class TestCurve(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCurve)


if __name__ == '__main__':
    unittest.main(verbosity=2)
