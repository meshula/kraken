from kraken.core.configs.config import Config


class OSSConfig(Config):
    """Test configuration."""

    def __init__(self):
        super(OSSConfig, self).__init__()

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
                                   "CtrlSpace"       : ["location", "sep", "name", "sep", "type"],
                                   "FKControl"       : ["location", "sep", "name", "sep", "type"],
                                   "IKControl"       : ["location", "sep", "name", "sep", "type"],
                                   "MCControl"       : ["location", "sep", "name", "sep", "type"],
                                   "default"         : ["component", "sep", "location", "sep", "name", "sep", "type"],
                                   "Joint"           : ["location", "sep", "name", "sep", "type"],
                                   "Transform"       : ["location", "sep", "name", "sep", "type"]
                                  }
                       }

        return nameTemplate




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerConfig(OSSConfig)
