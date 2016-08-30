
import unittest

from kraken.core.objects.components.component_output_port import ComponentOutputPort


class TestComponentOutputPort(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentOutputPort)


if __name__ == '__main__':
    unittest.main(verbosity=2)
