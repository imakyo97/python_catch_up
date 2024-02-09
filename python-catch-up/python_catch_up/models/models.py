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

class Programmer(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(20)
    technologies: fields.ManyToManyRelation["Technology"] = fields.ManyToManyField(
        model_name="models.Technology",
        related_name="programmers",
        through="ProgrammerTechnology",
    )
    
    def __str__(self) -> str:
        return self.name

class Technology(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(20)
    programmers = fields.ManyToManyRelation[Programmer]

    def __str__(self) -> str:
        return self.name
    
class ProgrammerTechnology(Model):
    programmer_id = fields.IntField()
    technology_id = fields.IntField()

    def __str__(self) -> str:
        return f"{self.programmerId}"
