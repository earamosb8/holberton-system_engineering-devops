#!/usr/bin/python3
"""requests todo and users from
   https://jsonplaceholder.typicode.com"""
import requests
import sys


if __name__ == "__main__":
    emp_id = sys.argv[1]
    urltodo = 'https://jsonplaceholder.typicode.com/todos/'
    urluser = 'https://jsonplaceholder.typicode.com/users/'
    tasks = requests.get(urltodo, params={'userId': emp_id})
    user = requests.get(urluser, params={'id': emp_id})

    tasks_dic = tasks.json()
    user_dic = user.json()

    complete_taks = []

    total_tasks = len(tasks_dic)
    employee = user_dic[0].get('name')

    for task in tasks_dic:
        if task.get('completed') is True:
            complete_taks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(complete_taks), total_tasks))

    for task in complete_taks:
        print("\t {}".format(task.get('title')))
