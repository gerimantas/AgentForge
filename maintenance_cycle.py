# /AgentForge/maintenance_cycle.py

import config
from crewai import Crew, Process
# Importuojame MŪSŲ naujus Palaikymo Ciklo agentus
from agents import researcher_agent, synthesizer_agent, rule_engineer_agent
# Importuojame MŪSŲ naujas Palaikymo Ciklo užduotis
from tasks_maintenance import research_task, synthesis_task, rule_engineering_task

def run_maintenance_cycle():
    """
    Funkcija, kuri sukuria ir paleidžia Palaikymo Ciklo komandą.
    """
    print("\n### Pradedamas Žinių Bazės Palaikymo Ciklas (3-agentų logika)... ###")
    print("### Tai gali užtrukti kelias minutes... ###")

    # Sukuriame komandą Palaikymo ciklui su nauja agentų grandine
    maintenance_crew = Crew(
        agents=[researcher_agent, synthesizer_agent, rule_engineer_agent],
        tasks=[research_task, synthesis_task, rule_engineering_task],
        process=Process.sequential,
        verbose=True
    )

    result = maintenance_crew.kickoff()

    print("\n\n########################")
    print("## Palaikymo Ciklo Rezultatas:")
    print("########################\n")
    print(result)