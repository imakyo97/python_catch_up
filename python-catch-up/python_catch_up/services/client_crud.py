from models import models
from schemas import schemas
from schemas.error_response import MyException

async def get_clients_count(filter: dict[str, str | int]) -> int: # type: ignore
    count = await models.Client.filter(**filter).all().count()
    return count

async def get_clients(order_by: (str), rangeStart: int, rangeEnd: int, filter: dict[str, str | int]) -> list[schemas.ClientPydantic]:
    clients = await schemas.ClientPydantic.from_queryset(
        models.Client.filter(**filter).all().order_by(order_by)
    )
    return clients[rangeStart:rangeEnd]

async def get_client(id: int) -> schemas.ClientPydantic:
    orm_client = await models.Client.get_or_none(id=id)
    if not orm_client:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    client = await schemas.ClientPydantic.from_tortoise_orm(orm_client)
    return client

async def get_client_in_bulk(ids: list[int]) -> list[schemas.ClientPydantic]:
    clients_dict = await models.Client.in_bulk(ids, "id")
    clients = [await schemas.ClientPydantic.from_tortoise_orm(client) for key, client in clients_dict.items()]
    return clients

async def create_client(client_data: schemas.ClientPydanticData) -> schemas.ClientPydantic:
    orm_client = await models.Client.create(**client_data.model_dump())
    client = await schemas.ClientPydantic.from_tortoise_orm(orm_client)
    return client

async def update_client(id: int, client_data: schemas.ClientPydanticData) -> schemas.ClientPydantic:
    orm_client = await models.Client.get_or_none(id=id)
    if not orm_client:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    orm_client.name=client_data.name # type: ignore
    await orm_client.save()
    client = await schemas.ClientPydantic.from_tortoise_orm(orm_client)
    return client

async def delete_client(id: int) -> schemas.ClientPydantic:
    orm_client = await models.Client.get_or_none(id=id)
    if not orm_client:
        raise MyException(
            code=404, 
            title="ユーザが存在しません",
            message="画面を更新して、再度やり直してください"
        )
    client = await schemas.ClientPydantic.from_tortoise_orm(orm_client)
    await orm_client.delete()
    return client

async def delete_many_client(ids: list[int]) -> list[schemas.ClientPydantic]:
    clients_dict = await models.Client.in_bulk(ids, "id")
    for key, client in clients_dict.items():
        await client.delete()
    clients = [await schemas.ClientPydantic.from_tortoise_orm(client) for key, client in clients_dict.items()]
    return clients