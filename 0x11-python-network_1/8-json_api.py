#!/usr/bin/python3
"""script that sends a POST request new"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url,
                             data=data)

    try:
        y = response.json()
        if not y:
            print("No result")
        else:
            print("[{}] {}".format(y.get("id"),
                                   y.get("name")))
    except ValueError:
        print("Not a valid JSON")
