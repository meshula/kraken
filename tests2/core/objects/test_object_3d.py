
import unittest

from kraken.core.objects.object_3d import Object3D


class TestObject3D(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestObject3D)


if __name__ == '__main__':
    unittest.main(verbosity=2)
