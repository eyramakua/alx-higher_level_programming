#!/bin/bash
# a Bash script that displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | cut -d '' -f2
