@echo off
REM Simple venv activator for VS Code
cd /d "%~dp0"
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo AgentForge venv activated ✓
) else (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo AgentForge venv created and activated ✓
)
