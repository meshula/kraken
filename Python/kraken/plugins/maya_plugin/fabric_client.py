import FabricEngine.Core

from kraken.log.utils import fabricCallback
from kraken.plugins.maya_plugin.utils import *


def getClient():
    """Gets the Fabric client from the DCC. This ensures that the same client
    is used, instead of a new one being created each time one is requiredself.

    Returns:
        Fabric Client.

    """

    contextID = pm.FabricCanvasGetContextID()
    if contextID == '':
        raise ValueError('Kraken Maya could not construct a client!')

    options = {
        'contextID': contextID,
        'reportCallback': fabricCallback,
        'guarded': True
    }

    client = FabricEngine.Core.createClient(options)

    return client
