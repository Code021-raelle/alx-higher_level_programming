#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
htbn_0e_0_usa.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Execute the query to select all states with names starting "N"
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    # Fetch all the rows
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)
