#!/usr/bin/python3
""" a script that prints the first State object from the database """

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
    states = session.query(State).order_by(State.id).first()

    # print results
    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
