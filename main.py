import datetime
from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from starlette.responses import RedirectResponse

import models
import schemas
from database import SessionLocal, engine
from schemas import Record

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/records/", response_model=List[schemas.Products], status_code=status.HTTP_200_OK)
def show_records(offset: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    records = db.query(models.Product).order_by(models.Product.id).offset(offset).limit(limit).all()
    return records


@app.get("/productsale/", status_code=status.HTTP_200_OK)
async def show_records(offset: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    records = db.query(models.Product.is_sale, func.count(models.Product.inventory).label('count')).group_by(
        models.Product.is_sale).all()
    return records


@app.post("/records/", status_code=status.HTTP_200_OK)
def add_records(records: Record, db: Session = Depends(get_db)):
    db_record = models.Record(
        date=datetime.datetime.strptime("2022-10-10", "%Y-%m-%d"),
        country=records.country,
        cases=records.cases,
        deaths=records.deaths,
        recoveries=records.recoveries,
    )
    db.add(db_record)
    db.commit()
    db.close()
    return {"message": "Data Saved Successfully"}


@app.get("/record/{id}")
async def get_records(id: int, db: Session = Depends(get_db)) -> schemas.Products:
    db_record = db.query(models.Product).filter(models.Product.id == id).first()
    if db_record:
        return db_record
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
