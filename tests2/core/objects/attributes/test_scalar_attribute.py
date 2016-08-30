
import unittest

from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute


class TestScalarAttribute(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestScalarAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
