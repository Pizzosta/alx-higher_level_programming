#!/usr/bin/python3
""" a script that prints all City objects from the database """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    state_city = (session.query(State, City).filter(State.id == City.state_id).
                  order_by(City.id))

    # all returned records
    for state, city in state_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
