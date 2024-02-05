from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    code: int
    title: str
    message: str

class MyException(Exception):
    def __init__(self, code: int, title: str, message: str) -> None:
        self.code = code
        self.title = title
        self.message = message

def my_exception_handler(request: Request, exc: MyException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.code,
        content=ErrorResponse(code=exc.code, title=exc.title, message=exc.message).model_dump()
    )

not_found = {404: {"model": ErrorResponse}}