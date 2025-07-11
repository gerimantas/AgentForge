"""
Test script for main functionality
"""
from agentforge.ui.cli.main_menu import main
import sys
from unittest.mock import patch

print("Testing main menu functionality...")

# Test 1: Import test
try:
    from agentforge.core.config import PROJECT_ROOT
    print("✅ Config imported successfully")
except Exception as e:
    print(f"❌ Config import failed: {e}")

# Test 2: Main menu mock test
try:
    with patch('builtins.input', return_value='5'):
        try:
            main()
        except SystemExit:
            pass
    print("✅ Main menu test passed!")
except Exception as e:
    print(f"❌ Main menu test failed: {e}")

print("\nAll tests completed!")
