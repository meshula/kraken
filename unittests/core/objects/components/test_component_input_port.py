
import unittest


from kraken.core.objects.components.component import Component
from kraken.core.objects.components.component_input import ComponentInput
from kraken.core.objects.components.component_input_port import ComponentInputPort
from kraken.core.objects.components.component_output_port import ComponentOutputPort


class TestComponentInputPort(unittest.TestCase):

    def testSetDataType(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        testSetDataType = cmpInputPort.setDataType('Mat44')

        self.assertTrue(testSetDataType)
        self.assertEqual(cmpInputPort._dataType, 'Mat44')

    def testGetDataType(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        dataType = cmpInputPort.getDataType()

        self.assertEqual(dataType, 'Scalar')

    def testIsConnected(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        self.assertFalse(cmpInputPort.isConnected())

        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        cmpInputPort.setConnection(cmpOutputPort)

        self.assertTrue(cmpInputPort.isConnected())

    def testGetConnection(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        cmpInputPort.setConnection(cmpOutputPort)

        cmpInputPortConn = cmpInputPort.getConnection()

        self.assertEqual(cmpInputPortConn, cmpOutputPort)

    def testSetConnection(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpOutputPort1 = ComponentOutputPort('testOutput1', None, 'Mat44')

        self.assertRaises(TypeError, lambda: cmpInputPort.setConnection(cmpOutputPort1))

        cmpOutputPort2 = ComponentOutputPort('testOutput2', None, 'Scalar')
        testSetConn = cmpInputPort.setConnection(cmpOutputPort2)

        self.assertTrue(testSetConn)
        self.assertRaises(ValueError, lambda: cmpInputPort.setConnection(cmpOutputPort2))

    def testRemoveConnection(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpOutputPort = ComponentOutputPort('testOutput', None, 'Scalar')
        testSetConn = cmpInputPort.setConnection(cmpOutputPort)

        self.assertTrue(testSetConn)

        testRemConn = cmpInputPort.removeConnection()
        self.assertTrue(testRemConn)

    def testCanConnectTo(self):
        testComponent = Component('testComponent')

        # Need to ensure the input and output port objects have different
        # parents to allow them to be connected.
        cmpInputPort = ComponentInputPort('testCmpInputPort', testComponent, 'Scalar')
        cmpOutputPort1 = ComponentOutputPort('testOutput1', None, 'Scalar')
        cmpOutputPort2 = ComponentOutputPort('testOutput2', testComponent, 'Scalar')
        cmpOutputPort3 = ComponentOutputPort('testOutput3', None, 'Mat44')
        testCanConn1 = cmpInputPort.canConnectTo(cmpOutputPort1)
        testCanConn2 = cmpInputPort.canConnectTo(cmpOutputPort2)
        testCanConn3 = cmpInputPort.canConnectTo(cmpOutputPort3)

        self.assertTrue(testCanConn1)
        self.assertFalse(testCanConn2)
        self.assertFalse(testCanConn3)

    def testSetTarget(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpInput = ComponentInput('testCmpInput')
        testSetTgt = cmpInputPort.setTarget(cmpInput)

        self.assertTrue(testSetTgt)
        self.assertEqual(cmpInputPort._target, cmpInput)

    def testGetTarget(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpInput = ComponentInput('testCmpInput')
        cmpInputPort.setTarget(cmpInput)

        self.assertEqual(cmpInputPort.getTarget(), cmpInput)

    def testGetIndex(self):
        cmpInputPort = ComponentInputPort('testCmpInputPort', None, 'Scalar')
        cmpInput = ComponentInput('testCmpInput')
        cmpInputPort.setTarget(cmpInput)
        index = cmpInputPort.getIndex()

        self.assertEqual(index, 0)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentInputPort)


if __name__ == '__main__':
    unittest.main(verbosity=2)
