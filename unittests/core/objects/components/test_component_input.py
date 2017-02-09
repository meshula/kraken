
import unittest

from kraken.core.objects.components.component_input import ComponentInput


class TestComponentInput(unittest.TestCase):

    def testInstance(self):
        cmpInput = ComponentInput('test')

        self.assertIsNotNone(cmpInput)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestComponentInput)


if __name__ == '__main__':
    unittest.main(verbosity=2)
