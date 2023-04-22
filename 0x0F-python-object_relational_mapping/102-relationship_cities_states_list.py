#!/usr/bin/python3
""" a script that lists all City objects from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # generate database schema
    Base.metadata.create_all(engine)

    # create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # execute query
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.states.name))

    # close session
    session.close()
