#!/usr/bin/python3
''' Sends a POST request to a specified URL with an email as a parameter.

Usage: ./2-post_email.py <URL>
'''
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    params = {'email': email}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')  # data should be in bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        web_page = response.read()
        print(web_page.decode('utf-8'))
