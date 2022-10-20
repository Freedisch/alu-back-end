#!/usr/bin/python3
"""validation"""

import csv
import requests
import sys


if __name__=="__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}" \
        .format(sys.argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(sys.argv[1])).json()
    content = []

    for task in todo:
        if task['userId'] == sys.argv[1]:
            content.append([str(sys.argv[1]),
            user["username"],
            todo["completed"],
            todo["title"]])
        
    csv_file = "{}.csv".format(sys.argv[1])
    with open(csv_file, 'w', newline='') as csv:
        write = csv.writer(csv, quoting=csv.QUOTE_ALL)
        for row in content:
            for item in row:
                str(item)
            write.writerow(row)
