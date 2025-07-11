@echo off
cd /d "c:\ai_projects\AgentForge"
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated!
echo Current directory: %cd%
echo Python version:
python --version
echo Installing dependencies...
pip install -r requirements.txt
echo Dependencies installed!
echo.
echo To run AgentForge:
echo python main.py
echo.
echo To deactivate virtual environment, type: deactivate
cmd /k
