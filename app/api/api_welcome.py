from fastapi import APIRouter
from app.schemas import sche_base

router = APIRouter()

@router.get("/")
def welcome_test():
    return sche_base.DataResponce().success_responce(data = "Welcome test")