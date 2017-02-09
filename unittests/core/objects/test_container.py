
import unittest

from kraken.core.objects.locator import Locator
from kraken.core.objects.container import Container


class TestContainer(unittest.TestCase):

    def testAddItem(self):
        testLocator = Locator('testLocator')
        testContainer = Container('TestContainer')
        testAdd = testContainer.addItem('testLocator', testLocator)

        self.assertTrue(testAdd)
        self.assertIn('testLocator', testContainer._items)
        self.assertEqual(testLocator.getComponent(), testContainer)

    def testGetItems(self):
        testLocator = Locator('testLocator')
        testContainer = Container('TestContainer')
        testContainer.addItem('testLocator', testLocator)

        containerItems = testContainer.getItems()

        self.assertTrue(type(containerItems) is dict)
        self.assertIn('testLocator', containerItems)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestContainer)


if __name__ == '__main__':
    unittest.main(verbosity=2)
