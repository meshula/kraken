
import unittest


from kraken.core.objects.components.component import Component
from kraken.core.objects.components.component_input_port import ComponentInputPort
from kraken.core.objects.components.component_output_port import ComponentOutputPort
from kraken.core.objects.components.component_output import ComponentOutput


class TestComponentOutputPort(unittest.TestCase):

    def testSetDataType(self):
        cmpOutputPort = ComponentOutputPort('testCmpOutputPort', None, 'Scalar')
        testSetDataType = cmpOutputPort.setDataType('Mat44')

        self.assertTrue(testSetDataType)
        self.assertEqual(cmpOutputPort._dataType, 'Mat44')

    def testGetDataType(self):
        cmpOutputPort = ComponentOutputPort('testCmpOutputPort', None, 'Scalar')
        dataType = cmpOutputPort.getDataType()

        self.assertEqual(dataType, 'Scalar')

    def testIsConnected(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        self.assertFalse(cmpOutputPort.isConnected())

        cmpInputPort.setConnection(cmpOutputPort)

        self.assertTrue(cmpOutputPort.isConnected())

    def testGetConnection(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        cmpInputPort.setConnection(cmpOutputPort)

        cmpOutputPortConn = cmpOutputPort.getConnection(0)

        self.assertIs(cmpOutputPortConn, cmpInputPort)

    def testGetNumConnections(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')

        self.assertEqual(cmpOutputPort.getNumConnections(), 0)

        cmpInputPort.setConnection(cmpOutputPort)

        self.assertEqual(cmpOutputPort.getNumConnections(), 1)

    def testCanConnectTo(self):
        testComponent = Component('testComponent')

        # Need to ensure the input and output port objects have different
        # parents to allow them to be connected.
        cmpInputPort = ComponentInputPort('testCmpInputPort', testComponent, 'Scalar')
        cmpOutputPort1 = ComponentOutputPort('testOutput1', None, 'Scalar')
        cmpOutputPort2 = ComponentOutputPort('testOutput2', testComponent, 'Scalar')
        cmpOutputPort3 = ComponentOutputPort('testOutput3', None, 'Mat44')

        testCanConn1 = cmpOutputPort1.canConnectTo(cmpInputPort)
        testCanConn2 = cmpOutputPort2.canConnectTo(cmpInputPort)
        testCanConn3 = cmpOutputPort3.canConnectTo(cmpInputPort)

        self.assertTrue(testCanConn1)
        self.assertFalse(testCanConn2)
        self.assertFalse(testCanConn3)

    def testSetTarget(self):
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        cmpOutput = ComponentOutput('testCmpOutput')
        testSetTgt = cmpOutputPort.setTarget(cmpOutput)

        self.assertTrue(testSetTgt)
        self.assertIs(cmpOutputPort._target, cmpOutput)

    def testGetTarget(self):
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        cmpOutput = ComponentOutput('testCmpOutput')
        cmpOutputPort.setTarget(cmpOutput)

        self.assertIs(cmpOutputPort.getTarget(), cmpOutput)



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentOutputPort)


if __name__ == '__main__':
    unittest.main(verbosity=2)
