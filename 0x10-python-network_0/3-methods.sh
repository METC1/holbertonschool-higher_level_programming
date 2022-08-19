#!/bin/bash
#Script that takes URL, and then displays the methods the server will accept
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " --complement -f 1
