
import unittest

from kraken.core.objects.locator import Locator


class TestLocator(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestLocator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
