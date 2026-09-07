@echo off
setlocal
title Build Easy Tracker EXE
cd /d "%~dp0"

echo ==========================================
echo   EASY TRACKER - EXE BUILDER
echo ==========================================
echo.

set "PYTHON_CMD="
where py >nul 2>nul
if not errorlevel 1 set "PYTHON_CMD=py"

if not defined PYTHON_CMD (
    where python >nul 2>nul
    if not errorlevel 1 set "PYTHON_CMD=python"
)

if not defined PYTHON_CMD (
    echo ERROR: Python was not found.
    echo Install Python 3 from:
    echo https://www.python.org/downloads/windows/
    pause
    exit /b 1
)

echo Using: %PYTHON_CMD%
echo.
echo Installing/updating PySide6 and PyInstaller...
%PYTHON_CMD% -m pip install --upgrade PySide6 PyInstaller
if errorlevel 1 (
    echo.
    echo ERROR: Dependency installation failed.
    pause
    exit /b 1
)

echo.
echo Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist "Easy Tracker.spec" del /q "Easy Tracker.spec"

set "ICON_ARG="
if exist app_icon.ico (
    echo Found app_icon.ico - embedding icon.
    set "ICON_ARG=--icon=app_icon.ico"
) else (
    echo No app_icon.ico found - using default icon.
)

echo.
echo Building executable...
%PYTHON_CMD% -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "Easy Tracker" ^
    %ICON_ARG% ^
    easy_tracker.py

if errorlevel 1 (
    echo.
    echo BUILD FAILED.
    pause
    exit /b 1
)

if exist job_applications.csv copy /Y job_applications.csv "dist\job_applications.csv" >nul
if exist tracker_settings.txt copy /Y tracker_settings.txt "dist\tracker_settings.txt" >nul
if exist app_icon.ico copy /Y app_icon.ico "dist\app_icon.ico" >nul

echo.
echo ==========================================
echo BUILD COMPLETE
echo ==========================================
echo.
echo Your app is here:
echo   dist\Easy Tracker.exe
echo.
echo Keep job_applications.csv beside the EXE.
echo.
explorer "dist"
pause
