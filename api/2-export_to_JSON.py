# Import necessary libraries
import requests  # Used to make HTTP requests to the API
import json      # Used to work with JSON data
import sys       # Used to access command-line arguments

def get_employee_info(employee_id):
    """
    Retrieves employee information and their TODO list from a REST API,
    then exports the data to a JSON file.

    Args:
        employee_id (int): The ID of the employee whose data is to be retrieved.

    Returns:
        None
    """
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Get employee information
    response = requests.get(user_endpoint)
    user_data = response.json()
    user_id = user_data.get("id")
    user_name = user_data.get("username")

    # Get TODO list for the employee
    response = requests.get(todos_endpoint)
    todos_data = response.json()

    # Create a JSON file for the user
    filename = f"{user_id}.json"

    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        }
        tasks.append(task_info)

    user_tasks = {str(user_id): tasks}

    with open(filename, 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)

    print(f"JSON file '{filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_and_export_to_json.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Ensure employee_id is an integer
        employee_id = int(employee_id)
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
