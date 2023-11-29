"""Test for Employee router"""

from unittest.mock import ANY
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.employee import EmployeeCreate

client = TestClient(app)


def test_get_employees(mocker):
    """Test get employees"""
    mock = mocker.patch("app.crud.crud_employee.get_employees", return_value=[
                        {"id": 1, "first_name": "first", "last_name": "last"}])
    response = client.get("/employees/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "first_name": "first", "last_name": "last"}]
    mock.assert_called()


def test_get_employee(mocker):
    """Test get single employee"""
    mock = mocker.patch("app.crud.crud_employee.get_employee", return_value={
                        "id": 1, "first_name": "first", "last_name": "last"})
    response = client.get("/employees/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "first_name": "first", "last_name": "last"}
    mock.assert_called_with(ANY, 1)


def test_create_employee(mocker):
    """Test create employee"""
    mock = mocker.patch("app.crud.crud_employee.create_employee", return_value={
                        "id": 1, "first_name": "first", "last_name": "last"})
    response = client.post(
        "/employees/", json={"first_name": "first", "last_name": "last"})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "first_name": "first", "last_name": "last"}
    mock.assert_called_with(ANY, EmployeeCreate(
        first_name="first", last_name="last"))


def test_update_employee(mocker):
    """Test update employee"""
    mock = mocker.patch("app.crud.crud_employee.update_employee", return_value={
                        "id": 1, "first_name": "first", "last_name": "last"})
    response = client.put(
        "/employees/1", json={"first_name": "first", "last_name": "last"})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "first_name": "first", "last_name": "last"}
    mock.assert_called_with(ANY, 1, EmployeeCreate(
        first_name="first", last_name="last"))


def test_delete_employee(mocker):
    """Test delete employee"""
    mock = mocker.patch("app.crud.crud_employee.delete_employee", return_value={
                        "message": "Employee deleted"})
    response = client.delete("/employees/2")

    assert response.status_code == 200
    assert response.json() == {"message": "Employee deleted"}
    mock.assert_called_with(ANY, 2)
