import MySQLdb
import sys

def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve the states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the query result
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states(username, password, database_name)
