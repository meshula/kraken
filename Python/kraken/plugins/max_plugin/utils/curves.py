
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

    splineShape = MaxPlus.SplineShape__CastFrom(curve.BaseObject)
    shape = splineShape.GetShape()

    data = []
    for i in xrange(shape.GetNumSplines()):
        subCrv = shape.GetSpline(i)
        lineType = subCrv.GetLineType(0)
        knotPoints = [subCrv.GetKnotPoint(x) for x in xrange(subCrv.KnotCount())]
        subCurveData = {
            'points': [[round(y, 3) for y in [x.X, x.Y, x.Z]] for x in knotPoints],
            'degree': 1 if lineType == 1 else 3,
            'closed': subCrv.Closed()
        }

        data.append(subCurveData)

    return data
