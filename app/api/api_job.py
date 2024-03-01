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
    
@router.get("/get-all-job")
def get_all_job(page: int, limit: int, db: Session = Depends(dbConnection.get_db)):
    try:
        data_job = srv_job.get_all_job(db = db, page=page, limit=limit)
        result = [sche_job.JobResponce.model_validate(job) for job in data_job]
        return DataResponce().success_responce(data=result)
    except Exception as e:
        return DataResponce().fail_responce()

@router.get("/get-job-data")
def get_job_data(title: str, db: Session = Depends(dbConnection.get_db)):
    try:
        data_job = srv_job.get_job_infor(db = db, title = title)
        result = [sche_job.JobDetail.model_validate(job) for job in data_job]
        return DataResponce().success_responce(data=result)
    except Exception as e:
        print(e)
        return DataResponce().fail_responce()

@router.post("/create/")
def create_new_job(job_data:sche_job.JobCreate, db: Session = Depends(dbConnection.get_db)):
    try: 
        new_job = srv_job.create_job(db = db, data=job_data)
        result = sche_job.JobDetail.model_validate(new_job)
        return DataResponce().success_responce(data=result)
    except Exception as e:
        print(f"Lỗi: {e}")
        return DataResponce().fail_responce()
    

@router.delete("/delete-by-id")
def delete_by_id(id: int, db: Session = Depends(dbConnection.get_db)):
    try:
        srv_job.delete_job_by_id(db = db, id = id)
        return DataResponce().success_responce(data = "Delete successful")
    except Exception as e:
        print(e)
        return DataResponce().fail_responce()

@router.put("/update-job-data")
def update_job_data(data: sche_job.JobUpdate, db: Session = Depends(dbConnection.get_db)):
    try:
        update_data = srv_job.update_job(db = db, data = data)
        if update_data: 
            return DataResponce().success_responce(data="Success")
    except Exception as e:
        print(e)
        return DataResponce().fail_responce()