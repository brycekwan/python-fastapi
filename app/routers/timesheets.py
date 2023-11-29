"""Module for projects endpoints"""
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from app.schemas.timesheet import Timesheet, TimesheetCreate, TimesheetUpdate
from app.crud import crud_timesheet
from app.db.db import get_db

router = APIRouter()


@router.get("/timesheets/", response_model=list[Timesheet], tags=["Timesheets"])
def list_timesheets(db: Session = Depends(get_db)):
    """return list of timesheets"""
    return crud_timesheet.get_timesheets(db)


@router.get("/timesheets/{timesheet_id}", response_model=Timesheet, tags=["Timesheets"])
def get_timesheet(timesheet_id: int, db: Session = Depends(get_db)):
    """retrieve timesheet by id"""
    return crud_timesheet.get_timesheet(db, timesheet_id)


@router.post("/timesheets/", response_model=Timesheet, tags=["Timesheets"])
def create_timesheet(timesheet: TimesheetCreate, db: Session = Depends(get_db)):
    """create timesheet"""
    return crud_timesheet.create_timesheet(db, timesheet)


@router.put("/timesheets/{timesheet_id}", response_model=Timesheet, tags=["Timesheets"])
def update_timesheet(timesheet_id: int, timesheet: TimesheetUpdate, db: Session = Depends(get_db)):
    """update timesheet by id"""
    return crud_timesheet.update_timesheet(db, timesheet_id, timesheet)


@router.delete("/timesheets/{timesheet_id}", response_model=None, tags=["Timesheets"])
def delete_timesheet(timesheet_id: int, db: Session = Depends(get_db)):
    """delete timesheet by id"""
    return crud_timesheet.delete_timesheet(db, timesheet_id)
