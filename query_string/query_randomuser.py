import requests
import json
from pprint import pprint
from os import time

response = requests.get('https://randomuser.me/api/')