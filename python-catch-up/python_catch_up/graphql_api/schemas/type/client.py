import strawberry
import datetime


@strawberry.type
class Client:
    id: strawberry.ID
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

@strawberry.input
class ClientData:
    name: str
