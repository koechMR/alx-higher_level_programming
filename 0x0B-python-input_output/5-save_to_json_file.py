#!/usr/bin/python3
"""Define a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Write objects to a text file using JSON rep"""
    with open(filename, "w") as x:
        json.dump(my_obj, x)
