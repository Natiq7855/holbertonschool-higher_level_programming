#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class inherits from Base and links to the MySQL table 'cities'.
    """
    __tablename__ = 'cities'

    # Auto-generated, unique integer, can't be null, primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # String with max 128 characters, can't be null
    name = Column(String(128), nullable=False)

    # Foreign key to states.id, can't be null
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
