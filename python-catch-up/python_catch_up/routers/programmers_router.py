from schemas.schemas import Programmer, ProgrammerData
from schemas.error_response import not_found
from typing import List

from fastapi import APIRouter
from services import programmers_crud

router = APIRouter(
    prefix="/programmers",
    tags=["programmers"]
)

@router.get("/", status_code=200, summary="プログラマー一覧取得API")
async def get_programmers(response_model=List[Programmer]) -> List[Programmer]:
    return await programmers_crud.get_programmers()

@router.get("/{programmer_id}", status_code=200, responses={**not_found}, summary="プログラマー取得API")
async def get_programmer(programmer_id: int, response_model=Programmer) -> Programmer:
    return await programmers_crud.get_programmer(programmer_id=programmer_id)

@router.post("/create", status_code=201, summary="プログラマー作成API")
async def create_programmer(programmer_data: ProgrammerData, response_model=Programmer) -> Programmer:
    return await programmers_crud.create_programmer(programmer_data=programmer_data)

@router.put("/{programmer_id}", status_code=200, responses={**not_found}, summary="プログラマー更新API")
async def update_programmer(programmer_id: int, programmer_data: ProgrammerData, response_model=Programmer) -> Programmer:
    return await programmers_crud.update_programmer(programmer_id=programmer_id, programmer_data=programmer_data)

@router.delete("/{programmer_id}", status_code=200, responses={**not_found}, summary="プログラマー削除API")
async def delete_programmer(programmer_id: int, response_model=Programmer) -> Programmer:
    return await programmers_crud.delete_programmer(programmer_id=programmer_id)
