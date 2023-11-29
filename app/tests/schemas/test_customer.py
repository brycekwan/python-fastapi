"""Tests for Customer Pydantic model"""
import pytest

from pydantic import ValidationError
from app.schemas.customer import Customer


def test_maximum_name_length():
    """Test maximum name length"""

    with pytest.raises(ValidationError) as err:
        Customer(id=1, name="x"*51)
    assert (err.value.errors(include_url=False)[0]["msg"]) == "String should have at most 50 characters"
