"""Pydantic Timesheet Model"""
from typing import Annotated
from pydantic import BaseModel, Field


class TimesheetBase(BaseModel):
    """Attributes for reading and writing to Timesheet"""
    hours: Annotated[float, Field(gt=0)]


class TimesheetCreate(TimesheetBase):
    """Model for creating timesheet"""
    project_id: int
    work_order_id: int
    employee_id: int


class TimesheetUpdate(TimesheetBase):
    """Model for updating timesheet"""


class Timesheet(TimesheetBase):
    """Model for reading timesheet"""
    id: int
    project_id: int
    work_order_id: int
    employee_id: int

    class Config:
        """Config to read from ORM"""
        orm_mode = True
