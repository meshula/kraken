
import unittest

from kraken.core.objects.components.component import Component


class TestComponent(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetNameDecoration(self):
        pass
        # getNameDecoration

    def testGetComponentColor(self):
        pass
        # getComponentColor

    def testSetComponentColor(self):
        pass
        # setComponentColor

    def testGetLocation(self):
        pass
        # getLocation

    def testSetLocation(self):
        pass
        # setLocation

    def testGetGraphPos(self):
        pass
        # getGraphPos

    def testSetGraphPos(self):
        pass
        # setGraphPos

    def testGetLayer(self):
        pass
        # getLayer

    def testGetOrCreateLayer(self):
        pass
        # getOrCreateLayer

    def testAddItem(self):
        pass
        # addItem

    def testGetItems(self):
        pass
        # getItems

    def testAddChild(self):
        pass
        # addChild

    def testGetHierarchyNodes(self):
        pass
        # getHierarchyNodes

    def testGetInputs(self):
        pass
        # getInputs

    def testCheckInputIndex(self):
        pass
        # checkInputIndex

    def testCreateInput(self):
        pass
        # createInput

    def testAddInput(self):
        pass
        # addInput

    def testRemoveInputByIndex(self):
        pass
        # removeInputByIndex

    def testRemoveInputByName(self):
        pass
        # removeInputByName

    def testGetNumInputs(self):
        pass
        # getNumInputs

    def testGetInputByIndex(self):
        pass
        # getInputByIndex

    def testGetInputByName(self):
        pass
        # getInputByName

    def testGetOutputs(self):
        pass
        # getOutputs

    def testCheckOutputIndex(self):
        pass
        # checkOutputIndex

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
