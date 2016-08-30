
import unittest

from kraken.core.objects.attributes.integer_attribute import IntegerAttribute


class TestIntegerAttribute(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestIntegerAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
