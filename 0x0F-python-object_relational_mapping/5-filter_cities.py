#!/usr/bin/python3
"""
Lists all cities matching a specific state from the database
"""

import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    pswd = sys.argv[2]
    dname = sys.argv[3]
    staten = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=pswd, db=dname, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities " +
                "JOIN states ON cities.state_id = states.id " +
                "WHERE states.name = %s ORDER BY cities.id ASC", (staten,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
