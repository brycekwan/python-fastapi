"""Test Timesheet router"""

from unittest.mock import ANY
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.timesheet import TimesheetCreate, TimesheetUpdate

client = TestClient(app)


def test_get_timesheets(mocker):
    """Test get list of timesheets"""
    mock = mocker.patch("app.crud.crud_timesheet.get_timesheets", return_value=[
                        {"id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30}])
    response = client.get("/timesheets/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30}]
    mock.assert_called()


def test_get_timesheet(mocker):
    """Test get single timesheet"""
    mock = mocker.patch("app.crud.crud_timesheet.get_timesheet", return_value={
        "id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30})
    response = client.get("/timesheets/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "project_id": 1,
                               "employee_id": 1, "work_order_id": 1, "hours": 30}
    mock.assert_called_with(ANY, 1)


def test_create_timesheet(mocker):
    """Test create timesheet"""
    mock = mocker.patch("app.crud.crud_timesheet.create_timesheet", return_value={
        "id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30})
    response = client.post(
        "/timesheets/", json={"project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30}
    mock.assert_called_with(ANY, TimesheetCreate(
        project_id=1, employee_id=1, work_order_id=1, hours=30))


def test_update_timesheet(mocker):
    """Test update timesheet"""
    mock = mocker.patch("app.crud.crud_timesheet.update_timesheet", return_value={
        "id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30})
    response = client.put("/timesheets/2", json={"hours": 50})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "project_id": 1, "employee_id": 1, "work_order_id": 1, "hours": 30}
    mock.assert_called_with(ANY, 2, TimesheetUpdate(hours=50))


def test_delete_timesheet(mocker):
    """Test delete timesheet"""
    mock = mocker.patch("app.crud.crud_timesheet.delete_timesheet", return_value={
                        "message": "Timesheet deleted"})
    response = client.delete("/timesheets/2")

    assert response.status_code == 200
    assert response.json() == {"message": "Timesheet deleted"}
    mock.assert_called_with(ANY, 2)
