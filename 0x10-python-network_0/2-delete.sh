#!/bin/bash
#Script that takes URL, sends a DELETE request the the URL and then displays the body of the response
curl -s -X DELETE -L  "$1"
