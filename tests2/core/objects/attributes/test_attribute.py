
import unittest

from kraken.core.objects.attributes.attribute import Attribute


class TestAttribute(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetValue(self):
        pass
        # getValue

    def testSetValue(self):
        pass
        # setValue

    def testSetValueChangeCallback(self):
        pass
        # setValueChangeCallback

    def testGetKeyable(self):
        pass
        # getKeyable

    def testGetLock(self):
        pass
        # getLock

    def testSetLock(self):
        pass
        # setLock

    def testSetAnimatable(self):
        pass
        # setAnimatable

    def testGetAnimatable(self):
        pass
        # getAnimatable

    def testGetRTVal(self):
        pass
        # getRTVal

    def testValidateValue(self):
        pass
        # validateValue

    def testIsConnected(self):
        pass
        # isConnected

    def testGetConnection(self):
        pass
        # getConnection

    def testConnect(self):
        pass
        # connect

    def testDisconnect(self):
        pass
        # disconnect



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
