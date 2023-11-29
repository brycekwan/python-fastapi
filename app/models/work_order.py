'''Work Order Table Definition'''
from sqlalchemy import Column, Integer, Double

from app.db.base import Base


class WorkOrder(Base):
    '''Class representing Work Order table definition'''
    __tablename__ = 'work_order'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer)
    employee_id = Column(Integer)
    rate = Column(Double)
