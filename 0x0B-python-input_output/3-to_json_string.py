#!/usr/bin/python3
"""Defines a string-to-JSON """
import json


def to_json_string(my_obj):
    """Return the JSON representation """
    return json.dumps(my_obj)
