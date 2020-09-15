#!/usr/bin/python3
"""requests todo and users from
   https://jsonplaceholder.typicode.com"""
import json
import requests


if __name__ == '__main__':
    emp_id = 1
    u_tasks = {}
    urltodo = 'https://jsonplaceholder.typicode.com/todos/'
    urluser = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(urluser).json()

    for emp_id in range(1, len(users) + 1):
        tasks = requests.get(urltodo, params={'userId': emp_id})
        user = requests.get(urluser, params={'id': emp_id})

        todo_dict = tasks.json()
        user_dict = user.json()
        task_list = []
        employee = user_dict[0].get('username')

        for task in todo_dict:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        u_tasks[emp_id] = task_list

    with open("todo_all_employees.json", "w+") as jsonfile:
        json.dump(u_tasks, jsonfile)
