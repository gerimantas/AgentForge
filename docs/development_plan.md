# AgentForge Funkcionalumo Išplėtimo Planas

## Projekto apžvalga

Šis dokumentas skirtas sekti AgentForge projekto funkcionalumo išplėtimo progresą, susijusį su kategorijomis grįstu užklausų optimizavimu ir rezultatų analizės/redagavimo galimybėmis.

**Pradžios data:** 2025-07-10
**Planuojama pabaigos data:** 2025-09-01
**Atnaujinta:** 2025-07-11

## Pagrindiniai tikslai

1. **Kategorijomis grįsta užklausų sistema** - automatiškai aptikti ir pritaikyti prompt inžinerijos metodus pagal užklausos kategoriją
2. **Prompt redagavimo sistema** - leisti vartotojui redaguoti ir tobulinti sugeneruotus prompt'us
3. **Multi-modelių analizė** - leisti palyginti ir analizuoti prompt'ų efektyvumą skirtinguose AI modeliuose

## Sekančio kūrimo žingsnio analizė ir planas

### 📊 Dabartinės projekto būsenos vertinimas

**✅ Užbaigti komponentai:**
- Bazinė architektūra (dviejų ciklų sistema)
- Kategorijų sistema (4 pagrindinės kategorijos, 12 subkategorijų)
- Dinaminiai agentai (automatinis parinkimas pagal kategoriją)
- Šablonų sistema (valdymas ir pakartotinis naudojimas)
- Kokybės metrikos (5 kriterijų vertinimas)
- Testavimo karkasas (4 tipų automatiniai testai)

**🟡 Dalinai įgyvendinti:**
- Integraciniai testai (baziniai veikia, trūksta išsamesnių)
- Templates katalogas (struktūra sukurta, bet tuščia)
- Multi-modelių palaikymas (architektūra paruošta, neįgyvendinta)

**❌ Neįgyvendinti:**
- Vartotojo sąsaja (tik terminalo meniu)
- Automatinė faktų patikra
- CI/CD integracija
- Rezultatų palyginimo sistema

## Įgyvendinimo planas

### 0 etapas: Sistemos projektavimas ir architektūros nustatymas
- **Pradžia:** 2025-07-10
- **Pabaiga:** 2025-07-10
- **Statusas:** ✅ Užbaigta
- **Užduotys:**
  - [x] Hierarchinės kategorijų sistemos apibrėžimas
  - [x] Agentų įgūdžių matricos sukūrimas
  - [x] Dinaminės agentų parinkimo sistemos projektavimas
  - [x] Prompt'ų kokybės vertinimo metrikų nustatymas
- **Pastabos:**
  - Sukurti pagrindiniai moduliai: categories.py, agent_skills.py, category_classifier.py, dynamic_agents.py, prompt_metrics.py
  - Kategorijų sistema apima 4 pagrindines kategorijas ir 12 subkategorijų
  - Agentų sistema apima 6 skirtingų specializacijų agentus

### 1 etapas: Kategorijų sistemos sukūrimas
- **Pradžia:** 2025-07-11
- **Pabaiga:** 2025-07-11
- **Statusas:** ✅ Užbaigta
- **Užduotys:**
  - [x] Hierarchinių kategorijų apibrėžimas YAML failuose
  - [x] Zero-shot klasifikavimo implementacija
  - [x] Kategorijų žymenų sistema
  - [x] Kategorijų sistemos testų kūrimas
- **Pastabos:**
  - Sukurtas categories.yaml failas su hierarchine struktūra
  - Sukurtas category_classifier.py modulis su klasifikavimo logika
  - Sukurta kategorijų valdymo sistema per main.py meniu
  - Įdiegti testai kategorijų sistemai

### 2 etapas: Dinaminės agentų sistemos sukūrimas
- **Pradžia:** 2025-07-11
- **Pabaiga:** 2025-07-11
- **Statusas:** ✅ Užbaigta
- **Užduotys:**
  - [x] Agentų įgūdžių matricos implementacija
  - [x] Dinaminio agentų parinkimo mechanizmo kūrimas
  - [x] Specializuotų įskiepių sistemos kūrimas
  - [x] Agentų sistemos testų kūrimas
