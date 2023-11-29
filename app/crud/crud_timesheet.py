"""CRUD helper methods for Timesheet"""
from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.models.timesheet import Timesheet
from app.schemas.timesheet import TimesheetCreate, TimesheetUpdate


def get_timesheet(db: Session, timesheet_id: int):
    """Retrieve timesheet by id"""
    return db.query(Timesheet).filter(Timesheet.id == timesheet_id).first()


def get_timesheets(db: Session):
    """Retrieve all timesheets"""
    return db.query(Timesheet).all()


def create_timesheet(db: Session, timesheet: TimesheetCreate):
    """Create timesheet"""
    timesheet_model = Timesheet(**timesheet.model_dump())
    db.add(timesheet_model)
    db.flush()
    db.commit()
    return timesheet_model


def update_timesheet(db: Session, timesheet_id: int, timesheet: TimesheetUpdate):
    """Update timesheet"""
    timesheet_model = db.query(Timesheet).filter(
        Timesheet.id == timesheet_id).first()
    if timesheet_model is None:
        raise HTTPException(status_code=404, detail="Timesheet not found")
    for key, value in timesheet.model_dump().items():
        setattr(timesheet_model, key, value)
    db.commit()
    db.refresh(timesheet_model)
    return timesheet_model


def delete_timesheet(db: Session, timesheet_id):
    """Delete timesheet"""
    db.query(Timesheet).filter(Timesheet.id == timesheet_id).delete()

    return JSONResponse({"message": "Timesheet deleted"}, 200)
