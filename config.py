# /AgentForge/config.py

import os
from dotenv import load_dotenv

# Užkrauname aplinkos kintamuosius iš .env failo
# Bet kuris scenarijus, kuris importuos šį failą, automatiškai
# įvykdys šią eilutę.
load_dotenv()

# Nuskaitome API raktus iš aplinkos ir patikriname, ar jie egzistuoja
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not OPENAI_API_KEY or not SERPER_API_KEY:
    raise ValueError(
        "KRITINĖ KLAIDA: OPENAI_API_KEY arba SERPER_API_KEY nėra nustatyti .env faile."
    )

# Papildomi konfigūracijos nustatymai su saugikliais
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "3"))  # Sumažinam default reikšmę nuo 10 iki 3
VERBOSE = os.getenv("VERBOSE", "True").lower() == "true"

# Tikrinama, ar MAX_ITERATIONS yra protingo dydžio
if MAX_ITERATIONS > 5:
    print(f"WARNING: MAX_ITERATIONS set to {MAX_ITERATIONS}, which may cause slow performance.")
    print("Consider setting it to a lower value (1-3) in .env file.")

# Nustatome OpenAI API raktą kaip OS aplinkos kintamąjį.
# Tai yra būtina, nes CrewAI biblioteka ieško rakto būtent per os.environ.
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# --- SISTEMOS SAUGIKLIAI IR NUSTATYMAI ---

# Maksimalus iteracijų skaičius Vykdymo Ciklui,
# siekiant išvengti begalinių ciklų.
MAX_ITERATIONS = 15