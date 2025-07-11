@echo off
REM AgentForge virtualios aplinkos aktyvavimo scriptas
REM Šis failas sukurs, aktyvuos venv ir paruoš darbo aplinką

echo.
echo ================================================
echo   AgentForge Virtual Environment Setup
echo ================================================
echo.

REM Pereiti į projekto katalogą
cd /d "c:\ai_projects\AgentForge"

REM Tikrinti ar venv egzistuoja
if not exist venv (
    echo [1/4] Kuriama virtuali aplinka...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo KLAIDA: Nepavyko sukurti virtualios aplinkos
        echo Patikrinkite ar Python yra įdiegtas
        pause
        exit /b 1
    )
    echo ✓ Virtuali aplinka sukurta
) else (
    echo [1/4] Virtuali aplinka jau egzistuoja ✓
)

REM Aktyvuoti venv
echo [2/4] Aktyvuojama virtuali aplinka...
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo KLAIDA: Nepavyko aktyvuoti virtualios aplinkos
    pause
    exit /b 1
)
echo ✓ Virtuali aplinka aktyvuota

REM Patikrinti Python versiją
echo [3/4] Python versija:
python --version

REM Instaliuoti priklausomybes
echo [4/4] Instaliuojamos priklausomybės...
pip install -r requirements.txt --quiet --disable-pip-version-check
if %ERRORLEVEL% neq 0 (
    echo KLAIDA: Nepavyko instaliuoti priklausomybių
    pause
    exit /b 1
)
echo ✓ Priklausomybės instaliuotos

echo.
echo ================================================
echo   Setup baigtas sėkmingai!
echo ================================================
echo.
echo Galite naudoti šias komandas:
echo   python main.py          - Paleisti AgentForge
echo   python -m pytest tests/ - Paleisti testus
echo   deactivate              - Išjungti venv
echo.
echo VS Code: Atidaryti terminale ir venv bus aktyvuotas automatiškai
echo.

REM Palikti terminalą atvirą su aktyvuotu venv
cmd /k
