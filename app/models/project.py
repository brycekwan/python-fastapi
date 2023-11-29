'''Project Table Definition'''
from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Project(Base):
    '''Class representing Project table definition'''
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
