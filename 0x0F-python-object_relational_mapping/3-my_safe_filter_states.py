#!/usr/bin/python3
"""
Filters the states table by user input
"""

import MySQLdb
import sys


def list_all_match(mysql_username="", mysql_password="", database_name="",
                   match=""):
    """Takes an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument"""
    con = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                          passwd=mysql_password, db=database_name,
                          charset="utf8")
    cur = con.cursor()
    sql = "SELECT * FROM states WHERE name =%s ORDER BY id ASC"
    cur.execute(sql, (match,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match = sys.argv[4]
    list_all_match(username, password, database, match)
