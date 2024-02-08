from schemas.user import User, UserData
from schemas.error_response import not_found
from typing import List

from fastapi import APIRouter
from services import users_crud

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", status_code=200, summary="ユーザー一覧取得API")
async def get_users(response_model=List[User]) -> List[User]:
    return await users_crud.get_users()

@router.get("/{user_id}", status_code=200, responses={**not_found}, summary="ユーザー取得API")
async def get_user(user_id: int, response_model=User) -> User:
    return await users_crud.get_user(user_id=user_id)

@router.post("/create", status_code=201, summary="ユーザー作成API")
async def create_user(user_data: UserData, response_model=User) -> User:
    return await users_crud.create_user(user_data=user_data)

@router.put("/{user_id}", status_code=200, responses={**not_found}, summary="ユーザー更新API")
async def update_user(user_id: int, user_data: UserData, response_model=User) -> User:
    return await users_crud.update_user(user_id=user_id, user_data=user_data)

@router.delete("/{user_id}", status_code=200, responses={**not_found}, summary="ユーザー削除API")
async def delete_user(user_id: int, response_model=User) -> User:
    return await users_crud.delete_user(user_id=user_id)
