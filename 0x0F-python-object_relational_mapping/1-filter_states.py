#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""

import MySQLdb
import sys


def list_all_n(mysql_username="", mysql_password="", database_name=""):
    """
    Lists all states with a name starting with N
    """
    con = MySQLdb.connect(host="localhost", port=3306, user=username,
                          passwd=password, db=database,
                          charset="utf8")
    cur = con.cursor()
    sql = "SELECT * FROM states WHERE name LIKE BINARY 'N%'  ORDER BY id ASC"
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_all_n(username, password, database)
