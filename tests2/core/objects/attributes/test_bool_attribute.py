
import unittest

from kraken.core.objects.attributes.bool_attribute import BoolAttribute


class TestBoolAttribute(unittest.TestCase):

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
    return unittest.TestLoader().loadTestsFromTestCase(TestBoolAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
