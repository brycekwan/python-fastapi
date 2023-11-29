"""Test Work Order router"""

from unittest.mock import ANY
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.work_order import WorkOrderCreate, WorkOrderUpdate

client = TestClient(app)


def test_get_work_orders(mocker):
    """Test get list of work orders"""
    mock = mocker.patch("app.crud.crud_work_order.get_work_orders", return_value=[
                        {"id": 1, "project_id": 1, "employee_id": 1, "rate": 120.0}])
    response = client.get("/work_orders/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "project_id": 1, "employee_id": 1, "rate": 120.0}]
    mock.assert_called()


def test_get_work_order(mocker):
    """Test get single work order"""
    mock = mocker.patch("app.crud.crud_work_order.get_work_order", return_value={
                        "id": 1, "project_id": 1, "employee_id": 1, "rate": 120.0})
    response = client.get("/work_orders/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "project_id": 1,
                               "employee_id": 1, "rate": 120.0}
    mock.assert_called_with(ANY, 1)


def test_create_work_order(mocker):
    """Test create work order"""
    mock = mocker.patch("app.crud.crud_work_order.create_work_order", return_value={
                        "id": 1, "project_id": 1, "employee_id": 1, "rate": 120.0})
    response = client.post(
        "/work_orders/", json={"project_id": 1, "employee_id": 1, "rate": 120.0})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "project_id": 1, "employee_id": 1, "rate": 120.0}
    mock.assert_called_with(ANY, WorkOrderCreate(
        project_id=1, employee_id=1, rate=120.0))


def test_update_work_order(mocker):
    """Test update work order"""
    mock = mocker.patch("app.crud.crud_work_order.update_work_order", return_value={
                        "id": 1, "project_id": 1, "employee_id": 1, "rate": 150.0})
    response = client.put("/work_orders/2", json={"rate": 150.0})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "project_id": 1, "employee_id": 1, "rate": 150.0}
    mock.assert_called_with(ANY, 2, WorkOrderUpdate(rate=150.0))


def test_delete_work_order(mocker):
    """Test delete work order by id"""
    mock = mocker.patch("app.crud.crud_work_order.delete_work_order", return_value={
                        "message": "Work order deleted"})
    response = client.delete("/work_orders/2")

    assert response.status_code == 200
    assert response.json() == {"message": "Work order deleted"}
    mock.assert_called_with(ANY, 2)
