'''Create db dependency'''
from app.db.session import SessionLocal


def get_db():
    '''return db session'''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
