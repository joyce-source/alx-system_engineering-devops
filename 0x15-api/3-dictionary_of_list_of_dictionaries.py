#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import json
import requests
import sys


def export_all_employee_tasks():
    """
    Fetches the TODO list progress for all employees.
    Exports the TODO list data to a JSON file in the specified format.

    Returns:
        None: The function exports the data to the JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com/users'
    employees_response = requests.get(base_url)
    employees_data = employees_response.json()

    all_tasks = {}

    for employee in employees_data:
        employee_id = employee['id']
        employee_name = employee['name']
        todos_url = (f'https://jsonplaceholder.typicode.com/todos?'
                     f'userId={employee_id}')
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        employee_tasks = [
            {"username": employee_name, "task": task['title'],
                "completed": task['completed']}
            for task in todos_data
        ]
        all_tasks[str(employee_id)] = employee_tasks

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    export_all_employee_tasks()
