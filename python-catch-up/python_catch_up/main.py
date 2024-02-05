from python_catch_up.models.error_response import MyException, my_exception_handler

import uvicorn
from fastapi import FastAPI, Request


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

@app.exception_handler(MyException)
def custom_my_exception_handler(request: Request, exc: MyException):
    return my_exception_handler(request=request, exc=exc)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)