import json
import requests

# Function to fetch user data from the given URL
def fetch_user_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

# Function to export tasks in JSON format
def export_tasks_to_json():
    base_url = 'https://jsonplaceholder.typicode.com/'
    users = fetch_user_data(base_url + 'users')
    tasks = fetch_user_data(base_url + 'todos')

    # Create a dictionary to store tasks for each user
    user_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Initialize an empty list for the user's tasks
        user_task_list = []

        # Find tasks associated with the current user
        for task in tasks:
            if task['userId'] == user_id:
                task_data = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_task_list.append(task_data)

        # Add the user's task list to the dictionary
        user_tasks[user_id] = user_task_list

    # Export the user_tasks dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)

if __name__ == '__main__':
    export_tasks_to_json()
