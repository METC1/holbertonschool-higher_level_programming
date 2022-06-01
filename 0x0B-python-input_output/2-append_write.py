#!/usr/bin/python3
"""
Appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """
    append_write Appends a string at the end of a text file
    encoded in UTF-8 and returns the number of characters
    added
    """
    with open(filename, "a", "utf-8") as f:
        return f.write(text)