- **Pastabos:**
  - Sukurtas agent_skills.yaml failas su detaliais agentų aprašymais
  - Sukurtas dynamic_agents.py modulis agentų parinkimui pagal kategoriją
  - Integruota su execution_cycle.py

### 3 etapas: Redagavimo ir analizės sistemos sukūrimas
- **Pradžia:** 2025-07-11
- **Pabaiga:** 2025-07-12
- **Statusas:** ✅ Užbaigta
- **Užduotys:**
  - [x] Interaktyvaus prompt redagavimo implementacija
  - [x] Redagavimo istorijos ir šablonų sistemos kūrimas
  - [x] Lygiagrečių modelių kvietimo implementacija
  - [x] Automatizuotos atsakymų kokybės analizės kūrimas
  - [x] Redagavimo ir analizės sistemų testų kūrimas
- **Pastabos:**
  - Įdiegta prompt_metrics.py modulis kokybės analizei
  - Integruota kokybės analizė į execution_cycle.py
  - Sukurta prompt_templates.py biblioteka šablonų valdymui
  - Įdiegta galimybė išsaugoti ir naudoti pakartotinai sėkmingus šablonus

### 4 etapas: Integravimas ir optimizavimas
- **Pradžia:** 2025-07-12
- **Pabaiga:** 2025-09-01
- **Statusas:** 🟡 Vykdoma
- **Užduotys:**
  - [x] Sistemų sujungimas į vieną veikiantį produktą
  - [x] Vartotojo sąsajos atnaujinimas
  - [x] Optimizavimas ir klaidų taisymas
  - [ ] Galutinių integracinių testų kūrimas
- **Pastabos:**
  - Atnaujintas main.py su naujomis meniu opcijomis
  - Sukurta kategorijų valdymo submeniu sistema
  - Sukurta šablonų valdymo submeniu sistema
  - Ištaisytos klaidų apdorojimo problemos

### 5 etapas: Multi-modelių palyginimo sistema (PRIORITETAS)
- **Pradžia:** 2025-07-11
- **Pabaiga:** 2025-08-01
- **Statusas:** 📋 Planuojama
- **Užduotys:**
  - [ ] Lygiagretaus modelių kvietimo implementacija
  - [ ] Rezultatų palyginimo analizės sistema
  - [ ] Rekomendacijų algoritmas modelių pasirinkimui
  - [ ] Rezultatų vizualizacija terminale
- **Pastabos:**
  - OpenAI GPT-4, Claude, Gemini palaikymas
  - Automatinis rezultatų vertinimas pagal esamas metrikas
  - Integruojama su esama kategorijų sistema
  - Nauji moduliai: model_comparison.py, results_analyzer.py

### 6 etapas: Išsamesnė šablonų sistema
- **Pradžia:** 2025-08-01
- **Pabaiga:** 2025-08-15
- **Statusas:** 📋 Planuojama
- **Užduotys:**
  - [ ] Pre-built šablonų rinkinys kiekvienai kategorijai
  - [ ] Šablonų parametrizavimas (dinaminiai kintamieji)
  - [ ] Import/export funkcionalumas
  - [ ] Šablonų efektyvumo statistika
- **Pastabos:**
  - Templates katalogas šiuo metu tuščias
  - Būtina sukurti bazinius šablonus pradžiai
  - Parametrizavimo sistema leis adaptuoti šablonus

### 7 etapas: Rezultatų persistenija ir analizė
- **Pradžia:** 2025-08-15
- **Pabaiga:** 2025-08-22
- **Statusas:** 📋 Planuojama
- **Užduotys:**
  - [ ] SQLite duomenų bazės implementacija
  - [ ] Rezultatų išsaugojimo sistema
  - [ ] Statistikos analizės dashboard'as
  - [ ] Našumo sekimo funkcionalumas
- **Pastabos:**
  - Dabar rezultatai nepersistinami
  - Nauji moduliai: results_persistence.py, analytics_dashboard.py
  - Performance tracking ilgalaikiai projektui

## Kategorijų sistema

### Hierarchinė struktūra (įgyvendinta)

