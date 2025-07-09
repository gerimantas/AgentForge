# /AgentForge/tasks_maintenance.py

from crewai import Task
# Importuojame MŪSŲ naujus Palaikymo Ciklo agentus
from agents import researcher_agent, synthesizer_agent, rule_engineer_agent

# --- MAINTENANCE CYCLE TASKS (NEW 3-STEP LOGIC) ---

# Užduotis Nr. 1: Tyrimas (lieka panaši, bet dabar rezultatas keliauja toliau)
research_task = Task(
    description=f"""Review the list of trusted sources in 'source_registry.yaml'
    using the YAML Read Tool. Systematically check each 'active'
    status source and find the latest information (last 3-6 months)
    related to 'prompt engineering' techniques. Summarize your findings.""",
    expected_output="""A structured text report outlining the 2-3 most
    important techniques or insights discovered. Each insight must be
    briefly described and include a URL to the original source.""",
    agent=researcher_agent
)

# Užduotis Nr. 2: Sintezė (nauja)
synthesis_task = Task(
    description="""Analyze the report provided by the Researcher. First, save
    the full raw report to 'ziniu_baze.md' using the File Write Tool for
    archival purposes. Second, synthesize the key findings into a single,
    concise, and actionable strategic insight. This insight should explain
    a new technique or principle in simple terms.""",
    expected_output="""A short, human-readable summary of a single strategic
    insight, ready to be passed to the Rule Engineer. For example:
    'A new technique called "Step-Back Prompting" has emerged. It involves
    asking the LLM to first take a step back and think about the broader
    concepts and principles before tackling the specific question, which
    improves reasoning in complex scenarios.'""",
    agent=synthesizer_agent,
    context=[research_task]
)

# Užduotis Nr. 3: Taisyklės Inžinerija (nauja)
rule_engineering_task = Task(
    description="""Take the strategic insight provided by the Synthesizer and
    convert it into a new, valid rule for our system. You MUST:
    1. Read 'kanonine_sistema.yaml' using the YAML Read Tool to understand
       its existing structure and find the last used rule_id.
    2. Create a new, unique rule_id (e.g., if the last was STR003, yours is STR004).
    3. Formulate a short, clear 'name' and technical 'description' for the rule.
    4. Determine the appropriate 'category' (e.g., 'Structure' or 'Advanced Reasoning').
    5. Append this new, perfectly formatted rule to the 'kanonine_sistema.yaml' file
       using the File Write Tool.""",
    expected_output="""A final confirmation message stating that the
    'kanonine_sistema.yaml' file has been successfully updated with the new rule.""",
    agent=rule_engineer_agent,
    # Svarbu: šios užduoties kontekstas yra TIK Sintetintojo rezultatas.
    context=[synthesis_task]
)