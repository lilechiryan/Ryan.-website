@echo off
REM BK BOND MASTERS CONSTRUCTION LTD - Flask Application Launcher

echo.
echo ========================================
echo BK BOND MASTERS CONSTRUCTION LTD
echo Flask Web Application
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask application...
echo.
echo The website will be available at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
