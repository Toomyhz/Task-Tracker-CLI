import time
import json

def get_time():
    local_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d- %H:%M:%S",local_time)
    return formatted_time

def read_json(type='all'):
    try:
        with open('.\database.json', 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                data = []
            else:
                data = json.loads(content)
    except:
        data = []
    finally:
        return data
    
def save_json(data):
    with open("database.json", 'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4)

def get_id():
    data = read_json()
    if data == []:
        new_id = 1
    else:
       for i in data:
        if i['id']:
            new_id = i['id'] + 1

    return new_id