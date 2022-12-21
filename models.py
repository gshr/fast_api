from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import Date
from database import Base


class Record(Base):
    __tablename__ = "Records"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    country = Column(String(255), index=True)
    cases = Column(Integer)
    deaths = Column(Integer)
    recoveries = Column(Integer)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    inventory = Column(Integer)
    is_sale = Column(Boolean)
    created_at = Column(Date)
