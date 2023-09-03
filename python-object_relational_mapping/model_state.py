#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    Represents a state in the states table.

    Attributes:
        id (int): An auto-generated unique integer representing the state's ID.
        name (str): A string representing the state's name (up to 128 characters).
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
