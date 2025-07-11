"""
AgentForge - Prompt Engineering and AI Agent Management System

A sophisticated framework for managing AI agents, prompt optimization, 
and automated prompt engineering workflows using CrewAI.
"""

__version__ = "0.4.0"
__author__ = "AgentForge Team"

# Core components
from .core import config
from .workflows import run_execution_cycle, run_maintenance_cycle

__all__ = [
    "config",
    "run_execution_cycle",
    "run_maintenance_cycle"
]
