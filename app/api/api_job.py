from fastapi import APIRouter
from app.schemas.sche_job import JobItem
from app.schemas.sche_base import DataResponce
from app.services import srv_job

router = APIRouter()

@router.get("/")
def welcome_simple_app():
    return DataResponce().success_responce(data="Welcome to CRUD app")


@router.post("/create/", response_model=JobItem)
async def create_new_job(job_data:JobItem):
    try: 
        new_job = await srv_job.create_job(job_data)
        return DataResponce().success_responce(data=new_job)
    except Exception as e:
        print(e)
        return DataResponce().fail_responce()
