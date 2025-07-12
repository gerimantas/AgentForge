"""
AgentForge Workflows
==================

Šis modulis saugo pagrindinius AgentForge darbo ciklus:
- Palaikymo ciklas (maintenance cycle)
- Vykdymo ciklas (execution cycle)

Stage 2: Using simplified workflows for testing
"""

try:
    # Import simplified workflows that don't hang
    from .simple_execution import run_execution_cycle, test_execution_cycle
    from .simple_maintenance import run_maintenance_cycle, test_maintenance_cycle
    __all__ = ["run_execution_cycle", "run_maintenance_cycle", "test_execution_cycle", "test_maintenance_cycle"]
    print("✅ Simplified workflows loaded successfully")
except ImportError as e:
    print(f"⚠️ Nepavyko importuoti simplified workflow modulių: {e}")
    __all__ = []
