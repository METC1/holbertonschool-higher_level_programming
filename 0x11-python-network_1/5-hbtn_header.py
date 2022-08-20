#!/usr/bin/python3
"""
Script that takes URL , sends a request to the URL
and displays the X-request-Id of the response
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    output = req.headers.get("X-Request-Id")
    print(output)
