"""Pydantic Customer Model"""
from typing import Annotated
from pydantic import BaseModel, StringConstraints


class CustomerBase(BaseModel):
    """Attributes for customer"""
    name: Annotated[str, StringConstraints(max_length=50)]


class CustomerCreate(CustomerBase):
    """Attributes for customer creation"""
    pass


class Customer(CustomerBase):
    """Attributes for reading Customer"""
    id: int

    class Config:
        """Config to read from ORM"""
        orm_mode = True
