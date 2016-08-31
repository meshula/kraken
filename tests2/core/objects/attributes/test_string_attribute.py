
import unittest

from kraken.core.objects.attributes.string_attribute import StringAttribute


class TestStringAttribute(unittest.TestCase):

    def testGetName(self):
        pass

    def testSetValue(self):
        pass
        # setValue

    def testGetRTVal(self):
        pass
        # getRTVal

    def testGetDataType(self):
        pass
        # getDataType



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestStringAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
