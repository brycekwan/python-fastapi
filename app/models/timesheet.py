'''Timesheet Table Definition'''
from sqlalchemy import Column, Integer, String, Double

from app.db.base import Base


class Timesheet(Base):
    '''Class representing Timesheet table definition'''
    __tablename__ = 'timesheet'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(String)
    work_order_id = Column(String)
    employee_id = Column(String)
    hours = Column(Double)
