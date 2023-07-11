#!/usr/bin/python3
"""Defines file function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file

    Args:
        filename (str): name of the file to write
        text (str): text to be writen
    Returns:
        number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
