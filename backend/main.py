from fastapi import Depends, FastAPI

from .routers import upload

app = FastAPI()


app.include_router(upload.router)
