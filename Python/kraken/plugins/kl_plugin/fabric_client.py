import FabricEngine.Core

from kraken.log.utils import fabricCallback


def getClient():
    """Gets the Fabric client from the DCC. This ensures that the same client
    is used, instead of a new one being created each time one is requiredself.

    Returns:
        Fabric Client.

    """

    options = {
        # 'contextID': contextID,
        'reportCallback': fabricCallback,
        'guarded': True
    }

    return FabricEngine.Core.createClient(options)
