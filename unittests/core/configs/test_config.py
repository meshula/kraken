
import unittest

from kraken.core.configs.config import Config


class TestConfig(unittest.TestCase):

    def testGetModulePath(self):
        config = Config.getInstance()
        modulePath = config.getModulePath()

        self.assertIsNotNone(modulePath)
        self.assertTrue(type(modulePath) is str)
        self.assertEquals(modulePath, "kraken.core.configs.config.Config")

        config.clearInstance()

    def testInitObjectSettings(self):
        config = Config.getInstance()
        settings = config.initObjectSettings()

        self.assertIsNotNone(settings)
        self.assertTrue(type(settings) is dict)
        self.assertTrue(type(settings) is dict)

        config.clearInstance()

    def testGetObjectSettings(self):
        config = Config.getInstance()
        settings = config.getObjectSettings()

        self.assertIsNotNone(settings)
        self.assertTrue(type(settings) is dict)
        self.assertTrue(settings['joint']['size'] is not None)

        config.clearInstance()

    def testInitColors(self):
        config = Config.getInstance()
        colors = config.initColors()

        self.assertIsNotNone(colors)
        self.assertTrue(type(colors) is dict)
        self.assertEquals(len(colors), 148)

        config.clearInstance()

    def testGetColors(self):
        config = Config.getInstance()
        colors = config.getColors()

        self.assertIsNotNone(colors)
        self.assertTrue(type(colors) is dict)
        self.assertEquals(len(colors), 148)

        config.clearInstance()

    def testInitColorMap(self):
        config = Config.getInstance()
        colorMap = config.initColorMap()

        self.assertIsNotNone(colorMap)
        self.assertTrue(type(colorMap) is dict)
        self.assertTrue('Default' in colorMap)
        self.assertTrue('Control' in colorMap)
        self.assertEquals(
            len(set(['default', 'L', 'M', 'R'] + colorMap['Control'].keys())), 4)

        config.clearInstance()

    def testGetColorMap(self):
        config = Config.getInstance()
        colorMap = config.getColorMap()

        self.assertIsNotNone(colorMap)
        self.assertTrue(type(colorMap) is dict)
        self.assertTrue('Default' in colorMap)
        self.assertTrue('Control' in colorMap)
        self.assertEquals(
            len(set(['default', 'L', 'M', 'R'] + colorMap['Control'].keys())), 4)

        config.clearInstance()

    def testInitNameTemplate(self):
        config = Config.getInstance()
        nameTemplate = config.initNameTemplate()
        requiredKeys = ['locations', 'mirrorMap', 'separator', 'types', 'formats']

        self.assertIsNotNone(nameTemplate)
        self.assertTrue(type(nameTemplate) is dict)
        self.assertEquals(
            len(set(requiredKeys + nameTemplate.keys())), 5)

        config.clearInstance()

    def testGetNameTemplate(self):
        config = Config.getInstance()
        nameTemplate = config.getNameTemplate()
        requiredKeys = ['locations', 'mirrorMap', 'separator', 'types', 'formats']

        self.assertIsNotNone(nameTemplate)
        self.assertTrue(type(nameTemplate) is dict)
        self.assertEquals(
            len(set(requiredKeys + nameTemplate.keys())), 5)

        config.clearInstance()

    def testInitControlShapes(self):
        config = Config.getInstance()
        controlShapes = config.initControlShapes()

        self.assertIsNotNone(controlShapes)
        self.assertTrue(type(controlShapes) is dict)

        config.clearInstance()

    def testGetControlShapes(self):
        config = Config.getInstance()
        controlShapes = config.getControlShapes()

        self.assertIsNotNone(controlShapes)
        self.assertTrue(type(controlShapes) is dict)

        config.clearInstance()

    def testGetExplicitNaming(self):
        config = Config.getInstance()

        self.assertTrue(type(config.getExplicitNaming()) is bool)

        config.clearInstance()

    def testSetExplicitNaming(self):
        config = Config.getInstance()
        config.setExplicitNaming(True)

        self.assertTrue(config.getExplicitNaming())

        config.clearInstance()

    @unittest.expectedFailure
    def testSetExplicitNamingTypeFail(self):
        """This should fail as explicit naming requires a bool value."""

        config = Config.getInstance()
        config.setExplicitNaming("test")

        config.clearInstance()

    def testGetMetaData(self):
        config = Config.getInstance()
        testMetaData = config.getMetaData('test', value='testValue')

        self.assertEquals(testMetaData, 'testValue')

        config.clearInstance()

    def testSetMetaData(self):
        config = Config.getInstance()
        setMetaData = config.setMetaData('test', 'testValue')

        self.assertTrue(setMetaData)

        config.clearInstance()

    @unittest.expectedFailure
    def testSetMetaDataTypeFail(self):
        """This should fail as meta data requires a string key."""

        config = Config.getInstance()
        config.setMetaData(5, 'testValue')

        config.clearInstance()

    def testGetInstance(self):
        config = Config.getInstance()

        self.assertIsNotNone(config)

        config.clearInstance()

    def testMakeCurrent(self):
        Config.makeCurrent()
        config = Config.getInstance()

        self.assertIsNotNone(config)

        config.clearInstance()

    def testClearInstance(self):
        result = Config.clearInstance()

        self.assertTrue(result)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestConfig)


if __name__ == '__main__':
    unittest.main(verbosity=2)
