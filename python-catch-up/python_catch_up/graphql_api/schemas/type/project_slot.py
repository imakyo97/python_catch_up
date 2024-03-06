import strawberry
import datetime


@strawberry.type
class ProjectSlot:
    id: strawberry.ID
    project_id: strawberry.ID
    name: str
    start_date: datetime.date
    end_date: datetime.date
    budget: int
    created_at: datetime.datetime
    updated_at: datetime.datetime