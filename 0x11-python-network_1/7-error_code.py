#!/usr/bin/python3
"""
Script that takes URL , sends a request to the URL
and displays the error code  of the response if any
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if int(req.status_code) < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
