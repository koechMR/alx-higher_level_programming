#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
