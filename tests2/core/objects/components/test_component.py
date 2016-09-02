
import unittest

from kraken.core.maths.vec2 import Vec2
from kraken.core.objects.container import Container
from kraken.core.objects.layer import Layer
from kraken.core.objects.locator import Locator

from kraken.core.objects.components.component import Component
from kraken.core.objects.components.component_input_port import ComponentInputPort
from kraken.core.objects.components.component_input import ComponentInput
from kraken.core.objects.components.component_output_port import ComponentOutputPort
from kraken.core.objects.components.component_output import ComponentOutput


class TestComponent(unittest.TestCase):

    # ======
    # Setup
    # ======
    @classmethod
    def setUpClass(cls):
        cls._container = Container('testContainer')
        layer = Layer('testLayer', parent=cls._container)
        cls._container.addItem('testLayer', layer)

        cls._component = Component('testComponent',
                                   parent=cls._container,
                                   location='M')

        cls._component.addInput('testInput', 'Mat44')
        cls._component.addOutput('testOutput', 'Mat44')

    def getComponent(self):
        return self._component

    def getContainer(self):
        return self._container

    # ======
    # Tests
    # ======
    def testGetNameDecoration(self):
        component = self.getComponent()
        nameDec = component.getNameDecoration()

        self.assertEqual(nameDec, ':M')

    def testGetComponentColor(self):
        component = self.getComponent()
        cmpColor = component.getComponentColor()

        self.assertEqual(cmpColor, (154, 205, 50, 255))

    def testSetComponentColor(self):
        component = self.getComponent()
        setColor = component.setComponentColor(0, 155, 0, 255)
        cmpColor = component.getComponentColor()

        self.assertTrue(setColor)
        self.assertEqual(cmpColor, (0, 155, 0, 255))

        component.setComponentColor(154, 205, 50, 255)

    def testGetLocation(self):
        component = self.getComponent()
        location = component.getLocation()

        self.assertEqual(location, 'M')

    def testSetLocation(self):
        component = self.getComponent()
        setLocation = component.setLocation('L')
        location = component.getLocation()

        self.assertTrue(setLocation)
        self.assertEqual(location, 'L')

        setLocation = component.setLocation('M')

    def testGetGraphPos(self):
        component = self.getComponent()
        graphPos = component.getGraphPos()

        self.assertEqual(graphPos.x, 0)
        self.assertEqual(graphPos.y, 0)

    def testSetGraphPos(self):
        component = self.getComponent()

        component.setGraphPos(Vec2(5, 5))

        graphPos = component.getGraphPos()
        self.assertEqual(graphPos.x, 5)
        self.assertEqual(graphPos.y, 5)

        component.setGraphPos(Vec2(0, 0))

    def testGetLayer(self):
        componentLocal = Component('testComponentLocal',
                                   location='M')

        getLayerTest = componentLocal.getLayer('testLayer')
        self.assertIsNone(getLayerTest)

        component = self.getComponent()
        getLayerTest = component.getLayer('testLayer')

        self.assertIsNotNone(getLayerTest)
        self.assertTrue(type(getLayerTest) is Layer)

    def testGetOrCreateLayer(self):
        componentLocal = Component('testComponentLocal',
                                   location='M')

        newLayer = componentLocal.getOrCreateLayer('testCreateLayer')

        self.assertIsNotNone(newLayer)
        self.assertTrue(newLayer.getParent() is None)

        container = self.getContainer()
        component = self.getComponent()
        layer = component.getOrCreateLayer('testLayer')

        self.assertIsNotNone(layer)
        self.assertEqual(layer, container.getChildByName('testLayer'))

    def testAddItem(self):
        component = Component('testComponentLocal',
                              location='M')

        layer = Layer('testLayer')
        testAddItem = component.addItem('testLayer', layer)

        self.assertTrue(testAddItem)
        self.assertTrue(layer in component.getItems().values())

    def testGetItems(self):
        component = Component('testComponentLocal',
                              location='M')

        layer = Layer('testLayer')
        testAddItem = component.addItem('testLayer', layer)
        cmpItems = component.getItems()

        self.assertTrue(testAddItem)
        self.assertTrue(type(cmpItems) is dict)
        self.assertTrue(layer in cmpItems.values())

    def testAddChild(self):
        component = Component('testComponentLocal',
                              location='M')

        testLocator = Locator('testLocator')

        self.assertRaises(NotImplementedError, lambda: component.addChild(testLocator))

    def testGetHierarchyNodes(self):
        component = Component('testComponentLocal', location='M')

        layer = component.getOrCreateLayer('testCreateLayer')
        testLoc = Locator('testLocator', parent=layer)

        self.assertRaises(AssertionError, lambda: component.getHierarchyNodes(Locator))

        hrcNodes = component.getHierarchyNodes('Locator')
        self.assertIsNotNone(hrcNodes)
        self.assertTrue(testLoc in hrcNodes)

    def testGetInputs(self):
        component = self.getComponent()
        inputs = component.getInputs()

        self.assertIsNotNone(inputs)
        self.assertTrue('testInput' in [x.getName() for x in inputs])

    def testCheckInputIndex(self):
        component = self.getComponent()
        testInputIndex = component.checkInputIndex(0)

        self.assertTrue(testInputIndex)
        self.assertRaises(IndexError, lambda: component.checkInputIndex(1))

    def testCreateInput(self):
        component = Component('testComponentLocal', location='M')

        component.createInput('testXfoInput', 'Xfo')
        component.createInput('testBooleanInput', 'Boolean')
        component.createInput('testFloatInput', 'Float')
        component.createInput('testIntegerInput', 'Integer')
        component.createInput('testStringInput', 'String')

        inputs = component.getInputs()

        self.assertTrue('testXfoInput' in [x.getName() for x in inputs])
        self.assertTrue('testBooleanInput' in [x.getName() for x in inputs])
        self.assertTrue('testFloatInput' in [x.getName() for x in inputs])
        self.assertTrue('testIntegerInput' in [x.getName() for x in inputs])
        self.assertTrue('testStringInput' in [x.getName() for x in inputs])

        self.assertRaises(NotImplementedError, lambda: component.createInput('testVecInput', 'Vec3'))

    def testAddInput(self):
        component = Component('testComponentLocal', location='M')
        component.addInput('testXfoInput', 'Xfo')

        inputs = component.getInputs()

        self.assertTrue('testXfoInput' in [x.getName() for x in inputs])

    def testRemoveInputByIndex(self):
        component = Component('testComponentLocal', location='M')
        component.addInput('testXfoInput', 'Xfo')
        component.removeInputByIndex(0)

        inputs = component.getInputs()

        self.assertEqual(len(inputs), 0)

    def testRemoveInputByName(self):
        component = Component('testComponentLocal', location='M')
        component.addInput('testXfoInput', 'Xfo')
        component.removeInputByName('testXfoInput')

        inputs = component.getInputs()

        self.assertEqual(len(inputs), 0)

    def testGetNumInputs(self):
        component = Component('testComponentLocal', location='M')

        component.createInput('testXfoInput', 'Xfo')
        component.createInput('testBooleanInput', 'Boolean')
        numInputs = component.getNumInputs()

        self.assertEqual(numInputs, 2)

    def testGetInputByIndex(self):
        component = Component('testComponentLocal', location='M')
        inputPort = component.addInput('testXfoInput', 'Xfo')
        testGetInput = component.getInputByIndex(0)

        self.assertIs(testGetInput, inputPort)

    def testGetInputByName(self):
        component = Component('testComponentLocal', location='M')
        component.addInput('testXfoInput', 'Xfo')
        testGetInput = component.getInputByName('testXfoInput')

        self.assertIsNotNone(testGetInput)

    def testGetOutputs(self):
        component = Component('testComponentLocal', location='M')
        component.addOutput('testXfoInput', 'Xfo')

        inputs = component.getOutputs()

        self.assertEqual(len(inputs), 1)

    def testCheckOutputIndex(self):
        component = self.getComponent()
        testOutputIndex = component.checkOutputIndex(0)

        self.assertTrue(testOutputIndex)
        self.assertRaises(IndexError, lambda: component.checkOutputIndex(1))

    def testCreateOutput(self):
        pass
        # createOutput

    def testAddOutput(self):
        pass
        # addOutput

    def testGetNumOutputs(self):
        pass
        # getNumOutputs

    def testGetOutputByIndex(self):
        pass
        # getOutputByIndex

    def testGetOutputByName(self):
        pass
        # getOutputByName

    def testEvalOperators(self):
        pass
        # evalOperators

    def testCheckOperatorIndex(self):
        pass
        # checkOperatorIndex

    def testAddOperator(self):
        pass
        # addOperator

    def testRemoveOperatorByIndex(self):
        pass
        # removeOperatorByIndex

    def testRemoveOperatorByName(self):
        pass
        # removeOperatorByName

    def testGetNumOperators(self):
        pass
        # getNumOperators

    def testGetOperatorByIndex(self):
        pass
        # getOperatorByIndex

    def testGetOperatorByName(self):
        pass
        # getOperatorByName

    def testGetOperatorByType(self):
        pass
        # getOperatorByType

    def testGetOperatorIndex(self):
        pass
        # getOperatorIndex

    def testMoveOperatorToIndex(self):
        pass
        # moveOperatorToIndex

    def testGetOperators(self):
        pass
        # getOperators

    def testSaveData(self):
        pass
        # saveData

    def testLoadData(self):
        pass
        # loadData

    def testCopyData(self):
        pass
        # copyData

    def testPasteData(self):
        pass
        # pasteData

    def testSaveAllObjectData(self):
        pass
        # saveAllObjectData

    def testSaveObjectData(self):
        pass
        # saveObjectData

    def testLoadAllObjectData(self):
        pass
        # loadAllObjectData

    def testLoadObjectData(self):
        pass
        # loadObjectData

    def testGetRigBuildData(self):
        pass
        # getRigBuildData

    def testDetach(self):
        pass
        # detach

    def testAttach(self):
        pass
        # attach

    def testGetComponentType(self):
        pass
        # getComponentType



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponent)


if __name__ == '__main__':
    unittest.main(verbosity=2)
