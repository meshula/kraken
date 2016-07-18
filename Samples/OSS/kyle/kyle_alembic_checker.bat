call kyle_environment.bat

set FABRIC_LOG_LEVEL=3
set FABRIC_DIR=Z:\dist\fabric\releases\FabricEngine-2.2.0-Windows-x86_64
python %FABRIC_DIR%/bin/canvas.py "%FABRIC_kyle_DIR%/kyle_alembic_checker.canvas"

::PAUSE
