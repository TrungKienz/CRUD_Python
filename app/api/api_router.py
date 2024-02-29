from fastapi import APIRouter

from app.api import api_job

router = APIRouter()

router.include_router(api_job.router, tags=["job"], prefix="/job")