"""Test for Project router"""

from unittest.mock import ANY
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.project import ProjectCreate

client = TestClient(app)


def test_get_projects(mocker):
    """Test get list of projects"""
    mock = mocker.patch("app.crud.crud_project.get_projects",
                        return_value=[{"id": 1, "name": "project"}])
    response = client.get("/projects/")

    assert response.status_code == 200
    assert response.json() == [{"id": 1, "name": "project"}]
    mock.assert_called()


def test_get_project(mocker):
    """Test get single project"""
    mock = mocker.patch("app.crud.crud_project.get_project",
                        return_value={"id": 1, "name": "project"})
    response = client.get("/projects/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "project"}
    mock.assert_called_with(ANY, 1)


def test_create_project(mocker):
    """Test create project"""
    mock = mocker.patch("app.crud.crud_project.create_project",
                        return_value={"id": 1, "name": "project"})
    response = client.post("/projects/", json={"name": "project"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "project"}
    mock.assert_called_with(ANY, ProjectCreate(name="project"))


def test_update_project(mocker):
    """Test update project"""
    mock = mocker.patch("app.crud.crud_project.update_project",
                        return_value={"id": 1, "name": "project"})
    response = client.put("/projects/2", json={"name": "project2"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "project"}
    mock.assert_called_with(ANY, 2, ProjectCreate(name="project2"))


def test_delete_project(mocker):
    """Test delete proejct"""
    mock = mocker.patch("app.crud.crud_project.delete_project",
                        return_value={"message": "Project deleted"})
    response = client.delete("/projects/2")

    assert response.status_code == 200
    assert response.json() == {"message": "Project deleted"}
    mock.assert_called_with(ANY, 2)
