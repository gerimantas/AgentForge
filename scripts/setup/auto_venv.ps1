# Auto-startup script for AgentForge venv
# PowerShell versija

Write-Host "Loading AgentForge environment..." -ForegroundColor Yellow
Set-Location "c:\ai_projects\AgentForge"

# Tikrinti ar venv egzistuoja
if (!(Test-Path "venv")) {
    Write-Host "Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to create virtual environment" -ForegroundColor Red
        Write-Host "Please check if Python is installed" -ForegroundColor Red
        exit 1
    }
}

# Aktyvuoti venv
try {
    & "venv\Scripts\Activate.ps1"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to activate virtual environment" -ForegroundColor Red
        Write-Host "You may need to change PowerShell execution policy:" -ForegroundColor Yellow
        Write-Host "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
        exit 1
    }
} catch {
    Write-Host "ERROR: PowerShell execution policy may be restricting script execution" -ForegroundColor Red
    Write-Host "Run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
    exit 1
}

# Pasisveikinimo žinutė
Write-Host ""
Write-Host "=====================================" -ForegroundColor Green
Write-Host "  AgentForge Environment Ready!" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green
Write-Host "Virtual environment: " -NoNewline -ForegroundColor White
Write-Host "ACTIVE" -ForegroundColor Green
Write-Host "Python version: " -NoNewline -ForegroundColor White
python --version
Write-Host ""
Write-Host "Available commands:" -ForegroundColor Cyan
Write-Host "  python main.py     - Run AgentForge" -ForegroundColor White
Write-Host "  pip install -r requirements.txt - Install dependencies" -ForegroundColor White
Write-Host "  deactivate        - Exit venv" -ForegroundColor White
Write-Host ""
