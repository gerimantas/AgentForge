@echo off
REM AgentForge projekto struktūros analizės skriptas
REM Windows batch failas

echo =================================================
echo      AgentForge Projekto Struktūros Analizė
echo =================================================
echo.

REM Tikrinimas ar esame teisigoje vietoje
if not exist "main.py" (
    echo KLAIDA: Šis skriptas turi būti paleidžiamas iš AgentForge root katalogo
    echo Dabartinis katalogas: %CD%
    echo.
    pause
    exit /b 1
)

REM Sukurti tools/migration katalogą jei jo nėra
if not exist "tools\migration" (
    echo Kuriamas tools\migration katalogas...
    mkdir "tools\migration"
)

REM Pereiti į tools/migration katalogą ir paleisti skriptą
echo Paleidžiama projekto struktūros analizė...
echo.

cd tools\migration
python run_scanner.py

if %ERRORLEVEL% equ 0 (
    echo.
    echo ===== ANALIZĖ BAIGTA SĖKMINGAI =====
    echo.
    echo Ataskaita išsaugota: tools\migration\reports\
    echo.
    echo Tolimesni žingsniai:
    echo 1. Peržiūrėkite sukurtą ataskaitos failą
    echo 2. Patvirtinkite migracijos žemėlapį development_plan.md
    echo 3. Pradėkite Phase 0 migracijos
    echo.
) else (
    echo.
    echo ===== KLAIDA VYKDANT ANALIZĘ =====
    echo.
    echo Patikrinkite Python aplinką ir dependencies
)

echo.
pause
cd ..\..
