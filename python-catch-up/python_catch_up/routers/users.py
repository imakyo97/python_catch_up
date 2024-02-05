from python_catch_up.schemas.user import User, UserData
from python_catch_up.schemas.error_response import MyException, not_found
from typing import List

from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fake_users = [
    User(id=1, name="太郎", favorite_technology=[]),
    User(id=2, name="二郎", favorite_technology=[])
]

@router.get("/", status_code=200, summary="ユーザー一覧取得API")
def get_users(response_model=List[User]) -> List[User]:
    return fake_users

@router.get("/{user_id}", status_code=200, responses={**not_found}, summary="ユーザー取得API")
def get_user(user_id: int, response_model=User) -> User:
    for user in fake_users:
        if user.id == user_id:
            return user
    raise MyException(
        code=404, 
        title="ユーザが存在しません",
        message="画面を更新して、再度やり直してください"
    )

@router.post("/create", status_code=201, summary="ユーザー作成API")
def create_user(user_data: UserData, response_model=User) -> User:
    increment_id = fake_users[-1].id + 1
    user = User(id=increment_id, name=user_data.name, favorite_technology=user_data.favorite_technology)
    fake_users.append(user)
    return user

@router.put("/{user_id}", status_code=200, responses={**not_found}, summary="ユーザー更新API")
def update_user(user_id: int, user_data: UserData, response_model=User) -> User:
    for i, user in enumerate(fake_users):
        if user.id == user_id:
            fake_users[i] = User(id=user.id, name=user_data.name, favorite_technology=user_data.favorite_technology)
            return fake_users[i]
    raise MyException(
        code=404, 
        title="ユーザが存在しません",
        message="画面を更新して、再度やり直してください"
    )

@router.delete("/{user_id}", status_code=200, responses={**not_found}, summary="ユーザー削除API")
def delete_user(user_id: int, response_model=User) -> User:
    for i, user in enumerate(fake_users):
        if user.id == user_id:
            return fake_users.pop(i)
    raise MyException(
        code=404, 
        title="ユーザが存在しません",
        message="画面を更新して、再度やり直してください"
    )
