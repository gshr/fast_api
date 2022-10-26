from typing import List
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from  schemas import Record
import models, schemas
from database import SessionLocal, engine
import datetime

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


@app.get("/records/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records = db.query(models.Record).all()
    return records

@app.post("/records/")
def add_records(records:Record,db: Session = Depends(get_db)):
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

@app.get("/record/{id_no}")
def get_records(id_no,db:Session = Depends(get_db)) -> schemas.Record:
    print(id_no)
    
    db_record = db.query(models.Record).filter(models.Record.id == id_no).all()
    if db_record:
        return db_record
    raise HTTPException(status_code=404,detail="Item not found")



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
