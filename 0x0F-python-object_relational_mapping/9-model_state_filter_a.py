#!/usr/bin/python3
""" a script that lists all State objects
that contain the letter a from the database """

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

    # Execute query
    states = session.query(State).filter(State.name.like("%a%")).all()

    # print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
