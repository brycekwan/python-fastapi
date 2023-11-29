import pytest

from pydantic import ValidationError
from app.schemas.work_order import WorkOrder


def test_rate_greater_than_zero():
    with pytest.raises(ValidationError) as err:
        WorkOrder(id=1, project_id=1, employee_id=1, rate=-1)

    assert (err.value.errors(include_url=False)[
            0]['msg']) == 'Input should be greater than 0'
