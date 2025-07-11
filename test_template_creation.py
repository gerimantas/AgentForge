import os
from datetime import datetime
import yaml

TEMPLATES_DIR = 'templates'
TEMPLATES_INDEX_FILE = os.path.join(TEMPLATES_DIR, 'index.yaml')

index = {
    'templates': {},
    'metadata': {
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'count': 0
    }
}

if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

with open(TEMPLATES_INDEX_FILE, 'w', encoding='utf-8') as file:
    yaml.dump(index, file, sort_keys=False, default_flow_style=False)

print('✅ Template index created manually')
