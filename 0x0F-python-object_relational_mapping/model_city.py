#!/usr/bin/python3
""" a python file that contains the class definition of a City and
inherits from the Base model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

stateMeta = MetaData()  # parameterize metadata for modular use

Base = declarative_base(metadata=stateMeta)  # create Base instance


class City(Base):
    """Creates an instance of City

    Args:
        id(int): id of city
        name(str): name of city
        state_id: id of city in the state
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey("states.id"))
