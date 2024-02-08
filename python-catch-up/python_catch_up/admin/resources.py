import os
from admin.constants import BASE_DIR
from models.models import Admin, User
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
class Users(Model):
    label = "ユーザー管理"
    model = User
    icon = "fas fa-users"
    page_pre_title = "ユーザーリスト"
    page_title = "ユーザー管理"
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
        "favorite_technology",
    ]

@app.register
class AdminResource(Model):
    label = "管理者"
    model = Admin
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
