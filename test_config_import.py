print('1. Testing config import...')
from agentforge.core.config import PROJECT_ROOT, OPENAI_API_KEY
print(f'2. PROJECT_ROOT: {PROJECT_ROOT}')
print(f'3. OPENAI_API_KEY: {OPENAI_API_KEY is not None}')
print('4. Config imported successfully')
