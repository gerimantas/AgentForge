# /AgentForge/custom_tools.py

import yaml
from crewai.tools import tool
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# --- TOOL 1: File Write Tool ---
@tool("File Write Tool")
def file_write_tool(file_path: str, text: str) -> str:
    """Use this tool to write text into a file.
    The tool takes two arguments:
    - file_path: The path to the file you want to write to.
    - text: The text content to write into the file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return f"File successfully saved at: {file_path}"
    except Exception as e:
        return f"Error writing file: {e}"

# --- TOOL 2: YAML File Read Tool ---
@tool("YAML File Read Tool")
def yaml_read_tool(file_path: str) -> str:
    """Use this tool to read the contents of a YAML file.
    The tool takes one argument:
    - file_path: The path to the YAML file you want to read.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.dump(yaml.safe_load(f))
    except Exception as e:
        return f"Error reading YAML file: {e}"

# --- TOOL 3: Fact-Checking Tool ---
@tool("Fact-Checking Tool")
def fact_checker_tool(statement: str) -> str:
    """Use this tool to verify a specific statement.
    The tool returns one of three possible answers: 'CONFIRMED_TRUE',
    'CONFIRMED_FALSE', or 'UNVERIFIABLE'.
    The tool takes one argument:
    - statement: The statement that needs to be checked.
    """
    fact_checker_agent = Agent(
        role="Fact Checker",
        goal=f"""Thoroughly verify the factual accuracy of the statement '{statement}'.
        Use the search tool to find reliable sources (news agencies, encyclopedias,
        scientific papers) that either confirm or deny this statement.
        Be objective and unbiased.""",
        backstory="""You are a seasoned fact-checker working for a major news
        agency. Your specialty is debunking disinformation and separating
        facts from opinions.""",
        verbose=False,
        allow_delegation=False,
        tools=[SerperDevTool()]
    )

    fact_checking_task = Task(
        description=f"""Verify the following statement: '{statement}'.
        Provide the final answer as ONE of these three strings:
        CONFIRMED_TRUE, CONFIRMED_FALSE, UNVERIFIABLE.
        Add a single sentence explaining your decision.""",
        expected_output="The final verdict and a brief explanation.",
        agent=fact_checker_agent
    )

    temp_crew = Crew(
        agents=[fact_checker_agent],
        tasks=[fact_checking_task],
        verbose=False
    )

    result = temp_crew.kickoff()
    return result
# /AgentForge/custom_tools.py ... (pridėti pabaigoje)

from langdetect import detect

# ... (ankstesnių įrankių kodas) ...


# --- ĮRANKIS NR. 4: Kalbos Atpažinimas ---
# Šiam įrankiui nereikia @tool dekoratoriaus, nes jį naudosime tiesiogiai
# Python kode, o ne per agentą.
def detect_language(text: str) -> str:
    """Nustato teksto kalbos kodą (pvz., 'en', 'lt')."""
    try:
        lang_code = detect(text)
        return lang_code
    except:
        # Jei nepavyksta nustatyti, darome prielaidą, kad tai anglų k.
        return "en"


# --- ĮRANKIS NR. 5: Teksto Vertimas ---
# Sukuriame specializuotą įrankį, kuris veiks kaip vertimo paslauga.
@tool("Teksto Vertimo Įrankis")
def translate_text_tool(text_to_translate: str, target_language: str) -> str:
    """Naudok šį įrankį, kad išverstum tekstą į nurodytą kalbą.
    Įrankis priima du argumentus:
    - text_to_translate: tekstas, kurį reikia išversti.
    - target_language: kalba, į kurią reikia versti (pvz., 'Lithuanian').
    """
    # Sukuriame laikiną vertėjo agentą
    translator_agent = Agent(
        role="Profesionalus Vertėjas",
        goal=f"Tiksliai ir natūraliai išversti pateiktą tekstą į {target_language} kalbą.",
        backstory="""Esi patyręs lingvistas ir vertėjas, puikiai išmanantis
        tiek šaltinio, tiek tikslo kalbos niuansus. Tavo tikslas - ne pažodinis
        vertimas, o sklandus, idiomatiškas ir kontekstą atitinkantis tekstas.""",
        verbose=False,
        allow_delegation=False,
        # Vertėjui nereikia specifinių įrankių
        tools=[]
    )

    # Sukuriame laikiną užduotį šiam agentui
    translation_task = Task(
        description=f"""Išversk šį tekstą į {target_language} kalbą:
        ---
        {text_to_translate}
        ---""",
        expected_output="Išverstas tekstas.",
        agent=translator_agent
    )

    # Sukuriame laikiną komandą ir ją paleidžiame
    temp_crew = Crew(
        agents=[translator_agent],
        tasks=[translation_task],
        verbose=False
    )

    translated_result = temp_crew.kickoff()
    return translated_result