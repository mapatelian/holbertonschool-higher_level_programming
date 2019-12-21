#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""

import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    pswd = sys.argv[2]
    dname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=pswd, db=dname, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE " +
                "name LIKE BINARY 'N%' ORDER BY 'states.id' ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
