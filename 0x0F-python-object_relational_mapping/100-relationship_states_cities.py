#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name="California")

    new_city = City(name="San Francisco", state=new_state)

    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()

    session.close()
