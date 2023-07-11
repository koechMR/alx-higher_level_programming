#!/usr/bin/python3
"""defines a text file"""


def read_file(filename=""):
    """print content in utf-8 format"""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content, end="")
