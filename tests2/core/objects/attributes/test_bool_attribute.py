
import unittest

from kraken.core.objects.attributes.bool_attribute import BoolAttribute


class TestBoolAttribute(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBoolAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
