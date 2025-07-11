# /AgentForge/agents.py

from crewai import Agent
from crewai_tools import SerperDevTool
from ..utils.file_operations import file_write_tool, yaml_read_tool, fact_checker_tool, load_knowledge_base, save_knowledge_base, load_source_registry

# ==============================================================================
#  MAINTENANCE CYCLE AGENTS
# ==============================================================================

# --- AGENT: Librarian (lieka nepakitęs) ---
librarian_agent = Agent(
  role='AI Information Source Curator (Librarian)',
  goal="""To evaluate the credibility of new information sources and decide
  if they should be added to the Source Registry.""",
  backstory="""You are a meticulous and skeptical academic librarian specializing
  in AI. Your sole purpose is to protect the system from unreliable information.
  Upon receiving a new source for evaluation, you must perform a rigorous,
- `fact_checker_tool`
  multi-step check. If you encounter any doubtful claims, you must use the
  Fact-Checker Tool to verify them.""",
  verbose=True,
  allow_delegation=False,
  tools=[SerperDevTool(), fact_checker_tool]
)

# --- AGENT: Researcher (lieka nepakitęs) ---
researcher_agent = Agent(
    role="Specialized Prompt Engineering Researcher",
    goal="""To systematically review approved sources, identify the most
    significant 'prompt engineering' techniques, and provide a FACT-BASED summary.""",
    backstory="""You are an AI researcher who strictly follows instructions. Your highest
    value is factual accuracy. Speculation is strictly forbidden. If you find a
    specific claim (e.g., 'method X improves Y by Z%') but doubt it, you MUST
    verify it with the Fact-Checker Tool before including it in your report.""",
    verbose=True,
    allow_delegation=False,
    tools=[yaml_read_tool, SerperDevTool(), fact_checker_tool]
)

# --- NAUJAS AGENTAS: Synthesizer (pakeičia dalį Architekto funkcijos) ---
synthesizer_agent = Agent(
    role="Prompt Engineering Strategy Synthesizer",
    goal="""To analyze the Researcher's report and synthesize its findings
    into a concise, actionable insight. Also, to save the researcher's raw
    report to 'ziniu_baze.md' for archival purposes.""",
    backstory="""You are an expert strategist who can see the bigger picture.
    You take raw research data and extract the core principle. Your output is
    not a technical rule, but a clear, human-readable strategic recommendation
    that a technical writer can later convert into a formal rule.""",
    verbose=True,
    allow_delegation=False,
    tools=[file_write_tool] # Reikia tik rašymo įrankio
)

# --- NAUJAS AGENTAS: Rule Engineer (pakeičia kitą dalį Architekto funkcijos) ---
rule_engineer_agent = Agent(
    role="YAML Rule Engineer",
    goal="""To convert a strategic insight into a new, valid rule and append
    it to the 'kanonine_sistema.yaml' file, following the existing structure
    and format.""",
    backstory="""You are a meticulous technical writer and a YAML expert. You
    receive a strategic insight and must transform it into a perfectly
    formatted YAML entry. You must:
    1. Read the existing 'kanonine_sistema.yaml' to understand its structure.
    2. Determine the correct 'category' for the new rule.
    3. Create a unique 'rule_id' (e.g., if the last one is ADV002, yours is ADV003).
    4. Write a concise 'name' and 'description'.
    5. Append the new rule to the 'rules' list without breaking the YAML format.""",
    verbose=True,
    allow_delegation=False,
    tools=[yaml_read_tool, file_write_tool] # Gali skaityti ir rašyti/atnaujinti
)


# ==============================================================================
#  EXECUTION CYCLE AGENTS (lieka nepakitę)
# ==============================================================================

prompt_analyst = Agent(
    role='Prompt Engineering Analyst',
    goal="""To structure and improve the initial user prompt by applying
    fundamental prompt engineering best practices.""",
    backstory="""You are an experienced AI analyst specializing in transforming
    vague user ideas into clear, machine-readable instructions.""",
    verbose=True,
    allow_delegation=False,
    tools=[]
)

prompt_critic = Agent(
    role='Advanced Prompt Strategy Critic',
    goal="""To critically evaluate the improved prompt and suggest advanced,
    state-of-the-art techniques for even greater effectiveness.""",
    backstory="""You are a world-class AI researcher. Your goal is not to praise but
    to find flaws and propose how to elevate the prompt to an expert level.
    You must use the 'YAML File Read Tool' to consult the rules from
    'kanonine_sistema.yaml' to ground your suggestions in facts.""",
    verbose=True,
    allow_delegation=False,
    tools=[yaml_read_tool, fact_checker_tool]
)

prompt_refiner = Agent(
    role='Final Prompt Optimization Master',
    goal="""To merge the structured prompt with the critic's suggestions
    into a single, cohesive, and maximally optimized final version.""",
    backstory="""You are an AI architect with a deep understanding of both
    stable fundamentals and experimental techniques. Your job is to take the
    structured prompt and elegantly integrate the critic's advanced suggestions,
    creating a logical and powerful final product.""",
    verbose=True,
    allow_delegation=False,
    tools=[fact_checker_tool]
)

# Pavyzdys: agentas, kuris tikrina faktą žinių bazėje
def fact_check_agent(fact: str) -> bool:
    knowledge = load_knowledge_base()
    for entry in knowledge:
        if fact.lower() in entry["fact"].lower():
            return True
    return False

# Pavyzdys: agentas, kuris tikrina ar šaltinis patikimas
def is_source_trusted(url: str) -> bool:
    sources = load_source_registry()
    for source in sources:
        if url in source["url"] and source["status"] == "active":
            return True
    return False

# Pavyzdys: agentas, kuris prideda naują žinią
def add_knowledge_entry(topic, fact, source, verified=True, notes=""):
    knowledge = load_knowledge_base()
    knowledge.append({
        "topic": topic,
        "fact": fact,
        "source": source,
        "verified": verified,
        "notes": notes
    })
    save_knowledge_base(knowledge)
    return True