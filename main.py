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

def save_user(users):
    users_list = {
    'results':users
    }
    f = open(f'data_point/{times}_randomuser.json','w')
    results = json.dumps(users_list)
    f.write(results)
    return f.close()
