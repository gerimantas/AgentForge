# AgentForge

AgentForge – An autonomous agent system for knowledge base maintenance and prompt optimization.

---

## AI Assistants & Development Guidelines

### GitHub Copilot Instructions
This project includes specialized instructions for AI assistants in `.github/copilot-instructions.md`. These instructions help AI better understand the project architecture and follow development standards.

**Usage:**
- GitHub Copilot: May automatically use instructions in the future
- Other AI assistants: Reference the file manually

### AI Assistant Workflow Rules:
1. Always provide an action plan first
2. Wait for user confirmation
3. Execute only one step at a time
4. Stop and wait for confirmation before proceeding

---

## Architecture Overview

```
+-------------------+
|     main.py       |
+-------------------+
         |
         v
+-------------------+         +-------------------+
| MaintenanceCycle  |<------->| ExecutionCycle    |
+-------------------+         +-------------------+
         |                             |
         v                             v
+-------------------+         +-------------------+
| tasks_maintenance |         | tasks_execution   |
+-------------------+         +-------------------+
         |                             |
         v                             v
+-------------------+         +-------------------+
|     agents.py     |<------->|   custom_tools.py |
+-------------------+         +-------------------+
         |                    |
         v                    v
+-------------------+    +-------------------+
|  ziniu_baze.yaml  |    | source_registry.yaml |
+-------------------+    +-------------------+
         |                    |
         v                    v
+-------------------+    +-------------------+
| kanonine_sistema.yaml |  test_system.py   |
+-------------------+    +-------------------+
                              |
                              v
                         +-------------------+
                         | test_results      |
+-------------------+
```

---

## Project Status

**Current Version:** 0.4.0
**Status:** In Development

Recently implemented changes:
- ✅ Structured knowledge base (YAML format)
- ✅ Agent integration with YAML knowledge base
- ✅ Updated documentation README
- ✅ Function optimization and bug fixes
- ✅ Implemented automated testing framework
- ✅ Added test result accumulation system
- ✅ Project structure reorganization into agentforge/ package
- ✅ File organization and structure cleanup
- ✅ GitHub Copilot instructions added

---

## Agent Descriptions

### Maintenance Cycle (Knowledge Base Maintenance)
- **Researcher**  
  Finds new reliable sources, verifies facts using active sources from `source_registry.yaml`.
- **Synthesizer**  
  Summarizes new information, integrates it into the structured knowledge base `ziniu_baze.yaml`.
- **Rule Engineer**  
  Creates and updates knowledge base rules in `kanonine_sistema.yaml` file.

### Execution Cycle (Prompt Optimization)
- **Prompt Analyst**  
  Analyzes user queries, identifies objectives and applies basic prompt engineering techniques.
- **Prompt Critic**  
  Evaluates agent suggestions, looks for weaknesses, suggests improvements based on knowledge base.
- **Prompt Refiner**  
  Optimizes queries according to rules and knowledge base, provides final result.

---

## Usage Examples

### 1. Project Launch

```bash
# First time setup (Windows)
scripts\setup\setup_env.bat

# Daily usage
scripts\setup\start.bat

# Or directly
python main.py
```

### 2. Knowledge Base Update

Select the knowledge base maintenance cycle and follow instructions in terminal:

```
> 1 (Maintenance Cycle)
```

System automatically:
1. Researcher checks reliable sources and provides new information
2. Synthesizer integrates it into knowledge base (ziniu_baze.yaml)
3. Rule Engineer updates rules (kanonine_sistema.yaml)

### 3. Query Optimization

Select the query execution cycle, enter your query:

```
> 2 (Execution Cycle)
> "Help me write a letter to my employer about a salary increase"
```

System automatically:
1. Analyzes the query
2. Applies knowledge base techniques
3. Provides optimized query

### 4. System Testing

Select the system testing option:

```
> 3 (System Tests)
```

System:
1. Runs all integration and unit tests
2. Shows test results
3. Suggests saving test results:
   - If tests successful - usually no need to save results
   - If tests failed - recommended to save results for analysis

---

## File Structure

### Organized Project Structure (v0.4.0):
```
AgentForge/
├── .github/                 # GitHub configuration
│   └── copilot-instructions.md  # AI assistant instructions
├── .vscode/                 # VS Code settings
├── agentforge/              # Main Python package
│   ├── core/               # Base components (config.py)
│   ├── agents/             # Agent system and dynamic selection
│   ├── categories/         # Query categorization system
│   ├── workflows/          # Execution and maintenance cycles
│   ├── templates/          # Template management system
│   ├── utils/              # Helper tools (file operations)
│   └── ui/                 # User interface (CLI)
├── data/                   # Data files
│   ├── config/            # YAML configurations
│   ├── knowledge_base/    # Knowledge base files
│   └── results/           # Test and analysis results
├── scripts/               # Automation scripts
│   ├── setup/            # Environment setup scripts
│   └── maintenance/      # Maintenance scripts
├── tests/                 # Testing system
│   ├── integration/      # Integration tests
│   └── manual/           # Manual tests and debug
├── tools/                 # Developer tools
│   ├── debug/            # Debug scripts
│   └── migration/        # Migration tools
├── docs/                  # Documentation
├── templates/             # Template files
├── main.py               # Main entry point
└── requirements.txt      # Python dependencies
```

### Main Components:
- **main.py** – main entry point
- **agentforge/workflows/** – knowledge base maintenance and query optimization cycles
- **agentforge/agents/** – agent descriptions and dynamic selection logic
- **agentforge/utils/file_operations.py** – helper tools (file read/write, YAML, fact checking)
- **agentforge/core/config.py** – API keys, guards, configuration
- **Data files:**
  - `ziniu_baze.yaml` – structured knowledge base
  - `kanonine_sistema.yaml` – knowledge base rules
  - `source_registry.yaml` – source registry
  - `test_results/` – testing results directory

---

## Testing System

### Automated Tests
The system includes these tests:

1. **Configuration tests** – check if API keys and settings are correctly loaded
2. **Language detection tests** – check if system can identify input language
3. **Execution cycle tests** – check query optimization functionality
4. **YAML file operation tests** – check knowledge base read/write functions

### Running Tests
```bash
python test_system.py
```

or by selecting option "3" in the menu.

### Test Results
- Test results are saved in `test_results/` directory
- Uses file rotation system to prevent log from becoming too large
- Old log entries are automatically cleaned

---

## Requirements

- Python 3.10+
- Dependencies from `requirements.txt`:
  ```
  pip install -r requirements.txt
  ```
- Packages:
  - langdetect
  - crewai
  - crewai_tools
  - pyyaml
  - python-dotenv
- `.env` file with API keys:
  ```
  OPENAI_API_KEY=...
  SERPER_API_KEY=...
  MAX_ITERATIONS=3
  VERBOSE=True
  ```

---

## Next Steps

- [x] Testing framework implementation
- [ ] Knowledge base visualization UI
- [ ] Automatic fact checking
- [ ] Dynamic routing and resource management
- [ ] CI/CD integration with GitHub Actions

---

## Contact and Support

For questions, contact the project author or submit an issue to GitHub Issues.