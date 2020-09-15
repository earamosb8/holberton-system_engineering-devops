#!/usr/bin/python3
"""requests todo and users from
   https://jsonplaceholder.typicode.com"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    urltodo = 'https://jsonplaceholder.typicode.com/todos/'
    urluser = 'https://jsonplaceholder.typicode.com/users/'
    tasks = requests.get(urltodo, params={'userId': emp_id})
    user = requests.get(urluser, params={'id': emp_id})

    tasks_dic = tasks.json()
    user_dic = user.json()

    employee = user_dic[0].get('username')

    with open(emp_id + '.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks_dic:
            status = task['completed']
            title = task['title']
            csvwriter.writerow(["{}".format(emp_id),
                                "{}".format(employee),
                                "{}".format(status),
                                "{}".format(title)])
