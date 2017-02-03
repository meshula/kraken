
import unittest

from kraken.core.objects.layer import Layer


class TestLayer(unittest.TestCase):

    def testInstance(self):
        layer = Layer('test')

        self.assertIsNotNone(layer)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestLayer)


if __name__ == '__main__':
    unittest.main(verbosity=2)
