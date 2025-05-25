from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_settings
from sqlalchemy import text
from src.db.entities import Base

#import models (important for Alembic)
from src.db import entities

# Create synchronous database engine
engine = create_engine(get_settings().DATABASE_URL, echo=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_schema():
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS py_khnu;"))
        conn.commit()

create_schema()

Base.metadata.create_all(engine)

# Dependency to get a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
