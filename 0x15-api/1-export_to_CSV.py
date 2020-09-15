#!/usr/bin/python3
"""Export data in the CSV format"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = "{}/users/{}".format(url, sys.argv[1])
    username = requests.get(user_id).json().get('name')
    tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1])).json()
                                  .format(url, sys.argv[1])).json()

    with open('{}.csv'.format(sys.argv[1]), 'w') as csv_file:
        file_write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            file_write.writerow([sys.argv[1], username, task['completed'],
                                 task['title']])
