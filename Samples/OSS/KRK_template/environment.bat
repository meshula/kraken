::set FABRIC_CHARNAME_DIR=%~dp0

set FABRIC_DIR=Z:\dist\fabric\releases\published

set PATH=%FABRIC_DIR%\bin;%PATH%

set FABRIC_LOG_LEVEL=0
set KRAKEN_PATH=Z:\dist\fabric\Kraken
::set KRAKEN_PATH=V:\oculusstorystudio\Kraken

echo %KRAKEN_PATH%
echo on

set THIRD_PARTY=Z:\dist\fabric\ThirdParty

set KRAKEN_PATHS=%KRAKEN_PATH%\Python\OSS

set FABRIC_EXTS_PATH=.;%KRAKEN_PATH%\Exts;%THIRD_PARTY%;%FABRIC_DIR%\Exts;%FABRIC_EXTS_PATH%

set FABRIC_DFG_PATH=%KRAKEN_PATH%\Presets\DFG;%KRAKEN_PATH%\Presets;%FABRIC_DIR%\Presets\DFG;%FABRIC_DFG_PATH%

set PYTHONPATH=%FABRIC_DIR%\Python\2.7;%KRAKEN_PATH%\Python;%PYTHONPATH%;

::PAUSE