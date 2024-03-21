#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name"
                .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database_name)

    cursor = db.cursor()

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
    rows = cursor.fetchall()

    cities = [row[0] for row in rows]

    # Print each city name
    if cities:
        print(", ".join(cities))

    # Close the database connection
    cursor.close()
    db.close()
