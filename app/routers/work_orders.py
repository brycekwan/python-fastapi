"""Module for work order endpoints"""
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.schemas.work_order import WorkOrder, WorkOrderCreate, WorkOrderUpdate
from app.crud import crud_work_order
from app.db.db import get_db

router = APIRouter()


@router.get("/work_orders/", response_model=list[WorkOrder], tags=["Work Orders"])
def list_work_orders(db: Session = Depends(get_db)):
    """return list of work orders"""
    return crud_work_order.get_work_orders(db)


@router.get("/work_orders/{work_order_id}", response_model=WorkOrder, tags=["Work Orders"])
def get_work_order(work_order_id: int, db: Session = Depends(get_db)):
    """retrieve work order by id"""
    return crud_work_order.get_work_order(db, work_order_id)


@router.post("/work_orders/", response_model=WorkOrder, tags=["Work Orders"])
def create_work_order(work_order: WorkOrderCreate, db: Session = Depends(get_db)):
    """Create work order"""
    return crud_work_order.create_work_order(db, work_order)


@router.put("/work_orders/{work_order_id}", response_model=WorkOrder, tags=["Work Orders"])
def update_work_order(work_order_id: int, work_order: WorkOrderUpdate, db: Session = Depends(get_db)):
    """Update work order"""
    return crud_work_order.update_work_order(db, work_order_id, work_order)


@router.delete("/work_orders/{work_order_id}", response_model=None, tags=["Work Orders"])
def delete_work_order(work_order_id: int, db: Session = Depends(get_db)):
    """Delete work order by id"""
    return crud_work_order.delete_work_order(db, work_order_id)
