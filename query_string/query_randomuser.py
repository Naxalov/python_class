import requests
import json
from pprint import pprint
count = 5
URL = 'https://randomuser.me/api'
response = requests.get(f'{URL}?results={count}')
data = response.json()
print(len(data['results']))