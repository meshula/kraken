
import unittest

from kraken.core.objects.container import Container


class TestContainer(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestContainer)


if __name__ == '__main__':
    unittest.main(verbosity=2)
