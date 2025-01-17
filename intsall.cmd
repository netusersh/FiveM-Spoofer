@echo off
title Spoofer Setup
cls

:start
set /p choice="Do you have Python installed? [Y/N]: "
set choice=%choice:~0,1%
set choice=%choice:~0,1%
if /i "%choice%"=="Y" goto :finish
if /i "%choice%"=="N" goto :install_python

echo Invalid choice. Please type Y or N.
timeout 3 >nul
cls
goto :start

:install_python
cls
echo Opening the Python installer download page...
start https://www.python.org/ftp/python/3.13.1/python-3.13.1-amd64.exe
echo.
echo Once the installation is complete:
echo 1. Ensure Python is added to PATH during the setup process.
echo 2. Close this window and restart the script to proceed.
timeout 10 >nul
goto :finish
color 7
exit

:finish
echo This script doesnt need modules to install.
echo Starting Script...
timeout 3>nul
py spoofer.py
