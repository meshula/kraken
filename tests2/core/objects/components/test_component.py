
import unittest

from kraken.core.objects.components.component import Component


class TestComponent(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponent)


if __name__ == '__main__':
    unittest.main(verbosity=2)
