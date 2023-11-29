"""Pydantic Project Model"""
from typing import Annotated
from pydantic import BaseModel, StringConstraints


class ProjectBase(BaseModel):
    """Attributes for reading and writing to Project"""
    name: Annotated[str, StringConstraints(
        max_length=50, strip_whitespace=True)]


class ProjectCreate(ProjectBase):
    """Model for writing"""

class Project(ProjectBase):
    """Model for reading"""
    id: int

    class Config:
        """Config to read from ORM"""
        orm_mode = True
