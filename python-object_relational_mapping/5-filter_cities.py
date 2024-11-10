#!/usr/bin/python3
"""
Script that lists all cities of a given state
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
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    mydb.close()
