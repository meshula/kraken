"""Kraken Softimage Plug-in."""

import os


def dccTest():
    """Returns true or false after checking if the `KRAKEN_DCC` environment
    variable is set to use this plugin.

    .. note::
        The variable value to activate the Softimage plugin is: `Softimage`.

    Returns:
        bool: True if the environment variable is set to use this plugin.

    """

    krakenDCC = os.environ.get('KRAKEN_DCC')
    if krakenDCC == "Softimage":
        return True
    else:
        return False
