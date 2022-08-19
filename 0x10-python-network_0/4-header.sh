#!/bin/bash
#Script that takes URL, sends a GET request and then displays the body and send a header variable
curl -s -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"
