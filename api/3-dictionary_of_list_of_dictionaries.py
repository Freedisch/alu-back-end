#!/usr/bin/python3
"""validation"""

import json
import requests
import sys


if __name__ == "__main__":

    todo = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    content = []
    task_list = {}
    for task in todo:
        _id = task["userId"]
        user = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(_id)).json()
        task_list[_id] = []
        task_list[_id].append({
            "username": user['username'],
            "task": task["title"],
            "completed": task["completed"]
        })
    with open("todo_all_employees.json", 'w') as file:
        json.dump(task_list, file)
