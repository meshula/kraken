
import unittest

from kraken.core.objects.components.component_output_port import ComponentOutputPort


class TestComponentOutputPort(unittest.TestCase):

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

    def testGetNumConnections(self):
        pass
        # getNumConnections

    def testCanConnectTo(self):
        pass
        # canConnectTo

    def testSetTarget(self):
        pass
        # setTarget

    def testGetTarget(self):
        pass
        # getTarget



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentOutputPort)


if __name__ == '__main__':
    unittest.main(verbosity=2)
