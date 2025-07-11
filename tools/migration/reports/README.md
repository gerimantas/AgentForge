# /AgentForge/tools/migration/reports/README.md

# Migracijos Ataskaitų Katalogas

Šiame kataloge saugomi projekto struktūros analizės ir migracijos ataskaitų failai.

## Failų tipai:

### `project_structure_analysis_*.txt`
- Dabartinės projekto struktūros ataskaitos
- Python failų analizė (eilutės, klasės, funkcijos)
- Migracijos žemėlapis
- Statistika

### `migration_phase_*.txt`
- Kiekvienos migracijos fazės ataskaitos
- Sėkmės/nesėkmės statusai
- Rollback informacija

### `validation_reports_*.txt`
- Validacijos rezultatai po kiekvienos fazės
- Import'ų patikrinimas
- Testų rezultatai

## Naudojimas:

```bash
# Sukurti naują struktūros analizę
cd tools/migration
python run_scanner.py

# Peržiūrėti naujausią ataskaitą
# Atidaryti paskutinį project_structure_analysis_*.txt failą
```

## Pastaba:

Seni ataskaitos failai (>30 dienų) automatiškai trinami palaikant švarų katalogą.
