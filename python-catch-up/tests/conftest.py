import os
import shutil
import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from main import app
from httpx import AsyncClient
from config import Settings


def setup_dir():
    target_dir = 'tests/tmp'
    shutil.rmtree(target_dir)
    os.mkdir(target_dir)

@pytest.fixture(scope="session", autouse=True)
def setup():
    setup_dir()

@pytest_asyncio.fixture(scope="function", autouse=True)
async def client(mocker):
    # config.pyのget_settingsメソッドをモックに置き換える
    mocker.patch(
        "config.get_settings", 
        return_value=Settings(
            db_path="tests/tmp/test_db.sqlite3", 
            db_url="sqlite://tests/tmp/test_db.sqlite3"
        )
    )
    # lifespanを実行して、DB接続
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            yield(ac)

