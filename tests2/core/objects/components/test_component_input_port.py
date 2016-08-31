
import unittest

from kraken.core.objects.components.component_input_port import ComponentInputPort


class TestComponentInputPort(unittest.TestCase):

    def testGetName(self):
        pass

    def testSetDataType(self):
        pass
        # setDataType

    def testGetDataType(self):
        pass
        # getDataType

    def testIsConnected(self):
        pass
        # isConnected

    def testGetConnection(self):
        pass
        # getConnection

    def testSetConnection(self):
        pass
        # setConnection

    def testRemoveConnection(self):
        pass
        # removeConnection

    def testCanConnectTo(self):
        pass
        # canConnectTo

    def testSetTarget(self):
        pass
        # setTarget

    def testGetTarget(self):
        pass
        # getTarget

    def testGetIndex(self):
        pass
        # getIndex



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentInputPort)


if __name__ == '__main__':
    unittest.main(verbosity=2)
