# AgentForge Projekto Failus Struktūros Analizės Template

## Naudojimas

### 1. Paleidimas per Python:
```bash
cd tools/migration
python run_scanner.py
```

### 2. Paleidimas per batch failą (Windows):
```bash
# Iš AgentForge root katalogo
run_project_analysis.bat
```

### 3. Paleidimas tiesiogiai:
```bash
cd AgentForge
python -m tools.migration.run_scanner
```

## Kas sukuriama:

### Ataskaitos failas:
- **Vieta:** `tools/migration/reports/project_structure_analysis_YYYYMMDD_HHMMSS.txt`
- **Turinys:**
  - Dabartinė failų struktūra (medžio formatu)
  - Python failų analizė (eilutės, klasės, funkcijos, import'ai)
  - Migracijos žemėlapis (dabartinis → naujas)
  - Statistika

### Migracijos žemėlapis:
```
Dabartinis failas → Nauja vieta:
📦 config.py → agentforge/core/config.py
📦 agents.py → agentforge/agents/__init__.py
📦 categories.py → agentforge/categories/manager.py
...
```

## Naujos struktūros katalogas:

### Siūlomas naujas katalogas `agentforge/`:

```
agentforge/                    # Pagrindinis package (NAUJAS)
├── core/                      # Baziniai komponentai (NAUJAS)
│   ├── config.py             # <- iš config.py
│   ├── exceptions.py         # (NAUJAS)
│   └── base_classes.py       # (NAUJAS)
├── agents/                   # Agentų sistema (NAUJAS)
│   ├── __init__.py          # <- iš agents.py
│   ├── skills.py            # <- iš agent_skills.py
│   └── dynamic_selection.py # <- iš dynamic_agents.py
├── categories/              # Kategorijų sistema (NAUJAS)
│   ├── manager.py           # <- iš categories.py
│   └── classifier.py        # <- iš category_classifier.py
├── workflows/               # Darbo ciklai (NAUJAS)
│   ├── maintenance.py       # <- iš maintenance_cycle.py
│   ├── execution.py         # <- iš execution_cycle.py
│   └── tasks/               # (NAUJAS)
│       ├── maintenance_tasks.py # <- iš tasks_maintenance.py
│       └── execution_tasks.py   # <- iš tasks_execution.py
├── templates/               # Šablonų sistema (NAUJAS)
│   └── manager.py           # <- iš prompt_templates.py
├── analysis/                # Analizės moduliai (NAUJAS)
│   └── metrics.py           # <- iš prompt_metrics.py
├── ui/                      # Vartotojo sąsaja (NAUJAS)
│   └── cli/                 # (NAUJAS)
│       └── main_menu.py     # <- iš main.py (dalis)
└── utils/                   # Pagalbiniai įrankiai (NAUJAS)
    └── file_operations.py   # <- iš custom_tools.py
```

### Siūlomas naujas katalogas `data/`:

```
data/                        # Duomenų failai (NAUJAS)
├── config/                  # Konfigūracijos (NAUJAS)
│   ├── categories.yaml      # <- iš categories.yaml
│   └── agent_skills.yaml    # <- iš agent_skills.yaml
├── knowledge_base/          # Žinių bazė (NAUJAS)
│   ├── ziniu_baze.yaml      # <- iš ziniu_baze.yaml
│   ├── kanonine_sistema.yaml # <- iš kanonine_sistema.yaml
│   └── source_registry.yaml # <- iš source_registry.yaml
├── templates/               # Šablonų failai (NAUJAS)
│   ├── information_retrieval/
│   ├── creative_content/
│   ├── analysis/
│   └── development/
└── results/                 # Rezultatai (NAUJAS)
    ├── comparisons/
    ├── metrics/
    └── exports/
```

### Siūlomas naujas katalogas `tests/`:

```
tests/                       # Testų sistema (REORGANIZUOTA)
├── unit/                    # Unit testai (NAUJAS)
│   ├── test_agents/
│   ├── test_categories/
│   └── test_workflows/
├── integration/             # Integraciniai testai (NAUJAS)
│   └── test_full_workflow.py # <- iš test_system.py
└── fixtures/                # Testų duomenys (NAUJAS)
    └── sample_data.py
```

## Migracijos procesas:

1. **Phase 0:** Pasiruošimas (automatizacijos įrankiai)
2. **Phase 1:** Core infrastruktūra
3. **Phase 2:** Agentų sistema
4. **Phase 3:** Kategorijų sistema
5. **Phase 4:** Workflows
6. **Phase 5:** Templates & Analysis
7. **Phase 6:** Tests
8. **Phase 7:** UI & Finalization

## Privalumai naujos struktūros:

### ✅ Profesionalumas:
- Atitinka Python packaging standartus
- Aiški modulinė architekatūra
- Separation of concerns

### ✅ Palaikymas:
- Lengvas naujų funkcijų pridėjimas
- Aiški navigacija
- Testų organizacija

### ✅ Skalability:
- Package struktūra leidžia augti
- Aiški priklausomybių grandinė
- Import'ų optimizacija

## Po migracijos:

### Entry points:
```bash
# Vietoj:
python main.py

# Bus:
python main.py  # (naujas wrapper)
# arba
python -m agentforge
```

### Import'ai:
```python
# Vietoj:
from agents import prompt_analyst
from categories import load_categories

# Bus:
from agentforge.agents import prompt_analyst
from agentforge.categories.manager import load_categories
```

### Konfigūracija:
```python
# Vietoj:
import config

# Bus:
from agentforge.core import config
```
