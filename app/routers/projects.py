"""Module for projects endpoints"""
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.schemas.project import ProjectCreate, Project
from app.crud import crud_project

from app.db.db import get_db

router = APIRouter()


@router.get("/projects/", response_model=list[Project], tags=["Projects"])
def list_projects(db: Session = Depends(get_db)):
    """return list of projects"""
    return crud_project.get_projects(db)


@router.get("/projects/{project_id}", response_model=Project, tags=["Projects"])
def get_project(project_id: int, db: Session = Depends(get_db)):
    """retrieve project by id"""
    return crud_project.get_project(db, project_id)


@router.post("/projects/", response_model=Project, tags=["Projects"])
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    """Create project"""
    return crud_project.create_project(db, project)


@router.put("/projects/{project_id}", response_model=Project, tags=["Projects"])
def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    """Update project by id"""
    return crud_project.update_project(db, project_id, project)


@router.delete("/projects/{project_id}", response_model=None, tags=["Projects"])
def delete_project(project_id: int, db: Session = Depends(get_db)):
    """Delete project by id"""
    return crud_project.delete_project(db, project_id)
