#!/usr/bin/python3
''' A python script that fetches https://alx-intranet.hbtn.io/status '''
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        web_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(web_page)))
        print("\t- content: {}".format(web_page))
        print("\t- utf8 content: {}".format(web_page.decode("utf-8")))
