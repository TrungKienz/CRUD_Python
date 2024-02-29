import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Setting(BaseSettings):
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    SQL_DATABASE_URL: str = os.getenv("SQL_DATABASE__URL", "")
    PORT: int = os.getenv("PORT", 8000)
    HOST: str = os.getenv("HOST", "0.0.0.0")


setting = Setting()