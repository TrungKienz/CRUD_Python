from app.model.model_job import Job
from app.schemas.sche_job import JobItem
from fastapi_sqlalchemy import db

async def create_job (data: JobItem): 
    new_job = Job (
        title = data.title,
        begin_at = data.begin_at,
        end_at = data.end_at,
        status = False,
        content = data.content
    )

    await db.session.add(new_job)
    db.session.commit()
    return new_job

