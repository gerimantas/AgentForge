@echo off
echo.
echo ==========================================
echo   AgentForge Development Environment
echo ==========================================
echo.

REM Ensure we're in the right directory
cd /d "%~dp0"

REM Check if venv exists
if not exist "venv\Scripts\python.exe" (
    echo Virtual environment not found. Please run setup_env.bat first.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Clear screen and show status
cls
echo.
echo ==========================================
echo   AgentForge - Ready to Use!
echo ==========================================
echo.
echo Virtual Environment: ACTIVE
echo Python Version: 
python --version
echo.
echo Available Commands:
echo   python main.py                 - Run AgentForge
echo   python -m pytest tests/        - Run Tests  
echo   pip install -r requirements.txt - Install Dependencies
echo   deactivate                     - Exit Virtual Environment
echo.
echo ==========================================
echo.
