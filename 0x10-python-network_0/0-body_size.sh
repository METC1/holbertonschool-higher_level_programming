#!/bin/bash
#Script that takes URL, sends a requesto the the URL and then displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
