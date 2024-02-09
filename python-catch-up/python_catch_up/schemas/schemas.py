from typing import List

from pydantic import BaseModel, Field

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


