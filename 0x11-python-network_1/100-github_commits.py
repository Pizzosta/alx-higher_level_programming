#!/usr/bin/python3
"""
a Python script that takes 2 arguments
and lists the 10 most recent commits on a given GitHub repository
"""

import sys
import requests

if __name__ == '__main__':
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repository_name)

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except KeyError:
        pass
