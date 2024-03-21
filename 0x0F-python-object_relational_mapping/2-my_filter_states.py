#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of htbn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
                "Usage: {} username password database_name state_name"
                .format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database_name)
    cursor = db.cursor()

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    row = cursor.fetchone()

    # Print each row
    if row:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()
