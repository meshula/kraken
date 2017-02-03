
import unittest

from kraken.core.objects.ctrlSpace import CtrlSpace


class TestCtrlSpace(unittest.TestCase):

    def testInstance(self):
        ctrlSpace = CtrlSpace('test')

        self.assertIsNotNone(ctrlSpace)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestCtrlSpace)


if __name__ == '__main__':
    unittest.main(verbosity=2)
