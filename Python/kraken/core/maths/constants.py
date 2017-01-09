"""Kraken - math.constants module."""


PI = 3.141592653589793
DEG_TO_RAD = 0.017453292519943295
RAD_TO_DEG = 57.29577951308232

AXIS_NAME_TO_TUPLE_MAP = {
    'POSX': (1, 0, 0),
    'POSY': (0, 1, 0),
    'POSZ': (0, 0, 1),
    'NEGX': (-1, 0, 0),
    'NEGY': (0, -1, 0),
    'NEGZ': (0, 0, -1)
}

AXIS_NAME_TO_INT_MAP = {
    'POSX': 0,
    'POSY': 1,
    'POSZ': 2,
    'NEGX': 3,
    'NEGY': 4,
    'NEGZ': 5
}

ROT_ORDER_STR_TO_INT_MAP = {
    'zyx': 0,
    'ZYX': 0,
    'xzy': 1,
    'XZY': 1,
    'yxz': 2,
    'YXZ': 2,
    'yzx': 3,
    'YZX': 3,
    'xyz': 4,
    'XYZ': 4,
    'zxy': 5,
    'ZXY': 5
}

ROT_ORDER_INT_TO_STR_MAP = {
    0: 'ZYX',
    1: 'XZY',
    2: 'YXZ',
    3: 'YZX',
    4: 'XYZ',
    5: 'ZXY'
}