import os
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
import aioredis
from python_catch_up.constants import BASE_DIR
from python_catch_up.models.models import Admin


login_provider = UsernamePasswordProvider(
    admin_model=Admin,
    login_logo_url="https://preview.tabler.io/static/logo.svg"
)

async def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf8")
    await admin_app.configure(
        logo_url="https://preview.tabler.io/static/logo-white.svg",
        template_folders=[os.path.join(BASE_DIR, "templates")],
        providers=[login_provider],
        redis=redis,
    )