#!/usr/bin/python3
"""Represents State class and an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """Representation of State class
    args:
        __tablename___(str): Name of the table
        id (Integer): unique identifier of table's row
        name (String): name of states
        cities (Integer): State-City relationship
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states')
