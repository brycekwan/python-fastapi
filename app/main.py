"""Main app"""
from fastapi import FastAPI
from app.routers import customers, employees, projects, timesheets, work_orders
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

app.include_router(customers.router)
app.include_router(employees.router)
app.include_router(projects.router)
app.include_router(timesheets.router)
app.include_router(work_orders.router)
