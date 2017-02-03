
import unittest

from kraken.core.maths.xfo import Xfo
from kraken.core.maths.vec3 import Vec3
from kraken.core.maths.rotation_order import RotationOrder
from kraken.core.objects.object_3d import Object3D
from kraken.core.objects.components.component import Component
from kraken.core.objects.component_group import ComponentGroup
from kraken.core.objects.container import Container


class TestObject3D(unittest.TestCase):

    def testGetPropertyValues(self):
        testObj3D = Object3D('testObj3D')
        testXfo = testObj3D.xfo
        testRO = testObj3D.ro
        testLocalXfo = testObj3D.localXfo
        testGlobalXfo = testObj3D.globalXfo

        self.assertIsNotNone(testXfo)
        self.assertEqual(testXfo, Xfo())
        self.assertIsNotNone(testRO)
        self.assertEqual(testRO, RotationOrder())
        self.assertIsNotNone(testLocalXfo)
        self.assertEqual(testLocalXfo, Xfo())
        self.assertIsNotNone(testGlobalXfo)
        self.assertEqual(testGlobalXfo, Xfo())

    def testSetPropertyValues(self):
        testObj3D = Object3D('testObj3D')
        newXfo = Xfo(tr=Vec3(0, 5, 0))
        testObj3D.xfo = newXfo

        self.assertEqual(testObj3D.xfo, newXfo)

    def testGetBuildName(self):
        testCmp = Component('testComponent', location='M')
        testCmpGrp = ComponentGroup('testCmpGrp', testCmp)
        testCmp.addItem('testCmpGrp', testCmpGrp)
        testObj3D = Object3D('testObj3D', parent=testCmpGrp)
        buildName = testObj3D.getBuildName()

        self.assertEqual(buildName, 'testComponent_M_testObj3D_null')

        testCmp = Component('testComponent', location='M')
        testCmpGrp = ComponentGroup('testCmpGrp', testCmp)
        testCmp.addItem('testCmpGrp', testCmpGrp)
        testObj3D = Object3D('testObj3D', parent=testCmpGrp)
        testObj3D.setFlag('EXPLICIT_NAME')
        buildName = testObj3D.getBuildName()

        self.assertEqual(buildName, 'testObj3D')

    def testSetName(self):
        testObj3D = Object3D('testObj3D')
        setNameCall = testObj3D.setName('myObj')

        self.assertTrue(setNameCall)
        self.assertEqual(testObj3D._name, 'myObj')

    def testGetContainer(self):
        testObj3D = Object3D('testObj3D')
        container = testObj3D.getContainer()

        self.assertIsNone(container)

        testContainer = Container('TestContainer')
        testParent = Object3D('testParent', parent=testContainer)
        testObj3D = Object3D('testObj3D', parent=testParent)
        testContainer.addItem('testObj3D', testObj3D)

        self.assertIs(testObj3D.getContainer(), testContainer)

    def testGetLayer(self):
        pass
        # getLayer

    def testHasChild(self):
        pass
        # hasChild

    def testAddChild(self):
        pass
        # addChild

    def testSetParent(self):
        pass
        # setParent

    def testRemoveChildByIndex(self):
        pass
        # removeChildByIndex

    def testRemoveChildByName(self):
        pass
        # removeChildByName

    def testRemoveChild(self):
        pass
        # removeChild

    def testGetDescendents(self):
        pass
        # getDescendents

    def testGetChildren(self):
        pass
        # getChildren

    def testGetNumChildren(self):
        pass
        # getNumChildren

    def testGetChildByIndex(self):
        pass
        # getChildByIndex

    def testGetChildByName(self):
        pass
        # getChildByName

    def testGetChildByDecoratedName(self):
        pass
        # getChildByDecoratedName

    def testGetChildrenByType(self):
        pass
        # getChildrenByType

    def testSetFlag(self):
        pass
        # setFlag

    def testTestFlag(self):
        pass
        # testFlag

    def testClearFlag(self):
        pass
        # clearFlag

    def testGetFlags(self):
        pass
        # getFlags

    def testAddAttributeGroup(self):
        pass
        # addAttributeGroup

    def testRemoveAttributeGroupByIndex(self):
        pass
        # removeAttributeGroupByIndex

    def testRemoveAttributeGroupByName(self):
        pass
        # removeAttributeGroupByName

    def testGetNumAttributeGroups(self):
        pass
        # getNumAttributeGroups

    def testGetAttributeGroupByIndex(self):
        pass
        # getAttributeGroupByIndex

    def testGetAttributeGroupByName(self):
        pass
        # getAttributeGroupByName

    def testCheckConstraintIndex(self):
        pass
        # checkConstraintIndex

    def testConstrainTo(self):
        pass
        # constrainTo

    def testAddConstraint(self):
        pass
        # addConstraint

    def testRemoveConstraintByIndex(self):
        pass
        # removeConstraintByIndex

    def testRemoveConstraintByName(self):
        pass
        # removeConstraintByName

    def testRemoveAllConstraints(self):
        pass
        # removeAllConstraints

    def testGetNumConstraints(self):
        pass
        # getNumConstraints

    def testGetConstraintByIndex(self):
        pass
        # getConstraintByIndex

    def testGetConstraintByName(self):
        pass
        # getConstraintByName

    def testGetVisibilityAttr(self):
        pass
        # getVisibilityAttr

    def testGetVisibility(self):
        pass
        # getVisibility

    def testSetVisibility(self):
        pass
        # setVisibility

    def testGetShapeVisibilityAttr(self):
        pass
        # getShapeVisibilityAttr

    def testGetShapeVisibility(self):
        pass
        # getShapeVisibility

    def testSetShapeVisibility(self):
        pass
        # setShapeVisibility

    def testSetColor(self):
        pass
        # setColor

    def testGetColor(self):
        pass
        # getColor

    def testLockRotation(self):
        pass
        # lockRotation

    def testLockScale(self):
        pass
        # lockScale

    def testLockTranslation(self):
        pass
        # lockTranslation


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestObject3D)


if __name__ == '__main__':
    unittest.main(verbosity=2)
