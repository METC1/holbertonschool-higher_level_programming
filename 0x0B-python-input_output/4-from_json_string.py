#!/usr/bin/python3
"""
Returns an object (Python data structure) as JSON string
"""
import json


def from_json_string(my_str):
    """
    The function that returns an object
    (Python data structure) as a JSON string
    """
    return json.loads(my_str)
