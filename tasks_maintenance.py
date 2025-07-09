# /AgentForge/tasks_maintenance.py

from crewai import Task
from agents import researcher_agent, architect_agent

# --- MAINTENANCE CYCLE TASKS ---

# Task for the Researcher
research_task = Task(
    description=f"""Review the list of trusted sources in 'source_registry.yaml'
    using the YAML Read Tool. Systematically check each source with an 'active'
    status and find the latest information (last 3-6 months) related to
    'prompt engineering' techniques. Summarize your findings.""",
    expected_output="""A structured text report outlining the 2-3 most
    important techniques or insights discovered. Each insight must be
    briefly described and include a URL to the original source.""",
    agent=researcher_agent
)

# Task for the Architect
architect_task = Task(
    description="""Analyze the report provided by the Researcher on new techniques.
    First, save the full report to the 'ziniu_baze.md' file using the
    File Write Tool. Second, based on this report, formulate 3-5 universal,
    high-level rules or principles that other agents should follow when
    optimizing prompts. Write these rules into the 'kanonine_sistema.md' file.""",
    expected_output="""A success message confirming that both files
    ('ziniu_baze.md' and 'kanonine_sistema.md') have been created/updated.""",
    agent=architect_agent,
    context=[research_task]
)