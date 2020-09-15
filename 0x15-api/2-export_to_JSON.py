#!/usr/bin/python3
"""requests todo and users from
   https://jsonplaceholder.typicode.com"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    urltodo = 'https://jsonplaceholder.typicode.com/todos/'
    urluser = 'https://jsonplaceholder.typicode.com/users/'
    tasks = requests.get(urltodo, params={'userId': emp_id})
    user = requests.get(urluser, params={'id': emp_id})

    tasks = tasks.json()
    user = user.json()
    user_tasks = {}
    task_list = []

    employee = user[0].get('username')

    with open("{}.json".format(emp_id), "w+") as jsonfile:
        for task in tasks:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[emp_id] = task_list
        data = json.dumps(user_tasks)
        jsonfile.write(data)
