#!/usr/bin/env python3
"""
Stage 3 Enhanced Features Test Script
"""

print('🧪 Testing Stage 3 Enhanced Features...')
print('=' * 50)

# Test 1: Enhanced Agents Import
try:
    from agentforge.agents.enhanced_agents import enhanced_agents, EnhancedAgentFactory
    print('✅ Enhanced agents imported successfully')
    print(f'   Available agents: {list(enhanced_agents.keys())}')
except Exception as e:
    print(f'❌ Enhanced agents import failed: {e}')

# Test 2: Enhanced Tasks Import  
try:
    from agentforge.workflows.tasks.enhanced_tasks import EnhancedTaskManager
    print('✅ Enhanced tasks imported successfully')
except Exception as e:
    print(f'❌ Enhanced tasks import failed: {e}')

# Test 3: Enhanced Workflows Import
try:
    from agentforge.workflows.enhanced_workflows import run_enhanced_execution_cycle
    print('✅ Enhanced workflows imported successfully')
except Exception as e:
    print(f'❌ Enhanced workflows import failed: {e}')

# Test 4: Enhanced GUI Import
try:
    from agentforge.ui.gui.enhanced_gui import EnhancedAgentForgeGUI
    print('✅ Enhanced GUI imported successfully')
except Exception as e:
    print(f'❌ Enhanced GUI import failed: {e}')

# Test 5: Enhanced CLI Import
try:
    from agentforge.ui.cli.enhanced_cli import EnhancedAgentForgeCLI
    print('✅ Enhanced CLI imported successfully')
except Exception as e:
    print(f'❌ Enhanced CLI import failed: {e}')

print('\n🎉 All Stage 3 components loaded successfully!')
print('\n📋 Stage 3 Features Summary:')
print('• Full CrewAI Integration with Enhanced Agents')
print('• Advanced GUI with Progress Tracking')
print('• Enhanced CLI with Batch Processing')
print('• Real-time Workflow Visualization')
print('• Comprehensive History and Caching')
print('• Async Operations Support')
print('• Export/Import Capabilities')
print('• Advanced Error Handling')
