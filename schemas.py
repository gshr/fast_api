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