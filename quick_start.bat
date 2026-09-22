@echo off
REM Quick Start Script for Smart Scam Detector
REM Windows PowerShell version

echo.
echo ===============================================
echo Smart Scam Message Detector - Quick Start
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if Node is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 16+ from https://nodejs.org/
    pause
    exit /b 1
)

echo ✓ Python and Node.js found
echo.

REM Step 1: Train model if not exists
if not exist "model\scam_detector_model.pkl" (
    echo [1/4] Training ML model...
    cd dataset
    python download_dataset.py
    python train_model.py
    cd ..
    echo.
)

REM Step 2: Start backend in a new window
echo [2/4] Starting Backend Server...
start cmd /k "cd backend && venv\Scripts\activate.bat && python app.py"
timeout /t 3 /nobreak
echo.

REM Step 3: Start frontend in a new window
echo [3/4] Starting Frontend Server...
start cmd /k "cd frontend && npm install && npm run dev"
timeout /t 3 /nobreak
echo.

REM Step 4: Open in browser
echo [4/4] Opening application in browser...
timeout /t 3 /nobreak
start http://localhost:5173/

echo.
echo ===============================================
echo ✓ Application started!
echo ===============================================
echo.
echo Frontend: http://localhost:5173/
echo Backend:  http://localhost:5000/
echo.
echo Keep both command windows running!
echo.
pause
