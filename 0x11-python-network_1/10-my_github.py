#!/usr/bin/python3
"""
Script that takes github credetials to only access your info,
uses the githubAPI and prints your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    usr = argv[1]
    pwd = argv[2]
    req = requests.get('https//api.github.com/user', auth=(usr, pwd))
    print(req.json().get('id'))
