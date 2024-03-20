#!/usr/bin/python3

import MySQLdb
import sys


def main(user, password, db, state_name):
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=password, db=db)

    # Use parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    results = cursor.fetchall()

    # Print each city name
    for row in results:
        print(row[0])

    # Close the database connection
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
