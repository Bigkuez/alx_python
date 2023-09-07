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

    # Query State objects containing the letter 'a' and order them by ID
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
