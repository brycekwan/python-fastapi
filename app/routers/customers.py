"""Module for customer endpoints"""
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.crud import crud_customer
from app.schemas.customer import Customer, CustomerCreate

from app.db.db import get_db

router = APIRouter()


@router.get("/customers/", response_model=list[Customer], tags=["Customers"])
def list_customers(db: Session = Depends(get_db)):
    """return list of customers"""
    return crud_customer.get_customers(db)


@router.get("/customers/{customer_id}", response_model=Customer, tags=["Customers"])
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """retrieve customer by id"""
    return crud_customer.get_customer(db, customer_id)


@router.post("/customers/", response_model=Customer, tags=["Customers"])
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    """create customer"""
    return crud_customer.create_customer(db, customer)


@router.put("/customers/{customer_id}", response_model=Customer, tags=["Customers"])
def update_customer(customer_id: int, customer: CustomerCreate, db: Session = Depends(get_db)):
    """update customer"""
    return crud_customer.update_customer(db, customer_id, customer)


@router.delete("/customers/{customer_id}", response_model=None, tags=["Customers"])
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """delete customer"""
    return crud_customer.delete_customer(db, customer_id)
