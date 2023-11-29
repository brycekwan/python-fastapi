"""Module for employee endpoints"""
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.schemas.employee import Employee, EmployeeCreate
from app.crud import crud_employee

from app.db.db import get_db

router = APIRouter()


@router.get("/employees/", response_model=list[Employee], tags=["Employees"])
def list_employees(db: Session = Depends(get_db)):
    """return list of customers"""
    return crud_employee.get_employees(db)


@router.get("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """retrieve customer by id"""
    return crud_employee.get_employee(db, employee_id)


@router.post("/employees/", response_model=Employee, tags=["Employees"])
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Create customer"""
    return crud_employee.create_employee(db, employee)


@router.put("/employees/{employee_id}", response_model=Employee, tags=["Employees"])
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Update customer by id"""
    return crud_employee.update_employee(db, employee_id, employee)


@router.delete("/employees/{employee_id}", response_model=None, tags=["Employees"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Delete customer by id"""
    return crud_employee.delete_employee(db, employee_id)
