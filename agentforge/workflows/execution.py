"""
AgentForge Execution Cycle
=========================

Šis modulis vykdo prompt optimizacijos ciklą.
"""

import sys
from typing import Optional, List
from agentforge.agents import prompt_analyst, prompt_critic, prompt_refiner
from agentforge.agents.simple_agents import BaseAgent
from agentforge.workflows.tasks.execution_tasks import create_execution_tasks
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
        return "\\n".join(results)

def run_execution_cycle(query: str, verbose: bool = True) -> Optional[str]:
    """
    Vykdo prompt optimizacijos ciklą.
    
    Args:
        query: Vartotojo užklausa
        verbose: Ar rodyti detalią informaciją
        
    Returns:
        Optimizuotas prompt'as arba None jei klaida
    """
    try:
        # Tikrinti API raktus
        validate_api_keys()
        
        if verbose:
            print(f"\\n🚀 Pradedamas vykdymo ciklas")
            print(f"📝 Užklausa: {query}")
            print("-" * 50)
        
        # Sukurti užduotis
        analysis_task, critique_task, refinement_task = create_execution_tasks(query)
        
        # Sukurti agentų komandą
        crew = SimpleCrew(
            agents=[prompt_analyst, prompt_critic, prompt_refiner],
            tasks=[analysis_task, critique_task, refinement_task],
            verbose=verbose
        )
        
        # Vykdyti optimizacijos procesą
        if verbose:
            print("⚙️  Vykdomas optimizacijos procesas...")
        
        result = crew.kickoff()
        
        if verbose:
            print("✅ Vykdymo ciklas baigtas sėkmingai!")
            print(f"📊 Rezultatas:")
            print("-" * 50)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Rezultato tipas: {type(result)}")
                print(f"Rezultatas: {result}")
        
        return str(result) if result else None
        
    except Exception as e:
        print(f"❌ Klaida vykdant optimizacijos ciklą: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        return None

def test_execution_cycle():
    """
    Testavimo funkcija vykdymo ciklui.
    """
    print("\\n🧪 Testuojamas vykdymo ciklas...")
    
    test_query = "Kaip sukurti gerą prompt'ą dirbtinio intelekto sistemai?"
    result = run_execution_cycle(test_query, verbose=True)
    
    if result:
        print(f"\\n✅ Testas sėkmingas!")
        print(f"📝 Rezultatas: {result[:200]}...")
    else:
        print("\\n❌ Testas nepavyko!")
    
    return result is not None

if __name__ == "__main__":
    test_execution_cycle()
