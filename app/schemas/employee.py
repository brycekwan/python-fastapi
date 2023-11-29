"""Pydantic Employee Model"""
from typing import Annotated
from pydantic import BaseModel, StringConstraints


class EmployeeBase(BaseModel):
    """Base model for Employee"""
    first_name: Annotated[str, StringConstraints(
        max_length=50, strip_whitespace=True)]
    last_name: Annotated[str, StringConstraints(
        max_length=50, strip_whitespace=True)]


class EmployeeCreate(EmployeeBase):
    """Model for writing to employee"""
    pass


class Employee(EmployeeBase):
    """Model for reading Employee"""
    id: int

    class Config:
        """Config to read from ORM"""
        orm_mode = True
