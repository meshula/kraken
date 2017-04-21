
import unittest

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.attribute import Attribute


class TestAttribute(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._attributeGroup = AttributeGroup('testAttributeGroup')
        cls._attribute = Attribute('test', True, parent=cls._attributeGroup)

    def getAttributeGroup(self):
        return self._attributeGroup

    def getAttribute(self):
        return self._attribute

    # ======
    # Tests
    # ======
    def testGetName(self):
        attribute = self.getAttribute()
        name = attribute.getName()

        self.assertTrue(type(name) is str)
        self.assertEquals(name, 'test')

    def testGetValue(self):
        attribute = self.getAttribute()
        value = attribute.getValue()

        self.assertIsNotNone(value)
        self.assertEquals(value, True)

    def testSetValue(self):
        attribute = self.getAttribute()
        attribute.setValue(False)

        value = attribute.getValue()

        self.assertIsNotNone(value)
        self.assertEquals(value, False)

        attribute.setValue(True)

    def testSetValueChangeCallback(self):
        attribute = self.getAttribute()

        def testCallback(newValue):
            print newValue

        attribute.setValueChangeCallback(testCallback)

        self.assertIsNotNone(attribute._callback)
        self.assertIs(attribute._callback, testCallback)

    def testGetKeyable(self):
        attribute = self.getAttribute()
        keyable = attribute.getKeyable()

        self.assertTrue(keyable)

    def testSetKeyable(self):
        attribute = self.getAttribute()

        attribute.setKeyable(False)
        self.assertFalse(attribute.getKeyable())

        attribute.setKeyable(True)
        self.assertTrue(attribute.getKeyable())

        self.assertRaises(TypeError, lambda: attribute.setKeyable(2.0))

    def testGetLock(self):
        attribute = self.getAttribute()
        lock = attribute.getLock()

        self.assertFalse(lock)

    def testSetLock(self):
        attribute = self.getAttribute()

        attribute.setLock(False)
        self.assertFalse(attribute.getLock())

        attribute.setLock(True)
        self.assertTrue(attribute.getLock())

        self.assertRaises(TypeError, lambda: attribute.setLock(2.0))

    def testGetAnimatable(self):
        attribute = self.getAttribute()
        animatable = attribute.getAnimatable()

        self.assertTrue(animatable)

    def testSetAnimatable(self):
        attribute = self.getAttribute()

        attribute.setAnimatable(True)
        self.assertTrue(attribute.getAnimatable())

        attribute.setAnimatable(False)
        self.assertFalse(attribute.getAnimatable())

        self.assertRaises(TypeError, lambda: attribute.setAnimatable(2.0))

    def testGetRTVal(self):
        attribute = self.getAttribute()

        self.assertRaises(NotImplementedError, lambda: attribute.getRTVal())

    def testValidateValue(self):
        attribute = self.getAttribute()

        self.assertRaises(NotImplementedError, lambda: attribute.validateValue(3))

    def testIsConnected(self):
        attribute = self.getAttribute()
        connected = attribute.isConnected()

        self.assertFalse(connected)

        attribute2 = Attribute('test', False)
        attribute.connect(attribute2)
        connected = attribute.isConnected()

        self.assertTrue(connected)

        attribute.disconnect()

    def testGetConnection(self):
        attribute = self.getAttribute()
        attribute2 = Attribute('test', False)
        attribute.connect(attribute2)

        connection = attribute.getConnection()

        self.assertIs(connection, attribute2)

        attribute.disconnect()

    def testConnect(self):
        attribute = self.getAttribute()
        attribute2 = Attribute('test', False)
        attribute.connect(attribute2)

        self.assertTrue(attribute.isConnected())
        self.assertIs(attribute.getConnection(), attribute2)

        attribute.disconnect()

    def testDisconnect(self):
        attribute = self.getAttribute()
        attribute2 = Attribute('test', False)
        attribute.connect(attribute2)

        attribute.disconnect()

        self.assertFalse(attribute.isConnected())
        self.assertIsNone(attribute.getConnection())



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
