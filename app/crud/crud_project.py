"""CRUD helper methods for Project"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.models.project import Project
from app.schemas.project import ProjectCreate


def get_project(db: Session, project_id: int):
    """Retrieve project by id"""
    return db.query(Project).filter(Project.id == project_id).first()


def get_projects(db: Session):
    """Retrieve all projects"""
    return db.query(Project).all()


def create_project(db: Session, project: ProjectCreate):
    """Create new project"""
    project_model = Project(**project.model_dump())
    db.add(project_model)
    db.flush()
    db.commit()
    return project_model


def update_project(db: Session, project_id: int, project: ProjectCreate):
    """Update project by id"""
    project_model = db.query(Project).filter(Project.id == project_id).first()
    if project_model is None:
        raise HTTPException(status_code=404, detail="Project not found")
    for key, value in project.model_dump(exclude_unset=True).items():
        setattr(project_model, key, value)

    db.commit()
    db.refresh(project_model)
    return project_model


def delete_project(db: Session, project_id: int):
    """Delete project by id"""
    db.query(Project).filter(Project.id == project_id).first()

    return JSONResponse({"message": "Project deleted"}, 200)
