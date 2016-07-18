set FABRIC_kyle_DIR=%~dp0

set FABRIC_LOG_LEVEL=0

set FABRIC_DIR=Z:\dist\fabric\releases\FabricEngine-2.3.0-auto-2016052610-Windows-x86_64

set PATH=%FABRIC_DIR%\bin;%PATH%

set KRAKEN_PATH=Z:\dist\fabric\Kraken
:: Set the kraken path based on where this script lives
:: We really need to have a proper environment setup eventually -TT
@setlocal enableextensions enabledelayedexpansion
@echo off
set cwd=%~dp0
set delim=fabric\kraken
set splitsub=@
call set tempstring=!cwd:%delim%=%splitsub%!
for /f "tokens=1* delims=%splitsub%" %%A in ("%tempstring%") do set part1=%%A& set part2=%%B
set LOCAL_KRAKEN_PATH=%part1%fabric\kraken
if not x%cwd:fabric\kraken=%==x%cwd% (
    echo *** setting KRAKEN_PATH = %LOCAL_KRAKEN_PATH%
    set KRAKEN_PATH=%LOCAL_KRAKEN_PATH%
)
@endlocal & SET KRAKEN_PATH=%KRAKEN_PATH%
echo on

set THIRD_PARTY=Z:\dist\fabric\ThirdParty

set KRAKEN_PATHS=%KRAKEN_PATH%\Python\OSS

set FABRIC_EXTS_PATH=%FABRIC_kyle_DIR%;%KRAKEN_PATH%\Samples\OSS;%KRAKEN_PATH%\Exts;%THIRD_PARTY%;%FABRIC_DIR%\Exts;%FABRIC_EXTS_PATH%

set FABRIC_DFG_PATH=%FABRIC_kyle_DIR%;%KRAKEN_PATH%\Presets\DFG;%KRAKEN_PATH%\Presets;%FABRIC_DIR%\Presets\DFG;%FABRIC_DFG_PATH%

set PYTHONPATH=%FABRIC_DIR%\Python\2.7;%KRAKEN_PATH%\Python;%PYTHONPATH%;

