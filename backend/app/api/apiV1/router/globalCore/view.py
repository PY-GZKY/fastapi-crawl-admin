# -*- coding: utf-8 -*
# @Time : 2020/11/10 15:00
import platform

import psutil
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.api.db.mongoCurd import do_info
from app.api.db.mongoDB import get_database
from app.api.db.redisCurd import RedisQueue
from app.api.db.session import get_db
from app.api.models.hosts import Hosts
from app.api.models.proTask import Project, Tasks
from app.api.utils.responseCode import resp_200, resp_500

router = APIRouter()


# 总项目数量/总任务数量
def globalCount(*, request: Request, db: Session = Depends(get_db),
                # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
                ):
    item = {}
    item["projectCount"] = db.query(Project).count()
    item["taskCount"] = db.query(Tasks).count()
    item["hostCount"] = db.query(Hosts).count()
    return resp_200(data=item)


# 系统信息
def systemParams(
        *, request: Request
):
    memory = psutil.virtual_memory()
    try:
        result = {
            "info":
                {
                    "title": "系统信息",
                    "bit_msg": platform.architecture()[0],
                    "platform": platform.platform(),
                },

            "mem":
                {
                    "title": "内存信息",
                    "mem_used": str(round(memory.used / (1024.0 * 1024.0 * 1024.0), 2)) + "Gb",  # 已使用内存
                    "mem_free": str(round(memory.free / (1024.0 * 1024.0 * 1024.0), 2)) + "Gb",  # 剩余内存
                    "mem_percent": str(memory.percent) + "%"  # 使用率
                },
            "cpu":
                {
                    "title": "CPU信息",
                    "cpu_cores": psutil.cpu_count(logical=False),
                    "free": psutil.cpu_times().user
                },
        }
        return resp_200(data=result)
    except:
        return resp_500()


# redis参数
def redisParam(
        *, request: Request,
        # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
):
    info = RedisQueue().info()
    # print(info)
    return resp_200(data=info)


# mongodb参数
async def mongoParam(
        *, request: Request,
        db: AsyncIOMotorClient = Depends(get_database),
        # token_data: Union[str, Any] = Depends(deps.check_jwt_token)
):
    mongo_info = await do_info(db)
    return resp_200(data=mongo_info)


# ------------------------------- 路由添加 --------------------------------

router.add_api_route(methods=['GET'], path="/global/count", endpoint=globalCount, summary="全局统计")
router.add_api_route(methods=['GET'], path="/global/system", endpoint=systemParams, summary="系统信息")
router.add_api_route(methods=['GET'], path="/global/redis", endpoint=redisParam, summary="redis参数")
router.add_api_route(methods=['GET'], path="/global/mongodb", endpoint=mongoParam, summary="mongodb参数")

""""""
