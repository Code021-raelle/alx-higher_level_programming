#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # connect to MySQL server
    conn = MySQLdb_connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    # Create a cursor object
    cur = conn.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
