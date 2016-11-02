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
                    "Default": "gold",

                    "Control": {
                                "default": "gold",
                                "L": "mediumseagreen",
                                "M": "gold",
                                "R": "mediumvioletred"
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
                                  "PivotControl": "piv",
                                  "Curve": "crv",
                                  "HierarchyGroup": "hrc",
                                  "Joint": "def",
                                  "RefJoint": "ref",
                                  "Layer": "",
                                  "Locator": "loc",
                                  "Transform": "xfo",
                                  "CtrlSpace": "space",
                                  "OrientationConstraint": "oriCns",
                                  "PoseConstraint": "poseCns",
                                  "PositionConstraint": "posCns",
                                  "ScaleConstraint": "sclCns",
                                  "KLOperator": "klOp",
                                  "CanvasOperator": "canvasOp"
                                 },
                        "formats":
                                  {
                                   "default"         : ["component", "sep", "location", "sep", "name", "sep", "type"],
                                   "Container"       : ["name"],
                                   "Layer"           : ["container", "sep", "name"],
                                   "Control"         : ["location", "sep", "name", "sep", "type"],
                                   "CtrlSpace"       : ["location", "sep", "name", "sep", "type"],
                                   "FKControl"       : ["location", "sep", "name", "sep", "type"],
                                   "IKControl"       : ["location", "sep", "name", "sep", "type"],
                                   "MCControl"       : ["location", "sep", "name", "sep", "type"],
                                   "Pivot"           : ["location", "sep", "name", "sep", "type"],
                                   "Joint"           : ["location", "sep", "name", "sep", "type"],
                                   "Transform"       : ["location", "sep", "name", "sep", "type"],
                                   "KLOperator"      : ["location", "sep", "name", "sep", "type"],
                                   "CanvasOperator"  : ["location", "sep", "name", "sep", "type"]
                                  }
                       }

        return nameTemplate




from kraken.core.kraken_system import KrakenSystem
ks = KrakenSystem.getInstance()
ks.registerConfig(OSSConfig)
