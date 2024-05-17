from fastapi import Depends, FastAPI
from .routers import upload, chat
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(chat.router)
