#!/usr/bin/python3
"""
Script that takes URL and email as arguments, sends a POST
request to the URL and displays the body of the response in utf-8
"""

from urllib import (request, parse)
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    value_enc = parse.urlencode(value)
    value_enc = value_enc.encode('ascii')
    req = request.Request(url, value_enc)
    with request.urlopen(url) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
