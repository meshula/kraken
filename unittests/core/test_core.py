
import unittest

import kraken.core


class TestCore(unittest.TestCase):

    def testGetVersion(self):
        version = kraken.core.getVersion()
        self.assertIsNotNone(version)
        self.assertEquals(len(version.split('.')), 3)

        if '-' in version:
            self.assertEquals(len(version.split('-')), 2)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCore)


if __name__ == '__main__':
    unittest.main(verbosity=2)
