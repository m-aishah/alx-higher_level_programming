#!/usr/bin/python3
''' Uses the Github API to display a user's id
    based on the given username and password.

Usage: ./10-my_github.py <username> <password>
'''
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auth = requests.auth.HTTPBasicAuth(username, password)
    r = requests.get('https://api.github.com/user', auth=auth)
    print(r.json().get("id"))
