"""CRUD helper methods for Customer"""
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_customer(db: Session, customer: CustomerCreate):
    """Create customer"""
    customer_model = Customer(**customer.model_dump())
    db.add(customer_model)
    db.flush()
    db.commit()
    return customer_model


def get_customer(db: Session, customer_id: int):
    """Retrieve customer by id"""
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


def get_customers(db: Session):
    """Retrieve all customers"""
    return db.query(Customer).all()


def update_customer(db: Session, customer_id: int, customer: CustomerCreate):
    """Update customer"""
    customer_model = db.query(Customer).filter(
        Customer.id == customer_id).first()
    if customer_model is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer.model_dump().items():
        setattr(customer_model, key, value)

    db.commit()
    db.refresh(customer_model)
    return customer_model


def delete_customer(db: Session, customer_id: int) -> JSONResponse:
    """Delete customer"""
    db.query(Customer).filter(Customer.id == customer_id).delete()
    db.commit()
    return JSONResponse({"message": "Customer deleted"}, 200)
