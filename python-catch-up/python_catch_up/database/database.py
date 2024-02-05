from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

DB_URL = "sqlite://data/db.sqlite3"

def init(app: FastAPI):    
    register_tortoise(
        app,
        db_url=DB_URL,
        modules={"models": ["python_catch_up.models.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
