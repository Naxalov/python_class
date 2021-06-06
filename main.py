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

users = []
#female

idx = 0
while idx <10:
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:

        data = response.json()
        gender = data["results"][0]["gender"] 
        print(gender)
        user = get_user(data)
        if gender =='female':
            users.append(user)
            idx +=1

# pprint(users)
save_user(users)

# user =