import logging

from kraken.log import getLogger

logger = getLogger('kraken')


def fabricCallback(source, level, line):
    """Callback method passed to the Fabric client to ensure that Fabric Core
    messages are logged through the Kraken logger.

    Fabric Report levels:

    * Error = 0
    * Warning = 1
    * Info = 2
    * Debug = 3

    """

    if level == 3:
        logger.debug(line)
    elif level == 2:
        logger.info(line)
    elif level == 1:
        logger.warn(line)
    elif level == 0:
        logger.error(line)
    elif level == 0:
        logger.critical(line)
