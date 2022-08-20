#!/usr/bin/python3
"""
Script that takes URL and email as arguments, sends a POST
request to the URL and displays the body of the response in utf-8
"""

from urllib import (request, parse)
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except request.HTTPError as error:
        print("Error code: {}".format(error.code))

