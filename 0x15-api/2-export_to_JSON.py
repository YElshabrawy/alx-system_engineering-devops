#!/usr/bin/python3
'''gg'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    userid = int(argv[1])
    url_usr = f'https://jsonplaceholder.typicode.com/users/{userid}'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    username = requests.get(url_usr).json()["username"]
    todos = requests.get(url_todos).json()
    filename = f"{userid}.json"
    out = {
        userid: []
    }

    for todo in todos:
        if (todo["userId"] == userid):
            obj = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": username
            }
            out[userid].append(obj)
    with open(filename, "w") as f:
        json.dump(out, f)
