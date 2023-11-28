#!/usr/bin/python3
''' Sends a POST request to a specified URL with the email as a parameter.

Usage: ./6-post_email.py <URL> <email>
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    params = {'email': email}
    r = requests.post(url, data=params)
    print(r.text)
