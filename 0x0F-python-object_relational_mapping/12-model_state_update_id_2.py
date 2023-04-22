#!/usr/bin/python3
""" script that changes the name of a State object from the database """

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

    # execute query
    state = session.query(State).filter(State.id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    # close session
    session.close()
