#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of htbn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    # Create a cursor object
    cur = conn.cursor()

    # Prepare SQL query
    query = "SELECT * FROM states
    WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4])

    # Execute SQL query
    cur.execute(query)

    # Fetch all rows and print them
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
