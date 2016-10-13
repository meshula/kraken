
import logging

from kraken.plugins.max_plugin.utils import *

from kraken.log import getLogger

logger = getLogger('kraken')


def curveToKraken(curve):
    """Converts a curve in Maya to a valid definition for Kraken.

    Args:
        curve (obj): Maya nurbs curve Object.

    Returns:
        list: The curve definition in kraken format.

    """

    # shapes = pm.listRelatives(curve, shapes=True)

    # data = []
    # for eachShape in shapes:
    #     subCurveData = {
    #         'points': [[round(y, 3) for y in [x.x, x.y, x.z]] for x in eachShape.getCVs()],
    #         'degree': eachShape.degree(),
    #         'closed': eachShape.form() == 'closed'
    #     }

    #     data.append(subCurveData)

    # return data

    logger.warning("'curveToKraken' not implemented for 3dsMax yet!")

    return None
