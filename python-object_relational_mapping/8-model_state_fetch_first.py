#!/usr/bin/python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a SQLAlchemy engine to connect to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database))

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object ordered by ID
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
