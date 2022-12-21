import csv
import datetime
import models
from database import SessionLocal, engine

db = SessionLocal()

# models.Base.metadata.create_all(bind=engine)


    
db_record = models.Record(
    date=datetime.datetime.strptime("2022-10-10", "%Y-%m-%d"),
    country="country",
    cases=123,
    deaths=12,
    recoveries=23,
)
db.add(db_record)

db.commit()

db.close()