from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from graphql_api.schemas.type.client import Client, ClientData
from graphql_api.schemas.type.meta_data import ListMetadata
from graphql_api.resolvers.client import (
    get_clients, 
    get_client,
    create_client,
    update_client,
    delete_client,
)

@strawberry.type
class Query:
    @strawberry.field
    async def allClients(self) -> List[Client]:
        return await get_clients()
    
    @strawberry.field
    async def _allClientsMeta(self) -> ListMetadata:
        return ListMetadata(count= len(await get_clients()))

    @strawberry.field
    async def Client(self, id: strawberry.ID) -> Client:
        return await get_client(client_id=int(id))

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def createClient(self, client_data: ClientData) -> Client:
        return await create_client(client_data=client_data)

    @strawberry.mutation
    async def updateClient(self, id: strawberry.ID, client_data: ClientData) -> Client:
        return await update_client(client_id=int(id), client_data=client_data)
    
    @strawberry.mutation
    async def deleteClient(self, id: strawberry.ID) -> Client:
        return await delete_client(client_id=int(id))

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
graphql_app = GraphQLRouter(schema)
