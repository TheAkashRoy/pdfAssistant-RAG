from fastapi import Depends, FastAPI
from .routers import upload, chat

app = FastAPI()


app.include_router(upload.router)
app.include_router(chat.router)
