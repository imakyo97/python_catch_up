from typing import List

from pydantic import BaseModel, Field
from tortoise import Tortoise
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from models.models import (
    Client,
    Project,
)

class Technology(BaseModel):
    id: int = Field(examples=[1])
    name: str = Field(examples=["Swift"])

    class Config:
        orm_mode = True

class Programmer(BaseModel):
    id: int = Field(examples=[1])
    name: str = Field(examples=["太郎"])
    technologies: List[Technology] = Field(examples=[[Technology(id=1, name="swift")]])

    class Config:
        orm_mode = True

class ProgrammerData(BaseModel):
    name: str = Field(examples=["太郎"])
    technologies: List[str] = Field(examples=[["swift"]])

Tortoise.init_models(["models.models"], "models")
ClientPydantic = pydantic_model_creator(Client, name="ClientPydantic")
ClientPydanticData = pydantic_model_creator(Client, name="ClientPydanticData", include=("name",))
ProjectPydantic = pydantic_model_creator(Project, name="ProjectPydantic", exclude=("project_budgets", "project_slots"))
ProjectPydanticInput = pydantic_model_creator(Project, name="ProjectPydanticInput", include=("client_id", "name", "start_date", "end_date"))
