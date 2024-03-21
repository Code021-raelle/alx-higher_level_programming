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

    new_state = State(name="California")

    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.add(new_city)

    session.commit()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