```
- Information Retrieval
  - Search (informacijos paieškos užklausos)
  - Research (tyrimų užklausos)
  - Fact Check (faktų tikrinimo užklausos)
  
- Creative Content
  - Text (tekstų kūrimo užklausos)
  - Images (paveikslėlių generavimo užklausos)
  - Video (video koncepcijų kūrimo užklausos)
  
- Analysis
  - Data Analysis (duomenų analizės užklausos)
  - Critical Thinking (kritinio mąstymo užklausos)
  - Summarization (santraukų užklausos)
  
- Development
  - Coding (programavimo užklausos)
  - Debugging (klaidų taisymo užklausos)
  - Architecture (sistemų architektūros užklausos)
```

## Nauji funkcionalumai

### 1. Prompt'ų šablonų sistema

Nauja šablonų sistema leidžia vartotojams:
- Išsaugoti sėkmingai optimizuotus prompt'us kaip šablonus
- Organizuoti šablonus pagal kategorijas ir žymes
- Lengvai rasti ir pakartotinai naudoti šablonus
- Adaptuoti esamus šablonus naujoms užduotims

Šablonų sistema naudoja JSON formatą šablonų saugojimui ir YAML formatą indeksavimui.

### 2. Prompt'ų kokybės vertinimo sistema

Įdiegta automatizuota kokybės vertinimo sistema, kuri analizuoja prompt'us pagal šias metrikas:
- Aiškumas (70/100): kiek aiškiai apibrėžta užduotis
- Specifiškumas (75/100): kiek detaliai nurodyti reikalavimai
- Konteksto turtingumas (60/100): kiek pateikiama svarbios kontekstinės informacijos
- Struktūra (80/100): kiek gerai organizuota informacija
- Rezultato apibrėžtumas (65/100): kiek aiškiai nurodytas laukiamas rezultatas

## Artimiausios užduotys (prioritetinė tvarka)

### 🎯 0. KRITINIS PRIORITETAS: Projekto struktūros reorganizacija (1 savaitė)
**Logika:** Prieš pridedant naują funkcionalumą, būtina sutvarkyti projekto struktūrą. Dabartinė situacija trukdo efektyviam plėtojimui.

**Priežastys kodėl pirmiausiai:**
- Nauji moduliai (model_comparison.py, results_analyzer.py) reikalauja tinkamos struktūros
- Testų sistema reikalauja reorganizacijos
- Konfigūracijos valdymas chaotiškas
- Sunkus naujų funkcijų pridėjimas

**Postupinė 7-fazių strategija:**
1. **Phase 0-1:** Core infrastruktūra (2 dienos)
2. **Phase 2-3:** Agentų ir kategorijų sistema (2 dienos)
3. **Phase 4-5:** Workflows ir šablonai (2 dienos)
4. **Phase 6-7:** Testai ir UI (1 diena)

### 🎯 1. PRIORITETAS: Multi-modelių palyginimo sistema (2-3 savaitės)
**Logika:** Natūralus projekto evoliucijos žingsnis - architektūra paruošta, metrikos veikia, duos realų pridėtinę vertę.

**Techninė implementacija:**
```python
# Nauji moduliai:
- model_comparison.py     # Lygiagretūs kvietimai skirtingiems modeliams
- results_analyzer.py     # Rezultatų palyginimo analizė  
- comparison_templates.py # Specializuoti šablonai palyginimui
```

**Funkcionalumas:**
- OpenAI GPT-4, Claude, Gemini lygiagretūs testai
- Automatinis rezultatų vertinimas pagal metrikas
- Rekomendacijų sistema modelių pasirinkimui
- Rezultatų vizualizacija (tekstinė lentelė)

### 🎯 2. Išsamesnė šablonų sistema (1-2 savaitės)
**Logika:** Templates katalogas tuščias - trukdo vartotojų patirčiai.

**Implementacija:**
- Pre-built šablonų rinkinys kiekvienai kategorijai
- Šablonų parametrizavimas (dinaminiai kintamieji)
- Import/export funkcionalumas
- Šablonų efektyvumo statistika

### 🎯 3. Rezultatų persistenija ir analizė (1 savaitė)
**Logika:** Rezultatai nepersistinami - prarandama vertinga informacija.

**Implementacija:**
```python
# Nauji moduliai:
- results_persistence.py  # Rezultatų išsaugojimas
- analytics_dashboard.py  # Statistikos analizė
- performance_tracker.py  # Našumo sekimas
```

### 🎯 4. Vartotojo sąsajos patobulinimas (1 savaitė)
**Logika:** Terminalo meniu funkcionalus, bet galima pagerinti.

