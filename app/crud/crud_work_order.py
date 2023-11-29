"""CRUD helper methods for Work Order"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.models.work_order import WorkOrder
from app.schemas.work_order import WorkOrderCreate, WorkOrderUpdate


def get_work_order(db: Session, work_order_id: int):
    """Retrieve work order by id"""
    return db.query(WorkOrder).filter(WorkOrder.id == work_order_id).first()


def get_work_orders(db: Session):
    """Retrieve all work order"""
    return db.query(WorkOrder).all()


def create_work_order(db: Session, work_order: WorkOrderCreate):
    """Create work order"""
    work_order_model = WorkOrder(**work_order.model_dump())
    db.add(work_order_model)
    db.flush()
    db.commit()
    return work_order_model


def update_work_order(db: Session, work_order_id: int, work_order: WorkOrderUpdate):
    """Update work order"""
    work_order_model = db.query(WorkOrder).filter(
        WorkOrder.id == work_order_id).first()
    if work_order_model is None:
        raise HTTPException(status_code=404, detail="Work order not found")
    for key, value in work_order.model_dump(exclude_unset=True).items():
        setattr(work_order_model, key, value)
    db.commit()
    db.refresh(work_order_model)
    return work_order_model


def delete_work_order(db: Session, work_order_id: int):
    db.query(WorkOrder).filter(WorkOrder.id == work_order_id).delete()
    return JSONResponse({"message": "Work order deleted"}, 200)
