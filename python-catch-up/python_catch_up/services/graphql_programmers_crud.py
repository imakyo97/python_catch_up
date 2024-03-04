from typing import List

import strawberry
from models import models
from schemas import graphql_schemas

async def __to_schema_programmer(orm_programmer: models.Programmer) -> graphql_schemas.Programmer:
    technologies = [graphql_schemas.Technology(id=strawberry.ID(str(i.id)), name=i.name) async for i in orm_programmer.technologies] 
    programmer = graphql_schemas.Programmer(id=strawberry.ID(str(orm_programmer.id)), name=orm_programmer.name, technologies=technologies)
    return programmer

async def get_programmers() -> List[graphql_schemas.Programmer]:
    programmers = await models.Programmer.all()
    result = []
    for orm_programmer in programmers:
        programmer = await __to_schema_programmer(orm_programmer=orm_programmer)
        result.append(programmer)
    return result

async def get_programmer(programmer_id: int) -> graphql_schemas.Programmer:
    orm_programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not orm_programmer:
        raise Exception(
            {
                "title": "ユーザが存在しません",
                "message": "画面を更新して、再度やり直してください"
            }
        )       
    programmer = await __to_schema_programmer(orm_programmer=orm_programmer)
    return programmer

async def create_programmer(programmer_data: graphql_schemas.ProgrammerFilter) -> graphql_schemas.Programmer:
    programmer = await models.Programmer.create(name=programmer_data.name)
    for technology_name in programmer_data.technologies:
        technology, created = await models.Technology.get_or_create(name=technology_name)
        await programmer.technologies.add(technology)
    programmer = await __to_schema_programmer(orm_programmer=programmer)
    return programmer

async def update_programmer(programmer_id: int, programmer_data: graphql_schemas.ProgrammerFilter) -> graphql_schemas.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise Exception(
            {
                "title": "ユーザが存在しません",
                "message": "画面を更新して、再度やり直してください"
            }
        )   
    programmer.name=programmer_data.name
    await programmer.technologies.clear()
    for technology_name in programmer_data.technologies:
        technology, created = await models.Technology.get_or_create(name=technology_name)
        await programmer.technologies.add(technology)
    await programmer.save()
    return await __to_schema_programmer(orm_programmer=programmer)

async def delete_programmer(programmer_id: int) -> graphql_schemas.Programmer:
    programmer = await models.Programmer.get_or_none(id=programmer_id)
    if not programmer:
        raise Exception(
            {
                "title": "ユーザが存在しません",
                "message": "画面を更新して、再度やり直してください"
            }
        )   
    cache = await __to_schema_programmer(orm_programmer=programmer)
    await programmer.delete()
    return cache
