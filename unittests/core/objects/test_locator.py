
import unittest

from kraken.core.objects.locator import Locator


class TestLocator(unittest.TestCase):

    def testInstance(self):
        locator = Locator('test')

        self.assertIsNotNone(locator)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestLocator)


if __name__ == '__main__':
    unittest.main(verbosity=2)
