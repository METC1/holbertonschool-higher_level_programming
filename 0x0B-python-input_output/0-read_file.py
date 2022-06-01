#!/usr/bin/python3
"""
    read_file
    Reads a file
"""


def read_file(filename=""):
    """
    Read atext file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
