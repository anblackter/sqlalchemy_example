#!/usr/bin/env python3
from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def db_curriculum_vitae() -> tuple[create_engine, sessionmaker, declarative_base]:
    """Creates the engine, session local and declarative base of curriculum vitae database ans returns each one."""

    engine = create_engine('mysql+pymysql://{user}:{pw}@{host}/{db}'.format(
        user=getenv('USER_DB'),
        pw=getenv('PASS_DB'),
        host=getenv('HOST_DB'),
        db=getenv('DB'),
    ))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    return engine, SessionLocal, Base
