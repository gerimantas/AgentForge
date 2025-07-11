#!/usr/bin/env python3
"""Test template system functionality"""

from agentforge.templates.manager import list_templates, format_template_list

try:
    templates = list_templates()
    print(f'✅ Templates loaded: {len(templates)}')
    print(format_template_list(templates))
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
