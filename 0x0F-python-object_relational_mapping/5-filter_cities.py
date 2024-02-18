#!/usr/bin/python3
'''task 3 '''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = db.cursor()
    curs.execute("""SELECT name FROM cities WHERE (SELECT id FROM states WHERE
                  BINARY name = %s) = state_id""", (sys.argv[4],))
    states = curs.fetchall()
    print(", ".join([state[0] for state in states]))
    curs.close()
    db.close()