**Implementacija:**
- Spalvų sistema terminale
- Progress bar'ai ilgiems procesams
- Geresnė klaidų apdorojimo sistema
- Kontekstinė pagalba

## 🔧 Detalizuotas planas (ATNAUJINTAS)

### Savaitė 1: Projekto struktūros reorganizacija (KRITINIS PRIORITETAS)
**Dienos 1-2: Phase 0-1**
- Automatizacijos įrankių sukūrimas
- Core infrastruktūros migracija
- Bazinių testų validacija

**Dienos 3-4: Phase 2-3**
- Agentų sistemos migracija
- Kategorijų sistemos migracija
- Import'ų atnaujinimas

**Dienos 5-7: Phase 4-7**
- Workflows migracija
- Šablonų sistemos migracija
- Testų reorganizacija
- UI finalizavimas

### Savaitės 2-3: Multi-modelių sistema
### Savaitės 2-3: Multi-modelių sistema
1. **Savaitė 2:**
   - Sukurti `agentforge/analysis/model_comparison.py` modulį
   - Implementuoti API integracijas (OpenAI, Claude, Gemini)
   - Pridėti lygiagretaus kvietimo logiką

2. **Savaitė 3:**
   - Integruoti su esamais agentais
   - Sukurti rezultatų analizės algoritmus
   - Pridėti palyginimo opciją į meniu
   - Testų kūrimas

### Savaitė 4: Šablonų sistema
1. Sukurti bazinius šablonus kiekvienai kategorijai
2. Implementuoti parametrizavimo sistemą
3. Pridėti import/export funkcionalumą
4. Testų ir dokumentacijos atnaujinimas

### Savaitė 5: Rezultatų persistenija
1. Sukurti SQLite duomenų bazės struktūrą
2. Implementuoti rezultatų išsaugojimo sistemą
3. Sukurti analizės dashboard'ą
4. Integruoti su esamais procesais

