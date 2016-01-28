from kraken.core.configs.config import Config


class OSSConfig(Config):
    """Test configuration."""

    def __init__(self):
        super(OSSConfig, self).__init__()

        self.oss_initControlShapes()

    # ======================
    # Color Mapping Methods
    # ======================
    def initColorMap(self):
        """Initializes the color values.

        Returns:
            dict: color definitions.

        """

        colorMap = {
                    "Control": {
                                "default": "yellowLight",
                                "L": "turqoiseMuted",
                                "M": "yellowLight",
                                "R": "mutedMagenta"
                               }
                   }

        return colorMap


     # ======================
    # Name Template Methods
    # ======================
    def initNameTemplate(self):
        """Initializes the name template.

        Returns:
            dict: name template.

        """

        nameTemplate = {
                        "locations": ["L", "R", "M"],
                        "mirrorMap": {
                                      "L": "R",
                                      "R": "L",
                                      "M": "M"
                                     },
                        "separator": "_",
                        "types": {
                                  "default": "null",
                                  "Component": "",
                                  "ComponentGroup": "cmp",
                                  "ComponentInput": "cmpIn",
                                  "ComponentOutput": "cmpOut",
                                  "Container": "",
                                  "Control": "an",
                                  "FKControl": "fk",
                                  "IKControl": "ik",
                                  "MCControl": "mc",
                                  "Curve": "crv",
                                  "HierarchyGroup": "hrc",
                                  "Joint": "def",
                                  "Layer": "",
                                  "Locator": "loc",
                                  "Transform": "xfo",
                                  "CtrlSpace": "space"
                                 },
                        "formats":
                                  {
                                   "Container"       : ["name"],
                                   "Layer"           : ["container", "sep", "name"],
                                   "Control"         : ["location", "sep", "name", "sep", "type"],
                                   "FKControl"       : ["location", "sep", "name", "sep", "type"],
                                   "IKControl"       : ["location", "sep", "name", "sep", "type"],
                                   "MCControl"       : ["location", "sep", "name", "sep", "type"],
                                   "default"         : ["location", "sep", "name", "sep", "type"],
                                   "Transform"       : ["location", "sep", "name", "sep", "type"]
                                  }
                       }

        return nameTemplate



  # ======================
    # Control Shape Methods
    # ======================
    def oss_initControlShapes(self):
        """modify the control shapes.

        Returns:
            shapes

        """

        controlShapes = {

                         "main": [
                              {
                              "points":  [
                                           [3.3166, 0.0000, 11.2661],
                                           [3.3166, 0.0000, 12.1030],
                                           [5.5276, 0.0000, 12.1030],
                                           [0.0000, 0.0000, 16.2875],
                                           [-5.5276, 0.0000, 12.1030],
                                           [-3.3166, 0.0000, 12.1030],
                                           [-3.3166, 0.0000, 11.2661],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [3.3166, 0.0000, 11.2661],
                                           [3.3166, 0.0000, 11.2661],
                                           [4.5318, 0.0000, 10.9408],
                                           [6.5792, 0.0000, 9.8464],
                                           [8.3737, 0.0000, 8.3737],
                                           [9.8464, 0.0000, 6.5792],
                                           [10.9408, 0.0000, 4.5318],
                                           [11.6147, 0.0000, 2.3103],
                                           [11.8422, 0.0000, 0.0000],
                                           [11.6147, 0.0000, -2.3103],
                                           [10.9408, 0.0000, -4.5318],
                                           [9.8464, 0.0000, -6.5792],
                                           [8.3737, 0.0000, -8.3737],
                                           [6.5792, 0.0000, -9.8464],
                                           [4.5318, 0.0000, -10.9408],
                                           [0.0000, 0.0000, -12.0087],
                                           [-4.5318, 0.0000, -10.9408],
                                           [-6.5792, 0.0000, -9.8464],
                                           [-8.3737, 0.0000, -8.3737],
                                           [-9.8464, 0.0000, -6.5792],
                                           [-10.9408, 0.0000, -4.5318],
                                           [-11.6147, 0.0000, -2.3103],
                                           [-11.8422, 0.0000, 0.0000],
                                           [-11.6147, 0.0000, 2.3103],
                                           [-10.9408, 0.0000, 4.5318],
                                           [-9.8464, 0.0000, 6.5792],
                                           [-8.3737, 0.0000, 8.3737],
                                           [-6.5792, 0.0000, 9.8464],
                                           [-4.5318, 0.0000, 10.9408],
                                           [-3.3166, 0.0000, 11.2661],
                                           [-3.3166, 0.0000, 11.2661],
                                         ],
                              "degree":  3,
                              "closed": False,
                              },
                             ],

                        }
        self._controlShapes.update(controlShapes)

from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerConfig(OSSConfig)
