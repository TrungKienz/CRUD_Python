from datetime import datetime
from app.model import model_job
from app.schemas import sche_job
from sqlalchemy.orm import Session

def create_job (db: Session, data: sche_job.JobCreate): 
    new_job = model_job.Job (
        title = data.title,
        begin_at = data.begin_at,
        end_at = data.end_at,
        status = False,
        content = data.content
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def get_job_infor(db: Session, title: str):
    reslut = db.query(model_job.Job).filter(model_job.Job.title == title).all()
    db.commit()
    return reslut

def delete_job_by_id(db: Session, id: int):
    result = db.query(model_job.Job).filter(model_job.Job.id == id).delete()
    db.commit()
    return result
    

def get_all_job(db: Session, page: int, limit: int):
    skip = (page - 1) * limit
    result = db.query(model_job.Job).offset(skip).limit(limit).all()
    db.commit()
    return result

def update_job(db: Session, data: sche_job.JobUpdate):
    result = db.query(model_job.Job).filter(model_job.Job.id == data.id).update({"title": data.title, "end_at": data.end_at, "status": data.status, "content": data.content})
    db.commit()
    print(result)
    return result