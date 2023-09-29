#!/usr/bin/python3
"""python script that takes in a URL and an email, sends a POST"""

import urllib.request
import sys
import urllib.parse


if __name__ == '__main__':
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as y:
        html = y.read()
        print('{}'.format(html.decode('utf-8')))
