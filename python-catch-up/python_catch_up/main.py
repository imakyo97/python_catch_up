from fastapi import FastAPI

from python_catch_up.routers import users

app = FastAPI()
app.include_router(users.router)
