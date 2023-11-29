"""Pydantic WorkOrder Model"""
from typing import Annotated
from pydantic import BaseModel, Field


class WorkOrderBase(BaseModel):
    """Attributes for reading and writing to WorkOrder"""
    rate: Annotated[float, Field(gt=0)]


class WorkOrderCreate(WorkOrderBase):
    """Attributes for create"""
    project_id: int
    employee_id: int


class WorkOrder(WorkOrderBase):
    """Atributes for read"""
    id: int
    project_id: int
    employee_id: int

    class Config:
        """Config to read from ORM"""
        orm_mode = True


class WorkOrderUpdate(WorkOrderBase):
    """Attributes for update"""
