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
- **Pabaiga:** 2025-07-25
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
- **Pradžia:** 2025-07-20
- **Pabaiga:** 2025-08-10
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
- **Pradžia:** 2025-08-10
- **Pabaiga:** 2025-08-25
- **Statusas:** 🟡 Vykdoma
- **Užduotys:**
  - [x] Interaktyvaus prompt redagavimo implementacija
  - [ ] Redagavimo istorijos ir šablonų sistemos kūrimas
  - [x] Lygiagrečių modelių kvietimo implementacija
  - [x] Automatizuotos atsakymų kokybės analizės kūrimas
  - [ ] Redagavimo ir analizės sistemų testų kūrimas
- **Pastabos:**
  - Įdiegta prompt_metrics.py modulis kokybės analizei
  - Integruota kokybės analizė į execution_cycle.py

### 4 etapas: Integravimas ir optimizavimas
- **Pradžia:** 2025-08-25
- **Pabaiga:** 2025-09-01
- **Statusas:** 🟡 Vykdoma
- **Užduotys:**
  - [x] Sistemų sujungimas į vieną veikiantį produktą
  - [x] Vartotojo sąsajos atnaujinimas
  - [ ] Optimizavimas ir klaidų taisymas
  - [ ] Galutinių integracinių testų kūrimas
- **Pastabos:**
  - Atnaujintas main.py su naujomis meniu opcijomis
  - Sukurta kategorijų valdymo submeniu sistema

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

### Kategorijos identifikavimo algoritmas (įgyvendintas)

1. Zero-shot klasifikavimas pagal pagrindines kategorijas
2. Patikslinti klasifikavimą pagal subkategorijas
3. Patikrinti ar yra specialių raktažodžių, nurodančių konkrečią kategoriją
4. Pasiūlyti vartotojui patvirtinti arba pakeisti nustatytą kategoriją

## Agentų įgūdžių matrica (įgyvendinta)

| Agentas                 | Info Retrieval | Creative | Analysis | Development |
|-------------------------|:--------------:|:--------:|:--------:|:-----------:|
| Prompt Analyst          |       4        |     3    |     5    |      3      |
| Prompt Critic           |       3        |     4    |     5    |      3      |
| Prompt Refiner          |       3        |     4    |     3    |      3      |
| Creative Specialist     |       2        |     5    |     2    |      1      |
| Technical Specialist    |       3        |     1    |     3    |      5      |
| Research Specialist     |       5        |     2    |     4    |      2      |

*Įgūdžių skalė: 1 (minimalus) - 5 (ekspertinis)*

## Prompt'ų kokybės vertinimo metrikos (įgyvendinta)

1. **Aiškumas** - kiek aiškiai apibrėžta užduotis ir kontekstas
2. **Specifiškumas** - kiek detaliai nurodyti reikalavimai
3. **Konteksto turtingumas** - kiek pateikiama svarbios kontekstinės informacijos
4. **Struktūra** - kiek gerai organizuota informacija
5. **Rezultato apibrėžtumas** - kiek aiškiai nurodytas laukiamas rezultatas

## Artimiausios užduotys

1. ~~Apibrėžti galutinius kategorijų aprašymus~~ ✅
2. ~~Sukurti zero-shot klasifikavimo eksperimentinį kodą~~ ✅
3. ~~Sukurti agentų įgūdžių konfigūracijos YAML failą~~ ✅
4. Integruoti kategorijų klasifikavimo sistemą su tikru AI modeliu
5. Integruoti dinaminių agentų sistemą į esamą AgentForge karkasą
6. Sukurti prototipinį interaktyvų redaktorių

## Sukurti artefaktai

### YAML failai:
- **categories.yaml** - hierarchinė kategorijų sistema su raktažodžiais ir pavyzdžiais
- **agent_skills.yaml** - agentų įgūdžių ir specializacijų aprašai

### Python moduliai:
- **categories.py** - kategorijų sistemos valdymo funkcijos
- **agent_skills.py** - agentų įgūdžių matricos valdymo funkcijos
- **category_classifier.py** - užklausų klasifikavimo į kategorijas funkcijos
- **dynamic_agents.py** - dinaminių agentų parinkimo sistema
- **prompt_metrics.py** - prompt'ų kokybės vertinimo metrikos

---

## Atnaujinimai

### 2025-07-10
- Sukurtas pradinis projekto planas
- Apibrėžtos pagrindinės kategorijos
- Sukurta preliminari agentų įgūdžių matrica

### 2025-07-10 (vėliau)
- Užbaigtas 0-tasis etapas
- Sukurti pagrindiniai moduliai: categories.py, agent_skills.py, category_classifier.py, dynamic_agents.py, prompt_metrics.py
- Apibrėžta detalesnė kategorijų hierarchija
- Sukurtas agentų įgūdžių konfigūracijos mechanizmas
- Sukurtas prompt'ų kokybės vertinimo mechanizmas

### 2025-07-11
- Sukurti konfigūraciniai YAML failai:
  - categories.yaml - hierarchinė kategorijų sistema
  - agent_skills.yaml - agentų įgūdžių matrica
- Atnaujintas progreso dokumentas
- Pradėti 1 ir 2 etapas