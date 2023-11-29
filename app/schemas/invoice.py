'''Pydantic Invoice Model'''
from pydantic import BaseModel


class Invoice(BaseModel):
    '''Attributes for reading and writing to Invoice'''
    id: int
    customer_id: int
    hours: float
    subtotal: float
    total: float

    class Config:
        '''Config to read from ORM'''
        orm_mode = True
