#!/usr/bin/python3
"""Lists all states"""

import sys
import MySQLdb


def list_all(mysql_username="", mysql_password="", database_name=""):
    """
    Lists all states
    """
    con = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                          passwd=mysql_password, db=database_name,
                          charset="utf8")
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_all(username, password, database)
