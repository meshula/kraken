import logging

from kraken.plugins.maya_plugin.utils import *

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
            om.MGlobal.displayError(msg)

        elif record.levelno == logging.ERROR:
            om.MGlobal.displayError(msg)

        elif record.levelno == logging.WARNING:
            om.MGlobal.displayWarning(msg)

        elif record.levelno == logging.INFORM:
            om.MGlobal.displayInfo(msg)

        elif record.levelno == logging.INFO:
            om.MGlobal.displayInfo(msg)

        elif record.levelno == logging.DEBUG:
            om.MGlobal.displayInfo(msg)

        else:
            om.MGlobal.displayInfo(msg)
