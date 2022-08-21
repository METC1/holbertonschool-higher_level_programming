#!/usr/bin/python3
"""
Script that takes in a letter , sends a POST request
to the URL 0.0.0.0:5000 with the letter as parameter
and prints if valid JSON response
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = ""
    if len(argv) != 1:
        letter = argv[1]
    datasend = {'q': letter}
    req = requests.post(url, data=datasend)
    try:
        response_json = req.json()
        if response_json:
            print("[{}] {}".format(response_json.get('id'),
                  response_json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
