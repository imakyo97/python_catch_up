from fastapi import FastAPI

from .routers import users

app = FastAPI()
app.router(users.router)
