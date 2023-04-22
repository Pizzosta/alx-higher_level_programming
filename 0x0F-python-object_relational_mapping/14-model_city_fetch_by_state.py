#!/usr/bin/python3
""" a script that prints all City objects from the database """

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    # Execute query
    for city, state in (session.query(City, State)
                        .filter(State.id == City.state_id)):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
