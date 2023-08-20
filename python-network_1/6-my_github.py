#!/usr/bin/python3
"""
    get_user_id a URL.
"""
import requests
import sys
"""
    get_user_id a URL.
"""
def get_user_id(username, password):
    """
    Uses the GitHub API to get the user id using Basic Authentication with a personal access token.
    """
    url = "https://api.github.com/ahimmii"
    headers = {"Authorization": f"Basic {username}:{password}"}

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
        print("Usage: python 6-my_github.py <username> <password>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        user_id = get_user_id(username, password)
        print(user_id)
