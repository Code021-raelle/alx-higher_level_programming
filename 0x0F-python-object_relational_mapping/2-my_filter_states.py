#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of htbn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def main(user, password, db, state_name):
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=password, db=db)
    cursor = db.cursor()

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)

    # Close the database connection
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
