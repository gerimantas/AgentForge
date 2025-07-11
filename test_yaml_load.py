import yaml

with open('templates/index.yaml', 'r', encoding='utf-8') as file:
    data = yaml.safe_load(file)
    print('✅ YAML loaded successfully')
    print(f'Templates count: {len(data.get("templates", {}))}')
    print(f'Data: {data}')
