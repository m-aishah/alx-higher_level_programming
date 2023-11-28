#!/usr/bin/python3
''' Lists 10 commits of a specified repository by a given user.

Usage: ./100-github_commits.py <repository> <owner_name>
'''
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)

    try:
        commits = r.json()
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")
                ))
    except IndexError:
        pass
