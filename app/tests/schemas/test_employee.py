"""Test for Employee Pydantic model"""
import pytest

from pydantic import ValidationError
from app.schemas.employee import Employee


def test_maximum_first_name_length():
    with pytest.raises(ValidationError) as err:
        Employee(id=1, first_name="x"*51, last_name="last")

    assert (err.value.errors(include_url=False)[
            0]["msg"]) == "String should have at most 50 characters"


def test_maximum_last_name_length():
    with pytest.raises(ValidationError) as err:
        Employee(id=1, first_name="first", last_name="last"*51)

    assert (err.value.errors(include_url=False)[
            0]["msg"]) == "String should have at most 50 characters"


def test_stripping_trailing_and_ending_whitespace():
    employee = Employee(id=1, first_name="   first ", last_name=" St Louis   ")
    assert (employee.first_name) == "first"
    assert (employee.last_name) == "St Louis"
