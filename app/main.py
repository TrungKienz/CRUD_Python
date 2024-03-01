import uvicorn

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from app.core.config import setting 
from app.api.api_router import router

def get_application() -> FastAPI:
    application = FastAPI(
        title="CRUD_Simple_App",
        docs_url="/docs",
        redoc_url="/re-docs"
    )

    application.add_middleware(DBSessionMiddleware, db_url=setting.DB_URL)

    application.include_router(router)
    
    return application 

app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host=setting.APP_HOST, port=setting.APP_PORT)
