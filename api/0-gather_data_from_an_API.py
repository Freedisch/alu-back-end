#!/usr/bin/python3
""" hope to get ride of the validation system """

import requests
import sys


"""Too tired"""

if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                        .format(sys.argv[1])).json()

    tasks = 0
    taskcompleted = []
    for task in todo:

        if task['userId'] == int(sys.argv[1]):
            tasks += 1

            if task['completed']:
                taskcompleted.append(task['title'])

    name = user['name']
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(taskcompleted), tasks))

    for task in taskcompleted:
        print("\t {}", format(task))
