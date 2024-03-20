#!/usr/bin/python3

import MySQLdb
import sys


def main(user, password, db):
    # Connect to the database
    db = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=password, db=db)
    cursor = db.cursor()

    # Execute the query to select all cities, sorted by id and join with states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)

    # Close the database connection
    db.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
