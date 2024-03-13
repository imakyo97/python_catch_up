import strawberry
from datetime import datetime

@strawberry.type
class Client:
    id: strawberry.ID
    name: str
    created_at: datetime
    updated_at: datetime

@strawberry.input
class ClientData:
    name: str

@strawberry.type
class ListMetadata:
    count: int

@strawberry.type
class Mutation:
    create_client: Client
    update_client: Client
    delete_client: Client

@strawberry.type
class Query:
    all_clients: list[Client]
    _all_clients_meta: ListMetadata
    client: Client

schema = strawberry.Schema(query=Query, mutation=Mutation)

