#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database
htbn_0e_0_usa.
"""
import MySQLdb
import sys


def main(user, password, db):
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=password, db=db)
    cursor = db.cursor()

    # Execute the query to select all states with names starting "N"
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)

    # Close the database connection
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
