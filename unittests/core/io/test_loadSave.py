import json
import unittest

from kraken.core.maths import *
from kraken.core.io.kraken_saver import KrakenSaver
from kraken.core.io.kraken_loader import KrakenLoader

from kraken_examples.bob_rig import BobRig


class TestLoadSave(unittest.TestCase):
    """TODO: Finish testing and fixing Loader / Saver"""

    @classmethod
    def setUpClass(cls):
        cls._loader = KrakenLoader()
        cls._saver = KrakenSaver()

    def testSaveJSONEncode(self):
        saver = self._saver
        bobRig = BobRig("Bob")

        jsonData = bobRig.jsonEncode(saver)

        self.assertIsNotNone(jsonData)
        self.assertTrue(type(jsonData) is dict)

    def testSaveJSONEncodeDump(self):
        saver = self._saver
        bobRig = BobRig("Bob")

        jsonData = bobRig.jsonEncode(saver)
        jsonDump = json.dumps(jsonData)

        self.assertTrue(type(jsonDump) is str)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestLoadSave)


if __name__ == '__main__':
    unittest.main(verbosity=2)
