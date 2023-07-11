#!/usr/bin/python3
"""Defines a file-appending function"""


def append_write(filename="", text=""):
    """Appends  string to the end of a UTF8

    Args:
        filename (str): name of the file
        text (str): string to append to
    """
    with open(filename, "a", encoding="utf-8") as x:
        return x.write(text)
