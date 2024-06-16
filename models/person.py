from __future__ import annotations
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Person(Base):
    """Define the model for the person Table."""

    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(250))
    phone = Column(String(100))
    title = Column(String(200))
    gender = Column(String(1))