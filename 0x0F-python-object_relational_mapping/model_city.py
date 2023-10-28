#!/usr/bin/python3
""" Contains City class (which links to the MySQL table- cities). """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Links to cities table of a MySQL database.

    __tablename__ (str): The name of the table.
    id (int): Primary key, unique id of a state.
    name (str): The name of a city.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
