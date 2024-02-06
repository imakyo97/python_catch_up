from contextlib import asynccontextmanager
from python_catch_up.database import database
from python_catch_up.admin import admin
from python_catch_up.schemas.error_response import MyException, my_exception_handler
from python_catch_up.routers import users_router
from tortoise import Tortoise

import uvicorn
from fastapi import FastAPI, Request
from fastapi_admin.app import app as admin_app

description = """
## Users
ユーザーを管理するAPI

- id: ユーザーID
- name: ユーザー名
- favorite_technology: 得意な技術
"""

tags_metadata = [
    {
        "name": "users",
        "description": "ユーザー管理API"
    },
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init(app=app)
    await admin.startup()
    yield
    await Tortoise.close_connections()

app = FastAPI(
    title="PythonCatchUpAPI",
    description= description,
    summary="Pythonキャッチアップのために作成するAPI",
    version="0.0.1",
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)
app.mount("/admin", admin_app)
app.include_router(users_router.router)

@app.exception_handler(MyException)
def custom_my_exception_handler(request: Request, exc: MyException):
    return my_exception_handler(request=request, exc=exc)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)