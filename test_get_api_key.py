import os

def get_api_key(key_name):
    print(f'Getting API key for: {key_name}')
    key = os.getenv(key_name)
    print(f'Key found: {key is not None}')
    if not key:
        print(f'WARNING: {key_name} not found in environment variables')
        return None
    print(f'Returning key for: {key_name}')
    return key

print('Testing get_api_key...')
result = get_api_key('OPENAI_API_KEY')
print(f'Result: {result is not None}')
print('Test completed successfully')
