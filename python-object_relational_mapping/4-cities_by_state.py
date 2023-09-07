#!/usr/bin/python3

import sys
import MySQLdb

def list_cities_and_states(username, password, database):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Create the SQL query to retrieve cities and states
        sql_query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """

        # Execute the query
        cursor.execute(sql_query)

        # Fetch all the results
        results = cursor.fetchall()

        # Close the cursor and the database connection
        cursor.close()
        db.close()

        # Print the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_cities_and_states(username, password, database)
