#!/usr/bin/python3
"""
Lists all cities matching a specific state from the database
"""

import sys
import MySQLdb


def list_all_match(mysql_username="", mysql_password="", database_name="",
                   match=""):
    """
    Lists all cities from a state from a database
    """
    con = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                          passwd=mysql_password, db=database_name,
                          charset="utf8")
    cur = con.cursor()
    sql = "SELECT cities.name FROM cities"
    sql += " JOIN states ON state_id=states.id WHERE "
    sql += "states.name LIKE BINARY %s ORDER BY cities.id ASC"
    cur.execute(sql, (match,))
    query_rows = cur.fetchall()
    print(", ".join(rows[0] for rows in query_rows))
    cur.close()
    con.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match = sys.argv[4]
    list_all_match(username, password, database, match)
