#!/usr/bin/python3


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwwd=sys.argv[2], db=sys.argv[3], charset="utf8")

