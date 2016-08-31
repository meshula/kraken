
import unittest

from kraken.core.objects.rig import Rig


class TestRig(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestRig)


if __name__ == '__main__':
    unittest.main(verbosity=2)
