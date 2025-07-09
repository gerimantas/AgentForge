# 1. Importuojame reikiamas klases ir bibliotekas
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# 2. Įkeliame aplinkos kintamuosius (API raktus) iš .env failo
load_dotenv()

# Patikriname, ar API raktai yra nustatyti
openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

if not openai_api_key or not serper_api_key:
    raise ValueError("OPENAI_API_KEY and SERPER_API_KEY must be set in the .env file.")

# 3. Sukuriame paieškos įrankį
# Agentai naudos šį įrankį informacijos paieškai internete
search_tool = SerperDevTool()

# 4. Apibrėžiame mūsų agentus
# Kiekvienas agentas turi rolę, tikslą ir "biografiją" (backstory),
# kas padeda LLM geriau suprasti jo kontekstą.

# Mūsų schemos atitikmuo: Žvalgas (Researcher)
market_researcher = Agent(
  role='Rinkos Tyrimų Analitikas',
  goal='Rasti naujausias ir aktualiausias AI tendencijas Lietuvoje',
  backstory="""Esi patyręs rinkos tyrimų analitikas, dirbantis pirmaujančioje
  technologijų įmonėje. Tavo specializacija - Vidurio ir Rytų Europos rinka,
  ypač domiesi dirbtinio intelekto adaptacija versle.""",
  verbose=True, # Leidžia matyti agento "minčių eigą" terminale
  allow_delegation=False, # Šis agentas negali perduoti užduočių kitiems
  tools=[search_tool] # Įrankiai, kuriuos agentas gali naudoti
)

# Mūsų schemos atitikmuo: Analitikas (panašus į Kritiką/Tobulintoją)
tech_analyst = Agent(
  role='Technologijų Strategijos Analitikas',
  goal='Išanalizuoti rinkos duomenis ir suformuluoti strategines įžvalgas',
  backstory="""Esi technologijų strategas, gebantis paversti sausus
  rinkos duomenis į aiškias, praktiškai pritaikomas verslo strategijas.
  Tavo tikslas - pateikti vadovybei 3 svarbiausias įžvalgas.""",
  verbose=True,
  allow_delegation=True # Šis agentas gali deleguoti užduotis (nors šiuo metu nėra kam)
)

# 5. Apibrėžiame užduotis agentams
research_task = Task(
  description="""Atlik išsamią analizę apie dirbtinio intelekto (AI)
  pritaikymo tendencijas Lietuvos verslo sektoriuje 2024-2025 metais.
  Identifikuok pagrindinius sektorius, kur AI taikomas aktyviausiai.""",
  expected_output='Išsami ataskaita, apimanti ne mažiau kaip 500 žodžių, su konkrečiais pavyzdžiais ir statistika.',
  agent=market_researcher # Šią užduotį vykdys market_researcher
)

analysis_task = Task(
  description="""Peržiūrėk rinkos tyrimų ataskaitą apie AI tendencijas Lietuvoje.
  Remdamasis šia ataskaita, suformuluok 3 pagrindines strategines įžvalgas
  technologijų įmonės vadovybei. Įžvalgos turi būti aiškios, trumpos ir paremtos duomenimis.""",
  expected_output='Trys sunumeruoti strateginių įžvalgų punktai su trumpais paaiškinimais.',
  agent=tech_analyst, # Šią užduotį vykdys tech_analyst
  context=[research_task] # Svarbu: šios užduoties kontekstas yra praeitos užduoties rezultatas
)

# 6. Susiejame agentus ir užduotis į Komandą (Crew)
# Procesas gali būti 'sequential' (vienas po kito) arba 'hierarchical'
projekt1_crew = Crew(
  agents=[market_researcher, tech_analyst],
  tasks=[research_task, analysis_task],
  process=Process.sequential,
  verbose=True # Pakeista iš '2' į 'True'
)

# 7. Paleidžiame komandos darbą!
result = projekt1_crew.kickoff()

print("\n\n########################")
print("## Komandos darbo rezultatas:")
print("########################\n")
print(result)