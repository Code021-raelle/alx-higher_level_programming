#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
import sys


def main(user, password, db):
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                user, password, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).join(City).order_by(State.id, City.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
