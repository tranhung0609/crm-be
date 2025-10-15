from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.api import router
# from api.home.home import home_router
from src.core.config import config
from src.core.database.mongo_async.mongo_motor_utils import connect_to_mongo, close_mongo_connection
from src.core.exceptions import CustomException
from src.core.helpers.logging import logger

def init_routers(app_: FastAPI) -> None:
    # app_.include_router(home_router)
    app_.include_router(router)

def init_listeners(app_: FastAPI) -> None:
    # Exception handler
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

    @app_.exception_handler(Exception)
    async def exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"message": "Có lỗi trong quá trình xử lý"},
        )


def init_loggers(app_: FastAPI) -> None:
    app_.logger = logger
    
# def init_cache() -> None:
#     Cache.init(backend=RedisBackend(), key_maker=CustomKeyMaker())

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="TNV 2.0 CMS API",
        description="TNV 2.0 CMS API",
        version="1.0.0",
        docs_url=None, #if config.ENV == "production" else "/docs",
        redoc_url=None, #if config.ENV == "production" else "/redoc",
        # dependencies=[Depends(Logger)],
        # middleware=make_middleware(),
    )
    init_loggers(app_=app_)
    init_routers(app_=app_)
    init_listeners(app_=app_)
    # init_cache()
    return app_

app = create_app()

@app.on_event("startup")
async def startup_app():
    '''
    Connect to mongo TN
    '''
    await connect_to_mongo(app)


@app.on_event("shutdown")
async def shutdown_app():
    # Stop kafka producer + kafka consumer
    '''
    Close mongo TN
    '''
    await close_mongo_connection(app)


@app.get("/")
def healthcheck():
    return JSONResponse(status_code=200, content={'Result': 'OK'})