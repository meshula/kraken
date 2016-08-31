
import unittest

from kraken.core.objects.scene_item import SceneItem


class TestSceneItem(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestSceneItem)


if __name__ == '__main__':
    unittest.main(verbosity=2)
