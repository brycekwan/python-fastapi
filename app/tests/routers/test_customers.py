"""Test for Customer router"""

from unittest.mock import ANY
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
from app.main import app
from app.schemas.customer import CustomerCreate

client = TestClient(app)


def test_list_customers(mocker):
    """Test list customers"""
    mock = mocker.patch("app.crud.crud_customer.get_customers",
                        return_value=[{"id": 1, "name": "customer"}])
    response = client.get("/customers/")

    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "customer"}]
    mock.assert_called()


def test_get_customer(mocker):
    """Test get single customer"""
    mock = mocker.patch("app.crud.crud_customer.get_customer",
                        return_value={"id": 1, "name": "customer"})
    response = client.get("/customers/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "customer"}
    mock.assert_called_with(ANY, 1)


def test_create_customer(mocker):
    """Test create customer"""
    mock = mocker.patch("app.crud.crud_customer.create_customer",
                        return_value={"id": 1, "name": "customer"})
    response = client.post("/customers/", json={"name": "customer"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "customer"}
    mock.assert_called_with(ANY, CustomerCreate(name="customer"))


def test_update_customer(mocker):
    """Test update customer"""
    mock = mocker.patch("app.crud.crud_customer.update_customer", return_value={
                        "id": 1, "name": "different customer"})
    response = client.put("/customers/1", json={"name": "different customer"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "different customer"}
    mock.assert_called_with(ANY, 1, CustomerCreate(name="different customer"))


def test_delete_customer(mocker):
    """Test delete customer"""
    mock = mocker.patch("app.crud.crud_customer.delete_customer",
                        return_value=JSONResponse({"message": "Customer deleted"}, 200))
    response = client.delete("/customers/1")

    assert response.status_code == 200
    assert response.json() == {"message": "Customer deleted"}
    mock.assert_called_with(ANY, 1)
