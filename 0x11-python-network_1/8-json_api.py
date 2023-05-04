#!/usr/bin/python3
"""
a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    value = {'q': q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=value)

    try:
        json_obj = response.json()
        if json_obj:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
