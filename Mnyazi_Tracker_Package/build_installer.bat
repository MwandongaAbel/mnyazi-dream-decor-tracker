@echo off
REM Build script for Mnyazi Dream Decor Event Tracker
REM Run this on a Windows machine with Python installed.
pip install -r requirements.txt
REM Create a one-file windowed executable with icon (optional)
REM Place icon.ico in assets/ if you have a .ico file. Otherwise PyInstaller will use default.
pyinstaller --noconfirm --onefile --windowed --add-data "assets;assets" main.py
echo Build complete. Check the "dist" folder for main.exe
pause