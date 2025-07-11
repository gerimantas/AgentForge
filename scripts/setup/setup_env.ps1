# AgentForge Environment Setup Script
# PowerShell versija

Write-Host "================================================" -ForegroundColor Green
Write-Host "   AgentForge Virtual Environment Setup" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green

# Pereiti į projekto katalogą
Set-Location "c:\ai_projects\AgentForge"

# Tikrinti ar venv egzistuoja
if (!(Test-Path "venv")) {
    Write-Host "[1/4] Kuriama virtuali aplinka..." -ForegroundColor Yellow
    python -m venv venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "KLAIDA: Nepavyko sukurti virtualios aplinkos" -ForegroundColor Red
        Write-Host "Patikrinkite ar Python yra įdiegtas" -ForegroundColor Red
        Read-Host "Paspauskite Enter kad tęsti..."
        exit 1
    }
    Write-Host "✓ Virtuali aplinka sukurta" -ForegroundColor Green
} else {
    Write-Host "[1/4] Virtuali aplinka jau egzistuoja ✓" -ForegroundColor Green
}

# Aktyvuoti venv
Write-Host "[2/4] Aktyvuojama virtuali aplinka..." -ForegroundColor Yellow
& "venv\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "KLAIDA: Nepavyko aktyvuoti virtualios aplinkos" -ForegroundColor Red
    Write-Host "Gali reikėti pakeisti PowerShell execution policy:" -ForegroundColor Yellow
    Write-Host "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Yellow
    Read-Host "Paspauskite Enter kad tęsti..."
    exit 1
}
Write-Host "✓ Virtuali aplinka aktyvuota" -ForegroundColor Green

# Patikrinti Python versiją
Write-Host "[3/4] Python versija:" -ForegroundColor Yellow
python --version

# Instaliuoti priklausomybes
Write-Host "[4/4] Instaliuojamos priklausomybės..." -ForegroundColor Yellow
pip install -r requirements.txt --quiet --disable-pip-version-check
if ($LASTEXITCODE -ne 0) {
    Write-Host "KLAIDA: Nepavyko instaliuoti priklausomybių" -ForegroundColor Red
    Read-Host "Paspauskite Enter kad tęsti..."
    exit 1
}
Write-Host "✓ Priklausomybės instaliuotos" -ForegroundColor Green

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "   Setup baigtas sėkmingai!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Galite naudoti šias komandas:" -ForegroundColor Cyan
Write-Host "  python main.py          - Paleisti AgentForge" -ForegroundColor White
Write-Host "  python -m pytest tests/ - Paleisti testus" -ForegroundColor White
Write-Host "  deactivate              - Išjungti venv" -ForegroundColor White
Write-Host ""
Write-Host "VS Code: Atidaryti terminale ir venv bus aktyvuotas automatiškai" -ForegroundColor Yellow
Write-Host ""

# Palikti PowerShell sesiją aktyvią
Write-Host "PowerShell sesija su aktyvuotu venv. Įveskite 'exit' kad išeiti." -ForegroundColor Gray
