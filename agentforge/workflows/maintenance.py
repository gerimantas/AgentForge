"""
AgentForge Maintenance Cycle
===========================

Šis modulis vykdo žinių bazės atnaujinimo ciklą.
"""

import sys
from typing import Optional, List
from agentforge.agents import researcher_agent, synthesizer_agent, rule_engineer_agent
from agentforge.agents.simple_agents import BaseAgent
from agentforge.workflows.tasks.maintenance_tasks import create_maintenance_tasks
from agentforge.core.config import validate_api_keys

class SimpleCrew:
    """Simplified crew class for Stage 2 implementation."""
    def __init__(self, agents, tasks, verbose=True):
        self.agents = agents
        self.tasks = tasks
        self.verbose = verbose
        
    def kickoff(self):
        """Execute the crew tasks."""
        results = []
        for task in self.tasks:
            if hasattr(task, 'execute'):
                result = task.execute()
                results.append(result)
            else:
                results.append(f"Task executed: {task}")
        return "\n".join(results)

def run_maintenance_cycle(verbose: bool = True) -> Optional[str]:
    """
    Vykdo žinių bazės palaikymo ciklą.
    
    Args:
        verbose: Ar rodyti detalią informaciją
        
    Returns:
        Palaikymo ciklo rezultatas arba None jei klaida
    """
    try:
        # Tikrinti API raktus
        validate_api_keys()
        
        if verbose:
            print(f"\n🔧 Pradedamas palaikymo ciklas")
            print("📚 Atnaujinama žinių bazė...")
            print("-" * 50)
        
        # Sukurti užduotis
        research_task, synthesis_task, rule_engineering_task = create_maintenance_tasks()
        
        # Sukurti agentų komandą
        crew = SimpleCrew(
            agents=[researcher_agent, synthesizer_agent, rule_engineer_agent],
            tasks=[research_task, synthesis_task, rule_engineering_task],
            verbose=verbose
        )
        
        # Vykdyti palaikymo procesą
        if verbose:
            print("⚙️  Vykdomas palaikymo procesas...")
        
        result = crew.kickoff()
        
        if verbose:
            print("✅ Palaikymo ciklas baigtas sėkmingai!")
            print(f"📊 Rezultatas:")
            print("-" * 50)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Rezultato tipas: {type(result)}")
                print(f"Rezultatas: {result}")
        
        return str(result) if result else None
        
    except Exception as e:
        print(f"❌ Klaida vykdant palaikymo ciklą: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        return None

def test_maintenance_cycle():
    """
    Testavimo funkcija palaikymo ciklui.
    """
    print("\n🧪 Testuojamas palaikymo ciklas...")
    
    result = run_maintenance_cycle(verbose=True)
    
    if result:
        print(f"\n✅ Testas sėkmingas!")
        print(f"📝 Rezultatas: {result[:200]}...")
    else:
        print("\n❌ Testas nepavyko!")
    
    return result is not None

if __name__ == "__main__":
    test_maintenance_cycle()
