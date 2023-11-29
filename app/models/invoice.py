'''Invoice Table Definition'''
from sqlalchemy import Column, Integer, Double

from app.db.base import Base


class Invoice(Base):
    '''Class representing Invoice table definition'''
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer)
    hours = Column(Double)
    subtotal = Column(Double)
    total = Column(Double)
