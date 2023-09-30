#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    y = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(y.json().get('id'))
