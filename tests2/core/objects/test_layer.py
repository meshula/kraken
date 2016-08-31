
import unittest

from kraken.core.objects.layer import Layer


class TestLayer(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestLayer)


if __name__ == '__main__':
    unittest.main(verbosity=2)
