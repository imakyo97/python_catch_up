import os

from admin.constants import BASE_DIR
from admin.custom_field import ProgrammerName, TechnologyName
from models import models
from fastapi_admin.app import app
from fastapi_admin.resources import Link
from fastapi_admin.file_upload import FileUpload
from fastapi_admin.resources import Field, Model
from fastapi_admin.widgets import displays, filters, inputs

upload = FileUpload(uploads_dir=os.path.join(BASE_DIR, "static", "uploads"))

# Linkのiconサイト: https://fontawesome.com/icons/
@app.register
class Home(Link):
    label = "Home"
    icon = "fas fa-home"
    url = "/admin"

@app.register
class Programmers(Model):
    label = "プログラマー管理"
    model = models.Programmer
    icon = "fas fa-users"
    page_pre_title = "プログラマーリスト"
    page_title = "プログラマー管理"
    filters = [
        filters.Search(
            name="id", 
            label="ID", 
            search_mode="contains", 
            placeholder="Search for id"
        ),
        filters.Search(
            name="name", 
            label="Name", 
            search_mode="contains", 
            placeholder="Search for name"
        ),
    ]
    fields = [
        "id",
        "name",
        Field(
            name="technologies",
            label="technologies",
            display=displays.InputOnly(),
            input_=inputs.ManyToMany(model=models.Technology)
        ),
    ]

@app.register
class Technology(Model):
    label = "IT技術管理"
    model = models.Technology
    icon = "fas fa-code"
    page_pre_title = "技術リスト"
    page_title = "IT技術管理"
    filters = [
        filters.Search(
            name="name", 
            label="Name", 
            search_mode="contains", 
            placeholder="Search for name"
        ),
    ]
    fields = [
        "id",
        "name",
        Field(
            name="programmers",
            label="programmers", 
            display=displays.InputOnly(),
            input_=inputs.ManyToMany(models.Programmer)
        ),
    ]

@app.register
class ProgrammerTechnology(Model):
    label = "プログラマーとIT技術の管理"
    model = models.ProgrammerTechnology
    icon = "fas fa-key"
    page_pre_title = "技術リスト"
    page_title = "IT技術管理"
    filters = [
        filters.Search(
            name="programmer_id", 
            label="programmerId", 
            search_mode="contains", 
            placeholder="Search for programmerId"
        ),
        filters.Search(
            name="technology_id", 
            label="technologyId", 
            search_mode="contains", 
            placeholder="Search for technologyId"
        ),
    ]
    fields = [
        Field(
            name="id",
            label="id",
            input_=inputs.DisplayOnly(),
        ),
        Field(
            name="programmer_id",
            label="programmer_id",
            input_=inputs.DisplayOnly(),
        ),
        ProgrammerName(
            name="programmer_id", 
            label="programmer_name", 
        ),
        Field(
            name="technology_id",
            label="technology_id",
            input_=inputs.DisplayOnly(),
        ),
        TechnologyName(
            name="technology_id", 
            label="technology_name", 
        )
    ]

@app.register
class AdminResource(Model):
    label = "管理者"
    model = models.Admin
    icon = "fas fa-user"
    page_pre_title = "admin list"
    page_title = "admin model"
    filters = [
        filters.Search(
            name="username",
            label="Name",
            search_mode="contains",
            placeholder="Search for username"
        ),
        filters.Date(name="created_at", label="CreatedAt"),
    ]
    fields = [
        "id",
        "username",
        Field(
            name="password",
            label="Password",
            display=displays.InputOnly(),
            input_=inputs.Password(),
        ),
        Field(name="email", label="Email", input_=inputs.Email()),
        Field(
            name="avatar",
            label="Avatar",
            display=displays.Image(width="40"),
            input_=inputs.Image(null=True, upload=upload),
        ),
        "created_at",
    ]

@app.register
class GitHub(Link):
    label = "GitHub"
    icon = "fab fa-github"
    url = "https://github.com/imakyo97/python_catch_up"
    target = "_blank"
