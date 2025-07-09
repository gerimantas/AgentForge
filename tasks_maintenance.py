# /AgentForge/tasks_maintenance.py

from crewai import Task
from agents import researcher_agent, architect_agent

# Apibrėžiame tyrimo užduotį Žvalgui
research_task = Task(
    description=f"""Peržiūrėk patikimų šaltinių sąrašą faile 'source_registry.yaml'
    naudodamas YAML Skaitymo Įrankį. Sistemingai patikrink kiekvieną 'active'
    statusą turintį šaltinį ir surask naujausią informaciją (paskutinių 3-6 mėn.)
    susijusią su 'prompt engineering' technikomis. Apibendrink savo radinius.""",
    expected_output="""Struktūrizuota tekstinė ataskaita, kurioje apžvelgiamos
    2-3 svarbiausios rastos technikos ar įžvalgos. Kiekviena įžvalga turi
    būti trumpai aprašyta ir pateikta su nuoroda į pirminį šaltinį.""",
    agent=researcher_agent
)

# Apibrėžiame taisyklių kūrimo užduotį Architektui
architect_task = Task(
    description="""Išanalizuok Žvalgo pateiktą ataskaitą apie naujas technikas.
    Pirma, išsaugok visą gautą ataskaitą į 'ziniu_baze.md' failą
    naudodamas Failo Įrašymo Įrankį. Antra, remdamasis šia ataskaita,
    suformuluok 3-5 universalias, aukšto lygio taisykles arba principus,
    kuriais turėtų vadovautis kiti agentai, optimizuodami užklausas.
    Šias taisykles įrašyk į 'kanonine_sistema.md' failą.""",
    expected_output="""Sėkmės pranešimas, patvirtinantis, kad abu failai
    ('ziniu_baze.md' ir 'kanonine_sistema.md') buvo sukurti/atnaujinti.""",
    agent=architect_agent,
    context=[research_task]
)