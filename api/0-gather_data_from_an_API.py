#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

def truncate(text, length):
    """
    Truncate text to the specified length.

    Args:
        text (str): The text to truncate.
        length (int): The maximum length.

    Returns:
        str: The truncated text.
    """
    if len(text) <= length:
        return text
    else:
        return text[:length]

def get_employee_info(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Get employee information
    response = requests.get(user_endpoint)
    user_data = response.json()
    employee_name = user_data.get("name")

    # Get TODO list for the employee
    response = requests.get(todos_endpoint)
    todos_data = response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task.get("completed"))

    # Display employee name and truncated task details
    output = []
    output.append(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task.get("completed"):
            task_title = truncate(task.get('title'), 30)  # Truncate task title to 30 characters
            output.append(f"     {task_title}")

    # Join output lines and truncate to a maximum of 244 characters
    output_text = "\n".join(output)
    truncated_output = truncate(output_text, 244)

    print(truncated_output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Ensure employee_id is an integer
        employee_id = int(employee_id)
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
