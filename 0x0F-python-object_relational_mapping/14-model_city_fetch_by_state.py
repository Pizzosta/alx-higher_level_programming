#!/usr/bin/python3
""" a script that prints all City objects from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # generate database schema
    Base.metadata.create_all(engine)

    # create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    cities = session.query(City).order_by(City.id).all()

    # delete all returned records
    for city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