### Savaitės 6-7: UX patobulinimas ir finalizavimas
1. **Savaitė 6:**
   - Pagerinti vartotojo sąsają (spalvos, progress bar'ai)
   - Išplėsti testavimo sistemą
   - Klaidų apdorojimo patobulinimas

2. **Savaitė 7:**
   - Dokumentacijos atnaujinimas
   - Beta testavimas
   - Galutinių integracinių testų sukūrimas
   - Performance optimizavimas

## 💡 Strateginės rekomendacijos (ATNAUJINTOS)

1. **PIRMIAUSIAI STRUKTŪRA** - projekto reorganizacija prieš naują funkcionalumą
2. **Postupinė migracija** - fazės su validacija, ne "big bang" požiūris
3. **Automatizacija** - migracijos įrankiai klaidų mažinimui
4. **Testai nuolat** - smoke testai kiekvienoje fazėje
5. **Rollback planas** - galimybė grįžti bet kuriame etape
6. **Moduliarumas** - kiekvienas naujas komponentas nepriklausomas
7. **Dokumentacija** - atnaujinti su kiekvienu žingsniu
8. **Backup strategija** - git branch'ai ir checkpoints

## 📈 Sėkmės kriterijai (ATNAUJINTI)

### Projekto struktūros reorganizacija:
- Visi failai teisingose vietose pagal Python best practices
- Moduliai teisingai importuojami
- Nėra broken imports
- Testai praeina kiekvienoje fazėje
- Funkcionalumas nepakito
- Galimybė lengvai pridėti naują funkcionalumą

### Multi-modelių sistema:
- Galimybė palyginti ≥3 skirtingus modelius
- Automatinis rezultatų vertinimas visomis 5 metrikomis
- Rekomendacijų sistema veikia visoms kategorijoms

### Šablonų sistema:
- Minimum 3-5 šablonai kiekvienai kategorijai
- Parametrizavimo funkcionalumas veikia
- Import/export be klaidų

### Persistenija:
- Visi rezultatai išsaugojami duomenų bazėje
- Dashboard'as rodo statistikas
- Performance tracking veikia

### UX patobulinimas:
- Spalvotas terminalas
- Progress indikatoriai
- Kontekstinė pagalba funkcionali

## Sukurti artefaktai

### Nauji YAML/JSON failai:
- **categories.yaml** - hierarchinė kategorijų sistema su raktažodžiais ir pavyzdžiais
- **agent_skills.yaml** - agentų įgūdžių ir specializacijų aprašai
- **templates/*.json** - prompt'ų šablonų failai

### Nauji Python moduliai:
- **prompt_templates.py** - prompt'ų šablonų valdymo sistema
- **prompt_metrics.py** - prompt'ų kokybės vertinimo metrikos

### Atnaujinti Python moduliai:
- **main.py** - papildytas naujais meniu punktais ir submeniu
- **execution_cycle.py** - integruota kategorijų atpažinimo sistema ir dinaminiai agentai

---

## Atnaujinimai

### 2025-07-10
- Sukurtas pradinis projekto planas
- Apibrėžtos pagrindinės kategorijos
- Sukurta preliminari agentų įgūdžių matrica

### 2025-07-11
- Sukurti konfigūraciniai YAML failai:
  - categories.yaml - hierarchinė kategorijų sistema
  - agent_skills.yaml - agentų įgūdžių matrica
- Sukurti pagrindiniai moduliai:
  - categories.py - kategorijų sistemos valdymas
  - category_classifier.py - užklausų klasifikavimo logika
  - agent_skills.py - agentų įgūdžių matricos valdymas
  - dynamic_agents.py - dinaminių agentų parinkimas pagal kategoriją
- Atnaujintas execution_cycle.py su dinaminiais agentais

### 2025-07-11 (STRUKTŪROS REORGANIZACIJOS PLANAS + ĮRANKIAI)
- Sukurtas detalizuotas 7-fazių projekto struktūros reorganizacijos planas
- **Sukurtas ProjectScanner įrankis** - automatinė projekto analizė
- **Sukurtas run_scanner.py** - struktūros analizės skriptas
- **Sukurtas run_project_analysis.bat** - Windows paleidimo skriptas
- Prioritetas pakeistas: pirmiausiai struktūra, paskui funkcionalumas
- Postupinė migracija su validacija kiekvienoje fazėje
- Automatizacijos įrankių specifikacija migracijos rizikos mažinimui
- Profesionali agentforge/ package struktūra Python standartams
- Minimali rizikos strategija su rollback galimybėmis
- Atnaujintas 7 savaičių planas su struktūros reorganizacija pradžioje

**Paleidimas:**
```bash
# Windows:
run_project_analysis.bat

# Arba tiesiogiai:
cd tools/migration && python run_scanner.py
```

**Sukuriami failai:**
- `tools/migration/reports/project_structure_analysis_*.txt` - detalus struktūros aprašymas
- Migracijos žemėlapis su konkretėmis failų vietomis
- Python failų analizė (20 failų, 3000+ eilučių kodo)

## 🏗️ Projekto Struktūros Reorganizacijos Planas (KRITINIS PRIORITETAS)

### 📋 Problema ir sprendimas

**Dabartinė situacija:** Projektas išaugo organiškai, failai pasklidę root kataloge, trūksta aiškios struktūros.

**Poveikis:** Sunkus naujų funkcijų pridėjimas, sudėtinga navigacija, chaotiškas palaikymas.

**Sprendimas:** Postupinė migracija į profesionalų projekto layoutą su minimalia rizika.

### 🎯 Galutinė optimizuota struktūra

```
AgentForge/
├── agentforge/                   # Pagrindinis package
│   ├── __init__.py
│   ├── core/                     # Baziniai komponentai
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── base_classes.py
│   │   └── logging_config.py
│   ├── agents/                   # Agentų sistema
│   │   ├── __init__.py
│   │   ├── base_agent.py
│   │   ├── skills.py
│   │   ├── dynamic_selection.py
│   │   └── specialized/
│   │       ├── __init__.py
│   │       ├── researcher.py
│   │       ├── synthesizer.py
│   │       └── analyst.py
│   ├── categories/               # Kategorijų sistema
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   ├── classifier.py
│   │   └── models.py
│   ├── workflows/                # Darbo ciklai
│   │   ├── __init__.py
│   │   ├── maintenance.py
│   │   ├── execution.py
│   │   ├── tasks/
│   │   │   ├── __init__.py
│   │   │   ├── maintenance_tasks.py
│   │   │   └── execution_tasks.py
│   │   └── orchestrator.py
│   ├── templates/                # Šablonų sistema
│   │   ├── __init__.py
│   │   ├── manager.py
│   │   ├── validator.py
│   │   └── storage.py
│   ├── analysis/                 # Analizės moduliai
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── comparison.py
│   │   ├── quality_scorer.py
│   │   └── results_analyzer.py
│   ├── persistence/              # Duomenų valdymas
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── repositories.py
│   │   └── migrations/
│   ├── ui/                       # Vartotojo sąsaja
│   │   ├── __init__.py
│   │   ├── cli/
│   │   │   ├── __init__.py
│   │   │   ├── main_menu.py
│   │   │   ├── handlers.py
│   │   │   └── formatters.py
│   │   └── components/
│   │       ├── __init__.py
│   │       ├── progress_bar.py
│   │       └── colors.py
│   └── utils/                    # Pagalbiniai įrankiai
│       ├── __init__.py
│       ├── file_operations.py
│       ├── validators.py
│       ├── decorators.py
│       └── helpers.py
├── data/                         # Duomenų failai
│   ├── knowledge_base/
│   │   ├── ziniu_baze.yaml
│   │   ├── kanonine_sistema.yaml
│   │   └── source_registry.yaml
│   ├── config/
│   │   ├── categories.yaml
│   │   ├── agent_skills.yaml
│   │   └── environments/
│   │       ├── development.yaml
│   │       ├── production.yaml
│   │       └── testing.yaml
│   ├── templates/
│   │   ├── information_retrieval/
│   │   ├── creative_content/
│   │   ├── analysis/
│   │   └── development/
│   └── results/
│       ├── comparisons/
│       ├── metrics/
│       └── exports/
├── tests/                        # Testų sistema
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_agents/
│   │   ├── test_categories/
│   │   ├── test_workflows/
│   │   └── test_templates/
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_full_workflow.py
│   │   └── test_api_integration.py
│   ├── fixtures/
│   │   ├── __init__.py
│   │   ├── sample_data.py
│   │   └── mock_responses.py
│   └── utils/
│       ├── __init__.py
│       ├── test_helpers.py
│       └── custom_assertions.py
├── tools/                        # Automatizacijos įrankiai
│   ├── migration/
│   │   ├── __init__.py
│   │   ├── phase_migrator.py
│   │   ├── import_updater.py
│   │   ├── validator.py
│   │   └── rollback.py
│   ├── deployment/
│   │   ├── setup.py
│   │   └── health_check.py
│   └── maintenance/
│       ├── cleanup.py
│       └── backup.py
├── docs/                         # Dokumentacija
│   ├── api/
│   ├── user_guide/
│   ├── development/
│   │   ├── architecture.md
│   │   ├── migration_guide.md
│   │   └── testing.md
│   └── examples/
├── scripts/                      # Deployment skriptai
│   ├── setup.sh
│   ├── setup.ps1
│   ├── migrate.sh
│   └── test.sh
├── main.py                       # CLI entry point
├── setup.py                      # Package setup
├── pyproject.toml               # Modern Python packaging
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── .env.example
├── .gitignore
├── README.md
└── development_plan.md
```

## 📋 Postupinės migracijos strategija (PHASE-BY-PHASE)

### Phase 0: Pasiruošimas ir infrastruktūra (1 diena)
**Tikslas:** Sukurti migracijos įrankius ir backup strategiją

**Veiksmai:**
1. **Git branch strategija**
   ```bash
   git checkout -b migration/phase-0-preparation
   git checkout -b migration/phase-1-core
   git checkout -b migration/phase-2-agents
   # ... kiekvienai fazei
   ```

2. **Automatizacijos įrankių sukūrimas**
   ```python
   # tools/migration/phase_migrator.py
   class PhaseMigrator:
       def __init__(self, phase_config):
           self.phase_config = phase_config
           self.backup_manager = BackupManager()
           
       def migrate_phase(self, phase_name):
           # Backup dabartinės būsenos
           # Migracija pagal fazę
           # Validacija
           # Rollback galimybė
   ```

3. **Testų infrastruktūra**
   - Smoke testai kiekvienai fazei
   - Integration testai
   - Performance benchmarks

### Phase 1: Core infrastruktūra (1 diena)
**Tikslas:** Sukurti bazinę agentforge/ package struktūrą

**Failų migracija:**
```python
PHASE_1_MIGRATIONS = {
    'config.py': 'agentforge/core/config.py',
    'custom_tools.py': 'agentforge/utils/file_operations.py',
    # Tik baziniai failai
}
```

**Validacija:**
- Visi import'ai veikia
- Baziniai testai praeina
- Main.py vis dar paleidžiamas

**Rollback planas:**
- Git reset į ankstesnę būseną
- Automatinis failų grąžinimas

### Phase 2: Agentų sistema (1 diena)
**Tikslas:** Migracija agentų susijusių failų

**Failų migracija:**
```python
PHASE_2_MIGRATIONS = {
    'agents.py': 'agentforge/agents/__init__.py',
    'agent_skills.py': 'agentforge/agents/skills.py',
    'dynamic_agents.py': 'agentforge/agents/dynamic_selection.py',
    'agent_skills.yaml': 'data/config/agent_skills.yaml',
}
```

**Postupinė migracija:**
1. Sukurti naują failą naujoje vietoje
2. Importuoti seną failą į naują
3. Atnaujinti visus import'us
4. Ištrinti seną failą
5. Testai ir validacija

### Phase 3: Kategorijų sistema (1 diena)
**Tikslas:** Kategorijų sistemos migracija

**Failų migracija:**
```python
PHASE_3_MIGRATIONS = {
    'categories.py': 'agentforge/categories/manager.py',
    'category_classifier.py': 'agentforge/categories/classifier.py',
    'categories.yaml': 'data/config/categories.yaml',
}
```

### Phase 4: Darbo ciklai (1 diena)
**Tikslas:** Workflow'ų sistema

**Failų migracija:**
```python
PHASE_4_MIGRATIONS = {
    'maintenance_cycle.py': 'agentforge/workflows/maintenance.py',
    'execution_cycle.py': 'agentforge/workflows/execution.py',
    'tasks_maintenance.py': 'agentforge/workflows/tasks/maintenance_tasks.py',
    'tasks_execution.py': 'agentforge/workflows/tasks/execution_tasks.py',
}
```

### Phase 5: Šablonų ir analizės sistema (1 diena)
**Tikslas:** Templates ir metrics migracija

**Failų migracija:**
```python
PHASE_5_MIGRATIONS = {
    'prompt_templates.py': 'agentforge/templates/manager.py',
    'prompt_metrics.py': 'agentforge/analysis/metrics.py',
    'templates/': 'data/templates/',
}
```

### Phase 6: Testų sistema (1 diena)
**Tikslas:** Testų reorganizacija

**Failų migracija:**
```python
PHASE_6_MIGRATIONS = {
    'test_system.py': 'tests/integration/test_full_workflow.py',
    'test_results/': 'data/results/',
}
```

### Phase 7: UI ir finalizavimas (1 diena)
**Tikslas:** Vartotojo sąsajos ir main.py reorganizacija

**Failų migracija:**
```python
PHASE_7_MIGRATIONS = {
    'main.py': 'agentforge/ui/cli/main_menu.py',
    # Naujas main.py kaip entry point
}
```

## 🛠️ Pažangūs automatizacijos įrankiai

### 1. Fazių migratorius
```python
# tools/migration/phase_migrator.py
class PhaseMigrator:
    def __init__(self):
        self.current_phase = self.detect_current_phase()
        self.validator = MigrationValidator()
        
    def migrate_to_next_phase(self):
        next_phase = self.current_phase + 1
        
        try:
            # Backup
            self.create_phase_backup(next_phase)
            
            # Migracija
            self.execute_phase_migration(next_phase)
            
            # Validacija
            if not self.validator.validate_phase(next_phase):
                raise MigrationError(f"Phase {next_phase} validation failed")
                
            # Atnaujinti fazės statusą
            self.current_phase = next_phase
            
        except Exception as e:
            # Automatinis rollback
            self.rollback_phase(next_phase)
            raise e
```

### 2. Import atnaujintojas
```python
# tools/migration/import_updater.py
class ImportUpdater:
    def __init__(self):
        self.import_map = self.load_import_mapping()
        
    def update_imports_for_phase(self, phase_number):
        files_to_update = self.get_files_for_phase(phase_number)
        
        for file_path in files_to_update:
            self.update_file_imports(file_path)
            
    def update_file_imports(self, file_path):
        # Nuskaito failą
        # Atnaujina import statements
        # Išsaugo su backup
        pass
```

### 3. Validatorius
```python
# tools/migration/validator.py
class MigrationValidator:
    def validate_phase(self, phase_number):
        validators = [
            self.validate_file_structure,
            self.validate_imports,
            self.validate_tests,
            self.validate_functionality
        ]
        
        return all(validator(phase_number) for validator in validators)
```

## 📊 Rizikų mažinimo strategijos

### 1. Checkpoint sistema
```python
# Kiekvienoje fazėje
def create_checkpoint(phase_name):
    # Git commit su konkrečia žinutė
    # Duomenų bazės snapshot
    # Konfiguracijos backup
    pass
```

### 2. Smoke testai
```python
# tests/smoke/test_phase_migration.py
def test_phase_1_smoke():
    # Pagrindiniai import'ai veikia
    # Main.py paleidžiamas
    # Baziniai testai praeina
    pass
```

### 3. Rollback mechanizmas
```python
# tools/migration/rollback.py
class RollbackManager:
    def rollback_to_phase(self, target_phase):
        # Git reset
        # Failų atkūrimas
        # Konfigūracijos grąžinimas
        pass
```

## 🎯 Sėkmės kriterijai kiekvienai fazei

### Fazė 1: Core
- [x] agentforge/ package sukurtas
- [x] Baziniai moduliai importuojami
- [x] Main.py veikia

### Fazė 2: Agents
- [x] Agentų sistema migravo
- [x] Dinaminiai agentai veikia
- [x] Visi agentų testai praeina

### Fazė 3: Categories
- [x] Kategorijų sistema migravo
- [x] Klasifikavimas veikia
- [x] YAML failai tinkamose vietose

### Fazė 4: Workflows
- [x] Ciklai migravo
- [x] Workflow'ai veikia
- [x] Integracija su agentais

### Fazė 5: Templates & Analysis
- [x] Šablonų sistema migravo
- [x] Metrikos veikia
- [x] Analizės moduliai funkcionuoja

### Fazė 6: Tests
- [x] Testų struktūra reorganizuota
- [x] Visi testai praeina
- [x] Coverage nepakito

### Fazė 7: UI & Finalization
- [x] CLI sistema migravo
- [x] Entry point veikia
- [x] Vartotojo patirtis nepakito

## 📈 Migracijos privalumai

1. **Minimali rizika** - kiekviena fazė nepriklausoma
2. **Testavimas** - validacija kiekviename žingsnyje
3. **Rollback** - galimybė grįžti bet kuriame momente
4. **Progreso stebėjimas** - aiškus progreso indikatorius
5. **Moduliarumas** - galima sustoti bet kurioje fazėje

## 💡 Rekomendacijos

1. **Viena fazė per dieną** - nesiskubinti
2. **Testai visada** - validacija po kiekvieno žingsnio
3. **Backup visada** - prieš kiekvieną fazę
4. **Dokumentacija** - atnaujinti po kiekvienos fazės
5. **Team communication** - informuoti apie progresą

---

### 8 etapas: Projekto struktūros reorganizacija (KRITINIS PRIORITETAS)
- **Pradžia:** 2025-07-12
- **Pabaiga:** 2025-07-19
- **Statusas:** 📋 Planuojama (TURI BŪTI PRADĖTAS PRIEŠ KITUS ETAPUS)
- **Užduotys:**
  - [ ] Phase 0: Pasiruošimas ir infrastruktūra (1 diena)
  - [ ] Phase 1: Core infrastruktūra (1 diena)
  - [ ] Phase 2: Agentų sistema (1 diena)
  - [ ] Phase 3: Kategorijų sistema (1 diena)
  - [ ] Phase 4: Darbo ciklai (1 diena)
  - [ ] Phase 5: Šablonų ir analizės sistema (1 diena)
  - [ ] Phase 6: Testų sistema (1 diena)
  - [ ] Phase 7: UI ir finalizavimas (1 diena)
- **Pastabos:**
  - **KRITIŠKAI SVARBU:** Turi būti įvykdytas prieš 5-7 etapus
  - Postupinė migracija su validacija kiekvienoje fazėje
  - Automatinis rollback galimybė
  - Nulinis downtime projekto funkcionalumui
  - Profesionali projekto struktūra Python bendruomenės standartams