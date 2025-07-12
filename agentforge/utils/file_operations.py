"""
AgentForge File Operations
=========================

Šis modulis saugo failinius veiksmus ir duomenų tvarkymą.
"""

import yaml
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from crewai.tools import tool

# Projekto šakninė direktorija
PROJECT_ROOT = Path(__file__).parent.parent.parent

def load_knowledge_base(filename: str = "ziniu_baze.yaml") -> List[Dict[str, Any]]:
    """
    Įkrauna žinių bazę iš YAML failo.
    
    Args:
        filename: Failo pavadinimas (galima be plėtinio)
        
    Returns:
        Žinių bazės sąrašas
    """
    # Užtikrinti kad failas turi .yaml plėtinį
    if not filename.endswith('.yaml'):
        filename += '.yaml'
    
    file_path = PROJECT_ROOT / "data" / "knowledge_base" / filename
    
    try:
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data if isinstance(data, list) else []
        else:
            print(f"⚠️ Žinių bazės failas nerastas: {file_path}")
            return []
    except Exception as e:
        print(f"❌ Klaida įkraunant žinių bazę {filename}: {e}")
        return []

def save_knowledge_base(knowledge_base: List[Dict[str, Any]], filename: str = "ziniu_baze.yaml") -> bool:
    """
    Išsaugo žinių bazę į YAML failą.
    
    Args:
        knowledge_base: Žinių bazės duomenys
        filename: Failo pavadinimas
        
    Returns:
        True jei sėkmingai išsaugota
    """
    # Užtikrinti kad failas turi .yaml plėtinį
    if not filename.endswith('.yaml'):
        filename += '.yaml'
    
    file_path = PROJECT_ROOT / "data" / "knowledge_base" / filename
    
    try:
        # Sukurti katalogą jei neegzistuoja
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(knowledge_base, f, default_flow_style=False, allow_unicode=True)
        
        print(f"✅ Žinių bazė išsaugota: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Klaida išsaugant žinių bazę {filename}: {e}")
        return False

def load_source_registry(filename: str = "source_registry.yaml") -> Dict[str, Any]:
    """
    Įkrauna šaltinių registrą iš YAML failo.
    
    Args:
        filename: Failo pavadinimas
        
    Returns:
        Šaltinių registro duomenys
    """
    # Užtikrinti kad failas turi .yaml plėtinį
    if not filename.endswith('.yaml'):
        filename += '.yaml'
    
    file_path = PROJECT_ROOT / "data" / "knowledge_base" / filename
    
    try:
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data if isinstance(data, dict) else {}
        else:
            print(f"⚠️ Šaltinių registro failas nerastas: {file_path}")
            return {}
    except Exception as e:
        print(f"❌ Klaida įkraunant šaltinių registrą {filename}: {e}")
        return {}

def save_source_registry(source_registry: Dict[str, Any], filename: str = "source_registry.yaml") -> bool:
    """
    Išsaugo šaltinių registrą į YAML failą.
    
    Args:
        source_registry: Šaltinių registro duomenys
        filename: Failo pavadinimas
        
    Returns:
        True jei sėkmingai išsaugota
    """
    # Užtikrinti kad failas turi .yaml plėtinį
    if not filename.endswith('.yaml'):
        filename += '.yaml'
    
    file_path = PROJECT_ROOT / "data" / "knowledge_base" / filename
    
    try:
        # Sukurti katalogą jei neegzistuoja
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(source_registry, f, default_flow_style=False, allow_unicode=True)
        
        print(f"✅ Šaltinių registras išsaugotas: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Klaida išsaugant šaltinių registrą {filename}: {e}")
        return False

# CrewAI Tools
@tool
def load_knowledge_base_tool(filename: str = "ziniu_baze.yaml") -> str:
    """
    Įkrauna žinių bazę iš YAML failo.
    
    Args:
        filename: Failo pavadinimas
        
    Returns:
        Žinių bazės turinys kaip tekstas
    """
    knowledge_base = load_knowledge_base(filename)
    return yaml.dump(knowledge_base, default_flow_style=False, allow_unicode=True)

@tool
def save_knowledge_base_tool(content: str, filename: str = "ziniu_baze.yaml") -> str:
    """
    Išsaugo žinių bazę į YAML failą.
    
    Args:
        content: YAML formatuotas turinys
        filename: Failo pavadinimas
        
    Returns:
        Rezultato pranešimas
    """
    try:
        # Konvertuoti tekstą į Python duomenų struktūrą
        data = yaml.safe_load(content)
        if not isinstance(data, list):
            data = [data] if data else []
        
        success = save_knowledge_base(data, filename)
        return "✅ Žinių bazė sėkmingai išsaugota" if success else "❌ Nepavyko išsaugoti žinių bazės"
    except Exception as e:
        return f"❌ Klaida išsaugant žinių bazę: {e}"

@tool
def load_source_registry_tool(filename: str = "source_registry.yaml") -> str:
    """
    Įkrauna šaltinių registrą iš YAML failo.
    
    Args:
        filename: Failo pavadinimas
        
    Returns:
        Šaltinių registro turinys kaip tekstas
    """
    source_registry = load_source_registry(filename)
    return yaml.dump(source_registry, default_flow_style=False, allow_unicode=True)

@tool
def file_write_tool(content: str, filename: str) -> str:
    """
    Rašo turinį į failą.
    
    Args:
        content: Turinys
        filename: Failo pavadinimas
        
    Returns:
        Rezultato pranešimas
    """
    try:
        file_path = PROJECT_ROOT / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"✅ Failas sėkmingai išsaugotas: {file_path}"
    except Exception as e:
        return f"❌ Klaida rašant failą {filename}: {e}"

@tool
def yaml_read_tool(filename: str) -> str:
    """
    Skaito YAML failą.
    
    Args:
        filename: Failo pavadinimas
        
    Returns:
        Failo turinys kaip tekstas
    """
    try:
        file_path = PROJECT_ROOT / filename
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return f"❌ Failas nerastas: {file_path}"
    except Exception as e:
        return f"❌ Klaida skaitant failą {filename}: {e}"

@tool
def fact_checker_tool(claim: str) -> str:
    """
    Tikrina faktų teisingumą naudojant internetinę paiešką.
    
    Args:
        claim: Teiginys, kurį reikia patikrinti
        
    Returns:
        Patikrinimo rezultatas
    """
    # Placeholder implementacija - realiai naudotų SerperDevTool ar kt.
    return f"📋 Fakto tikrinimas: '{claim}' - Reikalingas detalesnis tikrinimas su išoriniais šaltiniais."
