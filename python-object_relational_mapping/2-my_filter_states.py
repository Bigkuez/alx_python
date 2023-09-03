#!/usr/bin/python3

import sys
import MySQLdb

def search_states(username, password, database, search_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Create the SQL query using user input (search_name)
        sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
        
        # Execute the query with the user input as a parameter
        cursor.execute(sql_query, ('%' + search_name + '%',))

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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <search_name>".format(sys.argv[0]))
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        search_name = sys.argv[4]
        search_states(username, password, database, search_name)
