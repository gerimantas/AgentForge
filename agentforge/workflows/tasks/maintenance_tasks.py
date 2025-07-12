"""
AgentForge Maintenance Tasks
===========================

Šis modulis saugo palaikymo ciklo užduotis (tasks).
"""

from textwrap import dedent
from agentforge.agents.simple_agents import SimpleTask
from agentforge.agents import researcher_agent, synthesizer_agent, rule_engineer_agent
# Note: Temporarily removing tool imports for Stage 2 compatibility
# from agentforge.utils.file_operations import load_knowledge_base_tool, save_knowledge_base_tool, load_source_registry_tool

# Tyrimų užduotis
research_task = SimpleTask(
    description=dedent("""
    Atlik sisteminį tyrimą apie prompt engineering metodikas ir technikas.
    
    Tavo užduotis:
    1. Peržiūrėk patvirtintus šaltinius iš šaltinių registro
    2. Identifikuok svarbiausius prompt engineering principus
    3. Surink faktais pagrįstus duomenis
    4. Patikrink informacijos tikslumą
    
    Naudok tik patvirtintus šaltinius ir būk objektyvus.
    """),
    expected_output=dedent("""
    Detalizuotas tyrimų raportas su:
    - Raktinių principų sąrašu
    - Faktais pagrįstais duomenimis
    - Šaltinių nuorodomis
    - Rekomendacijomis
    """),
    agent=researcher_agent,
    tools=[]  # Simplified tools for now
)

# Sintezės užduotis
synthesis_task = SimpleTask(
    description=dedent("""
    Išanalizuok tyrėjo ataskaitą ir sukurk strateginius sprendimus.
    
    Tyrimo rezultatai: {research_result}
    
    Tavo užduotis:
    1. Išanalizuoti tyrimo duomenis
    2. Nustatyti pagrindinius principus
    3. Sukurti strateginius sprendimus
    4. Išsaugoti tyrimų duomenis žinių bazėje
    
    Orientuokis į praktinį pritaikymą.
    """),
    expected_output=dedent("""
    Strateginių sprendimų raportas su:
    - Pagrindiniais principais
    - Praktiniais rekomendacijomis
    - Įgyvendinimo gairėmis
    - Išsaugotais duomenimis
    """),
    agent=synthesizer_agent,
    tools=[]  # Simplified tools for now
)

# Taisyklių inžinerijos užduotis
rule_engineering_task = SimpleTask(
    description=dedent("""
    Sukurk formalias taisykles pagal strateginius sprendimus.
    
    Strateginiai sprendimai: {synthesis_result}
    
    Tavo užduotis:
    1. Konvertuoti strateginius sprendimus į taisykles
    2. Sukurti aiškias gaires
    3. Apibrėžti taikymo sritis
    4. Patikrinti taisyklių nuoseklumą
    
    Taisyklės turi būti:
    - Aiškios ir konkrečios
    - Lengvai taikomos
    - Veiksmingos
    - Suderinamos su esamomis
    """),
    expected_output=dedent("""
    Formalių taisyklių dokumentas su:
    - Struktūrizuotomis taisyklėmis
    - Taikymo pavyzdžiais
    - Įgyvendinimo gairėmis
    - Kokybes kriterijais
    """),
    agent=rule_engineer_agent,
    tools=[]  # Simplified tools for now
)

def create_maintenance_tasks():
    """
    Sukuria palaikymo ciklo užduotis.
    
    Returns:
        Tuple iš trijų užduočių
    """
    return research_task, synthesis_task, rule_engineering_task
