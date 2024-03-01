from typing import Generator
from app.core.config import setting
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(setting.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()