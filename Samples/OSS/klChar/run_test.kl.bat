set FABRIC_LOG_LEVEL=4

set FABRIC_PATH=Z:\dist\fabric\releases\FabricEngine-2.3.0-auto-2016052610-Windows-x86_64

set KRAKEN_PATH=Z:\dist\fabric\Kraken

set THIRD_PARTY=:\dist\fabric\ThirdParty

set KRAKEN_PATHS=%KRAKEN_PATH%\Python\OSS

set PATH=%FABRIC_PATH%\bin;%PATH%

set FABRIC_EXTS_PATH=%FABRIC_PATH%\Exts;%FABRIC_EXTS_PATH%;%KRAKEN_PATH%\Exts;%KRAKEN_PATH%\Samples\OSS\klChar;%THIRD_PARTY%

set FABRIC_DFG_PATH=%KRAKEN_PATH%\Presets\DFG;%KRAKEN_PATH%\Presets;%FABRIC_PATH%\Presets\DFG;

set PYTHONPATH=%PYTHONPATH%;%FABRIC_PATH%\Python\2.7;%KRAKEN_PATH%\Python

cd /d %KRAKEN_PATH%

start /WAIT  kl.exe "%KRAKEN_PATH%"/Samples/OSS/klChar/test.kl"