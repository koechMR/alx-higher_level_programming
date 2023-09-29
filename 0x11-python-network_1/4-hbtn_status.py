#!/usr/bin/python3
"""Script that fetches from url"""

import requests

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    y = requests.get(url)
    text = y.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
