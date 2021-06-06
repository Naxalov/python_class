import requests
import json
from pprint import pprint
from os import times

def get_user(data):
    user = {} 
    user['gender']= data["results"][0]["gender"] 
    user['first'] = data["results"][0]["name"]["first"]
    user['last'] = data["results"][0]["name"]["last"]
    user['city'] = data["results"][0]['location']['city']
    return user