#!/usr/bin/python3
"""Represents City class and an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """Representation of City class
    args:
        __tablename___(str): Name of the table
        id (int): unique identifier of table's row
        name (str): name of city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
