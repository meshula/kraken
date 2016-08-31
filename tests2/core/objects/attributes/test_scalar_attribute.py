
import unittest

from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute


class TestScalarAttribute(unittest.TestCase):

    def testGetName(self):
        pass

    def getRTVal(self):
        pass
        # getRTVal

    def validateValue(self):
        pass
        # validateValue

    def getDataType(self):
        pass
        # getDataType


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestScalarAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
