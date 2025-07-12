"""
AgentForge Execution Tasks
=========================

Šis modulis saugo vykdymo ciklo užduotis (tasks).
"""

from textwrap import dedent
from agentforge.agents.simple_agents import SimpleTask
from agentforge.agents import prompt_analyst, prompt_critic, prompt_refiner
# Note: Temporarily removing tool imports for Stage 2 compatibility
# from agentforge.utils.file_operations import load_knowledge_base_tool

# Analizės užduotis
analysis_task = SimpleTask(
    description=dedent("""
    Tiksliai išanalizuok šią užklausą ir nustatyk, koks prompt'as būtų optimaliausias.
    
    Užklausa: {query}
    
    Tavo analizė turi būti:
    1. Konkreti ir pagrįsta duomenimis
    2. Orientuota į rezultatą
    3. Aiškiai apibrėžianti optimizavimo tikslus
    
    Naudok žinių bazę papildomai informacijai gauti.
    """),
    expected_output=dedent("""
    Detalus prompt'o analizės raportas, kuriame būtų:
    - Užklausos tipo identifikacija
    - Siūlomi optimizavimo metodai
    - Konkretūs pagerinimo pasiūlymai
    - Tikėtinas rezultato pobūdis
    """),
    agent=prompt_analyst,
    tools=[]  # Simplified tools for now
)

# Kritikos užduotis
critique_task = SimpleTask(
    description=dedent("""
    Kritiškai įvertink analitiko pasiūlymą ir nustatyk galimus trūkumus.
    
    Analizės rezultatas: {analysis_result}
    
    Tavo kritika turi būti:
    1. Objektyvi ir konstruktyvi
    2. Pagrįsta geriausiomis praktikomis
    3. Orientuota į konkretų pagerinimą
    
    Ieškok:
    - Loginių spragų
    - Praleistų aspektų
    - Neoptimalių sprendimų
    - Galimų rizikos veiksnių
    """),
    expected_output=dedent("""
    Detalus kritikos raportas su:
    - Identifikuotais trūkumais
    - Alternatyvių sprendimų pasiūlymais
    - Rizikos vertinimu
    - Rekomendacijomis tobulinimui
    """),
    agent=prompt_critic,
    tools=[]  # Simplified tools for now
)

# Refinement užduotis
refinement_task = SimpleTask(
    description=dedent("""
    Sukurk optimalų prompt'ą atsižvelgiant į analizės ir kritikos rezultatus.
    
    Pradinė analizė: {analysis_result}
    Kritikos komentarai: {critique_result}
    
    Tavo finalinis prompt'as turi būti:
    1. Aiškus ir konkretus
    2. Optimizuotas pagal analizės išvadas
    3. Atsižvelgiantis į kritikos pastabas
    4. Praktiškai pritaikomas
    
    Pateik:
    - Galutinį optimizuotą prompt'ą
    - Trumpą paaiškinimą, kodėl šis sprendimas optimalus
    - Patarimus naudojimui
    """),
    expected_output=dedent("""
    Optimizuotas prompt'as su:
    - Aiškiai suformuluotu tekstu
    - Optimizavimo argumentais
    - Naudojimo rekomendacijomis
    - Tikėtinais rezultatais
    """),
    agent=prompt_refiner,
    tools=[]  # Simplified tools for now
)

# Konteksto kintamieji
def create_execution_tasks(query: str):
    """
    Sukuria vykdymo ciklo užduotis su konkrečia užklausa.
    
    Args:
        query: Vartotojo užklausa
        
    Returns:
        Tuple iš trijų užduočių
    """
    # Sukuriame užduotis su konkrečia užklausa
    analysis = SimpleTask(
        description=analysis_task.description.format(query=query),
        expected_output=analysis_task.expected_output,
        agent=analysis_task.agent,
        tools=analysis_task.tools
    )
    
    critique = SimpleTask(
        description=critique_task.description,
        expected_output=critique_task.expected_output,
        agent=critique_task.agent,
        tools=critique_task.tools
    )
    
    refinement = SimpleTask(
        description=refinement_task.description,
        expected_output=refinement_task.expected_output,
        agent=refinement_task.agent,
        tools=refinement_task.tools
    )
    
    return analysis, critique, refinement
