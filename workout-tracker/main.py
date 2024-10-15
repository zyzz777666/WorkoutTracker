import uvicorn
from fastapi import FastAPI

from core.config import settings

from api import router as api_router

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app="main:app",
                host=settings.run.host,
                port=settings.run.port,
                reload=True)
