#!/usr/bin/python3
'''script that takes in an argument and displays all values '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE BINARY name = '{:s}'"
                 .format(sys.argv[4])+"ORDER BY id ASC")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()
