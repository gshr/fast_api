import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('PSG_USER')}:{os.getenv('PSG_PASSWORD')}@{os.getenv('PSG_HOST')}/{os.getenv('PSG_DATABASE')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()