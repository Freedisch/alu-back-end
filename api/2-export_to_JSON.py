#!/usr/bin/python3
"""validation"""

import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                        .format(sys.argv[1])).json()
    content = []
    for task in todo:
        content.append(
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            }
        )
    file_name = "{}.json".format(sys.argv[1])
    with open(file_name, 'w') as file:
        json.dump({sys.argv[1]: content}, file)