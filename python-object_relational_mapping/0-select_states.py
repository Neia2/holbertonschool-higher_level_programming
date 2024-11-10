#!/usr/bin/python3
import MySQLdb
import sys

"""
Script that lists all states from the database hbtn_0e_0_usa
"""

def main():
    """
    Connects to a MySQL database and retrieves all states, sorted by id.
    """
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    mydb.commit()

    mydb.close()

if __name__ == "__main__":
    main()
