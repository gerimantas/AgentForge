# AgentForge GUI Integration Design Document

## Current AgentForge Architecture Analysis

### Entry Point Structure
- **main.py**: Entry point that imports from agentforge package
- **agentforge/ui/cli/main_menu.py**: Current CLI interface with menu system
- **agentforge/core/config.py**: Configuration management with API keys and project paths

### Existing Menu System
The CLI currently provides:
1. Maintenance Cycle (knowledge base updates)
2. Execution Cycle (prompt optimization) 
3. System tests
4. Category and agent management
5. Template management

### Key Patterns Observed
- **Lithuanian language**: Comments and UI text in Lithuanian
- **Workflow-based**: Two main cycles (maintenance/execution)
- **Centralized config**: Uses agentforge/core/config.py for settings
- **Package structure**: Follows agentforge/component/module pattern

## Proposed GUI Integration Plan

### Stage 1: Foundation (Requires User Approval)
**Goal**: Create minimal GUI entry point that integrates with existing structure

**Files to Create** (with user permission):
1. `agentforge/ui/gui_main.py` - GUI entry point
2. `agentforge/core/config.py` - EXTEND existing config (not replace)
3. `requirements.txt` - ADD GUI dependencies

**Integration Points**:
- Extend existing `main.py` to offer GUI/CLI choice
- Reuse existing workflows from `agentforge/workflows/`
- Follow existing Lithuanian language patterns
- Use existing configuration system

### Stage 2: Core GUI (After Stage 1 approval)
**Goal**: Create main GUI window with menu equivalent

**Components**:
- Main window with 5 menu options (same as CLI)
- Status display area
- Progress indicators for workflows
- Settings panel

### Stage 3: Advanced Features (After Stage 2 approval)
**Goal**: Enhanced GUI features

**Components**:
- Real-time workflow monitoring
- Visual template editor
- Agent performance dashboards
- Knowledge base browser

## Integration Strategy

### Minimal Disruption Approach
1. **NO changes** to existing CLI functionality
2. **NO changes** to existing workflows
3. **ADD** GUI as alternative interface
4. **EXTEND** config.py rather than replace

### File Structure Proposal
```
agentforge/
├── ui/
│   ├── cli/           # (existing - no changes)
│   │   └── main_menu.py
│   └── gui_main.py    # (new - GUI entry point)
├── core/
│   └── config.py      # (extend existing)
└── workflows/         # (existing - no changes)
```

## Questions for User Approval

1. **Should I extend the existing config.py** or create a separate GUI config?
2. **Should the GUI use Lithuanian language** like the CLI?
3. **Should I create a choice in main.py** between CLI and GUI modes?
4. **Which GUI framework** would you prefer? (Flet, Streamlit, Tkinter, etc.)

## Request for Permission

**I request permission to proceed with Stage 1 only**:
- Create `agentforge/ui/gui_main.py` 
- Extend `agentforge/core/config.py` with GUI settings
- Modify `main.py` to offer GUI/CLI choice
- Add GUI dependencies to requirements.txt

**I will NOT proceed beyond Stage 1 without explicit approval.**

---

*This design follows AgentForge development rules and maintains the existing architecture while adding GUI capability.*
