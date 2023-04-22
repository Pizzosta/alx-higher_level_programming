#!/usr/bin/python3
"""
Create a db schema using SQLAlchemy
The script will create a class definition of City and an instance
'Base = declarative_base()'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Creates an instance of City

    Args:
        id(int): id of city
        name(str): name of city
        state_id(int): id of State where City is located
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
