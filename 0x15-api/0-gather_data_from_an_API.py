#!/usr/bin/python3
'''used to gather todos by user input'''
import requests
from sys import argv

userid = int(argv[1])
url_usr = f'https://jsonplaceholder.typicode.com/users/{userid}'
url_todos = 'https://jsonplaceholder.typicode.com/todos'
count = 0
completed = 0
completed_todos = []

username = requests.get(url_usr).json()["name"]
todos = requests.get(url_todos).json()
for todo in todos:
    if (todo["userId"] == userid):
        count += 1
        if (todo["completed"]):
            completed += 1
            completed_todos.append(todo["title"])
print(f"Employee {username} is done with tasks({completed}/{count}):")
[print(x) for x in completed_todos]
