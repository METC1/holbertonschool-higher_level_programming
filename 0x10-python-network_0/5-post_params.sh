#!/bin/bash
#Script that takes URL, sends a POST request and then displays the body and send some  header variables
curl -s -X POST "$1" -F "email: test@gmail.com" -F "subject: I will always be here for PLD"
