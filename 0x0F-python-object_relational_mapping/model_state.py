#!/usr/bin/python3
""" Contains the class definintion of State """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ Declares a state class that represents the states table """

    __tablename__ = "states"
    id = Column(
                Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=False
            )
    name = Column(String(length=128), nullable=False)
