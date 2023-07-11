#!/usr/bin/python3
"""defines write function"""


def write_file(filename="", text=""):
    """write the content"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text) - text.count("\n")
