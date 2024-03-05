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
        return f"{self.programmer_id}"

class Client(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

class Project(Model):
    id = fields.BigIntField(pk=True)
    client_id = fields.ForeignKeyField(model_name="models.Client", related_name="projects")
    name = fields.CharField(255)
    start_date = fields.DateField()
    end_date = fields.DateField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

class ProjectSlot(Model):
    id = fields.BigIntField(pk=True)
    project_id = fields.ForeignKeyField(model_name="models.Project", related_name="project_slots")
    name = fields.CharField(255)
    start_date = fields.DateField()
    end_date = fields.DateField()
    budget = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)

class ProjectBudget(Model):
    id = fields.BigIntField(pk=True)
    project_id = fields.ForeignKeyField(model_name="models.Project", related_name="project_budgets")
    start_date = fields.DateField()
    end_date = fields.DateField()
    budget = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True)