'''Customer Table Definition'''
from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Customer(Base):
    '''Class representing Customer table definition'''
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
