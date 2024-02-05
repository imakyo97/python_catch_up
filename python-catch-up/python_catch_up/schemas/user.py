from typing import List

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(examples=[1])
    name: str = Field(examples=["太郎"])
    favorite_technology: List[str] = Field(examples=[["swift"]])

    class Config:
        orm_mode = True

class UserData(BaseModel):
    name: str = Field(examples=["太郎"])
    favorite_technology: List[str] = Field(examples=[["swift"]])    
