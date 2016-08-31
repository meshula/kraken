
import unittest

from kraken.core.objects.control import Control


class TestControl(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestControl)


if __name__ == '__main__':
    unittest.main(verbosity=2)
