#!/usr/bin/python3
"""
    search_user a URL.
"""
import requests
import sys
"""
    search_user a URL.
"""
def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the provided letter as a parameter.


    """
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    
    try:
        response = requests.post(url, data=data)
        try:
            json_data = response.json()
            if json_data:
                print(f"[{json_data['id']}] {json_data['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
