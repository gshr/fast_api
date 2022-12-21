from datetime import date
from pydantic import BaseModel


class Record(BaseModel):
    date: date
    country: str
    cases: int
    deaths: int
    recoveries: int

    class Config:
        orm_mode = True


class Products(BaseModel):
    id: int
    name: str
    price: int
    inventory: int
    is_sale: bool

    class Config:
        orm_mode = True
