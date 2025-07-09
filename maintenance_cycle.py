# /AgentForge/maintenance_cycle.py

import config
from crewai import Crew, Process
from agents import researcher_agent, architect_agent
from tasks_maintenance import research_task, architect_task

def run_maintenance_cycle():
    """
    Funkcija, kuri sukuria ir paleidžia Palaikymo Ciklo komandą.
    """
    print("### Pradedamas Žinių Bazės Palaikymo Ciklas... ###")
    print("### Tai gali užtrukti kelias minutes... ###")

    # Sukuriame komandą Palaikymo ciklui
    maintenance_crew = Crew(
        agents=[researcher_agent, architect_agent],
        tasks=[research_task, architect_task],
        process=Process.sequential,
        verbose=True
    )

    result = maintenance_crew.kickoff()

    print("\n\n########################")
    print("## Palaikymo Ciklo Rezultatas:")
    print("########################\n")
    print(result)