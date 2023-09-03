#!/usr/bin/python3

import sys
import MySQLdb

def list_cities(username, password, database):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password, db=database
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Define the SQL query to retrieve all cities sorted by cities.id
        sql_query = "SELECT * FROM cities ORDER BY id ASC"
        
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
        list_cities(username, password, database)
