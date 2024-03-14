#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. (Safe from SQL injection)
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

    # Prepare SQL query with placeholders
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute SQL query with user input as parameters
    cur.execute(query, (sys.argv[4],))

    # Fetch all rows and print them
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()
