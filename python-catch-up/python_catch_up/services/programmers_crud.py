from typing import List
from models import models
from schemas import schemas
from schemas.error_response import MyException

async def get_programmers() -> List[models.Programmer]:
    programmers = await models.Programmer.all()
    for programmer in programmers:
        await programmer.technologies.fetch_related(name)
        technologies_list = [technology for technology in programmer.technologies]
        programmer.technologies = technologies_list
    return programmers

async def get_programmer(programmer_id: int) -> models.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    return programmer

async def create_programmer(programmer_data: schemas.ProgrammerData) -> models.Programmer:
    programmer = models.Programmer(
        name=programmer_data.name,
        favorite_technology=programmer_data.favorite_technology
    )
    await programmer.save()
    return programmer

async def update_programmer(programmer_id: int, programmer_data: schemas.ProgrammerData) -> models.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    programmer.name=programmer_data.name
    programmer.favorite_technology=programmer_data.favorite_technology
    await programmer.save()
    return programmer

async def delete_programmer(programmer_id: int) -> models.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    await programmer.delete()
    return programmer
