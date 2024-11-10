#!/usr/bin/python3
"""
Script that lists states matching a user-provided name safely
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    mydb = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
        port=3306
    )

    cursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    mydb.close()
