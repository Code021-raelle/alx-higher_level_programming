#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing a state"""

    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "relationship_city.City", backref="state", cascade="all, delete")
