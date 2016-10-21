call environment.bat

set FABRIC_LOG_LEVEL=3

cd /d %FABRIC_CHARNAME_DIR%

cmd /k kl.exe %FABRIC_CHARNAME_DIR%/test.kl --opt --unguarded > test_results.txt
