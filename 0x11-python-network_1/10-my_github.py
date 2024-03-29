#!/usr/bin/python3
"""
A script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, personal_access_token)
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
