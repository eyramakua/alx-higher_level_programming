#!/usr/bin/python3
'''
sends a POST request to the passed URL with the email as a parameter
'''

import urllib.request
from sys import argv


if __name__ == "__main__":
    body = urllib.parse.urlencode({'email': argv[2]})
    body = body.encode('ascii')
    with urllib.request.urlopen(argv[1], body) as url:
        print(url.read().decode('utf-8'))
