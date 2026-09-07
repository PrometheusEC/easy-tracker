@echo off
setlocal
title Easy Tracker - PySide6
cd /d "%~dp0"

set "PYTHON_CMD="
where py >nul 2>nul
if not errorlevel 1 set "PYTHON_CMD=py"

if not defined PYTHON_CMD (
    where python >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    echo ERROR: Python was not found.
    echo.
    echo Install Python 3 from:
    echo https://www.python.org/downloads/windows/
    echo.
    pause
    exit /b 1
)

echo Checking PySide6...
%PYTHON_CMD% -c "import PySide6" >nul 2>nul

if errorlevel 1 (
    echo PySide6 is not installed.
    echo Installing PySide6...
    echo.
    %PYTHON_CMD% -m pip install PySide6
    if errorlevel 1 (
        echo.
        echo ERROR: PySide6 could not be installed.
        echo.
        pause
        exit /b 1
    )
)

echo Starting Easy Tracker...
echo.

%PYTHON_CMD% easy_tracker.py 2> error_log.txt
set "APP_EXIT=%ERRORLEVEL%"

if "%APP_EXIT%"=="0" (
    if exist error_log.txt del /q error_log.txt
    exit /b 0
)

echo.
echo ==========================================
echo THE TRACKER COULD NOT START
echo ==========================================
echo.
type error_log.txt
echo.
pause
exit /b %APP_EXIT%
