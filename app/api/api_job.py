import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import sche_job
from app.schemas.sche_base import DataResponce
from app.services import srv_job
from app.database import dbConnection

router = APIRouter()

@router.get("/")
def welcome_simple_app():
    return DataResponce().success_responce(data="Welcome to CRUD app")
    
@router.get("/get-job-data")
def get_job_data(title: str, db: Session = Depends(dbConnection.get_db)):
    try:
        data_job = srv_job.get_job_infor(db = db, title = title)
        return DataResponce().success_responce(data = data_job)
    except Exception as e:
        print(e)
        return DataResponce().fail_responce()

@router.post("/create/", response_model=sche_job.JobResponce)
def create_new_job(job_data:sche_job.JobCreate, db: Session = Depends(dbConnection.get_db)):
    try: 
        new_job = srv_job.create_job(db = db, data=job_data)
        return DataResponce().success_responce(data=new_job)
    except Exception as e:
        print(f"Lỗi: {e}")
        return DataResponce().fail_responce()
