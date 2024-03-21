#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(user, password, db):
    engine = create_engine(
            'mysql+mysqldb://{}:{}@locahost/ {}'.format(
                user, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)

    session.commit()

    session.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
