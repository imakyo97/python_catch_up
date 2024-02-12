import config
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from tortoise import Tortoise
from tortoise.exceptions import DoesNotExist, IntegrityError

# @app.on_eventが非推奨のためlifespanを使用するが、lifespanを使用すると@app.on_eventが処理されなくなる
# register_tortoise内部で@app.on_eventを使用しているため、DBをTortoise.initで初期化する
# https://github.com/tortoise/tortoise-orm/issues/1450
async def init(app: FastAPI):
    settings = config.get_settings()  
    await Tortoise.init(
        db_url=settings.db_url,
        modules={"models": ["models.models"]},
    )
    if not os.path.isfile(settings.db_path):
        await Tortoise.generate_schemas()
    
    # register_tortoise内部のハンドラーを定義
    @app.exception_handler(DoesNotExist)
    async def doesnotexist_exception_handler(request: Request, exc: DoesNotExist):
        return JSONResponse(status_code=404, content={"detail": str(exc)})

    @app.exception_handler(IntegrityError)
    async def integrityerror_exception_handler(request: Request, exc: IntegrityError):
        return JSONResponse(
            status_code=422,
            content={"detail": [{"loc": [], "msg": str(exc), "type": "IntegrityError"}]},
        )
