
import unittest

from kraken.core.objects.components.component_output import ComponentOutput


class TestComponentOutput(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentOutput)


if __name__ == '__main__':
    unittest.main(verbosity=2)
