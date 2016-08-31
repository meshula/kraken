
import unittest

from kraken.core.objects.constraints.constraint import Constraint


class TestConstraint(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestConstraint)


if __name__ == '__main__':
    unittest.main(verbosity=2)
