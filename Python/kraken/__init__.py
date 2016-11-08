"""Kraken Framework."""

import logging
import os

__all__ = ['core', 'helpers', 'plugins', 'ui']


krakenPath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))
if os.environ.get('KRAKEN_PATH', None) is None:
    os.environ['KRAKEN_PATH'] = krakenPath

krakenExtsPath = os.path.join(krakenPath, 'Exts')
if 'FABRIC_EXTS_PATH' in os.environ:
    if krakenExtsPath not in os.environ['FABRIC_EXTS_PATH']:
        os.environ['FABRIC_EXTS_PATH'] = krakenExtsPath + os.pathsep + os.environ['FABRIC_EXTS_PATH']

krakenPresetsPath = os.path.join(krakenPath, 'Presets', 'DFG')
if 'FABRIC_DFG_PATH' in os.environ:
    if krakenPresetsPath not in os.environ['FABRIC_DFG_PATH']:
        os.environ['FABRIC_DFG_PATH'] = krakenPresetsPath + os.pathsep + os.environ['FABRIC_DFG_PATH']


logging.basicConfig(format='[KRAKEN] %(levelname)s: %(message)s', level=logging.INFO)

# Custom inform level for use with UI label getting added to the status bar.
logging.INFORM = 25
logging.addLevelName(logging.INFORM, 'INFORM')
logging.Logger.inform = lambda inst, msg, *args, **kwargs: inst.log(logging.INFORM, msg, *args, **kwargs)


def release():
    print "RELEASE THE KRAKEN!!!!"
