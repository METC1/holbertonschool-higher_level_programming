#!/bin/bash
#Script that takes URL, sends a GET requesto the the URL and then displays only  the body of the response
curl -s -X GET -L "$1"
