
# -*- coding: utf-8 -*-
import datetime
import os
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any, Union

from fastapi import APIRouter, Depends, File, UploadFile
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request
from starlette.responses import FileResponse

from app.api.common import deps
from app.api.db.mongoCurd import do_find, do_find_select, do_count, do_info
from app.api.db.mongoDB import get_database
from app.api.logger import logger
from app.api.utils.responseCode import resp_200
from app.config import settings
from app.api.utils import responseCode

router = APIRouter()


# 上传文件(不定格式,二进制流处理)
async def uploadFile(
        # token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        file: UploadFile = File(...)
):
    logger.info(f"上传文件:{file.filename}")
    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    save_dir = f"{settings.BASE_DIR}/app/assets/uploadFile"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    try:
        name, suffix = os.path.splitext(file.filename)  # Path(file.filename).suffix
        print(suffix)
        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
    finally:
        file.file.close()
    return responseCode.resp_200(data={"file": file.filename, "content_type": file.content_type})


# 上传图片
async def uploadImage(
        # token_data: Union[str, Any] = Depends(deps.check_jwt_token),
        file: UploadFile = File(...)
):
    logger.info(f"上传文件:{file.filename}")

    save_dir = f"{settings.BASE_DIR}/app/assets/uploadAssets"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    try:
        suffix = Path(file.filename).suffix
        print(suffix)
        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
    finally:
        file.file.close()
    return responseCode.resp_200(data={"image": f"{tmp.name}"})


# 下载文件(指明路劲)
async def downloadFile(file_name: str):
    print(file_name)
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = basedir + '\\' + str(datetime.datetime.now().date())
    file_path = path + '\\' + file_name + '.xlsx'
    print(file_path)
    return FileResponse(file_path)


async def getMongoData(*, request: Request,
                       db: AsyncIOMotorClient = Depends(get_database),
                       # token_data: Union[str, Any] = Depends(deps.check_jwt_token),
                       currentPage: int,
                       pageSize:int
                       ):

    rows = await do_find_select(db, currentPage, pageSize)
    # info_result = await do_info(db)

    totalNum = await do_count(db)
    return resp_200(data={"queryList":rows,"totalNum":totalNum})


# router.add_api_route(methods=['PUT','POST'], path="/file", endpoint=uploadFile,
#                      summary="上传文件")
# router.add_api_route(methods=['PUT','POST'], path="/image", endpoint=uploadImage,
#                      summary="上传图片")
#
# router.add_api_route(methods=['PUT','POST'], path="/download/{file_name}", endpoint=downloadFile,
#                      summary="上传文件")

router.add_api_route(methods=['GET'], path="/mongoData", endpoint=getMongoData,
                     summary="mongo数据")
