#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and display"""

from sys import argv
import requests

if __name__ == '__main__':
    y = requests.get(argv[1])
    print(y.headers.get('X-Request-Id'))
