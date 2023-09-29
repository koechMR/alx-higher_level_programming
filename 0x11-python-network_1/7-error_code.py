#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays"""

import requests
from sys import argv

if __name__ == '__main__':
    y = requests.get(argv[1])
    status = y.status_code
    print(y.text) if status < 400 else print(
        "Error code: {}".format(y.status_code))
