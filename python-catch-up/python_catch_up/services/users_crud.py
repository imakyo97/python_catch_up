from typing import List
from models import models
from schemas import user
from schemas.error_response import MyException

async def get_users() -> List[models.User]:
    return await models.User.all()

async def get_user(user_id: int) -> models.User:
    user = await models.User.get_or_none(id=user_id)
    if not user:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    return user

async def create_user(user_data: user.UserData) -> models.User:
    user = models.User(
        name=user_data.name,
        favorite_technology=user_data.favorite_technology
    )
    await user.save()
    return user

async def update_user(user_id: int, user_data: user.UserData) -> models.User:
    user = await models.User.get_or_none(id=user_id)
    if not user:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    user.name=user_data.name
    user.favorite_technology=user_data.favorite_technology
    await user.save()
    return user

async def delete_user(user_id: int) -> models.User:
    user = await models.User.get_or_none(id=user_id)
    if not user:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    await user.delete()
    return user
