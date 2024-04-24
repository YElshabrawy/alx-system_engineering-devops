#!/usr/bin/python3
'''gg'''
import requests
from sys import argv


if __name__ == "__main__":
    userid = int(argv[1])
    url_usr = f'https://jsonplaceholder.typicode.com/users/{userid}'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    username = requests.get(url_usr).json()["username"]
    todos = requests.get(url_todos).json()
    filename = f"{userid}.csv"
    with open(filename, "w") as f:
        for todo in todos:
            if (todo["userId"] == userid):
                line = f'"{userid}","{username}"'
                line += f',"{todo["completed"]}","{todo["title"]}"\n'
                f.write(line)
    # Remove the last line
    with open(filename, "rb+") as f:
        f.seek(-1, 2)
        f.truncate()
