#!/usr/bin/python3
"""Python script that using API for employee IDreturns info about TODO list"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Parameters:
        employee_id (int):ID of employee whose TODO list is to be fetched

    Returns:
        None: The function prints the TODO list progress to standard output
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data['name']

        # Fetch todos for the specified employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]

        # Display the progress
        print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/"
              f"/{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task['title']}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
    except (KeyError, IndexError):
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
