set FABRIC_LOG_LEVEL=3

set FABRIC_PATH=Z:\dist\fabric\releases\FabricEngine-2.3.0-auto-2016052610-Windows-x86_64

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
    set KRAKEN_PATH=%LOCAL_KRAKEN_PATH%
)
echo KRAKEN_PATH = %KRAKEN_PATH%
echo on

set THIRD_PARTY=Z:\dist\fabric\ThirdParty

set KRAKEN_PATHS=%KRAKEN_PATH%\Python\OSS

set PATH=%FABRIC_PATH%\bin;%PATH%

set FABRIC_EXTS_PATH=%FABRIC_PATH%\Exts;%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;%KRAKEN_PATH%\Samples\OSS\klChar;%THIRD_PARTY%

set FABRIC_DFG_PATH=%KRAKEN_PATH%\Presets\DFG;%KRAKEN_PATH%\Presets;%FABRIC_PATH%\Presets\DFG;

set PYTHONPATH=%PYTHONPATH%;%FABRIC_PATH%\Python\2.7;%KRAKEN_PATH%\Python

cd /d %KRAKEN_PATH%

if "%USER%" == "bhx" (
    call cmd /k "%FABRIC_PATH%/bin/canvas"
)
else (
    call cmd /k "python "%FABRIC_PATH%"/bin/canvas.py"
)

