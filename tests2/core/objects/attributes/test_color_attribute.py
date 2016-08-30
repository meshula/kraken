
import unittest

from kraken.core.objects.attributes.color_attribute import ColorAttribute


class TestColorAttribute(unittest.TestCase):

    def testGetName(self):
        pass


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestColorAttribute)


if __name__ == '__main__':
    unittest.main(verbosity=2)
