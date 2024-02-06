import datetime
from tortoise.models import Model
from tortoise import fields
from fastapi_admin.models import AbstractAdmin

class Admin(AbstractAdmin):
    last_login = fields.DatetimeField(description="Last Login", default=datetime.datetime.now)
    email = fields.CharField(max_length=200, default="")
    avatar = fields.CharField(max_length=200, default="")
    intro = fields.TextField(default="")
    created_at = fields.DatetimeField(auto_now_add=True)

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(20)
    favorite_technology = fields.JSONField()
