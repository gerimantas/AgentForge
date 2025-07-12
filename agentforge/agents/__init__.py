"""
AgentForge Agents
================

Agent definitions for AgentForge system.
Stage 2: Using simplified agents to avoid CrewAI hanging issues.
"""

# Import simplified agents that don't cause hanging
from .simple_agents import (
    prompt_analyst, prompt_critic, prompt_refiner,
    researcher_agent, synthesizer_agent, rule_engineer_agent,
    librarian_agent, fact_check_agent, is_source_trusted, add_knowledge_entry
)

__all__ = [
    "prompt_analyst", "prompt_critic", "prompt_refiner",
    "researcher_agent", "synthesizer_agent", "rule_engineer_agent",
    "librarian_agent", "fact_check_agent", "is_source_trusted", "add_knowledge_entry"
]

# All agent definitions are now imported from simple_agents module
# This avoids CrewAI hanging issues while maintaining the same interface