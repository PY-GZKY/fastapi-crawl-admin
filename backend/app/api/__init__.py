# -*- coding: utf-8 -*-
"""
模仿Flask工厂模式
"""
import asyncio
import time
import traceback

import aioredis
from fastapi import FastAPI, Request, Depends
from fastapi.exceptions import RequestValidationError, ValidationError
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_utils.tasks import repeat_every
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.websockets import WebSocket, WebSocketDisconnect

from app.api.apiV1.core.spiderLog.saveLog import query_task_log
from app.api.apiV1.router.ws.view import notifier
from app.api.db.mongoDB import db, get_database
from app.api.db.session import database, __initMasterHost, get_db
from app.config import settings
from .apiV1.api import api_v1_router
from .apiV1.core.spiderStatus.getStatus import getSpiderStatus
from .db.mongoCurd import do_info
from .db.redisDB import RedisCore
from .logger import logger
from .models.proTask import Tasks
from .utils import responseCode
from .utils.customExc import PostParamsError, UserNotFound, UserTokenError
from urllib.parse import quote


def create_app():
    """
    生成FatAPI对象
    :return:
    """
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.PROJECT_NAME,  # 项目名称
        description=settings.DESCRIPTION,  # 项目简介
        docs_url=f"{settings.API_V1}/docs",  # 自定义 docs文档的访问路径
        redoc_url=f"{settings.API_V1}/redocs",  # 禁用 redoc文档
        openapi_url=f"{settings.API_V1}/openapi.json"
    )

    app.add_middleware(SessionMiddleware, secret_key="jwt")

    # 其余的一些全局配置可以写在这里 多了可以考虑拆分到其他文件夹

    register_redis(app)

    # 注册mysql
    register_mysql(app)

    # 注册mongodb
    register_mongodb(app)

    # 注册ws
    register_ws(app)

    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 注册定时任务
    # register_task(app)

    # 注册捕获全局异常
    register_exception(app)

    # 请求拦截
    register_middleware(app)

    # if settings.DEBUG:
    #     register_static_file(app)
    return app


def register_redis(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        redis = await RedisCore().get_redis_pool()

        # 先挂上 fastapi 对象
        app.state.redis = redis

        # 初始化缓存 FastAPICache
        FastAPICache.init(RedisBackend(redis), prefix=settings.REDIS_CACHE_KEY)
        logger.debug("REDIS 数据库初始化成功 ... DONE")

    @app.on_event('shutdown')
    async def shutdown():
        app.state.redis.close()
        await app.state.redis.wait_closed()


def register_mysql(app: FastAPI):
    # 添加数据库连接和关闭事件
    @app.on_event("startup")
    async def connect_to_mysql():
        await database.connect()
        logger.debug("MYSQL 数据库初始化成功 ... DONE")
        await database.disconnect()  # 马上关闭,就测试一下

        if __initMasterHost():
            logger.debug("Master 节点初始化成功 ... DONE")


def register_mongodb(app: FastAPI):
    # 添加数据库连接和关闭事件
    @app.on_event("startup")
    async def connect_to_mongo():
        try:
            db.client = AsyncIOMotorClient(settings.MONGODB_URL,
                                           maxPoolSize=settings.MAX_CONNECTIONS_COUNT,
                                           minPoolSize=settings.MIN_CONNECTIONS_COUNT)

            logger.debug("MONGODB 数据库初始化成功 ... DONE")
        except:
            logger.error("MONGODB 数据库初始化失败 ... DONE")

    @app.on_event("shutdown")
    async def close_mongo_connection():
        close_db()
        logger.debug("MONGODB 数据库连接关闭 ... DONE")


# redis 缓存任务日志　过期时间一周
def register_ws(app: FastAPI):
    @app.websocket("/ws/{taskId}")
    async def websocket_endpoint(*, db: Session = Depends(get_db), websocket: WebSocket, taskId):
        await notifier.connect(websocket)
        try:

            while 1:
                taskStatusInfo = getSpiderStatus(taskId)
                print(f"目前抓取状态: {taskStatusInfo}")

                # 如果已经运行完成，查询一次数据库日志
                if taskStatusInfo.get('data'):
                    recent_msgs = query_task_log(taskId)  # 根据 taskId 查询历史日志并传输到页面-最近一次
                    # await notifier.send_personal_message({"fuck":"fuck"})
                    await notifier.send_personal_message(recent_msgs, websocket)
                    print("完成抛出异常")
                    raise WebSocketDisconnect

                else:
                    # 任务正在运行中
                    recent_msgs = query_task_log(taskId)
                    await asyncio.sleep(1)
                    await notifier.send_personal_message(recent_msgs, websocket)

                # while 1:
                #     if taskInfo.task_status:
                #         print("完成抛出异常")
                #         raise WebSocketDisconnect
                #     # await notifier.send_personal_message({"fuck": "fuck"})
                #     recent_msgs = query_task_log(taskId)
                #     await asyncio.sleep(1)
                #     await notifier.send_personal_message(recent_msgs,websocket)
                #     _a+=1
                #     taskInfo = db.query(Tasks).filter(
                #         Tasks.task_id == taskId).first()
                #     print(_a)
                #     print(f"目前抓取状态: {taskInfo.task_status}")

        except WebSocketDisconnect:
            notifier.disconnect(websocket)
            print("Bye")

    @app.on_event("startup")
    async def connect_to_ws():
        # await notifier.push(None)
        logger.debug("WEBSOCKET 连接初始化成功 ... DONE")


def register_static_file(app: FastAPI) -> None:
    from fastapi.staticfiles import StaticFiles
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")


def register_router(app: FastAPI):
    """
    注册路由
    这里暂时把两个API服务写到一起，后面在拆分
    :param app:
    :return:
    """
    # 项目API
    app.include_router(
        api_v1_router,
        prefix=settings.API_V1  # 前缀
    )


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:8001",
                           "http://localhost:8002"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_task(app: FastAPI):
    # 尝试写一个定时任务
    @app.on_event("startup")
    @repeat_every(seconds=60 * 60)  # 1 hour
    async def con_task() -> None:
        logger.debug(f'你好 {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}!')


def register_exception(app: FastAPI):
    """
    全局异常捕获

    注意 别手误多敲一个s
    exception_handler
    exception_handlers
    两者有区别

        如果只捕获一个异常 启动会报错
        @exception_handlers(UserNotFound)
    TypeError: 'dict' object is not callable

    :param app:
    :return:
    """

    # 自定义异常 捕获
    @app.exception_handler(UserNotFound)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFound):
        """
        用户认证未找到
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"token未知用户\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

        return responseCode.resp_5001(message=exc.err_desc)

    @app.exception_handler(UserTokenError)
    async def user_token_exception_handler(request: Request, exc: UserTokenError):
        """
        用户token异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"用户认证异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return responseCode.resp_401(message=exc.err_desc)

    @app.exception_handler(PostParamsError)
    async def query_params_exception_handler(request: Request, exc: PostParamsError):
        """
        内部查询操作时，其他参数异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"参数查询异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

        return responseCode.resp_400(message=exc.err_desc)

    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, exc: ValidationError):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"内部参数验证错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return responseCode.resp_500(message=exc.errors())

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        请求参数验证异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"请求参数格式错误\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return responseCode.resp_422(message=exc.errors())

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """
        全局所有异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")
        return responseCode.resp_500(message="服务器内部错误")


def register_middleware(app: FastAPI):
    """
    请求响应拦截 hook

    https://fastapi.tiangolo.com/tutorial/middleware/
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        # logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers}\nIP:{request.client.host}")

        response = await call_next(request)

        return response
