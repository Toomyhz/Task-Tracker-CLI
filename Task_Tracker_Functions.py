from Functions import get_time ,read_json, save_json, get_id

def add_task(task_description):
    task_id = get_id()

    new_data = {
        'id':task_id,
        'description':task_description,
        'status':'todo',
        'created-at':get_time(),
        'updated-at':'none'
    }


    current_data = read_json()
    current_data.append(new_data)
    save_json(current_data)
    return print("Successfully saved!!")

def update_task(task_id,task_description):
    id_founded = 0
    data = read_json()
    for task in data:
        if task['id'] == task_id:
            id_founded = task['id']
            print(f"Founded {id_founded}")
            task['description'] = task_description
            task['updated-at'] = get_time()
    
    if id_founded == 0:
        print("Id not founded")
    else:
        save_json(data)
        return print("Task successfully updated!!")

def delete_task(task_id):
    id_founded = 0
    data = read_json()
    new_data = []

    for task in data:
        if task['id'] == task_id:
            id_founded = task['id']

    if id_founded == 0:
        print("Id not founded")
    else:
        for task in data:
            if task['id'] != task_id:
                new_data.append(task)
        save_json(new_data)
        print("Task successfully deleted!!")

def mark_in_progress(task_id):
    id_founded = 0
    data = read_json()
    for task in data:
        if task['id'] == task_id:
            id_founded = task['id']
            task['status'] = "in-progress"
            task['updated-at'] = get_time()
    if id_founded == 0:
        print("Id not founded")
    else:
        save_json(data)
        print("Task Updated!!")
    
def mark_done(task_id):
    id_founded = 0
    data = read_json()
    for task in data:
        if task['id'] == task_id:
            id_founded = task['id']
            task['status'] = "done"
            task['updated-at'] = get_time()
    if id_founded == 0:
        print("Id not founded")
    else:
        save_json(data)
        print("Task Updated!!")
    
def list_tasks(status = None):
    data = read_json()
    data_filtred = []
    print("List of Tasks")
    print("=============")
    print("ID | Task | Status")
    print("=============")
    if status:
        for task in data:
            if task['status'] == status:
                data_filtred.append(task)
        data = data_filtred

    for task in data:
        print(task['id']," |",task['description']," |",task['status'])
