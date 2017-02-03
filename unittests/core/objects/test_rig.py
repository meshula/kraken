
import unittest

from kraken.core.objects.rig import Rig


class TestRig(unittest.TestCase):

    def testGetName(self):
        pass

    def testWriteRigDefinitionFile(self):
        pass
        # writeRigDefinitionFile

    def testLoadRigDefinitionFile(self):
        pass
        # loadRigDefinitionFile

    def testLoadRigDefinition(self):
        pass
        # loadRigDefinition

    def testWriteGuideDefinitionFile(self):
        pass
        # writeGuideDefinitionFile

    def testGetData(self):
        pass
        # getData

    def testGetRigBuildData(self):
        pass
        # getRigBuildData


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestRig)


if __name__ == '__main__':
    unittest.main(verbosity=2)
