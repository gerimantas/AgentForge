# /AgentForge/run_curation.py

# 1. Importuojame reikiamus komponentus
import config  # Užtikrina, kad API raktai būtų nustatyti
from crewai import Crew, Process, Task
from agents import librarian_agent

# 2. Apibrėžiame užduotį Bibliotekininkui
# Ši užduotis prašo įvertinti naują, potencialų šaltinį.
# '{new_source_url}' bus pakeistas reikšme, kurią perduosime paleidžiant.
curation_task = Task(
    description="""Įvertink šio naujo informacijos šaltinio patikimumą:
    URL: {new_source_url}

    Atlik išsamią analizę pagal savo vidines instrukcijas (autoritetas,
    kryžminis patikrinimas, turinio kokybė). Pateik galutinį verdiktą
    ir išsamius argumentus.""",
    expected_output="""Detali analizė, suskirstyta į tris dalis:
    1. Autoritetas.
    2. Kryžminis Patikrinimas.
    3. Turinio Kokybė.
    Pabaigoje turi būti aiškus verdiktas: REKOMENDUOJAMA ĮTRAUKTI arba ATMESTAS.""",
    agent=librarian_agent
)

# 3. Sukuriame komandą (Crew), skirtą šiai vienai užduočiai
curation_crew = Crew(
    agents=[librarian_agent],
    tasks=[curation_task],
    process=Process.sequential,
    verbose=True
)

# 4. Paleidžiame komandos darbą su konkrečiais pradiniais duomenimis
if __name__ == "__main__":
    # Apibrėžiame naują šaltinį, kurį norime patikrinti.
    # Pavyzdžiui, paimkime žinomo DI tyrėjo Andrej Karpathy blogą.
    naujas_saltinis = "https://karpathy.ai/"

    print(f"### Pradedama naujo šaltinio patikra: {naujas_saltinis} ###")

    # "kickoff" metodui perduodame žodyną su pradiniais duomenimis.
    result = curation_crew.kickoff(
        inputs={'new_source_url': naujas_saltinis}
    )

    print("\n\n########################")
    print("## Bibliotekininko Verdiktas:")
    print("########################\n")
    print(result)