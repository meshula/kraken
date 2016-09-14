import os
import sys


def setupEnv():


    # currDir = os.path.split(__file__)[0]

    # krakenPythonPath = os.path.join(currDir, '..', '..', '..', 'Python')

    # if krakenPythonPath not in sys.path:
    #     sys.path.append(os.path.realpath(krakenPythonPath))

    # krakenPath = os.path.join(currDir, '..', '..', '..')
    # krakenExtsPath = os.path.join(currDir, '..', '..', '..', 'Exts')
    # krakenPresetPath = os.path.join(currDir, '..', '..', '..', 'Presets', 'DFG')

    # os.environ['FABRIC_EXTS_PATH'] = os.environ.get('FABRIC_EXTS_PATH', '') + ';' + os.path.realpath(krakenExtsPath)
    # os.environ['FABRIC_DFG_PATH'] = os.environ.get('FABRIC_DFG_PATH', '') + ';' + os.path.realpath(krakenPresetPath)
    # os.environ['KRAKEN_PATH'] = os.path.realpath(krakenPath)
    os.environ['KRAKEN_DCC'] = 'Max'

    # print os.environ.get('PYTHONPATH')
    # print os.environ.get('FABRIC_EXTS_PATH')
    # print os.environ.get('FABRIC_DFG_PATH')
    # print os.environ.get('KRAKEN_PATH')
    # print os.environ.get('KRAKEN_DCC')


setupEnv()
