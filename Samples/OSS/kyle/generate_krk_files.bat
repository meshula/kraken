call kyle_environment.bat

cd /d %KRAKEN_PATH%

cmd /k python %KRAKEN_PATH%\DCCIntegrations\kl\presetGen.py %KRAKEN_PATH%\Samples\OSS\kyle\kyle_rig.krg %KRAKEN_PATH%\Samples\OSS\kyle\Exts\ -c %KRAKEN_PATH%\Python\OSS\OSS_kraken_config.py --profiling 1000 

::PAUSE