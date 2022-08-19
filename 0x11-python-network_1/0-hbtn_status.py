#!/usr/bin/python3
"""
Script to fetch a URL
"""

from urlib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url)
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        content = "Body response:\n\t- type: {}\n\t- content: {}\n\t\
                - utf8 content: {}".format(html.__class__, html, html.decode())
        print(content)
