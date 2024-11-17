#!/usr/bin/python3
"""
Script that lists all states with names starting with 'N'
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    mydb = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
        port=3306
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    mydb.close()