from models import models
from fastapi_admin.resources import ComputeField
from fastapi import Request


class ProgrammerName(ComputeField):
    async def get_value(self, request: Request, obj: dict):  
        return await models.Programmer.get(id=obj["programmer_id"])

class TechnologyName(ComputeField):
    async def get_value(self, request: Request, obj: dict):  
        return await models.Technology.get(id=obj["technology_id"])