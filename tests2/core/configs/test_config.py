
import unittest

from kraken.core.configs.config import Config


class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._config = Config()

    def testGetModulePath(self):
        config = self._config.getInstance()
        modulePath = config.getModulePath()

        self.assertIsNotNone(modulePath)
        self.assertTrue(type(modulePath) is str)
        self.assertEquals(modulePath, "kraken.core.configs.config.Config")

    def testInitObjectSettings(self):
        config = self._config.getInstance()
        settings = config.initObjectSettings()

        self.assertIsNotNone(settings)
        self.assertTrue(type(settings) is dict)
        self.assertTrue(type(settings) is dict)

    def testGetObjectSettings(self):
        config = self._config.getInstance()
        settings = config.getObjectSettings()

        self.assertIsNotNone(settings)
        self.assertTrue(type(settings) is dict)
        self.assertTrue(settings['joint']['size'] is not None)

    def testInitColors(self):
        config = self._config.getInstance()
        colors = config.initColors()

        self.assertIsNotNone(colors)
        self.assertTrue(type(colors) is dict)
        self.assertEquals(len(colors), 148)

    def testGetColors(self):
        config = self._config.getInstance()
        colors = config.getColors()

        self.assertIsNotNone(colors)
        self.assertTrue(type(colors) is dict)
        self.assertEquals(len(colors), 148)

    def testInitColorMap(self):
        config = self._config.getInstance()
        colorMap = config.initColorMap()

        self.assertIsNotNone(colorMap)
        self.assertTrue(type(colorMap) is dict)
        self.assertTrue('Default' in colorMap)
        self.assertTrue('Control' in colorMap)
        self.assertEquals(
            len(set(['default','L','M','R'] + colorMap['Control'].keys())), 4)

    def testGetColorMap(self):
        config = self._config.getInstance()
        colorMap = config.getColorMap()

        self.assertIsNotNone(colorMap)
        self.assertTrue(type(colorMap) is dict)
        self.assertTrue('Default' in colorMap)
        self.assertTrue('Control' in colorMap)
        self.assertEquals(
            len(set(['default','L','M','R'] + colorMap['Control'].keys())), 4)

    def testInitNameTemplate(self):
        config = self._config.getInstance()
        nameTemplate = config.initNameTemplate()
        requiredKeys = ['locations', 'mirrorMap', 'separator', 'types', 'formats']

        self.assertIsNotNone(nameTemplate)
        self.assertTrue(type(nameTemplate) is dict)
        self.assertEquals(
            len(set(requiredKeys + nameTemplate.keys())), 5)

    def testGetNameTemplate(self):
        pass

    def testInitControlShapes(self):
        pass

    def testGetControlShapes(self):
        pass

    def testGetExplicitNaming(self):
        pass

    def testSetExplicitNaming(self):
        pass

    def testGetMetaData(self):
        pass

    def testSetMetaData(self):
        pass



    def testGetInstance(self):
        config = self._config.getInstance()

        self.assertIsNotNone(config)

    def testMakeCurrent(self):
        Config.makeCurrent()
        config = self._config.getInstance()

        self.assertIsNotNone(config)

    def testClearInstance(self):
        result = Config.clearInstance()

        self.assertTrue(result)


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestConfig)


if __name__ == '__main__':
    unittest.main(verbosity=2)