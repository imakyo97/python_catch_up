import strawberry
import datetime


@strawberry.type
class ProjectBudget:
    id: strawberry.ID
    project_id: strawberry.ID
    start_date: datetime.date
    end_date: datetime.date
    budget: int
    created_at: datetime.datetime
    updated_at: datetime.datetime