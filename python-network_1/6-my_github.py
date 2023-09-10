#!/usr/bin/python3
"""
get_user_id.py - Retrieve GitHub user ID using Basic Authentication with a personal access token.
"""
import requests
import sys
import base64

def get_user_id(username, personal_access_token):
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{username}:{personal_access_token}'.encode()).decode()}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("id")
        else:
            return None
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python get_user_id.py <username> <personal_access_token>")
    else:
        username = sys.argv[1]
        personal_access_token = sys.argv[2]
        user_id = get_user_id(username, personal_access_token)
        if user_id:
            print(f"GitHub User ID for {username}: {user_id}")
        else:
            print("Failed to retrieve user ID.")
