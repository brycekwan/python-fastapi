"""Test for Timesheet Pydantic model"""
import pytest
from pydantic import ValidationError
from app.schemas.timesheet import Timesheet


def test_hours_greater_than_zero():
    with pytest.raises(ValidationError) as err:
        Timesheet(id=1, project_id=1, work_order_id=1, employee_id=1, hours=-1)

    assert (err.value.errors(include_url=False)[
            0]['msg']) == "Input should be greater than 0"
