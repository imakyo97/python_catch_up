from models import models
from schemas import schemas
from schemas.error_response import MyException

async def get_projects_count(filter: dict[str, str | int]) -> int: # type: ignore
    count = await models.Project.filter(**filter).all().count()
    return count

async def get_projects(order_by: (str), rangeStart: int, rangeEnd: int, filter: dict[str, str | int]) -> list[schemas.ProjectPydantic]:
    projects = await schemas.ProjectPydantic.from_queryset(
        models.Project.filter(**filter).all().order_by(order_by)
    )
    return projects[rangeStart:rangeEnd]

async def get_project(id: int) -> schemas.ProjectPydantic:
    orm_project = await models.Project.get_or_none(id=id)
    if not orm_project:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    project = await schemas.ProjectPydantic.from_tortoise_orm(orm_project)
    return project

async def get_project_in_bulk(ids: list[int]) -> list[schemas.ProjectPydantic]:
    projects_dict = await models.Project.in_bulk(ids, "id")
    projects = [await schemas.ProjectPydantic.from_tortoise_orm(project) for key, project in projects_dict.items()]
    return projects

async def create_project(project_input: schemas.ProjectPydanticInput) -> schemas.ProjectPydantic:
    client = await models.Client.get(id=project_input.client_id) # type: ignore
    orm_project = await models.Project.create(
        client=client,
        name=project_input.name, # type: ignore
        start_date=project_input.start_date, # type: ignore
        end_date=project_input.end_date # type: ignore
    )
    project = await schemas.ProjectPydantic.from_tortoise_orm(orm_project)
    return project

async def update_project(id: int, project_input: schemas.ProjectPydanticInput) -> schemas.ProjectPydantic:
    orm_project = await models.Project.get_or_none(id=id)
    if not orm_project:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    await models.Project.filter(id=id).update(**project_input.model_dump())
    client = await schemas.ProjectPydantic.from_queryset_single(
        models.Project.get(id=id)
    )
    return client

async def delete_project(id: int) -> schemas.ProjectPydantic:
    orm_project = await models.Project.get_or_none(id=id)
    if not orm_project:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    project = await schemas.ProjectPydantic.from_tortoise_orm(orm_project)
    await orm_project.delete()
    return project

async def delete_many_project(ids: list[int]) -> list[schemas.ProjectPydantic]:
    projects_dict = await models.Project.in_bulk(ids, "id")
    for key, project in projects_dict.items():
        await project.delete()
    projects = [await schemas.ProjectPydantic.from_tortoise_orm(project) for key, project in projects_dict.items()]
    return projects