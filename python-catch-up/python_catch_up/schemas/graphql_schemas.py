from typing import List
import strawberry
import datetime


@strawberry.type
class Technology:
    id: strawberry.ID
    name: str

@strawberry.type
class Programmer:
    id: strawberry.ID
    name: str
    technologies: List[Technology]

@strawberry.input
class ProgrammerFilter:
    name: str
    technologies: List[str]

@strawberry.type
class ListMetadata:
    count: int

@strawberry.type
class Client:
    id: strawberry.ID
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

@strawberry.input
class ClientData:
    name: str

@strawberry.type
class Project:
    id: strawberry.ID
    client_id: strawberry.ID
    name: str
    start_date: datetime.date
    end_date: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime

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

@strawberry.type
class ProjectBudget:
    id: strawberry.ID
    project_id: strawberry.ID
    start_date: datetime.date
    end_date: datetime.date
    budget: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
