#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password detabase_name state_name".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found)

    session.close()
