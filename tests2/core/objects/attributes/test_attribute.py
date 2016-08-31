
import unittest

from kraken.core.objects.attributes.attribute import Attribute


class TestAttribute(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
