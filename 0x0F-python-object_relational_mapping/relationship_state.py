from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from model_state import Base


class State(Base):
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan")
