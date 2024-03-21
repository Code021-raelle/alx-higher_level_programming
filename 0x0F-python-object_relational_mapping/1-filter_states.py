#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
htbn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cursor = db.cursor()

    # Execute the query to select all states with names starting "N"
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    cursor.close()
    db.close()
