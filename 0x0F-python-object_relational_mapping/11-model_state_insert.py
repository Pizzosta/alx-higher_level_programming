#!/usr/bin/python3
""" a script that adds the State object “Louisiana”
to the database """

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

    # Create and add a new state to the session.
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # print results
    print("{}".format(new_state.id))
