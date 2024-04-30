#!/usr/bin/python3
"""
Define Class Sate
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.exit.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State; instance of Base
    Linked to MySQL table "states"
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
