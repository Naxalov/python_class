import requests
import json
from pprint import pprint
count = 5
URL = 'https://randomuser.me/api'
param = {
    'results':2,
    'gender':'female'
}
response = requests.get(url=URL,params=param)
data = response.json()
pprint(data['results'])