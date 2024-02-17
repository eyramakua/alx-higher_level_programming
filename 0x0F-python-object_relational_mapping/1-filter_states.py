#!/usr/bin/python3
''' script that lists all states with a name starting with N '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = db.cursor()
    curs.execute("""SELECT * FROM states WHERE name
                 LIKE BINARY 'N%' ORDER BY id ASC""")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()
