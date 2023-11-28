#!/usr/bin/python3
''' Displays the body of the reponse of a request sent to a specified URL.
    Prints error code if an error occurs.

Usage: ./3-error_code.py <URL>
'''
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
