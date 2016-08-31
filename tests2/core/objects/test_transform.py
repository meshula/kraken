
import unittest

from kraken.core.objects.transform import Transform


class TestTransform(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestTransform)


if __name__ == '__main__':
    unittest.main(verbosity=2)
