'''Employee Table Definition'''
from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Employee(Base):
    '''Class representing Employee table definition'''
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
