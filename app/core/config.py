import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Setting(BaseSettings):
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USERNAME: str = os.getenv("DB_USERNAME", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_URL: str = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    APP_PORT: int = os.getenv("APP_PORT", 8000)
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")


setting = Setting()