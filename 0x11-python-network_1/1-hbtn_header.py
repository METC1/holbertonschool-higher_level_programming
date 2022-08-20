#!/usr/bin/python3
"""
Script that takes URL as argument, sends a request to the URL and
display X-Request-Id variable value from header
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(url) as response:
        html = response.info()
        content = html.get("X-Request-Id")
        print(content)
