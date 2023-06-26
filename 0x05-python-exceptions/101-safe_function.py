#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as f:
        print("Exception:", f, file=sys.stderr)
        return None
