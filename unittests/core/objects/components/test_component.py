
import unittest

from kraken.core.maths.vec2 import Vec2
from kraken.core.objects.layer import Layer
from kraken.core.objects.locator import Locator

from kraken.core.objects.container import Container
from kraken.core.objects.components.component import Component
from kraken_components.biped.arm_component import ArmComponentGuide
from kraken.core.objects.operators.operator import Operator


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
        component = Component('testComponentLocal', location='M')

        component.createOutput('testXfoOutput', 'Xfo')
        component.createOutput('testBooleanOutput', 'Boolean')
        component.createOutput('testFloatOutput', 'Float')
        component.createOutput('testIntegerOutput', 'Integer')
        component.createOutput('testStringOutput', 'String')

        outputs = component.getOutputs()

        self.assertTrue('testXfoOutput' in [x.getName() for x in outputs])
        self.assertTrue('testBooleanOutput' in [x.getName() for x in outputs])
        self.assertTrue('testFloatOutput' in [x.getName() for x in outputs])
        self.assertTrue('testIntegerOutput' in [x.getName() for x in outputs])
        self.assertTrue('testStringOutput' in [x.getName() for x in outputs])

        self.assertRaises(NotImplementedError, lambda: component.createInput('testVecInput', 'Vec3'))

    def testAddOutput(self):
        component = Component('testComponentLocal', location='M')
        component.addOutput('testXfoOutput', 'Xfo')

        outputs = component.getOutputs()

        self.assertTrue('testXfoOutput' in [x.getName() for x in outputs])

    def testGetNumOutputs(self):
        component = Component('testComponentLocal', location='M')

        component.createOutput('testXfoOutput', 'Xfo')
        component.createOutput('testBooleanOutput', 'Boolean')
        numOutputs = component.getNumOutputs()

        self.assertEqual(numOutputs, 2)

    def testGetOutputByIndex(self):
        component = Component('testComponentLocal', location='M')
        outputPort = component.addOutput('testXfoOutput', 'Xfo')
        testGetOutput = component.getOutputByIndex(0)

        self.assertIs(testGetOutput, outputPort)

    def testGetOutputByName(self):
        component = Component('testComponentLocal', location='M')
        component.addOutput('testXfoOutput', 'Xfo')
        testGetInput = component.getOutputByName('testXfoOutput')

        self.assertIsNotNone(testGetInput)

    def testEvalOperators(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)
        component.evalOperators()

        self.assertTrue(testOperator.testFlag('HAS_EVALUATED'))

    def testCheckOperatorIndex(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)

        self.assertTrue(component.checkOperatorIndex(0))
        self.assertRaises(IndexError, lambda: component.checkOperatorIndex(1))

    def testAddOperator(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)

        self.assertTrue(testOperator in component._operators)

    def testRemoveOperatorByIndex(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)

        component.removeOperatorByIndex(0)

        self.assertEqual(len(component._operators), 0)

    def testRemoveOperatorByName(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)

        component.removeOperatorByName('testOperator')

        self.assertEqual(len(component._operators), 0)

    def testGetNumOperators(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)
        testOperator2 = Operator('testOperator2')
        component.addOperator(testOperator2)

        self.assertEqual(component.getNumOperators(), 2)

    def testGetOperatorByIndex(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)
        testOperator2 = Operator('testOperator2')
        component.addOperator(testOperator2)

        self.assertIs(component.getOperatorByIndex(1), testOperator2)

    def testGetOperatorByName(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)
        testOperator2 = Operator('testOperator2')
        component.addOperator(testOperator2)

        self.assertIs(component.getOperatorByName('testOperator2'), testOperator2)

    def testGetOperatorByType(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)

        ops = component.getOperatorByType('Operator')
        self.assertEqual(len(ops), 1)

        ops = component.getOperatorByType('Operator2')
        self.assertEqual(len(ops), 0)

    def testGetOperatorIndex(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)

        opIndex = component.getOperatorIndex(testOperator)
        self.assertEqual(opIndex, 0)

    def testMoveOperatorToIndex(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)
        testOperator2 = Operator('testOperator2')
        component.addOperator(testOperator2)

        testMove = component.moveOperatorToIndex(testOperator2, 0)
        self.assertTrue(testMove)
        self.assertEqual(component.getOperatorIndex(testOperator2), 0)

    def testGetOperators(self):
        component = Component('testComponentLocal', location='M')
        testOperator = Operator('testOperator')
        component.addOperator(testOperator)
        testOperator2 = Operator('testOperator2')
        component.addOperator(testOperator2)

        ops = component.getOperators()

        self.assertEqual(len(ops), 2)
        self.assertTrue(testOperator in ops)
        self.assertTrue(testOperator2 in ops)

    def testSaveData(self):
        component = Component('testComponentLocal', location='M')
        data = component.saveData()

        for key in ['class', 'name', 'location', 'graphPos']:
            self.assertTrue(key in data)

    def testLoadData(self):
        component = Component('testComponentLocal', location='M')
        data = component.saveData()

        data['location'] = 'L'

        component.loadData(data)

        self.assertEqual(component.getLocation(), 'L')

    def testCopyData(self):
        component = Component('testComponentLocal', location='M')
        data = component.copyData()

        for key in ['class', 'name', 'location', 'graphPos']:
            self.assertTrue(key in data)

    def testPasteData(self):
        component = Component('testComponentLocal', location='M')
        data = component.copyData()

        component2 = Component('testComponentLocal2', location='L')
        component2.pasteData(data, setLocation=True)

        component3 = Component('testComponentLocal3', location='L')
        component3.pasteData(data, setLocation=False)

        self.assertEqual(component2.getLocation(), 'M')
        self.assertEqual(component3.getLocation(), 'L')

    def testSaveAllObjectData(self):
        # TODO: Oculus Implement Test
        pass

    def testSaveObjectData(self):
        # TODO: Oculus Implement Test
        pass

    def testLoadAllObjectData(self):
        # TODO: Oculus Implement Test
        pass

    def testLoadObjectData(self):
        # TODO: Oculus Implement Test
        pass

    def testGetRigBuildData(self):
        armCmp = ArmComponentGuide('testComponentLocal', location='L')
        buildData = armCmp.getRigBuildData()

        for key in ['class', 'name', 'location']:
            self.assertTrue(key in buildData)

    def testDetach(self):
        component = Component('testComponentLocal', location='M')

        self.assertRaises(NotImplementedError, lambda: component.detach())

    def testAttach(self):
        container = Container('testContainer')
        component = Component('testComponentLocal', location='M')

        self.assertRaises(NotImplementedError, lambda: component.attach(container))

    def testGetComponentType(self):
        component = Component('testComponentLocal', location='M')
        armCmp = ArmComponentGuide('testComponentLocal', location='L')

        self.assertEqual(component.getComponentType(), 'Base')
        self.assertEqual(armCmp.getComponentType(), 'Guide')


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponent)


if __name__ == '__main__':
    unittest.main(verbosity=2)
