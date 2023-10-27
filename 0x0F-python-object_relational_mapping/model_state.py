#!/usr/bin/python3
""" Contains State class (which links to the MySQL table- states). """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Links to states table of a MySQL database.

    __tablename__ (str): The name of the table.
    id (int): Primary key, unique id of a state.
    name (str): Th ename of a state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
