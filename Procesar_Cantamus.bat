@echo off
chcp 65001 > nul
setlocal
set PYTHONIOENCODING=utf-8
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    set "PY_CMD=.venv\Scripts\python.exe"
) else if exist "venv\Scripts\python.exe" (
    set "PY_CMD=venv\Scripts\python.exe"
) else (
    set "PY_CMD=python"
)

%PY_CMD% scripts\procesar_cantamus_one_shot.py %*
if errorlevel 1 (
    echo.
    echo Ocurrio un problema durante el procesamiento.
    pause
) else (
    ping 127.0.0.1 -n 3 > nul
)
