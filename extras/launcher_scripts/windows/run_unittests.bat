@ECHO OFF

REM
REM Kraken unit test environment and execution.
REM Place this in the /unittest folder and 
REM change path to Fabric directory.
REM

SET "FABRIC_DIR=C:\Users\USERNAME\Documents\fabric\FabricEngine-2.4.0-Windows-x86_64"
REM Remove trailing backslash if there is one
IF %FABRIC_DIR:~-1%==\ SET "FABRIC_DIR=%FABRIC_DIR:~0,-1%"

SET "KRAKEN_PATH=%~dp0.."

SET "_OLD_PYTHON_VERSION=%PYTHON_VERSION%"
SET "PYTHON_VERSION=2.7"
SET "PATH=%FABRIC_DIR%\bin;%FABRIC_DIR%\Python\%PYTHON_VERSION%;%PATH%"
SET "PYTHONPATH=%FABRIC_DIR%\Python\%PYTHON_VERSION%;%KRAKEN_PATH%\Python;%PYTHONPATH%"
SET "PYTHON_VERSION=%_OLD_PYTHON_VERSION%"

SET "FABRIC_EXTS_PATH=%FABRIC_DIR%\Exts;%KRAKEN_PATH%\Exts"
SET "FABRIC_DFG_PATH=%FABRIC_DIR%\Presets\DFG;%KRAKEN_PATH%\Presets\DFG"

call python -m unittest discover

call cmd
