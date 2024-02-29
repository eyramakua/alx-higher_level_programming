#!/bin/bash
# a Bash script that displays the size of the body of the response
curl -sl "$1" | grep -i Content-Length | cut -d '' -f2
