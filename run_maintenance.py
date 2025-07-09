# /AgentForge/run_maintenance.py

import config
from crewai import Crew, Process
from agents import researcher_agent, architect_agent
from tasks_maintenance import research_task, architect_task

# Sukuriame komandą Palaikymo ciklui
maintenance_crew = Crew(
    agents=[researcher_agent, architect_agent],
    tasks=[research_task, architect_task],
    process=Process.sequential,
    verbose=True
)

# Paleidžiame komandos darbą
if __name__ == "__main__":
    print("### Pradedamas Žinių Bazės Palaikymo Ciklas... ###")

    result = maintenance_crew.kickoff()

    print("\n\n########################")
    print("## Palaikymo Ciklo Rezultatas:")
    print("########################\n")
    print(result)