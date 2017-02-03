
import unittest

from kraken.core.objects.scene_item import SceneItem


class TestSceneItem(unittest.TestCase):

    def testGetId(self):
        pass
        # getId

    def testGetTypeName(self):
        pass
        # getTypeName

    def testGetTypeHierarchyNames(self):
        pass
        # getTypeHierarchyNames

    def testIsTypeOf(self):
        pass
        # isTypeOf

    def testIsOfAnyType(self):
        pass
        # isOfAnyType

    def testGetName(self):
        pass
        # getName

    def testSetName(self):
        pass
        # setName

    def testGetPath(self):
        pass
        # getPath

    def testGetNameDecoration(self):
        pass
        # getNameDecoration

    def testGetDecoratedName(self):
        pass
        # getDecoratedName

    def testGetDecoratedPath(self):
        pass
        # getDecoratedPath

    def testGetParent(self):
        pass
        # getParent

    def testSetParent(self):
        pass
        # setParent

    def testGetSources(self):
        pass
        # getSources

    def testGetCurrentSource(self):
        pass
        # getCurrentSource

    def testAddSource(self):
        pass
        # addSource

    def testRemoveSource(self):
        pass
        # removeSource

    def testSetSource(self):
        pass
        # setSource

    def testGetComponent(self):
        pass
        # getComponent

    def testSetComponent(self):
        pass
        # setComponent

    def testGetMetaData(self):
        pass
        # getMetaData

    def testGetMetaDataItem(self):
        pass
        # getMetaDataItem

    def testSetMetaDataItem(self):
        pass
        # setMetaDataItem



def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSceneItem)


if __name__ == '__main__':
    unittest.main(verbosity=2)
