
import unittest

from kraken.core.objects.components.base_example_component import BaseExampleComponent


class TestBaseExampleComponent(unittest.TestCase):

    def testGetName(self):
        pass

    def testDetach(self):
        pass
        # detach

    def testAttach(self):
        pass
        # attach


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestBaseExampleComponent)


if __name__ == '__main__':
    unittest.main(verbosity=2)
