
import unittest

from kraken.core.builder import Builder
from kraken.core.configs.config import Config
from kraken.core.objects.rig import Rig


class TestBuilder(unittest.TestCase):

    def testBuilderClass(self):
        builder = Builder()

    def testBuild(self):
        builder = Builder()
        bobRig = Rig("testRig")

        self.assertIsNotNone(bobRig)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBuilder)


if __name__ == '__main__':
    unittest.main(verbosity=2)