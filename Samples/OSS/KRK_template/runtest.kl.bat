call environment.bat

set FABRIC_LOG_LEVEL=3

kl.exe test.kl --opt --unguarded > test_results.txt

echo results in %~dp0\test_results.txt
@ECHO OFF
PAUSE
