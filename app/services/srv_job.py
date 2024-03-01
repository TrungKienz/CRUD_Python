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

# job = Job(
#     title="Example Job",
#     begin_at=datetime.now(),
#     end_at=datetime.now(),
#     status=False,
#     content="Example content"
# )

# create_job(job)

def get_job_infor(db: Session, title: str):
    return db.query(model_job.Job).filter(model_job.Job.title == title)