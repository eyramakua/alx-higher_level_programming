#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa '''


import MySQLdb
import sys


if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=uname,
                         passwd=pwd, db=database, charset="utf8")
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    states = curs.fetchall()
    for state in states:
        print(state)
    curs.close()
    db.close()
