
import unittest

from kraken.core.objects.object_3d import Object3D


class TestObject3D(unittest.TestCase):

    def testGetName(self):
        pass

    def testGetPropertyValues(self):
        pass

    def testSetPropertyValues(self):
        pass

    def testGetBuildName(self):
        pass
        # getBuildName

    def testSetName(self):
        pass
        # setName

    def testGetContainer(self):
        pass
        # getContainer

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
