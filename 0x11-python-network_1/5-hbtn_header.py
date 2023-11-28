#!/usr/bin/python3
''' Displays the X-Request-id variable of a request made to a given URL.

Usage: ./5-hbtn_header.py <URL>
'''
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(dict(r.headers).get("X-Request-Id"))
