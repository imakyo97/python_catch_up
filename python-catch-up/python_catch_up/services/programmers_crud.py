from typing import List
from models import models
from schemas import schemas
from schemas.error_response import MyException

async def __to_schema_programmer(orm_programmer: models.Programmer) -> schemas.Programmer:
    technologies = [schemas.Technology(id=i.id, name=i.name) async for i in orm_programmer.technologies] 
    programmer = schemas.Programmer(id=orm_programmer.id, name=orm_programmer.name, technologies=technologies)
    return programmer

async def get_programmers() -> List[schemas.Programmer]:
    programmers = await models.Programmer.all()
    result = []
    for orm_programmer in programmers:
        # https://tortoise.github.io/models.html#manytomanyfield
        # 同期的に fetch_related を使って for で回す
        # await orm_programmer.fetch_related("technologies")
        # technologies = [schemas.Technology(id=i.id, name=i.name) for i in orm_programmer.technologies]     

        # 非同期的に await を使って for で回す
        # technologies = [schemas.Technology(id=i.id, name=i.name) for i in await orm_programmer.technologies.all()]

        # 非同期的に async を使って for で回す
        # technologies = [schemas.Technology(id=i.id, name=i.name) async for i in orm_programmer.technologies] 
        # programmer = schemas.Programmer(id=orm_programmer.id, name=orm_programmer.name, technologies=technologies)

        programmer = await __to_schema_programmer(orm_programmer=orm_programmer)
        result.append(programmer)
    return result

async def get_programmer(programmer_id: int) -> schemas.Programmer:
    orm_programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not orm_programmer:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    programmer = await __to_schema_programmer(orm_programmer=orm_programmer)
    return programmer

async def create_programmer(programmer_data: schemas.ProgrammerData) -> schemas.Programmer:
    programmer = await models.Programmer.create(name=programmer_data.name)
    for technology_name in programmer_data.technologies:
        technology, created = await models.Technology.get_or_create(name=technology_name)
        await programmer.technologies.add(technology)
    programmer = await __to_schema_programmer(orm_programmer=programmer)
    return programmer

async def update_programmer(programmer_id: int, programmer_data: schemas.ProgrammerData) -> schemas.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    programmer.name=programmer_data.name
    await programmer.technologies.clear()
    for technology_name in programmer_data.technologies:
        technology, created = await models.Technology.get_or_create(name=technology_name)
        await programmer.technologies.add(technology)
    await programmer.save()
    return await __to_schema_programmer(orm_programmer=programmer)

async def delete_programmer(programmer_id: int) -> schemas.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    cache = await __to_schema_programmer(orm_programmer=programmer)
    await programmer.delete()
    return cache
