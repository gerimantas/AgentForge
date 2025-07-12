You are working on the AgentForge project - a sophisticated AI prompt optimization system using CrewAI.

## Architecture
- **Two main workflows**: Maintenance Cycle (knowledge base updates) and Execution Cycle (prompt optimization)
- **Agent chains**: researcher → synthesizer → rule_engineer (maintenance) and prompt_analyst → prompt_critic → prompt_refiner (execution)
- **Entry point**: `main.py` → `agentforge.ui.cli.main_menu` → workflows in `agentforge/workflows/`

## Package Structure
```
agentforge/
├── core/           # Config, base classes
├── agents/         # Agent definitions & dynamic selection
├── categories/     # Query classification system
├── workflows/      # Main execution & maintenance cycles
├── templates/      # Prompt template management
├── utils/          # File operations, tools
└── ui/             # CLI interface
```

## Critical Development Rules
- **Always activate venv**: Use `scripts/setup/start.bat` or `python main.py`
- **Configuration**: All settings in `agentforge/core/config.py`, API keys in `.env`
- **Required APIs**: `OPENAI_API_KEY`, `SERPER_API_KEY`
- **File structure**: Scripts in `scripts/`, YAML configs in `data/config/`, never batch files in root

## Standard Patterns
### Agent Creation
```python
from crewai import Agent, Task, Crew, Process
from agentforge.agents import [specific_agent]
crew = Crew(agents=[...], tasks=[...], process=Process.sequential, verbose=config.VERBOSE)
```

### Imports
```python
from agentforge.core import config
from agentforge.workflows import run_execution_cycle, run_maintenance_cycle
```

### Testing
- Integration tests in `tests/integration/`
- Use `AgentForgeTestCase` base class
- Run via menu option 3 or `python -m pytest`

## AI Workflow Guidelines
1. **Action plans**: Always list steps only, no implementation
2. **Wait for confirmation**: Include "Please confirm to proceed."
3. **One step at a time**: Perform only the next logical step after approval
4. **Pause between steps**: Wait for confirmation before proceeding

## Key Commands
```cmd
# Setup: scripts\setup\setup_env.bat
# Run: python main.py
# VS Code: Ctrl+Shift+P → "Tasks: Run Task" → "Activate venv and run AgentForge"
```
