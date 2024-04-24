#!/usr/bin/python3
'''gg'''
import json
import requests


if __name__ == "__main__":
    url_todos = 'https://jsonplaceholder.typicode.com/todos'
    url_usrs = 'https://jsonplaceholder.typicode.com/users'
    filename = f"todo_all_employees.json"
    out = {}

    todos = requests.get(url_todos).json()
    usrs = requests.get(url_usrs).json()
    usrs = {user["id"]: user["username"] for user in usrs}

    for todo in todos:
        # if (not out[todo["userId"]]):
        if todo["userId"] not in out:
            out[todo["userId"]] = []
        obj = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": usrs[todo["userId"]]
        }
        out[todo["userId"]].append(obj)
    with open(filename, "w") as f:
        json.dump(out, f)
