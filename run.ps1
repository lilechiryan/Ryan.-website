# BK BOND MASTERS CONSTRUCTION LTD - Flask Application Launcher (PowerShell)

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "BK BOND MASTERS CONSTRUCTION LTD" -ForegroundColor Cyan
Write-Host "Flask Web Application" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.7 or higher from https://www.python.org" -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "Starting Flask application..." -ForegroundColor Green
Write-Host ""
Write-Host "Website URL: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Homepage: http://localhost:5000/" -ForegroundColor Cyan
Write-Host "Projects: http://localhost:5000/projects" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

python app.py
