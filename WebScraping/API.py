import requests
import json
response = requests.get('https://catfact.ninja/fact')

fact = json.loads(response.text)

print('Fact: ', fact['fact'])
print('Length By Json: ', fact['length'])
print('Length By len func: ', len(fact['fact']))
