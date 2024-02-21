from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter

from schemas import graphql_schemas
from services.graphql_programmers_crud import (
    get_programmers, 
    get_programmer,
    create_programmer,
    update_programmer,
    delete_programmer,
)


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    async def programmers(self) -> List[graphql_schemas.Programmer]:
        return await get_programmers()
    
    @strawberry.field
    async def programmer(self, id: strawberry.ID) -> graphql_schemas.Programmer:
        return await get_programmer(programmer_id=int(id))

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_programmer(self, programmer_data: graphql_schemas.ProgrammerData) -> graphql_schemas.Programmer:
        return await create_programmer(programmer_data=programmer_data)

    @strawberry.mutation
    async def update_programmer(self, id: strawberry.ID, programmer_data: graphql_schemas.ProgrammerData) -> graphql_schemas.Programmer:
        return await update_programmer(programmer_id=int(id), programmer_data=programmer_data)
    
    @strawberry.mutation
    async def delete_programmer(self, id: strawberry.ID) -> graphql_schemas.Programmer:
        return await delete_programmer(programmer_id=int(id))

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
