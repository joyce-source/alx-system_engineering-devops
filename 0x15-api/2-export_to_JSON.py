#!/usr/bin/python3
"""Python script to export data in the JSON format"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID.
    Also exports the TODO list data to a JSON file.

    Parameters:
        employee_id (int):ID of the employee whose TODO list to be fetched.

    Returns:
        None: The function prints the TODO list progress to the standard output
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

        # Display the progress
        print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/"
              f"{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task['title']}")

        # Export to JSON
        json_data = {str(employee_id): [
            {"task": task['title'],
                "completed": task['completed'],
                "username": employee_name}
            for task in todos_data
        ]}
        json_filename = f"{employee_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)
        print(f"Data exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
    except (KeyError, IndexError):
        print(f"Employee with ID {employee_id} not found.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
