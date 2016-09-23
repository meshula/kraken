import logging

from kraken.plugins.max_plugin.utils import *

logging.INFORM = 25


class DCCHandler(logging.Handler):
    """Logging Handler for Maya."""

    def emit(self, record):
        """Maps the logger calls to call the specific Maya logging calls so the
        messages appear in the DCC as well.

        .. note::

            Calls to these Maya specific methods are executed:
                - om.MGlobal.displayError
                - om.MGlobal.displayWarning
                - om.MGlobal.displayInfo

        """

        msg = self.format(record)

        if record.levelno == logging.CRITICAL:
            MaxPlus.Core.WriteLine('CRITICAL ' + msg)

        elif record.levelno == logging.ERROR:
            MaxPlus.Core.WriteLine('ERROR ' + msg)

        elif record.levelno == logging.WARNING:
            MaxPlus.Core.WriteLine('WARNING ' + msg)

        elif record.levelno == logging.INFORM:
            MaxPlus.Core.WriteLine('INFORM ' + msg)

        elif record.levelno == logging.INFO:
            MaxPlus.Core.WriteLine('INFO ' + msg)

        elif record.levelno == logging.DEBUG:
            MaxPlus.Core.WriteLine('DEBUG ' + msg)

        else:
            MaxPlus.Core.WriteLine(msg)
