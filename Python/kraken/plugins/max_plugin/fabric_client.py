import FabricEngine.Core

from kraken.log.utils import fabricCallback
from kraken.plugins.max_plugin.utils import *


def getClient():
    """Gets the Fabric client from the DCC. This ensures that the same client
    is used, instead of a new one being created each time one is requiredself.

    Returns:
        Fabric Client.

    """

    contextID = MaxPlus.Core.EvalMAXScript("fabric.ContextId").Get()
    if contextID == '':
        client = FabricEngine.Core.createClient()
        contextID = client.getContextID()
        MaxPlus.Core.EvalMAXScript("fabric.ContextId = \"" + str(contextID) + "\"")

    options = {
        'contextID': contextID,
        'reportCallback': fabricCallback,
        'guarded': True
    }

    client = FabricEngine.Core.createClient(options)

    return client
