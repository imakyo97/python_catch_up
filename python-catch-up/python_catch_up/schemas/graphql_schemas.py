from typing import List
import strawberry


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
