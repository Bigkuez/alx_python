# Import necessary libraries
import requests  # Used to make HTTP requests to the API
import csv       # Used to work with CSV files
import sys       # Used to access command-line arguments

def get_employee_info(employee_id):
    """
    Retrieves employee information and their TODO list from a REST API,
    then exports the data to a CSV file.

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

    # Create a CSV file for the user
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

    print(f"CSV file '{filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_and_export_to_csv.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        # Ensure employee_id is an integer
        employee_id = int(employee_id)
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
