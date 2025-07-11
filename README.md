# AgentForge

AgentForge – autonominių agentų sistema žinių bazės palaikymui ir užklausų optimizavimui.

---

## Architektūros schema

```
+-------------------+
|     main.py       |
+-------------------+
         |
         v
+-------------------+         +-------------------+
| MaintenanceCycle  |<------->| ExecutionCycle    |
+-------------------+         +-------------------+
         |                             |
         v                             v
+-------------------+         +-------------------+
| tasks_maintenance |         | tasks_execution   |
+-------------------+         +-------------------+
         |                             |
         v                             v
+-------------------+         +-------------------+
|     agents.py     |<------->|   custom_tools.py |
+-------------------+         +-------------------+
         |                    |
         v                    v
+-------------------+    +-------------------+
|  ziniu_baze.yaml  |    | source_registry.yaml |
+-------------------+    +-------------------+
         |                    |
         v                    v
+-------------------+    +-------------------+
| kanonine_sistema.yaml |  test_system.py   |
+-------------------+    +-------------------+
                              |
                              v
                         +-------------------+
                         | test_results      |
                         +-------------------+
```

---

## Projekto būsena

**Dabartinė versija:** 0.3.0
**Būsena:** Vystoma

Neseniai įgyvendinti pakeitimai:
- ✅ Struktūrizuota žinių bazė (YAML formatas)
- ✅ Agentų integracija su YAML žinių baze
- ✅ Atnaujintas dokumentacijos README
- ✅ Funkcijų optimizavimas ir klaidų taisymas
- ✅ Įdiegtas automatizuotas testavimo karkasas
- ✅ Pridėta testų rezultatų kaupimo sistema

---

## Agentų aprašymai

### Maintenance Cycle (Žinių bazės palaikymas)
- **Tyrėjas (Researcher)**  
  Suranda naujus patikimus šaltinius, tikrina faktus naudodamas aktyvius šaltinius iš `source_registry.yaml`.
- **Sintezatorius (Synthesizer)**  
  Apibendrina naują informaciją, integruoja į struktūrizuotą žinių bazę `ziniu_baze.yaml`.
- **Taisyklių inžinierius (Rule Engineer)**  
  Kuria ir atnaujina žinių bazės taisykles `kanonine_sistema.yaml` faile.

### Execution Cycle (Užklausų optimizavimas)
- **Analitikas (Prompt Analyst)**  
  Analizuoja vartotojo užklausą, identifikuoja tikslą ir pritaiko bazines prompt inžinerijos technikas.
- **Kritikas (Prompt Critic)**  
  Vertina agentų pasiūlymus, ieško trūkumų, siūlo patobulinimus remiantis žinių baze.
- **Tobulintojas (Prompt Refiner)**  
  Optimizuoja užklausą pagal taisykles ir žinių bazę, pateikia galutinį rezultatą.

---

## Naudojimo pavyzdžiai

### 1. Projekto paleidimas

```bash
# Pirmasis paleidimas (Windows)
scripts\setup\setup_env.bat

# Kasdienis naudojimas
scripts\setup\start.bat

# Arba tiesiai
python main.py
```

### 2. Žinių bazės atnaujinimas

Pasirinkite žinių bazės palaikymo ciklą ir sekite instrukcijas terminale:

```
> 1 (Maintenance Cycle)
```

Sistema automatiškai:
1. Tyrėjas patikrins patikimus šaltinius ir pateiks naują informaciją
2. Sintezatorius integruos ją į žinių bazę (ziniu_baze.yaml)
3. Taisyklių inžinierius atnaujins taisykles (kanonine_sistema.yaml)

### 3. Užklausos optimizavimas

Pasirinkite užklausos vykdymo ciklą, įveskite savo užklausą:

```
> 2 (Execution Cycle)
> "Padėk man parašyti laišką darbdaviui dėl algos pakėlimo"
```

Sistema automatiškai:
1. Analizuos užklausą
2. Pritaikys žinių bazės technikas
3. Pateiks optimizuotą užklausą

### 4. Sistemos testavimas

Pasirinkite sistemos testavimo opciją:

```
> 3 (Sistemos testai)
```

Sistema:
1. Paleis visus integracinius ir unit testus
2. Parodys testų rezultatus
3. Pasiūlys išsaugoti testų rezultatus:
   - Jei testai sėkmingi - paprastai nereikia saugoti rezultatų
   - Jei testai nepavyko - rekomenduojama išsaugoti rezultatus analizei

---

## Failų struktūra

- `main.py` – pagrindinis paleidimo taškas
- `maintenance_cycle.py`, `tasks_maintenance.py` – žinių bazės palaikymo ciklas
- `execution_cycle.py`, `tasks_execution.py` – užklausų optimizavimo ciklas
- `agents.py` – agentų aprašymai ir logika
- `custom_tools.py` – pagalbiniai įrankiai (failų skaitymas/rašymas, YAML, faktų tikrinimas ir kt.)
- `config.py` – API raktai, saugikliai, konfigūracija
- `test_system.py` – automatizuotas testavimo karkasas
- **Duomenų failai:**
  - `ziniu_baze.yaml` – struktūrizuota žinių bazė
  - `kanonine_sistema.yaml` – žinių bazės taisyklės
  - `source_registry.yaml` – šaltinių registras
  - `test_results/` – testavimo rezultatų katalogas

---

## Testavimo sistema

### Automatiniai testai
Sistemoje įdiegti šie testai:

1. **Konfigūracijos testai** – tikrina, ar teisingai įkelti API raktai ir nustatymai
2. **Kalbos aptikimo testai** – tikrina, ar sistema gali identifikuoti įvesties kalbą
3. **Vykdymo ciklo testai** – tikrina užklausos optimizavimo funkcionalumą
4. **YAML failų operacijų testai** – tikrina žinių bazės skaitymo/rašymo funkcijas

### Testų paleidimas
```bash
python test_system.py
```

arba per meniu pasirinkus opciją "3".

### Testų rezultatai
- Testų rezultatai išsaugomi `test_results/` kataloge
- Naudojama failų rotacijos sistema, kad žurnalas netaptų per didelis
- Seni žurnalo įrašai automatiškai valomi

---

## Reikalavimai

- Python 3.10+
- Priklausomybės iš `requirements.txt`:
  ```
  pip install -r requirements.txt
  ```
- Paketai:
  - langdetect
  - crewai
  - crewai_tools
  - pyyaml
  - python-dotenv
- `.env` failas su API raktais:
  ```
  OPENAI_API_KEY=...
  SERPER_API_KEY=...
  MAX_ITERATIONS=3
  VERBOSE=True
  ```

---

## Tolimesni žingsniai

- [x] Testavimo karkaso įdiegimas
- [ ] Žinių bazės atvaizdavimo vartotojo sąsaja
- [ ] Automatinė faktų patikra
- [ ] Dinaminis maršrutizavimas ir resursų valdymas
- [ ] CI/CD integracija su GitHub Actions

---

## Kontaktai ir pagalba

Kilus klausimams, kreipkitės į projekto autorių arba perkelkite problemą į GitHub Issues.

---