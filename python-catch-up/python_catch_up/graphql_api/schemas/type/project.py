import strawberry
import datetime

@strawberry.type
class Project:
    id: strawberry.ID
    client_id: strawberry.ID
    name: str
    start_date: datetime.date
    end_date: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime
