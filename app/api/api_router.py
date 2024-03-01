from fastapi import APIRouter

from app.api import api_job, api_welcome

router = APIRouter()

router.include_router(api_job.router, tags=["job"], prefix="/job")
router.include_router(api_welcome.router, tags=["welcome"], prefix="")