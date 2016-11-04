call environment.bat

cd /d %KRAKEN_PATH%

cmd /k python %KRAKEN_PATH%\DCCIntegrations\kl\presetGen.py .\kyle_rig.krg . -c %KRAKEN_PATH%\Python\OSS\OSS_kraken_config.py --profiling 1000

::PAUSE