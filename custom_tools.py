# /AgentForge/custom_tools.py

import yaml
from langdetect import detect
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

# --- TOOL 4: Language Detection Tool ---
@tool("Language Detection Tool")
def detect_language_tool(text: str) -> str:
    """Use this tool to detect the language of a given text.
    The tool takes one argument:
    - text: The text content to analyze.
    Returns the detected language code (e.g., 'en', 'lt').
    """
    try:
        lang_code = detect(text)
        return f"Detected language: {lang_code}"
    except Exception:
        # If detection fails, assume English
        return "Detected language: en"

# --- TOOL 5: Text Translation Tool ---
@tool("Text Translation Tool")
def translate_text_tool(text_to_translate: str, target_language: str) -> str:
    """Use this tool to translate text into the specified language.
    Arguments:
    - text_to_translate: the text to translate.
    - target_language: the target language (e.g., 'Lithuanian').
    """
    translator_agent = Agent(
        role="Professional Translator",
        goal=f"Accurately and naturally translate the given text into {target_language}.",
        backstory="""You are an experienced linguist and translator, well-versed in both the source and target languages. Your goal is to produce fluent, idiomatic, and contextually appropriate translations.""",
        verbose=False,
        allow_delegation=False,
        tools=[]
    )

    translation_task = Task(
        description=f"""Translate this text into {target_language}:
        ---
        {text_to_translate}
        ---""",
        expected_output="Translated text.",
        agent=translator_agent
    )

    temp_crew = Crew(
        agents=[translator_agent],
        tasks=[translation_task],
        verbose=False
    )

    translated_result = temp_crew.kickoff()
    return translated_result

# --- TOOL 6: Knowledge Base Tools ---
@tool("Knowledge Base Loader")
def load_knowledge_base_tool(filepath="ziniu_baze.yaml"):
    """Use this tool to load the knowledge base from a YAML file.
    The tool takes one argument:
    - filepath: The path to the knowledge base YAML file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return yaml.dump(data.get("knowledge", []))
    except Exception as e:
        return f"Error loading knowledge base: {e}"

@tool("Knowledge Base Saver")
def save_knowledge_base_tool(knowledge_yaml: str, filepath="ziniu_baze.yaml"):
    """Use this tool to save the knowledge base to a YAML file.
    The tool takes two arguments:
    - knowledge_yaml: The YAML string representation of the knowledge.
    - filepath: The path to the knowledge base YAML file.
    """
    try:
        knowledge = yaml.safe_load(knowledge_yaml)
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.safe_dump({"knowledge": knowledge}, f, allow_unicode=True)
        return f"Knowledge base successfully saved at: {filepath}"
    except Exception as e:
        return f"Error saving knowledge base: {e}"

# --- TOOL 7: Source Registry Tools ---
@tool("Source Registry Loader")
def load_source_registry_tool(filepath="source_registry.yaml"):
    """Use this tool to load the source registry from a YAML file.
    The tool takes one argument:
    - filepath: The path to the source registry YAML file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return yaml.dump(data.get("sources", []))
    except Exception as e:
        return f"Error loading source registry: {e}"

@tool("Source Registry Saver")
def save_source_registry_tool(sources_yaml: str, filepath="source_registry.yaml"):
    """Use this tool to save the source registry to a YAML file.
    The tool takes two arguments:
    - sources_yaml: The YAML string representation of the sources.
    - filepath: The path to the source registry YAML file.
    """
    try:
        sources = yaml.safe_load(sources_yaml)
        with open(filepath, "w", encoding="utf-8") as f:
            yaml.safe_dump({"sources": sources}, f, allow_unicode=True)
        return f"Source registry successfully saved at: {filepath}"
    except Exception as e:
        return f"Error saving source registry: {e}"

# Helper functions for internal use (not exposed as tools)
def load_knowledge_base(filepath="ziniu_baze.yaml"):
    """Load the knowledge base from a YAML file as a Python list."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("knowledge", [])

def save_knowledge_base(knowledge, filepath="ziniu_baze.yaml"):
    """Save the knowledge base (list of dicts) to a YAML file."""
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.safe_dump({"knowledge": knowledge}, f, allow_unicode=True)

def load_source_registry(filepath="source_registry.yaml"):
    """Load the source registry from a YAML file as a Python list."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("sources", [])

def save_source_registry(sources, filepath="source_registry.yaml"):
    """Save the source registry (list of dicts) to a YAML file."""
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.safe_dump({"sources": sources}, f, allow_unicode=True)