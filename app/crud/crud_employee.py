"""CRUD helper methods for Employee"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


def get_employee(db: Session, employee_id: int):
    """Retrieve employee by id"""
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employees(db: Session):
    """Retrieve all employees"""
    return db.query(Employee).all()


def create_employee(db: Session, employee: EmployeeCreate):
    """Create employee"""
    employee_model = Employee(**employee.model_dump())
    db.add(employee_model)
    db.flush()
    db.commit()
    return employee_model


def update_employee(db: Session, employee_id: int, employee: EmployeeCreate):
    """Update employee"""
    employee_model = db.query(Employee).filter(
        Employee.id == employee_id).first()
    if employee_model is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in employee.model_dump().items():
        setattr(employee_model, key, value)

    db.commit()
    db.refresh(employee_model)
    return employee_model


def delete_employee(db: Session, employee_id: int):
    """Delete employee"""
    db.query(Employee).filter(Employee.id == employee_id).delete()

    return JSONResponse({"message": "Employee deleted"}, 200)
