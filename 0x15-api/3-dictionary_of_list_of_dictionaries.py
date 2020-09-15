#!/usr/bin/python3
"""requests todo and users from
   https://jsonplaceholder.typicode.com"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = 1
    urltodo = 'https://jsonplaceholder.typicode.com/todos/'
    urluser = 'https://jsonplaceholder.typicode.com/users/'
    tasks = requests.get(urltodo, params={'userId': emp_id})
    user = requests.get(urluser, params={'id': emp_id})

    tasks = tasks.json()
    user = user.json()
    tasks_usdic = {}
    task_list = []

    employee = user[0].get('username')
    for task in tasks:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
            tasks_usdic[emp_id] = task_list

with open("todo_all_employees.json", "w+") as jsonfile:
        json.dump(tasks_usdic, jsonfile)
