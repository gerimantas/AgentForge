# /AgentForge/agentforge/core/config.py

import os
from pathlib import Path

# Rasime projekto šakninį katalogą
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Pabandysime užkrauti dotenv jei galima
try:
    from dotenv import load_dotenv
    # Ieškome .env failo projekto šaknyje
    env_path = PROJECT_ROOT / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"✅ Loaded .env from {env_path}")
    else:
        print(f"⚠️  No .env file found at {env_path}")
except ImportError:
    print("⚠️  python-dotenv not installed, using system environment variables")

def get_api_key(key_name):
    """Safely get API key with error handling."""
    key = os.getenv(key_name)
    if not key:
        print(f"WARNING: {key_name} not found in environment variables")
        return None
    return key

def validate_api_keys():
    """Validate that required API keys are present."""
    missing_keys = []
    if not OPENAI_API_KEY:
        missing_keys.append("OPENAI_API_KEY")
    if not SERPER_API_KEY:
        missing_keys.append("SERPER_API_KEY")
    
    if missing_keys:
        raise ValueError(
            f"KRITINĖ KLAIDA: Šie API raktai neegzistuoja: {', '.join(missing_keys)}"
        )
    return True

# Nuskaitome API raktus iš aplinkos
OPENAI_API_KEY = get_api_key("OPENAI_API_KEY")
SERPER_API_KEY = get_api_key("SERPER_API_KEY")

# Nustatome OpenAI API raktą kaip OS aplinkos kintamąjį jei jis egzistuoja
if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
if SERPER_API_KEY:
    os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# Papildomi konfigūracijos nustatymai
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "3"))
VERBOSE = os.getenv("VERBOSE", "True").lower() == "true"

# Tikrinama, ar MAX_ITERATIONS yra protingo dydžio
if MAX_ITERATIONS > 5:
    print(f"WARNING: MAX_ITERATIONS set to {MAX_ITERATIONS}, which may cause slow performance.")
    print("Consider setting it to a lower value (1-3) in .env file.")

# Maksimalus iteracijų skaičius Vykdymo Ciklui
MAX_ITERATIONS = 15

# Temperatūros nustatymai skirtingiems modeliams
TEMPERATURE = 0.7

# Modelių nustatymai
MODELS = {
    "default": "gpt-4o-mini",
    "advanced": "gpt-4o",
    "fast": "gpt-3.5-turbo"
}

def validate_api_keys():
    """Validate that required API keys are present."""
    if not OPENAI_API_KEY or not SERPER_API_KEY:
        raise ValueError(
            "KRITINĖ KLAIDA: OPENAI_API_KEY arba SERPER_API_KEY nėra nustatyti .env faile."
        )
    return True

# Papildomi konfigūracijos nustatymai su saugikliais
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "3"))  # Sumažinam default reikšmę nuo 10 iki 3
VERBOSE = os.getenv("VERBOSE", "True").lower() == "true"

# Tikrinama, ar MAX_ITERATIONS yra protingo dydžio
if MAX_ITERATIONS > 5:
    print(f"WARNING: MAX_ITERATIONS set to {MAX_ITERATIONS}, which may cause slow performance.")
    print("Consider setting it to a lower value (1-3) in .env file.")

# Nustatome OpenAI API raktą kaip OS aplinkos kintamąjį.
# Tai yra būtina, nes CrewAI biblioteka ieško rakto būtent per os.environ.
if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
if SERPER_API_KEY:
    os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# --- SISTEMOS SAUGIKLIAI IR NUSTATYMAI ---

# Maksimalus iteracijų skaičius Vykdymo Ciklui,
# siekiant išvengti begalinių ciklų.
MAX_ITERATIONS = 15