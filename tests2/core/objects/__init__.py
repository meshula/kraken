
import unittest

from attributes import suite as attributeSuite
from components import suite as componentSuite

loadAttributeSuite = attributeSuite()
loadComponentSuite = componentSuite()


def suite():
    suites = [
        loadAttributeSuite,
        loadComponentSuite]

    return unittest.TestSuite(suites)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
