#!/usr/bin/python3
"""script that takes in a URL, send a request to URL"""

import sys

if __name__ == "__main__":

    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as y:
        print('Error code:', y.code)
