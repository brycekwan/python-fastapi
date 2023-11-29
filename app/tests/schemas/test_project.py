"""Test for Project Pydantic model"""
import pytest

from pydantic import ValidationError
from app.schemas.project import Project


def test_maximum_name_length():
    """Test maximum name length to be less than 50 characters"""
    with pytest.raises(ValidationError) as err:
        Project(id=1, name="x"*51)

    assert (err.value.errors(include_url=False)[
            0]['msg']) == "String should have at most 50 characters"


def test_remove_trailing_and_ending_whitespace():
    """Test removing whitespace from name"""
    project = Project(id=1, name=" my project   ")

    assert (project.name) == "my project"
