import os
import shutil
import subprocess

fabricPath = os.environ.get("FABRIC_DIR")
kl2dfgPath = os.path.join(fabricPath, 'bin', 'kl2dfg.exe')
krakenPath = os.environ.get('KRAKEN_PATH')
krakenExtsPath = os.path.join(krakenPath, 'Exts')
krakenDFGPath = os.path.join(krakenPath, 'Presets', 'DFG', 'Kraken', 'Exts')

# Clear the Existing Presets
if os.path.exists(krakenDFGPath):
    shutil.rmtree(krakenDFGPath)

os.mkdir(krakenDFGPath)

for root, dirs, files in os.walk(krakenExtsPath):
    if root.endswith(('KrakenAnimation', 'KrakenForCanvas')):
        continue

    getExts = lambda x: [f for f in x if f.endswith(".fpm.json")]

    exts = getExts(files)
    if len(exts) < 1:
        continue

    for ext in exts:
        extPath = os.path.join(root, ext)

        subprocess.call("{} {} {}".format(kl2dfgPath, extPath, krakenDFGPath), shell=True)