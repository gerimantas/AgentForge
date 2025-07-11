# /AgentForge/tasks_maintenance.py

from crewai import Task
# Importuojame MŪSŲ naujus Palaikymo Ciklo agentus
from ...agents import researcher_agent, synthesizer_agent, rule_engineer_agent
# Importuojame naujas YAML žinių bazės ir šaltinių registro funkcijas
from ...utils.file_operations import load_knowledge_base_tool, save_knowledge_base_tool, load_source_registry_tool

# --- MAINTENANCE CYCLE TASKS (NEW 3-STEP LOGIC) ---

# Užduotis Nr. 1: Tyrimas (atnaujinta naudoti load_source_registry_tool)
research_task = Task(
    description=f"""Review the list of trusted sources using the Source Registry Loader tool.
    Systematically check each 'active' status source and find the latest information (last 3-6 months)
    related to 'prompt engineering' techniques. Summarize your findings.""",
    expected_output="""A structured text report outlining the 2-3 most
    important techniques or insights discovered. Each insight must be
    briefly described and include a URL to the original source.""",
    agent=researcher_agent
)

# Užduotis Nr. 2: Sintezė (atnaujinta naudoti Knowledge Base tools)
synthesis_task = Task(
    description="""Analyze the report provided by the Researcher. First, load 
    the current knowledge base using the Knowledge Base Loader tool.
    Then, synthesize the key findings into structured knowledge entries.
    Each entry should have topic, fact, source, and verified fields.
    Finally, save the updated knowledge base using the Knowledge Base Saver tool.""",
    expected_output="""A confirmation that the knowledge base has been successfully
    updated with the new entries, and a short human-readable summary of the 
    strategic insights added.""",
    agent=synthesizer_agent,
    context=[research_task]
)

# Užduotis Nr. 3: Taisyklės Inžinerija (paliekama beveik nepakeista)
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