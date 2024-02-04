from typing import List

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    favorite_technology: List[str]

class UserData(BaseModel):
    name: str
    favorite_technology: List[str]
