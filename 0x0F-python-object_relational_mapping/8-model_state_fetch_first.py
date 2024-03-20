#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main(user, password, db):
    # Create an engine that stores data in the local directory's
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                user, password, db), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the states table for the first state
    state = session.query(State).order_by(State.id).first()

    # Check if a state was found
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    # Class the session
    session.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
