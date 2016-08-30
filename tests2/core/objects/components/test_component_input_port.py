
import unittest

from kraken.core.objects.components.component_input_port import ComponentInputPort


class TestComponentInputPort(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentInputPort)


if __name__ == '__main__':
    unittest.main(verbosity=2)
