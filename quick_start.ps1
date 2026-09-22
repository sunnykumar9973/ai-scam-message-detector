# Quick Start Script for Smart Scam Detector - PowerShell Version
# Run from project root directory

Write-Host "
===============================================
Smart Scam Message Detector - Quick Start
===============================================
" -ForegroundColor Cyan

# Check Python
try {
    python --version | Out-Null
} catch {
    Write-Host "ERROR: Python not found. Install from https://www.python.org/" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Python found" -ForegroundColor Green

# Check Node
try {
    node --version | Out-Null
} catch {
    Write-Host "ERROR: Node.js not found. Install from https://nodejs.org/" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Node.js found" -ForegroundColor Green
Write-Host ""

# Step 1: Setup backend if first time
if (-not (Test-Path "model\scam_detector_model.pkl")) {
    Write-Host "[1/4] Training ML Model..." -ForegroundColor Yellow
    
    # Create venv if not exists
    if (-not (Test-Path "backend\venv")) {
        Write-Host "      Creating virtual environment..."
        cd backend
        python -m venv venv
        cd ..
    }
    
    # Install dependencies
    Write-Host "      Installing Python dependencies..."
    cd backend
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt | Out-Null
    cd ..
    
    # Download dataset and train
    Write-Host "      Downloading dataset..."
    cd dataset
    python download_dataset.py
    Write-Host "      Training model..."
    python train_model.py
    cd ..
    Write-Host ""
}

Write-Host "[2/4] Starting Backend Server..." -ForegroundColor Yellow
Write-Host "      Opening in new window (keep it running!)" -ForegroundColor Gray
Start-Process powershell -ArgumentList "-NoExit -Command `"cd backend; .\venv\Scripts\Activate.ps1; python app.py`""
Start-Sleep -Seconds 3

Write-Host ""
Write-Host "[3/4] Starting Frontend Server..." -ForegroundColor Yellow
Write-Host "      Opening in new window (keep it running!)" -ForegroundColor Gray
Start-Process powershell -ArgumentList "-NoExit -Command `"cd frontend; npm install; npm run dev`""
Start-Sleep -Seconds 3

Write-Host ""
Write-Host "[4/4] Opening browser..." -ForegroundColor Yellow
Start-Sleep -Seconds 2
Start-Process "http://localhost:5173/"

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "✓ Application started!" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Frontend: http://localhost:5173/" -ForegroundColor Green
Write-Host "Backend:  http://localhost:5000/" -ForegroundColor Green
Write-Host ""
Write-Host "Keep both terminal windows running!" -ForegroundColor Yellow
Write-Host ""
