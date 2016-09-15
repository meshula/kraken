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
            print(msg)

        elif record.levelno == logging.ERROR:
            print(msg)

        elif record.levelno == logging.WARNING:
            print(msg)

        elif record.levelno == logging.INFORM:
            print(msg)

        elif record.levelno == logging.INFO:
            print(msg)

        elif record.levelno == logging.DEBUG:
            print(msg)

        else:
            print(msg)
