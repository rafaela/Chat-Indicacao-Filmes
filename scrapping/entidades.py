import json
import ibm_watson

service=ibm_watson.AssistantV1(
    version='2019-04-24',
    username='apikey',
    password='gb7MZg0MdxivOX3hAQVzp6N0GvU4w14Gd9rOJ5AtaHzm',
    url='https://gateway.watsonplatform.net/assistant/api'
)

with open('categorias.json') as f:    
    data = json.load(f)

categorias = []

for item in data:
    categorias.append({
        'value': str(item['id']),
        'synonyms': [item['nome']]
    })

response=service.create_entity(
    workspace_id='5bf1bf5f-c55f-42d8-a9f7-3b3f4d5b9461',
    entity='categoria',
    values=categorias
).get_result()

print(json.dumps(response, indent=2))