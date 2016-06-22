@ECHO OFF
ECHO "Releasing The Kraken!"

set KRAKEN_PATH=C:\Users\Eric\Documents\dev\kraken
set FABRIC_EXTS_PATH=%KRAKEN_PATH%\Exts;
set FABRIC_DFG_PATH=%KRAKEN_PATH%\Presets\DFG;
set PYTHONPATH=%PYTHONPATH%;%KRAKEN_PATH%\Python;

call "C:\Program Files\Autodesk\Softimage 2015 SP1\Application\bin\XSI.bat"

echo OFF