@echo off
REM Auto-startup script for AgentForge venv
REM Šis failas automatiškai aktyvuojamas kaip VS Code terminal profile

echo Loading AgentForge environment...
cd /d "c:\ai_projects\AgentForge"

REM Tikrinti ar venv egzistuoja
if not exist venv (
    echo Virtual environment not found. Creating...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo ERROR: Failed to create virtual environment
        echo Please check if Python is installed
        exit /b 1
    )
)

REM Aktyvuoti venv
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 (
    echo ERROR: Failed to activate virtual environment
    exit /b 1
)

REM Pasisveikinimo žinutė
echo.
echo =====================================
echo  AgentForge Environment Ready! 
echo =====================================
echo Virtual environment: ACTIVE
echo Python version: 
python --version
echo.
echo Available commands:
echo   python main.py     - Run AgentForge
echo   pip install -r requirements.txt - Install dependencies
echo   deactivate        - Exit venv
echo.
