#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from model_state import Base


class State(Base):
    """Class representing a state"""

    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", back_populates="state", cascade="all, delete-orphan")

    def __str__(self):
        return "{}".format(self.name)
