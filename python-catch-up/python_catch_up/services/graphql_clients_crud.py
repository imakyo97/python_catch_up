from typing import List

import strawberry
from models import models
from schemas import graphql_schemas

async def __to_schema_client(orm_client: models.Client) -> graphql_schemas.Client:
    client = graphql_schemas.Client(
        id=strawberry.ID(str(orm_client.id)), 
        name=orm_client.name, 
        created_at=orm_client.created_at, 
        updated_at=orm_client.updated_at
    )
    return client

async def get_clients() -> List[graphql_schemas.Client]:
    clients = await models.Client.all()
    result = []
    for orm_client in clients:
        client = await __to_schema_client(orm_client=orm_client)
        result.append(client)
    return result

async def get_client(client_id: int) -> graphql_schemas.Client:
    orm_client = await models.Client.get_or_none(id=client_id)
    if not orm_client:
        raise Exception(
            {
                "title": "ユーザが存在しません",
                "message": "画面を更新して、再度やり直してください"
            }
        )       
    client = await __to_schema_client(orm_client=orm_client)
    return client

async def create_client(client_data: graphql_schemas.ClientData) -> graphql_schemas.Client:
    orm_client = await models.Client.create(name=client_data.name)
    client = await __to_schema_client(orm_client=orm_client)
    return client

async def update_client(client_id: int, client_data: graphql_schemas.ClientData) -> graphql_schemas.Client:
    client = await models.Client.get_or_none(id=client_id)
    if not client:
        raise Exception(
            {
                "title": "ユーザが存在しません",
                "message": "画面を更新して、再度やり直してください"
            }
        )   
    client.name=client_data.name
    await client.save()
    return await __to_schema_client(orm_client=client)

async def delete_client(client_id: int) -> graphql_schemas.Client:
    client = await models.Client.get_or_none(id=client_id)
    if not client:
        raise Exception(
            {
                "title": "ユーザが存在しません",
                "message": "画面を更新して、再度やり直してください"
            }
        )   
    cache = await __to_schema_client(orm_client=client)
    await client.delete()
    return cache
