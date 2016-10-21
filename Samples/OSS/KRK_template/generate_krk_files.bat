call environment.bat

cd /d %KRAKEN_PATH%

cmd /k python %KRAKEN_PATH%\DCCIntegrations\kl\presetGen.py %FABRIC_CHARNAME_DIR%\CHARNAME_rig.krg %FABRIC_CHARNAME_DIR% -c %KRAKEN_PATH%\Python\OSS\OSS_kraken_config.py --profiling 1000

::PAUSE