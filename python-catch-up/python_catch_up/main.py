from contextlib import asynccontextmanager
import os
from fastapi.staticfiles import StaticFiles
from admin.constants import BASE_DIR
from database import database
from admin import admin, admin_router
from schemas.error_response import MyException, my_exception_handler
from routers import programmers_router, graphql_router
from tortoise import Tortoise

import uvicorn
from fastapi import FastAPI, Request
from fastapi_admin.app import app as admin_app
from fastapi.middleware.cors import CORSMiddleware


description = """
## programmers
ユーザーを管理するAPI

- id: ユーザーID
- name: ユーザー名
- favorite_technology: 得意な技術
"""

tags_metadata = [
    {
        "name": "programmers",
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # CORSではhttp://localhost:3000のみ許可
    allow_methods=["POST"],  # CORSではPOSTのみ許可
)

admin_app.include_router(admin_router.router)
app.mount("/admin", admin_app)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)
app.include_router(programmers_router.router)
app.include_router(graphql_router.graphql_app, prefix="/graphql")

@app.exception_handler(MyException)
def custom_my_exception_handler(request: Request, exc: MyException):
    return my_exception_handler(request=request, exc=exc)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
