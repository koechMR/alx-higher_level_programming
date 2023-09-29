#!/usr/bin/python3
""" script that takes in a url sends a request"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as rep:
        print(dict(rep.headers).get("X-Request-Id"))
