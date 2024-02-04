from fastapi import FastAPI

from python_catch_up.routers import users

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

app = FastAPI(
    title="PythonCatchUpAPI",
    description= description,
    summary="Pythonキャッチアップのために作成するAPI",
    version="0.0.1",
    openapi_tags=tags_metadata,
)
app.include_router(users.router)
