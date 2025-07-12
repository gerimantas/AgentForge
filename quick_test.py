#!/usr/bin/env python3
"""
Quick Stage 2 Functionality Test
================================

Quick test to verify basic Stage 2 functionality.
"""

def test_basic_imports():
    """Test basic module imports."""
    print("Testing basic imports...")
    
    try:
        # Test core config
        from agentforge.core.config import OPENAI_API_KEY, SERPER_API_KEY
        print("✅ Core config imported")
        
        # Test file operations
        from agentforge.utils.file_operations import load_knowledge_base, load_source_registry
        print("✅ File operations imported")
        
        # Test GUI
        from agentforge.ui.gui.main_app import AgentForgeGUI
        print("✅ GUI imported")
        
        # Test CLI
        from agentforge.ui.cli.main_menu import main
        print("✅ CLI imported")
        
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_workflow_imports():
    """Test workflow imports separately."""
    print("\\nTesting workflow imports...")
    
    try:
        # Test individual workflow components
        from agentforge.agents import prompt_analyst, prompt_critic, prompt_refiner
        print("✅ Agents imported")
        
        from agentforge.workflows.tasks.execution_tasks import create_execution_tasks
        print("✅ Execution tasks imported")
        
        from agentforge.workflows.execution import run_execution_cycle
        print("✅ Execution workflow imported")
        
        from agentforge.workflows.maintenance import run_maintenance_cycle
        print("✅ Maintenance workflow imported")
        
        return True
        
    except Exception as e:
        print(f"❌ Workflow import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_configuration():
    """Test configuration."""
    print("\\nTesting configuration...")
    
    try:
        from agentforge.core.config import OPENAI_API_KEY, SERPER_API_KEY, validate_api_keys
        
        print(f"OpenAI API Key: {'✅ Set' if OPENAI_API_KEY else '❌ Not set'}")
        print(f"Serper API Key: {'✅ Set' if SERPER_API_KEY else '❌ Not set'}")
        
        # Try to validate (might fail if keys not set)
        try:
            validate_api_keys()
            print("✅ API keys validation passed")
        except Exception as e:
            print(f"⚠️ API keys validation failed: {e}")
            
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def main():
    """Main test function."""
    print("="*50)
    print("🧪 AgentForge Stage 2 Quick Test")
    print("="*50)
    
    test_functions = [
        test_basic_imports,
        test_workflow_imports,
        test_configuration
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test_func.__name__} crashed: {e}")
            failed += 1
    
    print("\\n" + "="*50)
    print(f"📊 Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("\\n🎉 All tests passed! Stage 2 is working!")
        print("\\n🚀 You can now:")
        print("   • Run 'python main.py' to use the interface")
        print("   • Choose CLI (1) or GUI (2) mode")
        print("   • Test workflows through the interface")
    else:
        print(f"\\n⚠️ {failed} tests failed. Some functionality may not work.")
    
    print("="*50)

if __name__ == "__main__":
    main()
