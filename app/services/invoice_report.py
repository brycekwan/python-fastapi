'''Service for Invoice reporting'''
from sqlalchemy.orm import Session

from app.models.employee import Employee


def get_employee(db: Session, employee_id: int):
    '''Retrieve employee by id'''
    return db.query(Employee).filter(Employee.id == employee_id).first()


def get_employees(db: Session):
    '''Retrieve all employees'''
    return db.query(Employee).all()
