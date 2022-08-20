#!/usr/bin/python3
"""
Script that takes URL and email as arguments, sends a POST
request to the URL and displays the body of the response in utf-8
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = requests.get(url).text
    output = "Body response:\n\t- type: {}\n\t- content: {}\
".format(type(req), req, req)
    print(output)
