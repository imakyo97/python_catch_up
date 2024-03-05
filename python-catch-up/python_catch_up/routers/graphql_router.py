from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from schemas import graphql_schemas
from services.graphql_programmers_crud import (
    get_programmers, 
    get_programmer,
    create_programmer,
    update_programmer,
    delete_programmer,
)
from services.graphql_clients_crud import (
    get_clients, 
    get_client,
    create_client,
    update_client,
    delete_client,
)

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    async def allProgrammers(self) -> List[graphql_schemas.Programmer]:
        return await get_programmers()
    
    @strawberry.field
    async def _allProgrammersMeta(self) -> graphql_schemas.ListMetadata:
        return graphql_schemas.ListMetadata(count= len(await get_programmers()))
    
    @strawberry.field
    async def programmer(self, id: strawberry.ID) -> graphql_schemas.Programmer:
        return await get_programmer(programmer_id=int(id))
    
    @strawberry.field
    async def allClients(self) -> List[graphql_schemas.Client]:
        return await get_clients()
    
    @strawberry.field
    async def _allClientsMeta(self) -> graphql_schemas.ListMetadata:
        return graphql_schemas.ListMetadata(count= len(await get_clients()))

    @strawberry.field
    async def Client(self, id: strawberry.ID) -> graphql_schemas.Client:
        return await get_client(client_id=int(id))

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def createProgrammer(self, programmer_data: graphql_schemas.ProgrammerFilter) -> graphql_schemas.Programmer:
        return await create_programmer(programmer_data=programmer_data)

    @strawberry.mutation
    async def updateProgrammer(self, id: strawberry.ID, programmer_data: graphql_schemas.ProgrammerFilter) -> graphql_schemas.Programmer:
        return await update_programmer(programmer_id=int(id), programmer_data=programmer_data)
    
    @strawberry.mutation
    async def deleteProgrammer(self, id: strawberry.ID) -> graphql_schemas.Programmer:
        return await delete_programmer(programmer_id=int(id))
    
    @strawberry.mutation
    async def createClient(self, client_data: graphql_schemas.ClientData) -> graphql_schemas.Client:
        return await create_client(client_data=client_data)

    @strawberry.mutation
    async def updateClient(self, id: strawberry.ID, client_data: graphql_schemas.ClientData) -> graphql_schemas.Client:
        return await update_client(client_id=int(id), client_data=client_data)
    
    @strawberry.mutation
    async def deleteClient(self, id: strawberry.ID) -> graphql_schemas.Client:
        return await delete_client(client_id=int(id))

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))
graphql_app = GraphQLRouter(schema)
