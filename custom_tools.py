# /AgentForge/custom_tools.py

import yaml
# GALUTINIS IR TEISINGAS IMPORTAS:
# @tool dekoratorius, skirtas specialiai CrewAI agentams.
from crewai.tools import tool

# Kiekviena funkcija tampa įrankiu su `@tool` dekoratoriumi.

@tool("Failo Įrašymo Įrankis")
def file_write_tool(file_path: str, text: str) -> str:
    """Naudok šį įrankį, kad įrašytum tekstą į failą.
    Įrankis priima du argumentus:
    - file_path: kelias iki failo, į kurį reikia rašyti.
    - text: tekstas, kurį reikia įrašyti į failą.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return f"Failas sėkmingai išsaugotas adresu: {file_path}"
    except Exception as e:
        return f"Klaida įrašant failą: {e}"

@tool("YAML Failo Skaitymo Įrankis")
def yaml_read_tool(file_path: str) -> str:
    """Naudok šį įrankį, kad nuskaitytum turinį iš YAML failo.
    Įrankis priima vieną argumentą:
    - file_path: kelias iki YAML failo, kurį reikia nuskaityti.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.dump(yaml.safe_load(f))
    except Exception as e:
        return f"Klaida nuskaitant YAML failą: {e}"