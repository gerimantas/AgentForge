# Scripts Directory

Šiame aplanke yra visi automatizavimo skriptai AgentForge projektui.

## Aplankų struktūra:

### `setup/` - Aplinkos paruošimo skriptai
- **activate.bat** - Paprastas venv aktyvavimas
- **activate_venv.bat** - Išsamus venv aktyvavimas
- **auto_venv.bat** - Automatinis venv aktyvavimas
- **auto_venv.ps1** - PowerShell automatinis venv aktyvavimas  
- **setup_env.bat** - Pilnas aplinkos paruošimas (CMD)
- **setup_env.ps1** - Pilnas aplinkos paruošimas (PowerShell)
- **start.bat** - Pagrindinis projekto paleidimo skriptas

### `maintenance/` - Palaikymo skriptai
- **update_repo.py** - Git repository atnaujinimas
- **run_curation.py** - Žinių bazės kuracija
- **run_project_analysis.bat** - Projekto struktūros analizė

## Naudojimas:

### Pirmasis paleidimas:
```cmd
scripts\setup\setup_env.bat
```

### Kasdienis naudojimas:
```cmd
scripts\setup\start.bat
```

### Projekto palaikymas:
```cmd
scripts\maintenance\update_repo.py "commit message"
```
