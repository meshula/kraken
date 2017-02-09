"""Kraken - base config module.

Classes:
Config -- Base config object used to configure builders.

"""

from kraken.core.maths import Color


class Config(object):
    """Base Configuration for Kraken builders."""

    __instance = None

    def __init__(self):
        super(Config, self).__init__()

        # the config is a singleton, so after the first is constructed, throw an error.
        if Config.__instance is not None:
            raise Exception("Config object constructed twice. Please always call 'Config.getInstance'")

        Config.__instance = self

        self._explicitNaming = False
        self._objectSettings = self.initObjectSettings()
        self._colors = self.initColors()
        self._colorMap = self.initColorMap()
        self._nameTemplate = self.initNameTemplate()
        self._controlShapes = self.initControlShapes()
        self._metaData = {}

    def getModulePath(self):
        return self.__module__ + '.' + self.__class__.__name__

    # ================
    # Object Settings
    # ================
    def initObjectSettings(self):
        """Initializes default object settings to be applied when certain
        objects are created.

        Returns:
            dict: object settings.

        """

        settings = {
            "joint": {
                "size": 1.0
            }
        }

        return settings


    def getObjectSettings(self):
        """Gets the colors defined in the config.

        Returns:
            dict: colors.

        """

        return self._objectSettings


    # ==============
    # Color Methods
    # ==============
    def initColors(self):
        """Initializes the color values.

        Returns:
            dict: color definitions.

        """

        # Note: These were taken from Maya and is the least common denominator since
        # you can't set colors by scalar values. :\
        #
        # Note 2: Autodesk just implemented this so we need to keep this implementation
        # for a while until it becomes the norm.

        colors = {
            'aliceblue': [0.94, 0.97, 1.0],
            'antiquewhite': [0.98, 0.92, 0.84],
            'aqua': [0.0, 1.0, 1.0],
            'aquamarine': [0.49, 1.0, 0.83],
            'azure': [0.94, 1.0, 1.0],
            'beige': [0.96, 0.96, 0.86],
            'bisque': [1.0, 0.89, 0.76],
            'black': [0.0, 0.0, 0.0],
            'blanchedalmond': [1.0, 0.92, 0.8],
            'blue': [0.0, 0.0, 1.0],
            'blueviolet': [0.54, 0.16, 0.88],
            'brown': [0.64, 0.16, 0.16],
            'burlywood': [0.87, 0.72, 0.52],
            'cadetblue': [0.37, 0.61, 0.62],
            'chartreuse': [0.49, 1.0, 0.0],
            'chocolate': [0.82, 0.41, 0.11],
            'coral': [1.0, 0.49, 0.31],
            'cornflowerblue': [0.39, 0.58, 0.92],
            'cornsilk': [1.0, 0.97, 0.86],
            'crimson': [0.86, 0.07, 0.23],
            'cyan': [0.0, 1.0, 1.0],
            'darkblue': [0.0, 0.0, 0.54],
            'darkcyan': [0.0, 0.54, 0.54],
            'darkgoldenrod': [0.72, 0.52, 0.04],
            'darkgray': [0.66, 0.66, 0.66],
            'darkgreen': [0.0, 0.39, 0.0],
            'darkgrey': [0.66, 0.66, 0.66],
            'darkkhaki': [0.74, 0.71, 0.41],
            'darkmagenta': [0.54, 0.0, 0.54],
            'darkolivegreen': [0.33, 0.41, 0.18],
            'darkorange': [1.0, 0.54, 0.0],
            'darkorchid': [0.59, 0.19, 0.8],
            'darkred': [0.54, 0.0, 0.0],
            'darksalmon': [0.91, 0.58, 0.47],
            'darkseagreen': [0.56, 0.73, 0.56],
            'darkslateblue': [0.28, 0.23, 0.54],
            'darkslategray': [0.18, 0.3, 0.3],
            'darkslategrey': [0.18, 0.3, 0.3],
            'darkturquoise': [0.0, 0.8, 0.81],
            'darkviolet': [0.58, 0.0, 0.82],
            'deeppink': [1.0, 0.07, 0.57],
            'deepskyblue': [0.0, 0.74, 1.0],
            'dimgray': [0.41, 0.41, 0.41],
            'dimgrey': [0.41, 0.41, 0.41],
            'dodgerblue': [0.11, 0.56, 1.0],
            'firebrick': [0.69, 0.13, 0.13],
            'floralwhite': [1.0, 0.98, 0.94],
            'forestgreen': [0.13, 0.54, 0.13],
            'fuchsia': [1.0, 0.0, 1.0],
            'gainsboro': [0.86, 0.86, 0.86],
            'ghostwhite': [0.97, 0.97, 1.0],
            'gold': [1.0, 0.84, 0.0],
            'goldenrod': [0.85, 0.64, 0.12],
            'gray': [0.5, 0.5, 0.5],
            'green': [0.0, 0.5, 0.0],
            'greenyellow': [0.67, 1.0, 0.18],
            'grey': [0.5, 0.5, 0.5],
            'honeydew': [0.94, 1.0, 0.94],
            'hotpink': [1.0, 0.41, 0.7],
            'indianred': [0.8, 0.36, 0.36],
            'indigo': [0.29, 0.0, 0.5],
            'ivory': [1.0, 1.0, 0.94],
            'khaki': [0.94, 0.9, 0.54],
            'lavender': [0.9, 0.9, 0.98],
            'lavenderblush': [1.0, 0.94, 0.96],
            'lawngreen': [0.48, 0.98, 0.0],
            'lemonchiffon': [1.0, 0.98, 0.8],
            'lightblue': [0.67, 0.84, 0.9],
            'lightcoral': [0.94, 0.5, 0.5],
            'lightcyan': [0.87, 1.0, 1.0],
            'lightgoldenrodyellow': [0.98, 0.98, 0.82],
            'lightgray': [0.82, 0.82, 0.82],
            'lightgreen': [0.56, 0.93, 0.56],
            'lightgrey': [0.82, 0.82, 0.82],
            'lightpink': [1.0, 0.71, 0.75],
            'lightsalmon': [1.0, 0.62, 0.47],
            'lightseagreen': [0.12, 0.69, 0.66],
            'lightskyblue': [0.52, 0.8, 0.98],
            'lightslategray': [0.46, 0.53, 0.59],
            'lightslategrey': [0.46, 0.53, 0.59],
            'lightsteelblue': [0.69, 0.76, 0.87],
            'lightyellow': [1.0, 1.0, 0.87],
            'lime': Color(0.0, 1.0, 0.0),
            'limegreen': [0.19, 0.8, 0.19],
            'linen': [0.98, 0.94, 0.9],
            'magenta': [1.0, 0.0, 1.0],
            'maroon': [0.5, 0.0, 0.0],
            'mediumaquamarine': [0.4, 0.8, 0.66],
            'mediumblue': [0.0, 0.0, 0.8],
            'mediumorchid': [0.72, 0.33, 0.82],
            'mediumpurple': [0.57, 0.43, 0.85],
            'mediumseagreen': [0.23, 0.7, 0.44],
            'mediumslateblue': [0.48, 0.4, 0.93],
            'mediumspringgreen': [0.0, 0.98, 0.6],
            'mediumturquoise': [0.28, 0.81, 0.8],
            'mediumvioletred': [0.78, 0.08, 0.52],
            'midnightblue': [0.09, 0.09, 0.43],
            'mintcream': [0.96, 1.0, 0.98],
            'mistyrose': [1.0, 0.89, 0.88],
            'moccasin': [1.0, 0.89, 0.7],
            'navajowhite': [1.0, 0.87, 0.67],
            'navy': [0.0, 0.0, 0.5],
            'oldlace': [0.99, 0.96, 0.9],
            'olive': [0.5, 0.5, 0.0],
            'olivedrab': [0.41, 0.55, 0.13],
            'orange': [1.0, 0.64, 0.0],
            'orangered': [1.0, 0.27, 0.0],
            'orchid': [0.85, 0.43, 0.83],
            'palegoldenrod': [0.93, 0.9, 0.66],
            'palegreen': [0.59, 0.98, 0.59],
            'paleturquoise': [0.68, 0.93, 0.93],
            'palevioletred': [0.85, 0.43, 0.57],
            'papayawhip': [1.0, 0.93, 0.83],
            'peachpuff': [1.0, 0.85, 0.72],
            'peru': [0.8, 0.52, 0.24],
            'pink': [1.0, 0.75, 0.79],
            'plum': [0.86, 0.62, 0.86],
            'powderblue': [0.69, 0.87, 0.9],
            'purple': [0.5, 0.0, 0.5],
            'rebeccapurple': [0.4, 0.2, 0.59],
            'red': [1.0, 0.0, 0.0],
            'rosybrown': [0.73, 0.56, 0.56],
            'royalblue': [0.25, 0.41, 0.88],
            'saddlebrown': [0.54, 0.27, 0.07],
            'salmon': [0.98, 0.5, 0.44],
            'sandybrown': [0.95, 0.64, 0.37],
            'seagreen': [0.18, 0.54, 0.34],
            'seashell': [1.0, 0.96, 0.93],
            'sienna': [0.62, 0.32, 0.17],
            'silver': [0.75, 0.75, 0.75],
            'skyblue': [0.52, 0.8, 0.92],
            'slateblue': [0.41, 0.35, 0.8],
            'slategray': [0.43, 0.5, 0.56],
            'slategrey': [0.43, 0.5, 0.56],
            'snow': [1.0, 0.98, 0.98],
            'springgreen': [0.0, 1.0, 0.49],
            'steelblue': [0.27, 0.5, 0.7],
            'tan': [0.82, 0.7, 0.54],
            'teal': [0.0, 0.5, 0.5],
            'thistle': [0.84, 0.74, 0.84],
            'tomato': [1.0, 0.38, 0.27],
            'turquoise': [0.25, 0.87, 0.81],
            'violet': [0.93, 0.5, 0.93],
            'wheat': [0.96, 0.87, 0.7],
            'white': [1.0, 1.0, 1.0],
            'whitesmoke': [0.96, 0.96, 0.96],
            'yellow': [1.0, 1.0, 0.0],
            'yellowgreen': [0.6, 0.8, 0.19]
        }

        return colors

    def getColors(self):
        """Gets the colors defined in the config.

        Returns:
            dict: colors.

        """

        return self._colors


    # ======================
    # Color Mapping Methods
    # ======================
    def initColorMap(self):
        """Initializes the color values.

        Returns:
            dict: color definitions.

        """

        colorMap = {
            "Default": "yellow",
            "Control": {
                "default": "yellow",
                "L": "lime",
                "M": "yellow",
                "R": "red"
            }
        }

        return colorMap

    def getColorMap(self):
        """Gets the color map defined in the config.

        Returns:
            dict: color map.

        """

        return self._colorMap


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
                "Control": "ctrl",
                "Curve": "crv",
                "HierarchyGroup": "hrc",
                "Joint": "def",
                "Layer": "",
                "Locator": "loc",
                "CtrlSpace": "ctrlSpace",
                "OrientationConstraint": "oriCns",
                "PoseConstraint": "poseCns",
                "PositionConstraint": "posCns",
                "ScaleConstraint": "sclCns",
                "KLOperator": "klOp",
                "CanvasOperator": "canvasOp"
            },
            "formats":
                {
                    "Container": ["name"],
                    "Layer": ["container", "sep", "name"],
                    "ComponentGroup": ["name", "sep", "location", "sep", "type"],
                    "default": ["component", "sep", "location", "sep", "name", "sep", "type"],
                    "KLOperator": ["component", "sep", "location", "sep", "name", "sep", "solverSource", "sep", "solverName", "sep", "type"],
                    "CanvasOperator": ["component", "sep", "location", "sep", "name", "sep", "solverSource", "sep", "solverName", "sep", "type"]
            }
        }

        return nameTemplate

    def getNameTemplate(self):
        """Returns the naming template for this configuration.

        Returns:
            dict: naming template.

        """

        return self._nameTemplate


    # ======================
    # Control Shape Methods
    # ======================
    def initControlShapes(self):
        """Initializes the control shapes.

        Returns:
            bool: True if successful.

        """

        controlShapes = {
                         "point": [
                                   {
                                    "points": [
                                               [0.0, 0.0, 0.0],
                                              ],
                                    "degree": 1,
                                    "closed": False
                                   }
                                  ],
                         "arrow": [
                            {
                                'points': [
                                    [0.05, 0.0, 0.25],
                                    [0.15, 0.0, 0.25],
                                    [0.0, 0.0, 0.5],
                                    [-0.15, 0.0, 0.25],
                                    [-0.05, 0.0, 0.25],
                                    [-0.05, 0.0, -0.5],
                                    [0.05, 0.0, -0.5],
                                    [0.05, 0.0, 0.25]],
                                'closed': False,
                                'degree': 1
                            }],
                         "arrow_thin": [
                            {
                                'points': [
                                    [0.0, 0.0, -0.5],
                                    [0.0, 0.0, 0.25],
                                    [-0.15, 0.0, 0.25],
                                    [0.0, 0.0, 0.5],
                                    [0.15, 0.0, 0.25],
                                    [0.0, 0.0, 0.25]],
                                'closed': False,
                                'degree': 1
                            }
                         ],
                         "arrows": [
                                    {
                                     "points": [
                                                [-0.05, 0.0, 0.05],
                                                [-0.05, 0.0, 0.25],
                                                [-0.15, 0.0, 0.25],
                                                [0.0, -0.0, 0.4],
                                                [0.15, 0.0, 0.25],
                                                [0.05, 0.0, 0.25],
                                                [0.05, 0.0, 0.05],
                                                [0.25, 0.0, 0.05],
                                                [0.25, 0.0, 0.15],
                                                [0.4, -0.0, 0.0],
                                                [0.25, 0.0, -0.15],
                                                [0.25, 0.0, -0.05],
                                                [0.05, 0.0, -0.05],
                                                [0.05, 0.0, -0.25],
                                                [0.15, 0.0, -0.25],
                                                [0.0, -0.0, -0.4],
                                                [-0.15, 0.0, -0.25],
                                                [-0.05, 0.0, -0.25],
                                                [-0.05, 0.0, -0.05],
                                                [-0.25, 0.0, -0.05],
                                                [-0.25, 0.0, -0.15],
                                                [-0.4, -0.0, -0.0],
                                                [-0.25, 0.0, 0.15],
                                                [-0.25, 0.0, 0.05]
                                               ],
                                     "degree": 1,
                                     "closed": True
                                    }
                                   ],
                         "axes": [
                                  {
                                   "points": [
                                              [0.0, 0.0, 0.0],
                                              [0.5, 0.0, 0.0]
                                             ],
                                   "closed": False,
                                   "degree": 1
                                  },
                                  {
                                   "points": [
                                              [0.0, 0.5, 0.0],
                                              [0.0, 0.0, 0.0]
                                             ],
                                   "closed": False,
                                   "degree": 1
                                  },
                                  {
                                   "points": [
                                              [0.0, 0.0, 0.0],
                                              [0.0, 0.0, 0.5]
                                             ],
                                   "closed": False,
                                   "degree": 1}
                                   ],
                         "axesHalfTarget": [
                                        {
                                         'points': [
                                                    [0.0, 0.0, 0.0],
                                                    [0.5, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.5, 0.0],
                                                    [0.0, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.0, 0.0],
                                                    [0.0, 0.0, 0.5]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.0, 0.0],
                                                    [-0.5, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [-0.25, 0.0, 0.0],
                                                    [-0.25, 0.066, 0.0],
                                                    [-0.196, 0.195, 0.0],
                                                    [0.0, 0.277, 0.0],
                                                    [0.196, 0.195, 0.0],
                                                    [0.25, 0.066, 0.0],
                                                    [0.25, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 3
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.0, 0.0],
                                                    [0.5, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.5, 0.0],
                                                    [0.0, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.0, 0.0],
                                                    [0.0, 0.0, 0.5]],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [0.0, 0.0, 0.0],
                                                    [-0.5, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 1
                                        },
                                        {
                                         'points': [
                                                    [-0.25, 0.0, 0.0],
                                                    [-0.25, 0.066, 0.0],
                                                    [-0.196, 0.195, 0.0],
                                                    [0.0, 0.277, 0.0],
                                                    [0.196, 0.195, 0.0],
                                                    [0.25, 0.066, 0.0],
                                                    [0.25, 0.0, 0.0]
                                                   ],
                                         'closed': False,
                                         'degree': 3
                                         },
                                         {
                                          'points': [
                                                     [0.0, 0.25, 0.0],
                                                     [0.0, 0.25, 0.033],
                                                     [0.0, 0.237, 0.098],
                                                     [0.0, 0.181, 0.181],
                                                     [0.0, 0.098, 0.237], [0.0, 0.033, 0.25], [0.0, 0.0, 0.25]
                                                    ],
                                          'closed': False,
                                          'degree': 3
                                         },
                                         {
                                          'points': [
                                                     [0.25, 0.0, 0.0],
                                                     [0.25, 0.0, 0.033],
                                                     [0.237, 0.0, 0.098],
                                                     [0.181, 0.0, 0.181],
                                                     [0.098, -0.0, 0.237],
                                                     [0.033, -0.0, 0.25],
                                                     [0.0, -0.0, 0.25]
                                                    ],
                                          'closed': False,
                                          'degree': 3
                                         },
                                         {
                                          'points': [
                                                     [-0.25, 0.0, 0.0],
                                                     [-0.25, 0.0, 0.033],
                                                     [-0.237, 0.0, 0.098],
                                                     [-0.181, 0.0, 0.181],
                                                     [-0.098, 0.0, 0.237],
                                                     [-0.033, 0.0, 0.25],
                                                     [0.0, 0.0, 0.25]
                                                    ],
                                          'closed': False,
                                          'degree': 3
                                          }
                                         ],
                         "circle": [
                                    {
                                     "points": [
                                                [0.35, 0.0, -0.35],
                                                [0.5, 0.0, 0.0],
                                                [0.35, 0.0, 0.35],
                                                [0.0, 0.0, 0.5],
                                                [-0.35, 0.0, 0.35],
                                                [-0.5, 0.0, 0.0],
                                                [-0.35, 0.0, -0.35],
                                                [0.0, 0.0, -0.5]
                                               ],
                                     "degree": 1,
                                     "closed": True
                                    }
                                   ],
                         "cube": [
                                   {
                                    "points": [
                                               [-0.5, -0.5, -0.5],
                                               [-0.5, 0.5, -0.5],
                                               [0.5, 0.5, -0.5],
                                               [0.5, -0.5, -0.5]
                                              ],
                                    "degree": 1,
                                    "closed": True
                                   },
                                   {
                                    "points": [
                                               [-0.5, -0.5, 0.5],
                                               [-0.5, 0.5, 0.5],
                                               [0.5, 0.5, 0.5],
                                               [0.5, -0.5, 0.5]
                                              ],
                                    "degree": 1,
                                    "closed": True
                                   },
                                   {
                                    "points": [
                                               [-0.5, -0.5, -0.5],
                                               [-0.5, -0.5, 0.5]
                                              ],
                                    "degree": 1,
                                    "closed": False
                                   },
                                   {
                                    "points": [
                                               [0.5, -0.5, -0.5],
                                               [0.5, -0.5, 0.5]
                                              ],
                                    "degree": 1,
                                    "closed": False
                                   },
                                   {
                                    "points": [
                                               [-0.5, 0.5, -0.5],
                                               [-0.5, 0.5, 0.5]
                                              ],
                                    "degree": 1,
                                    "closed": False
                                   },
                                   {
                                    "points": [
                                               [0.5, 0.5, -0.5],
                                               [0.5, 0.5, 0.5]
                                              ],
                                    "degree": 1,
                                    "closed": False
                                   }
                                  ],
                         "null": [
                                  {
                                   "points": [
                                              [-0.5, 0.0, 0.0],
                                              [0.5, 0.0, 0.0]
                                             ],
                                   "degree": 1,
                                   "closed": False
                                  },
                                  {
                                   "points": [
                                              [0.0, -0.5, 0.0],
                                              [0.0, 0.5, 0.0]
                                             ],
                                   "degree": 1,
                                   "closed": False
                                  },
                                  {
                                   "points": [
                                              [0.0, 0.0, -0.5],
                                              [0.0, 0.0, 0.5]
                                             ],
                                   "degree": 1,
                                   "closed": False
                                  }
                                 ],
                         "pin": [
                                 {
                                  "points": [
                                             [0.0, 0.0, -0.5],
                                             [-0.17, 0.0, -0.57],
                                             [-0.25, 0.0, -0.75],
                                             [-0.17, 0.0, -0.93],
                                             [0.0, 0.0, -1.0],
                                             [0.17, 0.0, -0.93],
                                             [0.25, 0.0, -0.75],
                                             [0.17, 0.0, -0.57],
                                             [0.0, 0.0, -0.5],
                                             [0.0, 0.0, 0.0]
                                            ],
                                  "degree": 1,
                                  "closed": False
                                 }
                                ],
                         "sphere": [
                                    {
                                     "points": [
                                                [0.0, 0.5, 0.0],
                                                [0.0, 0.35, -0.35],
                                                [0.0, 0.0, -0.5],
                                                [0.0, -0.35, -0.35],
                                                [0.0, -0.5, 0.0],
                                                [0.0, -0.35, 0.35],
                                                [0.0, 0.0, 0.5],
                                                [0.0, 0.35, 0.35]
                                               ],
                                     "degree": 1,
                                     "closed": True
                                    },
                                    {
                                     "points": [
                                                [0.0, 0.0, -0.5],
                                                [0.35, 0.0, -0.35],
                                                [0.5, 0.0, 0.0],
                                                [0.35, 0.0, 0.35],
                                                [0.0, 0.0, 0.5],
                                                [-0.35, 0.0, 0.35],
                                                [-0.5, 0.0, 0.0],
                                                [-0.35, 0.0, -0.35]
                                               ],
                                     "degree": 1,
                                     "closed": True
                                    },
                                    {
                                     "points": [
                                                [0.0, 0.5, 0.0],
                                                [0.35, 0.35, 0.0],
                                                [0.5, 0.0, 0.0],
                                                [0.35, -0.35, 0.0],
                                                [0.0, -0.5, 0.0],
                                                [-0.35, -0.35, 0.0],
                                                [-0.5, 0.0, 0.0],
                                                [-0.35, 0.35, 0.0]
                                               ],
                                     "degree": 1,
                                     "closed": True
                                    }
                                   ],
                         "square": [
                                    {
                                     "points": [
                                                [0.5, 0.0, -0.5],
                                                [0.5, 0.0, 0.5],
                                                [-0.5, 0.0, 0.5],
                                                [-0.5, 0.0, -0.5]
                                               ],
                                     "degree": 1,
                                     "closed": True
                                    }
                                   ],
                         "triangle": [
                                      {
                                       "points": [
                                                  [0.0,0.0,-0.5],
                                                  [-0.5,0.0,0.5],
                                                  [0.5,0.0,0.5]
                                                 ],
                                       "degree": 1,
                                       "closed": True
                                      }
                                     ],
                         "fkCircle": [
                                      {
                                       "points": [
                                                  [0.0, 0.35, -0.35],
                                                  [0.0, 0.46, -0.09],
                                                  [0.0, 0.55, 0.0],
                                                  [0.0, 0.46, 0.09],
                                                  [0.0, 0.35, 0.35],
                                                  [0.0, 0.09, 0.46],
                                                  [0.0, 0.0, 0.55],
                                                  [-0.0, -0.09, 0.46],
                                                  [-0.0, -0.35, 0.35],
                                                  [-0.0, -0.5, 0.0],
                                                  [-0.0, -0.35, -0.35],
                                                  [0.0, 0.0, -0.5]
                                                 ],
                                        "degree": 1,
                                        "closed": True
                                       },
                                       {
                                        "points": [
                                                   [0.0, 0.0, 0.0],
                                                   [1.0, 0.0, 0.0]
                                                  ],
                                        "degree": 1,
                                        "closed": False
                                       }
                                     ],
                         "vertebra": [
                                      {
                                       "points": [
                                                  [-0.5, -0.0, -0.5],
                                                  [0.5, 0.0, -0.5],
                                                  [0.25, 0.0, 0.5],
                                                  [-0.25, -0.0, 0.5]
                                                 ],
                                       "closed": True,
                                       "degree": 1
                                      },
                                      {
                                       "points": [
                                                  [0.0, 0.0, -0.5],
                                                  [0.0, 0.5, -0.5],
                                                  [0.0, 0.25, 0.5],
                                                  [0.0, 0.0, 0.5]
                                                 ],
                                       "closed": True,
                                       "degree": 1
                                      }
                                     ],
                          "jack": [
                                {
                              "points":  [
                                           [-0.0500, -0.5000, -0.0500],
                                           [-0.0500, 0.5000, -0.0500],
                                           [0.0500, 0.5000, -0.0500],
                                           [0.0500, -0.5000, -0.0500],
                                           [-0.0500, -0.5000, -0.0500],
                                         ],
                              "degree":  1,
                              "closed": True,
                              },
                              {
                              "points":  [
                                           [-0.0500, -0.5000, 0.0500],
                                           [-0.0500, 0.5000, 0.0500],
                                           [0.0500, 0.5000, 0.0500],
                                           [0.0500, -0.5000, 0.0500],
                                           [-0.0500, -0.5000, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": True,
                              },
                              {
                              "points":  [
                                           [-0.0500, -0.5000, -0.0500],
                                           [-0.0500, -0.5000, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [0.0500, -0.5000, -0.0500],
                                           [0.0500, -0.5000, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [-0.0500, 0.5000, -0.0500],
                                           [-0.0500, 0.5000, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [0.0500, 0.5000, -0.0500],
                                           [0.0500, 0.5000, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [-0.0500, -0.0500, -0.5000],
                                           [-0.0500, 0.0500, -0.5000],
                                           [0.0500, 0.0500, -0.5000],
                                           [0.0500, -0.0500, -0.5000],
                                           [-0.0500, -0.0500, -0.5000],
                                         ],
                              "degree":  1,
                              "closed": True,
                              },
                              {
                              "points":  [
                                           [-0.0500, -0.0500, 0.5000],
                                           [-0.0500, 0.0500, 0.5000],
                                           [0.0500, 0.0500, 0.5000],
                                           [0.0500, -0.0500, 0.5000],
                                           [-0.0500, -0.0500, 0.5000],
                                         ],
                              "degree":  1,
                              "closed": True,
                              },
                              {
                              "points":  [
                                           [-0.0500, -0.0500, -0.5000],
                                           [-0.0500, -0.0500, 0.5000],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [0.0500, -0.0500, -0.5000],
                                           [0.0500, -0.0500, 0.5000],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [-0.0500, 0.0500, -0.5000],
                                           [-0.0500, 0.0500, 0.5000],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [0.0500, 0.0500, -0.5000],
                                           [0.0500, 0.0500, 0.5000],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [-0.5000, -0.0500, -0.0500],
                                           [-0.5000, 0.0500, -0.0500],
                                           [0.5000, 0.0500, -0.0500],
                                           [0.5000, -0.0500, -0.0500],
                                           [-0.5000, -0.0500, -0.0500],
                                         ],
                              "degree":  1,
                              "closed": True,
                              },
                              {
                              "points":  [
                                           [-0.5000, -0.0500, 0.0500],
                                           [-0.5000, 0.0500, 0.0500],
                                           [0.5000, 0.0500, 0.0500],
                                           [0.5000, -0.0500, 0.0500],
                                           [-0.5000, -0.0500, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": True,
                              },
                              {
                              "points":  [
                                           [-0.5000, -0.0500, -0.0500],
                                           [-0.5000, -0.0500, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [0.5000, -0.0500, -0.0500],
                                           [0.5000, -0.0500, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [-0.5000, 0.0500, -0.0500],
                                           [-0.5000, 0.0500, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              {
                              "points":  [
                                           [0.5000, 0.0500, -0.0500],
                                           [0.5000, 0.0500, 0.0500],
                                         ],
                              "degree":  1,
                              "closed": False,
                              },
                              ],
                         "R": [
                                      {'closed': True,
                                        'degree': 2,
                                        'points': [[-0.097, 0.0, -0.03],
                                                   [-0.037, 0.0, -0.03],
                                                   [0.022, 0.0, -0.03],
                                                   [0.046, 0.0, -0.03],
                                                   [0.08, 0.0, -0.037],
                                                   [0.102, 0.0, -0.052],
                                                   [0.112, 0.0, -0.076],
                                                   [0.112, 0.0, -0.094],
                                                   [0.112, 0.0, -0.126],
                                                   [0.072, 0.0, -0.155],
                                                   [0.031, 0.0, -0.155],
                                                   [-0.033, 0.0, -0.155],
                                                   [-0.097, 0.0, -0.155],
                                                   [-0.097, 0.0, -0.093],
                                                   [-0.097, 0.0, -0.03]]},
                                       {'closed': True,
                                        'degree': 2,
                                        'points': [[0.083, -0.0, 0.114],
                                                   [0.078, -0.0, 0.101],
                                                   [0.062, -0.0, 0.078],
                                                   [0.04, -0.0, 0.061],
                                                   [0.014, -0.0, 0.052],
                                                   [-0.001, -0.0, 0.052],
                                                   [-0.049, -0.0, 0.052],
                                                   [-0.097, -0.0, 0.052],
                                                   [-0.097, -0.0, 0.148],
                                                   [-0.097, -0.0, 0.244],
                                                   [-0.141, -0.0, 0.244],
                                                   [-0.186, -0.0, 0.244],
                                                   [-0.186, -0.0, 0.005],
                                                   [-0.186, 0.0, -0.234],
                                                   [-0.079, 0.0, -0.234],
                                                   [0.028, 0.0, -0.234],
                                                   [0.047, 0.0, -0.234],
                                                   [0.082, 0.0, -0.232],
                                                   [0.114, 0.0, -0.225],
                                                   [0.143, 0.0, -0.212],
                                                   [0.156, 0.0, -0.201],
                                                   [0.18, 0.0, -0.181],
                                                   [0.203, 0.0, -0.124],
                                                   [0.203, 0.0, -0.094],
                                                   [0.203, 0.0, -0.05],
                                                   [0.161, -0.0, 0.012],
                                                   [0.124, -0.0, 0.029],
                                                   [0.14, -0.0, 0.041],
                                                   [0.164, -0.0, 0.076],
                                                   [0.174, -0.0, 0.102],
                                                   [0.199, -0.0, 0.173],
                                                   [0.225, -0.0, 0.244],
                                                   [0.177, -0.0, 0.244],
                                                   [0.129, -0.0, 0.244],
                                                   [0.106, -0.0, 0.179],
                                                   [0.083, -0.0, 0.114]]}
                                      ],
                         "L": [
                                      { 'closed': False,
                                        'degree': 1,
                                        'points': [[0.171, -0.0, 0.244],
                                                   [-0.137, -0.0, 0.244],
                                                   [-0.137, 0.0, -0.234],
                                                   [-0.048, 0.0, -0.234],
                                                   [-0.048, -0.0, 0.162],
                                                   [0.171, -0.0, 0.162],
                                                   [0.171, -0.0, 0.244]]}
                                      ],
                         "M": [
                                      { 'closed': False,
                                        'degree': 1,
                                        'points': [[0.225, 0.0, 0.244],
                                                   [0.139, 0.0, 0.244],
                                                   [0.139, 0.0, -0.062],
                                                   [0.036, 0.0, 0.244],
                                                   [-0.039, 0.0, 0.244],
                                                   [-0.141, 0.0, -0.062],
                                                   [-0.141, 0.0, 0.244],
                                                   [-0.228, 0.0, 0.244],
                                                   [-0.228, 0.0, -0.233],
                                                   [-0.112, 0.0, -0.233],
                                                   [-0.001, 0.0, 0.107],
                                                   [0.11, 0.0, -0.233],
                                                   [0.225, 0.0, -0.233],
                                                   [0.225, 0.0, 0.244]]}
                              ],
                         "direction": [
                                        {'closed': False,
                                          'degree': 1,
                                          'points': [[0.35, 0.0, -0.35],
                                                     [0.5, 0.0, 0.0],
                                                     [0.35, -0.0, 0.35],
                                                     [0.0, -0.0, 0.5],
                                                     [-0.35, -0.0, 0.35],
                                                     [-0.5, 0.0, 0.0],
                                                     [-0.35, 0.0, -0.35],
                                                     [0.0, 0.0, -0.5],
                                                     [0.0, 0.0, 0.0],
                                                     [0.0, -1.0, -0.0],
                                                     [0.0, 0.0, 0.0],
                                                     [0.0, 0.0, -0.5],
                                                     [0.35, 0.0, -0.35]]}
                            ],
                         "halfCircle": [
                                        {'closed': False,
                                          'degree': 1,
                                          'points': [[-1.858, -0.0, -0.0],
                                                     [-1.793, -0.0, -0.48],
                                                     [-1.607, -0.0, -0.928],
                                                     [-1.314, -0.0, -1.314],
                                                     [-0.928, -0.0, -1.607],
                                                     [-0.48, -0.0, -1.793],
                                                     [-0.0, -0.0, -1.858],
                                                     [0.48, -0.0, -1.793],
                                                     [0.928, -0.0, -1.607],
                                                     [1.314, -0.0, -1.314],
                                                     [1.607, -0.0, -0.928],
                                                     [1.793, -0.0, -0.48],
                                                     [1.858, -0.0, -0.0],
                                                     [-1.858, -0.0, -0.0]]}
                            ],
                         "squarePointed": [
                                        {'closed': True,
                                          'degree': 1,
                                          'points': [[-0.5, 0.0, -0.5],
                                                     [0.5, 0.0, -0.5],
                                                     [.75, 0.0, 0.0],
                                                     [0.5, 0.0, 0.5],
                                                     [-0.5, 0.0, 0.5],
                                                     [-0.5, 0.0, -0.5]]}
                            ]
                        }

        return controlShapes

    def getControlShapes(self):
        """Returns the control shapes for this configuration.

        Returns:
            dict: control shapes.

        """

        return self._controlShapes


    # =========================
    # Explicity Naming Methods
    # =========================
    def getExplicitNaming(self):
        """Returns the value of the explicit naming attribute.

        Returns:
            bool: current value.

        """

        return self._explicitNaming

    def setExplicitNaming(self, value):
        """Set the config to use explicit naming.

        Args:
            value (bool): whether to use explicit naming or not.

        Returns:
            bool: True if successful.

        """

        assert type(value) is bool, "Value argument is not of type: bool"

        self._explicitNaming = value

        return True


    # =========================
    # MetaData Methods
    # =========================
    def getMetaData(self, key, value=None):
        """Returns the value of a metaData flag.

        Args:
            key (str): Key to look up in the meta data
            value: Default value to use if not found

        Returns:
            str: current value or None for default value

        """

        assert type(key) is str, "Key value is not a string"

        return self._metaData.get(key, value)

    def setMetaData(self, key, value):
        """Set the config to contain a metaData flag.

        Args:
            key (str): the key under which to store the value
            value: the value to store for a given key

        Returns:
            bool: True if successful.

        """

        assert type(key) is str, "Key value is not a string"

        self._metaData[key] = value

        return True


    # ==============
    # Class Methods
    # ==============
    @classmethod
    def getInstance(cls):
        """This class method returns the singleton instance for the Config.

        Returns:
            object: The singleton config instance.

        """

        if Config.__instance is None:
            cls()
        elif not isinstance(Config.__instance, Config):
            raise Exception("Multiple different Config types have been constructed.")

        return Config.__instance


    @classmethod
    def makeCurrent(cls):
        """Sets this class t be the singleton instance Config.

        Returns:
            object: The singleton config instance.

        """

        Config.__instance = None
        Config.__instance = cls()


    @classmethod
    def clearInstance(cls):
        """Clears the instance variable of the config.

        Returns:
            bool: True if successful.

        """

        Config.__instance = None

        return True
