#!/usr/bin/env python3
"""
Stage 2 Test Script
==================

Test script to verify Stage 2 workflow implementation.
"""

import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def test_workflow_imports():
    """Test if workflow modules can be imported."""
    try:
        print("🧪 Testing workflow module imports...")
        
        # Test execution workflow
        from agentforge.workflows.execution import run_execution_cycle
        print("✅ Execution workflow imported successfully")
        
        # Test maintenance workflow  
        from agentforge.workflows.maintenance import run_maintenance_cycle
        print("✅ Maintenance workflow imported successfully")
        
        # Test CLI menu
        from agentforge.ui.cli.main_menu import main as cli_main
        print("✅ CLI menu imported successfully")
        
        # Test GUI app
        from agentforge.ui.gui.main_app import AgentForgeGUI
        print("✅ GUI app imported successfully")
        
        print("\\n🎉 All Stage 2 modules imported successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_configuration():
    """Test configuration loading."""
    try:
        print("\\n🧪 Testing configuration...")
        
        from agentforge.core.config import OPENAI_API_KEY, SERPER_API_KEY
        
        if OPENAI_API_KEY:
            print("✅ OpenAI API key configured")
        else:
            print("⚠️ OpenAI API key not configured")
            
        if SERPER_API_KEY:
            print("✅ Serper API key configured")
        else:
            print("⚠️ Serper API key not configured")
            
        print("✅ Configuration loaded successfully")
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_file_operations():
    """Test file operations."""
    try:
        print("\\n🧪 Testing file operations...")
        
        from agentforge.utils.file_operations import load_knowledge_base, load_source_registry
        
        # Test knowledge base loading
        kb = load_knowledge_base()
        print(f"✅ Knowledge base loaded: {len(kb)} entries")
        
        # Test source registry loading  
        sr = load_source_registry()
        print(f"✅ Source registry loaded: {len(sr.get('sources', []))} sources")
        
        print("✅ File operations working successfully")
        return True
        
    except Exception as e:
        print(f"❌ File operations error: {e}")
        return False

def main():
    """Main test function."""
    print("="*60)
    print("🚀 AgentForge Stage 2 Implementation Test")
    print("="*60)
    
    tests = [
        ("Module Imports", test_workflow_imports),
        ("Configuration", test_configuration),
        ("File Operations", test_file_operations)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\\n📋 Running {test_name} test...")
        try:
            if test_func():
                print(f"✅ {test_name} test passed")
                passed += 1
            else:
                print(f"❌ {test_name} test failed")
                failed += 1
        except Exception as e:
            print(f"❌ {test_name} test error: {e}")
            failed += 1
    
    print("\\n" + "="*60)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    print("="*60)
    
    if failed == 0:
        print("\\n🎉 All tests passed! Stage 2 implementation is working correctly!")
    else:
        print(f"\\n⚠️ {failed} tests failed. Check the errors above.")
        
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
