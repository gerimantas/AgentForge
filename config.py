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

# Nustatome OpenAI API raktą kaip OS aplinkos kintamąjį.
# Tai yra būtina, nes CrewAI biblioteka ieško rakto būtent per os.environ.
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY