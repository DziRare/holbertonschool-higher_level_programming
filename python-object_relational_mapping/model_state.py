#!/usr/bin/python3
"""The purpose of this module is to use ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Purpost of the class is to declare a table"""

    __tablename__ = "states"
    id = Column("id", Integer(11), primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)
