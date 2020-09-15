#!/usr/bin/python3
"""Gather data from an API. For a given employee ID, returns information
about his/her TODO list progress."""

import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = "{}/users/{}".format(url, sys.argv[1])
    username = requests.get(user_id).json().get('name')
    tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1])).json()
    complete_tasks = requests.get('{}/todos?userId={}&completed=true'
                                  .format(url, sys.argv[1])).json()
    tasks_len = len(tasks)
    done_tasks_len = len(complete_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(username, done_tasks_len, tasks_len))

    for task in complete_tasks:
        print("\t {}".format(task["title"]))
