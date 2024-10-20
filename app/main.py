from fastapi import FastAPI
from app.routers import healthcheck
import uvicorn
from app.core.config import settings

app = FastAPI()

app.include_router(healthcheck.router)

if __name__ == "__main__":
    uvicorn.run(
        "main.app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )



